# coding: utf-8
from __future__ import absolute_import

import json
import logging
import threading

import urllib3

from cloudtower.api_client import ApiClient
from cloudtower.configuration import Configuration
from cloudtower.exceptions import ApiException
from cloudtower import utils

logger = logging.getLogger(__name__)

DEFAULT_BASE_PATH = "/v2/api"
DEFAULT_SCHEME = "http"
DEFAULT_PROBE_TIMEOUT = 5
PROBE_PATH = "/api/healthz"
AUTH_API_PATH = "/api"
HOST_STATE_ACTIVE = "active"
HOST_STATE_PASSIVE = "passive"
HTTP_STATUS_OK = 200
HTTP_STATUS_TEMPORARY_REDIRECT = 307
REQUEST_ATTEMPTS = 2


class ActivePassiveException(ApiException):
    """Base exception for active-passive client errors."""
    default_reason = "active-passive client error"

    def __init__(self, status=None, reason=None, http_resp=None, host=None,
                 endpoints=None, active_hosts=None, failures=None,
                 strategy=None):
        if reason is None:
            reason = self.default_reason
        super(ActivePassiveException, self).__init__(
            status=status,
            reason=reason,
            http_resp=http_resp,
        )
        self.host = host
        self.endpoints = list(endpoints) if endpoints is not None else None
        self.active_hosts = (
            list(active_hosts) if active_hosts is not None else None
        )
        self.failures = list(failures) if failures is not None else None
        self.strategy = strategy


class ActivePassiveNoEndpoints(ActivePassiveException):
    default_reason = "active-passive client requires at least one endpoint"


class ActivePassiveDuplicateHost(ActivePassiveException):
    default_reason = "active-passive client endpoints must be unique"


class ActivePassiveNoActiveHost(ActivePassiveException):
    default_reason = "active-passive discover found no active host"


class ActivePassiveMultipleActives(ActivePassiveException):
    default_reason = "active-passive discover found multiple active hosts"


class ActivePassiveRetryExhausted(ActivePassiveException):
    default_reason = "active-passive request retry exhausted after discover"


class ActivePassiveFailoverRequired(ActivePassiveException):
    default_reason = "active-passive failover required"


class ActivePassiveUnknownHost(ActivePassiveException):
    default_reason = "active-passive host is not configured"


class FailoverStrategy(object):
    """Failover strategy for active-passive client."""
    DEFAULT = "default"
    MANUAL_FAILOVER = "manual_failover"
    ALWAYS_PROBE = "always_probe"


