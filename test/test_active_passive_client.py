# coding: utf-8
from __future__ import absolute_import

import pytest
try:
    from unittest import mock
except ImportError:
    import mock

from cloudtower.active_passive_client import (
    ActivePassiveApiClient,
    ActivePassiveNoEndpoints,
    ActivePassiveDuplicateHost,
    ActivePassiveNoActiveHost,
    ActivePassiveMultipleActives,
    ActivePassiveFailoverRequired,
    ActivePassiveRetryExhausted,
    FailoverStrategy,
    _coerce_endpoint,
)
from cloudtower.api_client import ApiClient
from cloudtower.configuration import Configuration
from cloudtower.exceptions import ApiException
from cloudtower import utils


class FakeResponse(object):
    def __init__(self, status, data=b""):
        self.status = status
        self.data = data
        self.reason = "OK"

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        return default


def make_client(endpoints=("http://host-a", "http://host-b"), **kwargs):
    return ActivePassiveApiClient(
        endpoints=endpoints,
        **kwargs
    )


class PatchEndpointRequests(object):
    def __init__(self, client, **kwargs):
        self.client = client
        self.kwargs = kwargs
        self.patchers = []
        self.mock = None

    def __enter__(self):
        self.mock = mock.Mock(**self.kwargs)
        for endpoint_client in self.client._api_clients_by_root_url.values():
            patcher = mock.patch.object(
                endpoint_client.rest_client.pool_manager,
                "request",
                self.mock,
            )
            patcher.start()
            self.patchers.append(patcher)
        return self.mock

    def __exit__(self, exc_type, exc_value, traceback):
        for patcher in reversed(self.patchers):
            patcher.stop()


def patch_endpoint_requests(client, **kwargs):
    return PatchEndpointRequests(client, **kwargs)


