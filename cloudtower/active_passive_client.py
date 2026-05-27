# coding: utf-8
from __future__ import absolute_import

import copy
import atexit
import logging
import threading
from multiprocessing.pool import ThreadPool

import six
from six.moves.urllib.parse import urlparse

from cloudtower.api_client import ApiClient
from cloudtower.configuration import (
    Configuration,
    DEFAULT_API_PATH,
    DEFAULT_PROBE_PATH,
)
from cloudtower.exceptions import ApiException
from cloudtower import utils

logger = logging.getLogger(__name__)

DEFAULT_PROBE_TIMEOUT = 5
DEFAULT_SCHEME = "http"
HOST_STATE_ACTIVE = "active"
HOST_STATE_PASSIVE = "passive"
HTTP_STATUS_TEMPORARY_REDIRECT = 307
REQUEST_ATTEMPTS = 2


_ENDPOINT_URL_FIELDS = (
    "_scheme",
    "_base_url",
    "_root_url",
    "_api_path",
    "_probe_path",
    "_probe_url",
    "_base_path",
)


def _remove_url_scheme(url):
    if url is None:
        return None
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc:
        path = parsed.path.strip("/")
        return parsed.netloc + ("/" + path if path else "")
    return url


def _coerce_endpoint(endpoint, configuration=None):
    if isinstance(endpoint, Configuration):
        return copy.deepcopy(endpoint)
    if isinstance(endpoint, six.string_types):
        return Configuration(
            root_url=endpoint,
            scheme=DEFAULT_SCHEME,
            api_path=DEFAULT_API_PATH,
            probe_path=DEFAULT_PROBE_PATH,
        )
    if not isinstance(endpoint, dict):
        return None

    root_url = _remove_url_scheme(endpoint.get("root_url"))
    base_url = _remove_url_scheme(endpoint.get("base_url"))

    host = endpoint.get("host") if "host" in endpoint else None
    if root_url is None and base_url is None and host is None:
        return None

    api_path = endpoint.get("api_path")
    probe_path = endpoint.get("probe_path")

    endpoint_config = Configuration(
        host=host,
        root_url=root_url,
        base_url=base_url,
        scheme=endpoint.get("scheme") or DEFAULT_SCHEME,
        api_path=api_path or DEFAULT_API_PATH,
        probe_path=probe_path or DEFAULT_PROBE_PATH,
    )
    if configuration is None:
        return endpoint_config

    result = copy.deepcopy(configuration)
    for name in _ENDPOINT_URL_FIELDS:
        setattr(result, name, getattr(endpoint_config, name))
    return result


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
    AUTO_FAILOVER = "auto_failover"
    MANUAL_FAILOVER = "manual_failover"
    ALWAYS_PROBE = "always_probe"


class _ActivePassiveEndpointApiClient(ApiClient):
    """Endpoint client used by active-passive routing.

    Active-passive requests must observe 307 responses directly so failover
    logic can run. Keep that redirect policy local to AP endpoint clients.
    """

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None, redirect=None):
        return super(_ActivePassiveEndpointApiClient, self).request(
            method, url,
            query_params=query_params,
            headers=headers,
            post_params=post_params,
            body=body,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            redirect=False,
        )