class ActivePassiveApiClient(ApiClient):
    """API client with active-passive endpoint support.

    Automatically discovers the active endpoint among a list of candidates,
    caches it, and failovers on 307 Temporary Redirect responses.
    """

    def __init__(self, endpoints=None, base_path=DEFAULT_BASE_PATH, schemes=None,
                 user_config=None, probe_timeout=None, failover_strategy=None,
                 configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1):
        """Initialize an active-passive API client.

        :param endpoints: List of host strings (e.g., ["172.21.152.75"]).
        :param base_path: Base path for API requests (default "/v2/api").
        :param schemes: List of URL schemes (default ["http"]).
        :param user_config: Optional dict with keys ``name``, ``password``,
            ``source`` for automatic login.
        :param probe_timeout: Timeout in seconds for healthz probes
            (default 5).
        :param failover_strategy: One of :class:`FailoverStrategy` constants.
        :param configuration: ``Configuration`` instance (optional).
        :param header_name: Default header name.
        :param header_value: Default header value.
        :param cookie: Default cookie.
        :param pool_threads: Thread-pool size for async requests.
        """
        if endpoints is None or len(endpoints) == 0:
            raise ActivePassiveNoEndpoints(
                status=0,
                endpoints=endpoints,
            )
        if schemes is None:
            schemes = [DEFAULT_SCHEME]

        seen = set()
        self._ordered_hosts = []
        for ep in endpoints:
            host = ep.strip()
            if not host:
                raise ActivePassiveNoEndpoints(
                    status=0,
                    host=host,
                    endpoints=endpoints,
                )
            if host in seen:
                raise ActivePassiveDuplicateHost(
                    status=0,
                    reason=(
                        "active-passive client endpoints must be unique: {}"
                        .format(host)
                    ),
                    host=host,
                    endpoints=endpoints,
                )
            seen.add(host)
            self._ordered_hosts.append(host)

        self._base_path = base_path
        self._schemes = schemes
        self._probe_timeout = (
            probe_timeout if probe_timeout is not None else DEFAULT_PROBE_TIMEOUT
        )
        self.failover_strategy = (
            failover_strategy
            if failover_strategy is not None
            else FailoverStrategy.DEFAULT
        )

        self._lock = threading.RLock()
        self._current_active_host = None
        self._current_active_host_url = None
        self._discover_event = None
        self._discover_err = None
        self._local = threading.local()

        if configuration is None:
            configuration = Configuration.get_default_copy()

        # Set an initial host so that RESTClientObject can be created;
        # the real active host is discovered on the first request.
        configuration.host = self._build_base_url(self._ordered_hosts[0])

        super(ActivePassiveApiClient, self).__init__(
            configuration=configuration,
            header_name=header_name,
            header_value=header_value,
            cookie=cookie,
            pool_threads=pool_threads,
        )

        if user_config is not None:
            self._login_with_user_config(user_config)

    # ------------------------------------------------------------------ #
    # Public helpers
    # ------------------------------------------------------------------ #
    @property
    def current_active_host(self):
        """Return the currently cached active host (host only)."""
        with self._lock:
            return self._current_active_host

    # ------------------------------------------------------------------ #
    # URL builders
    # ------------------------------------------------------------------ #
    @staticmethod
    def _build_url(scheme, host, path):
        return "{}://{}{}".format(scheme, host, path)

    def _build_base_url(self, host):
        scheme = self._schemes[0] if self._schemes else DEFAULT_SCHEME
        return self._build_url(scheme, host, self._base_path)

    def _build_probe_url(self, host):
        scheme = self._schemes[0] if self._schemes else DEFAULT_SCHEME
        return self._build_url(scheme, host, PROBE_PATH)

    # ------------------------------------------------------------------ #
    # Active-host lifecycle
    # ------------------------------------------------------------------ #
    def _clear_active_host(self):
        with self._lock:
            self._current_active_host = None
            self._current_active_host_url = None

    def _ensure_active_host(self):
        while True:
            with self._lock:
                if self.failover_strategy == FailoverStrategy.ALWAYS_PROBE:
                    self._current_active_host = None
                    self._current_active_host_url = None

                if self._current_active_host_url is not None:
                    return self._current_active_host_url

                if self._discover_event is not None:
                    event = self._discover_event
                    need_discover = False
                else:
                    event = threading.Event()
                    self._discover_event = event
                    need_discover = True

            if not need_discover:
                event.wait()
                with self._lock:
                    if self._current_active_host_url is not None:
                        return self._current_active_host_url
                    if self._discover_err is not None:
                        raise self._discover_err
                # Another thread discovered nothing; retry.
                continue

            try:
                host = self._discover()
                with self._lock:
                    self._current_active_host = host
                    self._current_active_host_url = self._build_base_url(host)
                    self._discover_err = None
                return self._current_active_host_url
            except Exception as e:
                with self._lock:
                    self._discover_err = e
                raise
            finally:
                event.set()
                with self._lock:
                    self._discover_event = None

    def _discover(self):
        active_hosts = []
        failures = []

        for host in self._ordered_hosts:
            try:
                state = self._probe_host(host)
                if state == HOST_STATE_ACTIVE:
                    active_hosts.append(host)
            except Exception as e:
                failures.append("{}: {}".format(host, str(e)))

        if len(active_hosts) == 1:
            logger.debug(
                "active-passive discover found active host: {}".format(
                    active_hosts[0]
                ),
            )
            return active_hosts[0]
        elif len(active_hosts) == 0:
            if len(failures) == 0:
                raise ActivePassiveNoActiveHost(
                    status=0,
                    endpoints=self._ordered_hosts,
                )
            raise ActivePassiveNoActiveHost(
                status=0,
                reason=(
                    "active-passive discover found no active host: {}"
                    .format("; ".join(failures))
                ),
                endpoints=self._ordered_hosts,
                failures=failures,
            )
        else:
            raise ActivePassiveMultipleActives(
                status=0,
                reason=(
                    "active-passive discover found multiple active hosts: {}"
                    .format(
                        ", ".join(
                            self._build_base_url(h) for h in active_hosts
                        )
                    )
                ),
                endpoints=self._ordered_hosts,
                active_hosts=active_hosts,
            )

    def _probe_host(self, host):
        url = self._build_probe_url(host)
        is_active = self._do_probe(url, timeout=self._probe_timeout)
        return HOST_STATE_ACTIVE if is_active else HOST_STATE_PASSIVE

    # ------------------------------------------------------------------ #
    # Authentication / login
    # ------------------------------------------------------------------ #
    def _login_with_user_config(self, user_config):
        active_host = self._ensure_active_host()
        self.configuration.host = active_host

        if isinstance(user_config, dict):
            username = user_config.get("name")
            password = user_config.get("password")
            source = user_config.get("source")
        else:
            username = getattr(user_config, "name", None)
            password = getattr(user_config, "password", None)
            source = getattr(user_config, "source", None)

        utils.login(self, username, password, source)

    def _get_auth_config_id(self, active_host_base_url):
        """Query authn strategies and return the LDAP config id if present."""
        # active_host_base_url is e.g. http://host/v2/api
        # We need to post to http://host/api
        scheme = self._schemes[0] if self._schemes else DEFAULT_SCHEME
        host = None
        for h in self._ordered_hosts:
            if active_host_base_url == self._build_base_url(h):
                host = h
                break
        if host is None:
            return None

        url = self._build_url(scheme, host, AUTH_API_PATH)
        body = json.dumps(
            {
                "operationName": None,
                "variables": {},
                "query": "{authnStrategies{id type}}",
            }
        )
        try:
            r = self.rest_client.pool_manager.request(
                "POST",
                url,
                body=body,
                headers={"Content-Type": "application/json"},
                redirect=False,
                timeout=urllib3.Timeout(total=self._probe_timeout),
            )
            if r.status != HTTP_STATUS_OK:
                return None
            data = json.loads(r.data.decode("utf-8"))
            for strategy in data.get("data", {}).get("authnStrategies", []):
                if strategy.get("type") == "LDAP":
                    return strategy.get("id")
        except Exception:
            pass
        return None

    # ------------------------------------------------------------------ #
    # ApiClient overrides
    # ------------------------------------------------------------------ #
    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None, redirect=None):
        """Override to route requests to the current active host."""
        if getattr(self._local, "bypass_active_passive", False):
            return super(ActivePassiveApiClient, self).request(
                method, url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                redirect=False,
            )

        active_host = self._ensure_active_host()
        if not url.startswith(active_host):
            for host in self._ordered_hosts:
                base_url = self._build_base_url(host)
                if url.startswith(base_url):
                    url = active_host + url[len(base_url):]
                    break
        return super(ActivePassiveApiClient, self).request(
            method, url,
            query_params=query_params,
            headers=headers,
            post_params=post_params,
            body=body,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            redirect=False,
        )

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_types_map=None, auth_settings=None,
                 async_req=None, _return_http_data_only=None,
                 collection_formats=None, _preload_content=True,
                 _request_timeout=None, _host=None, _request_auth=None):
        """Override to inject active-passive host selection and failover."""
        if async_req:
            return self.pool.apply_async(
                self._call_api_with_failover,
                (
                    resource_path, method,
                    path_params, query_params, header_params,
                    body, post_params, files,
                    response_types_map, auth_settings,
                    _return_http_data_only, collection_formats,
                    _preload_content, _request_timeout, _host, _request_auth,
                ),
            )
        return self._call_api_with_failover(
            resource_path, method,
            path_params, query_params, header_params,
            body, post_params, files,
            response_types_map, auth_settings,
            _return_http_data_only, collection_formats,
            _preload_content, _request_timeout, _host, _request_auth,
        )

    def _call_api_with_failover(self, resource_path, method,
                                path_params=None, query_params=None,
                                header_params=None, body=None,
                                post_params=None, files=None,
                                response_types_map=None, auth_settings=None,
                                _return_http_data_only=None,
                                collection_formats=None,
                                _preload_content=True, _request_timeout=None,
                                _host=None, _request_auth=None):
        """Internal wrapper that handles active-host discovery and 307 retry."""
        # When the caller explicitly supplies _host, bypass active-passive logic.
        if _host is not None:
            self._local.bypass_active_passive = True
            try:
                return super(ActivePassiveApiClient, self)._ApiClient__call_api(
                    resource_path, method,
                    path_params, query_params, header_params,
                    body, post_params, files,
                    response_types_map, auth_settings,
                    _return_http_data_only, collection_formats,
                    _preload_content, _request_timeout, _host, _request_auth,
                )
            finally:
                self._local.bypass_active_passive = False

        for attempt in range(REQUEST_ATTEMPTS):
            active_host = self._ensure_active_host()
            self.configuration.host = active_host

            try:
                return super(ActivePassiveApiClient, self)._ApiClient__call_api(
                    resource_path, method,
                    path_params, query_params, header_params,
                    body, post_params, files,
                    response_types_map, auth_settings,
                    _return_http_data_only, collection_formats,
                    _preload_content, _request_timeout, _host, _request_auth,
                )
            except ApiException as e:
                if e.status == HTTP_STATUS_TEMPORARY_REDIRECT:
                    with self._lock:
                        failed_host = self._current_active_host
                    self._clear_active_host()
                    if self.failover_strategy in (
                        FailoverStrategy.MANUAL_FAILOVER,
                        FailoverStrategy.ALWAYS_PROBE,
                    ):
                        raise ActivePassiveFailoverRequired(
                            status=HTTP_STATUS_TEMPORARY_REDIRECT,
                            host=failed_host,
                            endpoints=self._ordered_hosts,
                            strategy=self.failover_strategy,
                        )
                    if attempt == 0:
                        continue
                    raise ActivePassiveRetryExhausted(
                        status=HTTP_STATUS_TEMPORARY_REDIRECT,
                        host=failed_host,
                        endpoints=self._ordered_hosts,
                        strategy=self.failover_strategy,
                    )
                if self._should_clear_active_host_on_error(
                    e, response_types_map
                ):
                    self._clear_active_host()
                raise

    def _should_clear_active_host_on_error(self, err, response_types_map):
        if err.status is None or err.status == 0:
            return True
        if response_types_map is not None and err.status in response_types_map:
            return False
        return True