class TestActivePassiveApiClientInit(object):
    def test_exception_subclasses_have_default_reason(self):
        assert ActivePassiveNoEndpoints(status=0).reason == (
            "active-passive client requires at least one endpoint"
        )
        assert ActivePassiveFailoverRequired(status=307).reason == (
            "active-passive failover required"
        )

    def test_none_endpoints_raises(self):
        with pytest.raises(ActivePassiveNoEndpoints):
            ActivePassiveApiClient(endpoints=None)

    def test_no_endpoints_raises(self):
        with pytest.raises(ActivePassiveNoEndpoints):
            ActivePassiveApiClient(endpoints=[])

    def test_string_endpoint_uses_default_paths(self):
        client = ActivePassiveApiClient(endpoints=["host-a/tower-a"])

        endpoint = client._endpoints_by_root_url["http://host-a/tower-a"]
        assert endpoint.host == "http://host-a/tower-a/v2/api"
        assert endpoint.probe_url == "http://host-a/tower-a/api/healthz"

    def test_string_endpoint_preserves_explicit_scheme(self):
        client = ActivePassiveApiClient(endpoints=["https://host-a/tower-a"])

        endpoint = client._endpoints_by_root_url["https://host-a/tower-a"]
        assert endpoint.host == "https://host-a/tower-a/v2/api"
        assert endpoint.probe_url == "https://host-a/tower-a/api/healthz"

    def test_empty_dict_endpoint_raises(self):
        with pytest.raises(ActivePassiveNoEndpoints):
            ActivePassiveApiClient(endpoints=[{}])

    def test_coerce_endpoint_accepts_structured_dict(self):
        endpoint = _coerce_endpoint({
            "scheme": "https",
            "root_url": "host-a/tower-a",
            "api_path": "/custom/v2",
            "probe_path": "/custom/healthz",
        })

        assert endpoint.root_url == "https://host-a/tower-a"
        assert endpoint.host == "https://host-a/tower-a/custom/v2"
        assert endpoint.probe_url == (
            "https://host-a/tower-a/custom/healthz"
        )

    def test_coerce_endpoint_returns_none_for_invalid_endpoint(self):
        assert _coerce_endpoint({}) is None
        assert _coerce_endpoint(123) is None

    def test_dict_endpoint_uses_explicit_scheme_over_root_url_scheme(self):
        endpoint = _coerce_endpoint({
            "scheme": "https",
            "root_url": "http://host-a/tower-a",
        })

        assert endpoint.root_url == "https://host-a/tower-a"
        assert endpoint.host == "https://host-a/tower-a/v2/api"

    def test_coerce_endpoint_copies_configuration(self):
        configuration = Configuration(root_url="http://host-a/tower-a")

        endpoint = _coerce_endpoint(configuration)
        endpoint.root_url = "http://host-b/tower-b"

        assert endpoint is not configuration
        assert configuration.root_url == "http://host-a/tower-a"
        assert endpoint.root_url == "http://host-b/tower-b"

    def test_duplicate_endpoints_raises(self):
        with pytest.raises(ActivePassiveDuplicateHost) as exc_info:
            ActivePassiveApiClient(
                endpoints=[
                    {"root_url": "http://host-a"},
                    {"root_url": "http://host-a"},
                ]
            )
        assert exc_info.value.host == "http://host-a"
        assert exc_info.value.endpoints == [
            {"root_url": "http://host-a"},
            {"root_url": "http://host-a"},
        ]

    def test_structured_endpoint_keeps_per_node_paths(self):
        client = ActivePassiveApiClient(
            endpoints=[
                {
                    "scheme": "https",
                    "root_url": "host-a/tower-a",
                    "api_path": "/custom/v2",
                    "probe_path": "/custom/healthz",
                }
            ],
        )

        assert "https://host-a/tower-a" in client._endpoints_by_root_url
        endpoint = client._endpoints_by_root_url["https://host-a/tower-a"]
        assert endpoint.host == (
            "https://host-a/tower-a/custom/v2"
        )
        assert endpoint.probe_url == (
            "https://host-a/tower-a/custom/healthz"
        )

    def test_configuration_endpoint_keeps_per_node_paths(self):
        client = ActivePassiveApiClient(
            endpoints=[
                Configuration(
                    root_url="http://host-a/gateway/custom-api",
                    api_path="/graphql",
                    probe_path="/healthz",
                )
            ]
        )

        endpoint = client._endpoints_by_root_url[
            "http://host-a/gateway/custom-api"
        ]
        assert endpoint.host == (
            "http://host-a/gateway/custom-api/graphql"
        )
        assert endpoint.probe_url == (
            "http://host-a/gateway/custom-api/healthz"
        )

    def test_active_passive_client_does_not_keep_own_configuration(self):
        configuration = Configuration(host="http://control-plane/v2/api")
        client = ActivePassiveApiClient(
            endpoints=[
                {
                    "root_url": "http://host-a/tower-a",
                    "api_path": "/custom/v2",
                    "probe_path": "/custom/healthz",
                }
            ],
            configuration=configuration,
        )

        assert not hasattr(client, "configuration")
        assert not hasattr(client, "rest_client")
        assert configuration.host == "http://control-plane/v2/api"
        assert configuration.root_url == "http://control-plane"
        assert configuration.api_path == "/v2/api"
        endpoint_client = client._endpoint_client("http://host-a/tower-a")
        assert endpoint_client.configuration is not configuration
        assert endpoint_client.configuration.host == (
            "http://host-a/tower-a/custom/v2"
        )

        with patch_endpoint_requests(client, return_value=FakeResponse(200)):
            assert client._ensure_active_endpoint().host == (
                "http://host-a/tower-a/custom/v2"
            )

        assert configuration.host == "http://control-plane/v2/api"
        assert configuration.root_url == "http://control-plane"
        assert configuration.api_path == "/v2/api"

    def test_configuration_template_is_copied_to_endpoint_clients(self):
        configuration = Configuration(host="http://control-plane/v2/api")
        configuration.verify_ssl = False
        configuration.proxy = "http://proxy"
        configuration.api_key["Authorization"] = "token-template"

        client = ActivePassiveApiClient(
            endpoints=[
                {
                    "root_url": "http://host-a/tower-a",
                    "api_path": "/graphql",
                    "probe_path": "/healthz",
                }
            ],
            configuration=configuration,
        )

        endpoint_client = client._endpoint_client("http://host-a/tower-a")
        assert endpoint_client.configuration is not configuration
        assert endpoint_client.configuration.verify_ssl is False
        assert endpoint_client.configuration.proxy == "http://proxy"
        assert endpoint_client.configuration.api_key[
            "Authorization"
        ] == "token-template"
        assert endpoint_client.configuration.host == (
            "http://host-a/tower-a/graphql"
        )
        assert configuration.host == "http://control-plane/v2/api"

    def test_ldap_login_uses_temporary_client_with_active_endpoint(self):
        configuration = Configuration(host="http://control-plane/v2/api")
        client = ActivePassiveApiClient(
            endpoints=[
                {
                    "root_url": "http://host-a/tower-a",
                    "api_path": "/v2/api",
                    "probe_path": "/custom/healthz",
                }
            ],
            configuration=configuration,
        )
        seen = {}

        class LoginData(object):
            token = "token-a"

        class LoginResult(object):
            data = LoginData()

        class FakeUserApi(object):
            def __init__(self, api_client):
                seen["login_client"] = api_client

            def login(self, login_params):
                seen["login_params"] = login_params
                return LoginResult()

        def request(api_client, method, url, **kwargs):
            seen["authn_client"] = api_client
            seen["authn_method"] = method
            seen["authn_url"] = url
            return FakeResponse(
                200,
                b'{"data":{"authnStrategies":[{"id":"ldap-id","type":"LDAP"}]}}',
            )

        with client._lock:
            client._current_active_base_url = "http://host-a/tower-a"
        with mock.patch(
            "cloudtower.utils.UserApi",
            FakeUserApi,
        ):
            with mock.patch.object(
                ApiClient,
                "request",
                autospec=True,
                side_effect=request,
            ):
                client._login_with_user_config({
                    "name": "root",
                    "password": "password",
                    "source": "LDAP",
                })

        assert seen["authn_client"] is not client
        assert seen["login_client"] is seen["authn_client"]
        assert seen["authn_client"].configuration.host == (
            "http://host-a/tower-a/v2/api"
        )
        assert seen["authn_method"] == "POST"
        assert seen["authn_url"] == "http://host-a/tower-a/api"
        assert seen["login_params"]["username"] == "root"
        assert seen["login_params"]["password"] == "password"
        assert seen["login_params"]["source"] == "AUTHN"
        assert seen["login_params"]["auth_config_id"] == "ldap-id"
        assert configuration.host == "http://control-plane/v2/api"
        assert "Authorization" not in configuration.api_key
        for endpoint_client in client._api_clients_by_root_url.values():
            assert endpoint_client.configuration.api_key[
                "Authorization"
            ] == "token-a"

    def test_ldap_login_authn_url_removes_custom_api_path(self):
        configuration = Configuration(host="http://control-plane/v2/api")
        client = ActivePassiveApiClient(
            endpoints=[
                {
                    "root_url": "http://host-a/tower-a",
                    "api_path": "/graphql",
                    "probe_path": "/custom/healthz",
                }
            ],
            configuration=configuration,
        )
        seen = {}

        class LoginData(object):
            token = "token-a"

        class LoginResult(object):
            data = LoginData()

        class FakeUserApi(object):
            def __init__(self, api_client):
                pass

            def login(self, login_params):
                seen["login_params"] = login_params
                return LoginResult()

        def request(api_client, method, url, **kwargs):
            seen["authn_url"] = url
            return FakeResponse(
                200,
                b'{"data":{"authnStrategies":[{"id":"ldap-id","type":"LDAP"}]}}',
            )

        with client._lock:
            client._current_active_base_url = "http://host-a/tower-a"
        with mock.patch(
            "cloudtower.utils.UserApi",
            FakeUserApi,
        ):
            with mock.patch.object(
                ApiClient,
                "request",
                autospec=True,
                side_effect=request,
            ):
                client._login_with_user_config({
                    "name": "root",
                    "password": "password",
                    "source": "LDAP",
                })

        assert seen["authn_url"] == "http://host-a/tower-a/api"
        assert seen["login_params"]["source"] == "AUTHN"
        assert seen["login_params"]["auth_config_id"] == "ldap-id"

    def test_build_auth_api_url_falls_back_to_legacy_v2_api_suffix(self):
        class FakeConfiguration(object):
            host = "http://host-a/tower-a/v2/api"
            api_path = "/not-matching"

        assert utils._build_auth_api_url(FakeConfiguration()) == (
            "http://host-a/tower-a/api"
        )