class ActivePassiveApiClient(ApiClient):
    """API client with active-passive endpoint support.

    Automatically discovers the active endpoint among a list of candidates,
    caches it, and failovers on 307 Temporary Redirect responses.
    """

    def __init__(self, endpoints=None, user_config=None, probe_timeout=None,
                 failover_strategy=None, configuration=None, header_name=None,
                 header_value=None, cookie=None, pool_threads=1):
        """Initialize an active-passive API client.

        :param endpoints: List of dict or ``Configuration`` configs. Entries
            can set ``scheme``, ``root_url``, ``api_path``, and
            ``probe_path``.
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
        self._endpoints_by_root_url = {}
        if configuration is None:
            configuration = Configuration.get_default_copy()
        for ep in endpoints:
            endpoint = _coerce_endpoint(ep, configuration=configuration)
            if endpoint is None or not endpoint.root_url:
                raise ActivePassiveNoEndpoints(
                    status=0,
                    host=None,
                    endpoints=endpoints,
                )
            root_url = endpoint.root_url
            if root_url in self._endpoints_by_root_url:
                raise ActivePassiveDuplicateHost(
                    status=0,
                    reason=(
                        "active-passive client endpoints must be unique: {}"
                        .format(root_url)
                    ),
                    host=root_url,
                    endpoints=endpoints,
                )
            self._endpoints_by_root_url[root_url] = endpoint

        self._probe_timeout = (
            probe_timeout if probe_timeout is not None else DEFAULT_PROBE_TIMEOUT
        )
        self.failover_strategy = (
            failover_strategy
            if failover_strategy is not None
            else FailoverStrategy.AUTO_FAILOVER
        )

        self._lock = threading.RLock()
        self._current_active_base_url = None
        self._discover_event = None
        self._discover_err = None

        self.pool_threads = pool_threads
        self._pool = None
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        self.user_agent = 'OpenAPI-Generator/2.23.0/python'
        self.client_side_validation = configuration.client_side_validation
        self._api_clients_by_root_url = {}
        for root_url, endpoint in self._endpoints_by_root_url.items():
            endpoint_client = _ActivePassiveEndpointApiClient(
                configuration=endpoint,
                cookie=cookie,
                pool_threads=pool_threads,
            )
            endpoint_client.default_headers = self.default_headers
            self._api_clients_by_root_url[root_url] = endpoint_client
        self.last_response = {}

        if user_config is not None:
            self._login_with_user_config(user_config)

    # ------------------------------------------------------------------ #
    # Public helpers
    # ------------------------------------------------------------------ #
    @property
    def current_active_base_url(self):
        """Return the currently cached active endpoint base URL."""
        with self._lock:
            return self._current_active_base_url

    def _endpoint_root_urls(self):
        return list(self._endpoints_by_root_url.keys())

    def _endpoint_client(self, root_url):
        return self._api_clients_by_root_url[root_url]

    def _default_endpoint_client(self):
        return next(iter(self._api_clients_by_root_url.values()))

    def _record_endpoint_last_response(self, root_url, endpoint_client):
        if hasattr(endpoint_client, "last_response"):
            self.last_response[root_url] = endpoint_client.last_response

    @property
    def default_headers(self):
        return self._default_headers

    @default_headers.setter
    def default_headers(self, value):
        self._default_headers = value
        if hasattr(self, "_api_clients_by_root_url"):
            for endpoint_client in self._api_clients_by_root_url.values():
                endpoint_client.default_headers = value

    @property
    def cookie(self):
        return self._cookie

    @cookie.setter
    def cookie(self, value):
        self._cookie = value
        if hasattr(self, "_api_clients_by_root_url"):
            for endpoint_client in self._api_clients_by_root_url.values():
                endpoint_client.cookie = value

    @property
    def pool(self):
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def select_header_accept(self, accepts):
        return self._default_endpoint_client().select_header_accept(accepts)

    def select_header_content_type(self, content_types, method=None, body=None):
        return self._default_endpoint_client().select_header_content_type(
            content_types, method=method, body=body
        )

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, 'unregister'):
                atexit.unregister(self.close)
        for endpoint_client in self._api_clients_by_root_url.values():
            endpoint_client.close()

    # ------------------------------------------------------------------ #
    # Active endpoint lifecycle
    # ------------------------------------------------------------------ #
    def _clear_active_endpoint(self):
        with self._lock:
            self._current_active_base_url = None

    def _ensure_active_endpoint(self):
        while True:
            with self._lock:
                if self.failover_strategy == FailoverStrategy.ALWAYS_PROBE:
                    self._current_active_base_url = None

                if self._current_active_base_url is not None:
                    endpoint = self._endpoints_by_root_url[
                        self._current_active_base_url
                    ]
                    return endpoint

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
                    if self._current_active_base_url is not None:
                        endpoint = self._endpoints_by_root_url[
                            self._current_active_base_url
                        ]
                        return endpoint
                    if self._discover_err is not None:
                        raise self._discover_err
                # Another thread discovered nothing; retry.
                continue

            try:
                root_url = self._discover()
                with self._lock:
                    endpoint = self._endpoints_by_root_url[root_url]
                    self._current_active_base_url = root_url
                    self._discover_err = None
                return endpoint
            except Exception as e:
                with self._lock:
                    self._discover_err = e
                raise
            finally:
                event.set()
                with self._lock:
                    self._discover_event = None
                    self._discover_err = None

    def _discover(self):
        active_root_urls = []
        failures = []

        for root_url, endpoint in self._endpoints_by_root_url.items():
            try:
                state = self._probe_endpoint(endpoint)
                if state == HOST_STATE_ACTIVE:
                    active_root_urls.append(root_url)
            except Exception as e:
                failures.append("{}: {}".format(root_url, str(e)))

        if len(active_root_urls) == 1:
            logger.debug(
                "active-passive discover found active root URL: {}".format(
                    active_root_urls[0]
                ),
            )
            return active_root_urls[0]
        elif len(active_root_urls) == 0:
            if len(failures) == 0:
                raise ActivePassiveNoActiveHost(
                    status=0,
                    endpoints=self._endpoint_root_urls(),
                )
            raise ActivePassiveNoActiveHost(
                status=0,
                reason=(
                    "active-passive discover found no active root URL: {}"
                    .format("; ".join(failures))
                ),
                endpoints=self._endpoint_root_urls(),
                failures=failures,
            )
        else:
            raise ActivePassiveMultipleActives(
                status=0,
                reason=(
                    "active-passive discover found multiple active root URLs: {}"
                    .format(
                        ", ".join(
                            self._endpoints_by_root_url[h].host
                            for h in active_root_urls
                        )
                    )
                ),
                endpoints=self._endpoint_root_urls(),
                active_hosts=active_root_urls,
            )

    def _probe_endpoint(self, endpoint):
        endpoint_client = self._endpoint_client(endpoint.root_url)
        is_active = endpoint_client.do_probe(
            endpoint.probe_url, timeout=self._probe_timeout
        )
        return HOST_STATE_ACTIVE if is_active else HOST_STATE_PASSIVE

    # ------------------------------------------------------------------ #
    # Authentication / login
    # ------------------------------------------------------------------ #
    def _login_with_user_config(self, user_config):
        active_endpoint = self._ensure_active_endpoint()

        if isinstance(user_config, dict):
            username = user_config.get("name")
            password = user_config.get("password")
            source = user_config.get("source")
        else:
            username = getattr(user_config, "name", None)
            password = getattr(user_config, "password", None)
            source = getattr(user_config, "source", None)

        login_client = self._endpoint_client(active_endpoint.root_url)
        utils.login(login_client, username, password, source)
        authorization = login_client.configuration.api_key.get("Authorization")
        if authorization is not None:
            for endpoint_client in self._api_clients_by_root_url.values():
                endpoint_client.configuration.api_key[
                    "Authorization"
                ] = authorization

    # ------------------------------------------------------------------ #
    # ApiClient overrides
    # ------------------------------------------------------------------ #
    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None, redirect=None):
        """Send the already-built request URL without following redirects."""
        return self._default_endpoint_client().request(
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
            endpoint_client = self._default_endpoint_client()
            result = endpoint_client.call_api(
                resource_path, method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=body,
                post_params=post_params,
                files=files,
                response_types_map=response_types_map,
                auth_settings=auth_settings,
                _return_http_data_only=_return_http_data_only,
                collection_formats=collection_formats,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
                _host=_host,
                _request_auth=_request_auth,
            )
            self._record_endpoint_last_response(
                endpoint_client.configuration.root_url, endpoint_client
            )
            return result

        for attempt in range(REQUEST_ATTEMPTS):
            active_endpoint = self._ensure_active_endpoint()
            endpoint_client = self._endpoint_client(active_endpoint.root_url)

            try:
                result = endpoint_client.call_api(
                    resource_path, method,
                    path_params=path_params,
                    query_params=query_params,
                    header_params=header_params,
                    body=body,
                    post_params=post_params,
                    files=files,
                    response_types_map=response_types_map,
                    auth_settings=auth_settings,
                    _return_http_data_only=_return_http_data_only,
                    collection_formats=collection_formats,
                    _preload_content=_preload_content,
                    _request_timeout=_request_timeout,
                    _host=active_endpoint.host,
                    _request_auth=_request_auth,
                )
                self._record_endpoint_last_response(
                    active_endpoint.root_url, endpoint_client
                )
                return result
            except ApiException as e:
                if e.status == HTTP_STATUS_TEMPORARY_REDIRECT:
                    failed_base_url = active_endpoint.root_url
                    self._clear_active_endpoint()
                    if self.failover_strategy in (
                        FailoverStrategy.MANUAL_FAILOVER,
                        FailoverStrategy.ALWAYS_PROBE,
                    ):
                        raise ActivePassiveFailoverRequired(
                            status=HTTP_STATUS_TEMPORARY_REDIRECT,
                            host=failed_base_url,
                            endpoints=self._endpoint_root_urls(),
                            strategy=self.failover_strategy,
                        )
                    if attempt == 0:
                        continue
                    raise ActivePassiveRetryExhausted(
                        status=HTTP_STATUS_TEMPORARY_REDIRECT,
                        host=failed_base_url,
                        endpoints=self._endpoint_root_urls(),
                        strategy=self.failover_strategy,
                    )
                if self._should_clear_active_endpoint_on_error(
                    e, response_types_map
                ):
                    self._clear_active_endpoint()
                raise

    def _should_clear_active_endpoint_on_error(self, err, response_types_map):
        if err.status is None or err.status == 0:
            return True
        if response_types_map is not None and err.status in response_types_map:
            return False
        return True