class TestApiClientProbe(object):
    def test_call_api_preserves_api_exception_with_empty_body(self):
        client = ApiClient()
        err = ApiException(status=0, reason="connection failed")

        with mock.patch.object(client, "request", side_effect=err):
            with pytest.raises(ApiException) as exc_info:
                client._ApiClient__call_api(
                    "/v2/api/test",
                    "GET",
                    response_types_map={},
                    auth_settings=[],
                    collection_formats={},
                )

        assert exc_info.value is err
        assert exc_info.value.body is None

    def test_do_probe_uses_explicit_probe_url(self):
        client = ApiClient()
        calls = []

        def request_side_effect(method, url, **kwargs):
            calls.append((method, url, kwargs))
            return FakeResponse(200)

        with mock.patch.object(
            client.rest_client.pool_manager,
            "request",
            side_effect=request_side_effect,
        ):
            assert client.do_probe(
                "http://host-a/tower-a/custom/healthz",
                timeout=12,
            ) is True

        assert len(calls) == 1
        assert calls[0][0] == "GET"
        assert calls[0][1] == "http://host-a/tower-a/custom/healthz"
        assert calls[0][2]["timeout"].total == 12

    def test_do_probe_returns_false_for_redirect(self):
        client = ApiClient()
        calls = []

        def request_side_effect(method, url, **kwargs):
            calls.append(url)
            return FakeResponse(307)

        with mock.patch.object(
            client.rest_client.pool_manager,
            "request",
            side_effect=request_side_effect,
        ):
            assert client.do_probe("http://host-a/custom/probe") is False

        assert calls == ["http://host-a/custom/probe"]


class TestDiscovery(object):
    def test_probe_endpoint_uses_endpoint_probe_url(self):
        client = make_client(
            endpoints=(
                {
                    "root_url": "http://host-a/tower-a",
                    "probe_path": "/custom/healthz",
                },
            ),
            probe_timeout=12,
        )
        endpoint = client._endpoints_by_root_url["http://host-a/tower-a"]
        calls = []

        def do_probe(url, timeout=None):
            calls.append((url, timeout))
            return True

        endpoint_client = client._endpoint_client("http://host-a/tower-a")
        with mock.patch.object(
            endpoint_client, "do_probe", side_effect=do_probe
        ):
            assert client._probe_endpoint(endpoint) == "active"
        assert calls == [("http://host-a/tower-a/custom/healthz", 12)]

    def test_single_active_endpoint(self):
        client = make_client(endpoints=("http://host-a",))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(200)
            endpoint = client._ensure_active_endpoint()
        assert endpoint.host == "http://host-a/v2/api"
        assert client.current_active_base_url == "http://host-a"

    def test_passive_skipped_active_selected(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))

        def side_effect(method, url, **kwargs):
            if "host-a" in url:
                return FakeResponse(307)
            return FakeResponse(200)

        with patch_endpoint_requests(client, side_effect=side_effect):
            endpoint = client._ensure_active_endpoint()
        assert endpoint.host == "http://host-b/v2/api"
        assert client.current_active_base_url == "http://host-b"

    def test_no_active_raises(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(307)
            with pytest.raises(ActivePassiveNoActiveHost) as exc_info:
                client._ensure_active_endpoint()
        assert sorted(exc_info.value.endpoints) == [
            "http://host-a", "http://host-b"
        ]
        assert exc_info.value.failures is None

    def test_multiple_active_raises(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(200)
            with pytest.raises(ActivePassiveMultipleActives) as exc_info:
                client._ensure_active_endpoint()
        assert sorted(exc_info.value.endpoints) == [
            "http://host-a", "http://host-b"
        ]
        assert sorted(exc_info.value.active_hosts) == [
            "http://host-a", "http://host-b"
        ]

    def test_probe_error_recorded(self):
        client = make_client(endpoints=("http://host-a",))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.side_effect = Exception("connection refused")
            with pytest.raises(ApiException) as exc_info:
                client._ensure_active_endpoint()
            assert "connection refused" in str(exc_info.value)
            assert exc_info.value.endpoints == ["http://host-a"]
            assert exc_info.value.failures == [
                "http://host-a: connection refused"
            ]

    def test_discover_error_state_is_cleared_after_failure(self):
        client = make_client(endpoints=("http://host-a",))

        with mock.patch.object(
            client,
            "_discover",
            side_effect=ValueError("discover failed"),
        ):
            with pytest.raises(ValueError):
                client._ensure_active_endpoint()

        assert client._discover_event is None
        assert client._discover_err is None

    def test_probe_uses_configured_timeout(self):
        client = make_client(endpoints=("http://host-a",), probe_timeout=12)
        with patch_endpoint_requests(client) as mock_req:
            def probe_side_effect(method, url, **kwargs):
                if "host-a" in url:
                    return FakeResponse(200)
                return FakeResponse(307)

            mock_req.side_effect = probe_side_effect
            client._ensure_active_endpoint()

        timeout = mock_req.call_args[1]["timeout"]
        assert timeout.total == 12

    def test_endpoint_path_prefix_preserved_for_probe(self):
        client = make_client(endpoints=("http://host-a/tower-a",))
        calls = []

        def probe_side_effect(method, url, **kwargs):
            calls.append(url)
            return FakeResponse(200)

        with patch_endpoint_requests(client, side_effect=probe_side_effect):
            endpoint = client._ensure_active_endpoint()

        assert endpoint.host == "http://host-a/tower-a/v2/api"
        assert client.current_active_base_url == "http://host-a/tower-a"
        assert calls == ["http://host-a/tower-a/api/healthz"]


class TestRequestRouting(object):
    def test_request_uses_active_endpoint(self):
        client = make_client(endpoints=("http://host-a",))
        with patch_endpoint_requests(client) as mock_req:
            def probe_side_effect(method, url, **kwargs):
                if "host-a" in url:
                    return FakeResponse(200)
                return FakeResponse(307)

            mock_req.side_effect = probe_side_effect
            client._ensure_active_endpoint()

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.return_value = ("ok", 200, {})
            client.call_api("/test", "GET")

        assert client.current_active_base_url == "http://host-a"
        assert mock_call.call_count == 1
        assert mock_call.call_args[0][14] == "http://host-a/v2/api"

    def test_request_uses_provided_full_url_without_endpoint_routing(self):
        client = make_client(
            endpoints=(
                "http://host-a/tower-a",
                "http://host-b/gateway/custom-api",
            )
        )
        calls = []

        def request_side_effect(method, url, **kwargs):
            calls.append(url)
            return FakeResponse(200)

        with mock.patch.object(
            client._default_endpoint_client().rest_client.pool_manager,
            "request",
            side_effect=request_side_effect,
        ):
            client.request("GET", "http://host-a/tower-a/v2/api/test")

        assert calls == ["http://host-a/tower-a/v2/api/test"]
        assert client.current_active_base_url is None

    def test_call_api_uses_active_structured_endpoint_api_base_url(self):
        client = ActivePassiveApiClient(
            endpoints=[
                {
                    "root_url": "http://host-a/tower-a",
                    "api_path": "/v2/api",
                    "probe_path": "/api/healthz",
                },
                {
                    "root_url": "http://host-b/gateway/custom-api",
                    "api_path": "/graphql",
                    "probe_path": "/active-passive/healthz",
                },
            ]
        )
        calls = []

        def request_side_effect(method, url, **kwargs):
            calls.append(url)
            if url == "http://host-a/tower-a/api/healthz":
                return FakeResponse(307)
            return FakeResponse(200)

        with patch_endpoint_requests(client, side_effect=request_side_effect):
            client.call_api("/test", "GET", response_types_map={})

        assert set(calls[:-1]) == set([
            "http://host-a/tower-a/api/healthz",
            "http://host-b/gateway/custom-api/active-passive/healthz",
        ])
        assert calls[-1] == "http://host-b/gateway/custom-api/graphql/test"
        assert client.current_active_base_url == (
            "http://host-b/gateway/custom-api"
        )

    def test_call_api_records_endpoint_last_response(self):
        client = make_client(endpoints=("http://host-a",))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(200)
            client._ensure_active_endpoint()

        endpoint_client = client._endpoint_client("http://host-a")
        response = FakeResponse(200, b'{"ok":true}')

        def call_api_side_effect(*args, **kwargs):
            endpoint_client.last_response = response
            return ("ok", 200, {})

        with mock.patch.object(
            endpoint_client,
            "call_api",
            side_effect=call_api_side_effect,
        ):
            result = client.call_api("/test", "GET")

        assert result == ("ok", 200, {})
        assert endpoint_client.last_response is response
        assert client.last_response == {"http://host-a": response}

    def test_explicit_host_records_default_endpoint_last_response(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))
        endpoint_client = client._default_endpoint_client()
        response = FakeResponse(200, b'{"ok":true}')

        def call_api_side_effect(*args, **kwargs):
            endpoint_client.last_response = response
            return ("ok", 200, {})

        with mock.patch.object(
            endpoint_client,
            "call_api",
            side_effect=call_api_side_effect,
        ):
            result = client.call_api(
                "/test",
                "GET",
                _host="http://explicit/v2/api",
            )

        assert result == ("ok", 200, {})
        assert endpoint_client.last_response is response
        assert client.last_response == {"http://host-a": response}

    def test_request_uses_endpoint_snapshot_when_cache_is_cleared(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))
        endpoint = client._endpoints_by_root_url["http://host-a"]
        endpoint_client = client._endpoint_client("http://host-a")

        def ensure_active_endpoint():
            client._clear_active_endpoint()
            return endpoint

        with mock.patch.object(
            client,
            "_ensure_active_endpoint",
            side_effect=ensure_active_endpoint,
        ):
            with mock.patch.object(
                endpoint_client,
                "call_api",
                return_value=("ok", 200, {}),
            ) as mock_call:
                result = client.call_api("/test", "GET")

        assert result == ("ok", 200, {})
        assert mock_call.call_count == 1
        assert mock_call.call_args[1]["_host"] == "http://host-a/v2/api"
        assert client.current_active_base_url is None

    def test_request_disables_redirect_explicitly(self):
        client = make_client(endpoints=("http://host-a",))
        calls = []

        def request_side_effect(method, url, **kwargs):
            calls.append((method, url, kwargs))
            return FakeResponse(200)

        with mock.patch.object(
            client._default_endpoint_client().rest_client.pool_manager,
            "request",
            side_effect=request_side_effect,
        ):
            client.request("GET", "http://host-a/v2/api/test")

        assert len(calls) == 1
        assert calls[0][0] == "GET"
        assert calls[0][1] == "http://host-a/v2/api/test"
        assert calls[0][2]["redirect"] is False

    def test_endpoint_client_disables_redirect_for_call_api(self):
        client = make_client(endpoints=("http://host-a",))
        endpoint_client = client._endpoint_client("http://host-a")
        calls = []

        def request_side_effect(method, url, **kwargs):
            calls.append((method, url, kwargs))
            return FakeResponse(200, b'{"ok": true}')

        with mock.patch.object(
            endpoint_client.rest_client.pool_manager,
            "request",
            side_effect=request_side_effect,
        ):
            endpoint_client.call_api(
                "/test",
                "GET",
                response_types_map={200: "object"},
                auth_settings=[],
                collection_formats={},
                _host="http://host-a/v2/api",
            )

        assert len(calls) == 1
        assert calls[0][1] == "http://host-a/v2/api/test"
        assert calls[0][2]["redirect"] is False

    def test_regular_api_client_keeps_default_redirect_behavior(self):
        client = ApiClient()

        with mock.patch.object(
            client.rest_client.pool_manager,
            "request",
            return_value=FakeResponse(200),
        ) as mock_req:
            client.request("GET", "http://host-a/v2/api/test")

        assert "redirect" not in mock_req.call_args[1]

    def test_307_triggers_failover_and_retry(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))

        probe_calls = []

        def first_probe_side_effect(method, url, **kwargs):
            probe_calls.append(url)
            if "host-a" in url:
                return FakeResponse(200)
            return FakeResponse(307)

        with patch_endpoint_requests(
            client, side_effect=first_probe_side_effect
        ):
            # First discover caches host-a
            client._ensure_active_endpoint()

        # Simulate host-a becoming passive on the first real request
        call_count = [0]

        def call_api_side_effect(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                raise ApiException(status=307, reason="switch")
            return ("ok", 200, {})

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api",
            side_effect=call_api_side_effect,
        ):
            # After the first 307, discover runs again.
            # We need host-b to be active now.
            def second_probe_side_effect(method, url, **kwargs):
                if "host-a" in url:
                    return FakeResponse(307)
                return FakeResponse(200)

            with patch_endpoint_requests(
                client, side_effect=second_probe_side_effect
            ):
                result = client.call_api("/test", "GET")

        assert result == ("ok", 200, {})
        assert call_count[0] == 2

    def test_second_307_raises_retry_exhausted(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))

        def first_probe_side_effect(method, url, **kwargs):
            if "host-a" in url:
                return FakeResponse(200)
            return FakeResponse(307)

        with patch_endpoint_requests(
            client, side_effect=first_probe_side_effect
        ):
            client._ensure_active_endpoint()

        call_count = [0]

        def call_api_side_effect(*args, **kwargs):
            call_count[0] += 1
            raise ApiException(status=307, reason="switch")

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api",
            side_effect=call_api_side_effect,
        ):
            def second_probe_side_effect(method, url, **kwargs):
                if "host-a" in url:
                    return FakeResponse(307)
                return FakeResponse(200)

            with patch_endpoint_requests(
                client, side_effect=second_probe_side_effect
            ):
                with pytest.raises(ActivePassiveRetryExhausted):
                    client.call_api("/test", "GET")

        assert call_count[0] == 2

    def test_manual_failover_on_307(self):
        client = make_client(
            endpoints=("http://host-a", "http://host-b"),
            failover_strategy=FailoverStrategy.MANUAL_FAILOVER,
        )

        def probe_side_effect(method, url, **kwargs):
            if "host-a" in url:
                return FakeResponse(200)
            return FakeResponse(307)

        with patch_endpoint_requests(client, side_effect=probe_side_effect):
            client._ensure_active_endpoint()

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.side_effect = ApiException(status=307, reason="switch")
            with pytest.raises(ActivePassiveFailoverRequired) as exc_info:
                client.call_api("/test", "GET")
        assert exc_info.value.host == "http://host-a"
        assert sorted(exc_info.value.endpoints) == [
            "http://host-a", "http://host-b"
        ]
        assert exc_info.value.strategy == FailoverStrategy.MANUAL_FAILOVER

    def test_always_probe_strategy(self):
        client = make_client(
            endpoints=("http://host-a",),
            failover_strategy=FailoverStrategy.ALWAYS_PROBE,
        )
        probe_count = [0]

        def probe_side_effect(method, url, **kwargs):
            probe_count[0] += 1
            return FakeResponse(200)

        with patch_endpoint_requests(client, side_effect=probe_side_effect):
            with mock.patch(
                "cloudtower.api_client.ApiClient._ApiClient__call_api"
            ) as mock_call:
                mock_call.return_value = ("ok", 200, {})
                client.call_api("/test", "GET")
                client.call_api("/test", "GET")

        assert probe_count[0] == 2

    def test_always_probe_307_requires_manual_retry(self):
        client = make_client(
            endpoints=("http://host-a",),
            failover_strategy=FailoverStrategy.ALWAYS_PROBE,
        )

        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(200)
            with mock.patch(
                "cloudtower.api_client.ApiClient._ApiClient__call_api"
            ) as mock_call:
                mock_call.side_effect = ApiException(status=307, reason="switch")
                with pytest.raises(ActivePassiveFailoverRequired):
                    client.call_api("/test", "GET")

        assert mock_call.call_count == 1

    def test_explicit_host_bypasses_active_passive(self):
        client = make_client(endpoints=("http://host-a",))
        with mock.patch.object(
            client, "_ensure_active_endpoint",
            side_effect=AssertionError("probe should not run"),
        ):
            def call_api_side_effect(*args, **kwargs):
                client.request("GET", "http://explicit/v2/api/test")
                return ("ok", 200, {})

            with mock.patch(
                "cloudtower.api_client.ApiClient._ApiClient__call_api",
                side_effect=call_api_side_effect,
            ):
                with mock.patch(
                    "cloudtower.api_client.ApiClient.request",
                    return_value=FakeResponse(200),
                ):
                    client.call_api(
                        "/test", "GET", _host="http://explicit/v2/api"
                    )

        # No probe should have been triggered because _host was supplied
        assert client.current_active_base_url is None

    def test_explicit_host_uses_default_endpoint_client(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))
        default_client = client._default_endpoint_client()

        with mock.patch.object(
            client,
            "_ensure_active_endpoint",
            side_effect=AssertionError("probe should not run"),
        ):
            with mock.patch.object(
                default_client,
                "call_api",
                return_value=("ok", 200, {}),
            ) as mock_call:
                result = client.call_api(
                    "/test", "GET", _host="http://explicit/v2/api"
                )

        assert result == ("ok", 200, {})
        assert mock_call.call_args[1]["_host"] == "http://explicit/v2/api"
        assert client.current_active_base_url is None

    def test_default_headers_are_shared_by_endpoint_clients(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))

        client.user_agent = "custom-agent"
        client.set_default_header("X-Test", "yes")

        for endpoint_client in client._api_clients_by_root_url.values():
            assert endpoint_client.default_headers is client.default_headers
            assert endpoint_client.default_headers["User-Agent"] == (
                "custom-agent"
            )
            assert endpoint_client.default_headers["X-Test"] == "yes"

    def test_default_headers_assignment_updates_endpoint_clients(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))
        headers = {"User-Agent": "assigned-agent", "X-Test": "yes"}

        client.default_headers = headers

        assert client.default_headers is headers
        for endpoint_client in client._api_clients_by_root_url.values():
            assert endpoint_client.default_headers is headers

    def test_cookie_assignment_updates_endpoint_clients(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))

        client.cookie = "session=updated"

        assert client.cookie == "session=updated"
        for endpoint_client in client._api_clients_by_root_url.values():
            assert endpoint_client.cookie == "session=updated"

    def test_close_closes_all_endpoint_clients(self):
        client = make_client(endpoints=("http://host-a", "http://host-b"))
        close_mocks = []
        patchers = []
        for endpoint_client in client._api_clients_by_root_url.values():
            patcher = mock.patch.object(endpoint_client, "close")
            close_mocks.append(patcher.start())
            patchers.append(patcher)

        try:
            client.close()
        finally:
            for patcher in reversed(patchers):
                patcher.stop()

        for close_mock in close_mocks:
            assert close_mock.call_count == 1

    def test_recognizable_error_keeps_cache(self):
        client = make_client(endpoints=("http://host-a",))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(200)
            client._ensure_active_endpoint()

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.side_effect = ApiException(status=400, reason="bad request")
            with pytest.raises(ApiException):
                client.call_api(
                    "/test",
                    "GET",
                    response_types_map={200: "str", 400: "ErrorBody"},
                )

        assert client.current_active_base_url == "http://host-a"

    def test_unrecognized_error_clears_cache(self):
        client = make_client(endpoints=("http://host-a",))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(200)
            client._ensure_active_endpoint()

        assert client.current_active_base_url == "http://host-a"

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.side_effect = ApiException(status=502, reason="bad gateway")
            with pytest.raises(ApiException):
                client.call_api("/test", "GET")

        assert client.current_active_base_url is None


class TestAsync(object):
    def test_async_request(self):
        client = make_client(endpoints=("http://host-a",))
        with patch_endpoint_requests(client) as mock_req:
            mock_req.return_value = FakeResponse(200)
            client._ensure_active_endpoint()

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.return_value = ("ok", 200, {})
            future = client.call_api("/test", "GET", async_req=True)
            result = future.get(timeout=5)

        assert result == ("ok", 200, {})
