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
)
from cloudtower.api_client import ApiClient
from cloudtower.exceptions import ApiException


class FakeResponse(object):
    def __init__(self, status, data=b""):
        self.status = status
        self.data = data
        self.reason = "OK"

    def getheaders(self):
        return {}

    def getheader(self, name, default=None):
        return default


def make_client(endpoints=("host-a", "host-b"), **kwargs):
    return ActivePassiveApiClient(
        endpoints=list(endpoints),
        base_path="/v2/api",
        schemes=["http"],
        **kwargs
    )


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

    def test_duplicate_endpoints_raises(self):
        with pytest.raises(ActivePassiveDuplicateHost) as exc_info:
            ActivePassiveApiClient(endpoints=["host-a", "host-a"])
        assert exc_info.value.host == "host-a"
        assert exc_info.value.endpoints == ["host-a", "host-a"]


class TestDiscovery(object):
    def test_single_active_host(self):
        client = make_client(endpoints=("host-a",))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.return_value = FakeResponse(200)
            host = client._ensure_active_host()
        assert host == "http://host-a/v2/api"
        assert client.current_active_host == "host-a"

    def test_passive_skipped_active_selected(self):
        client = make_client(endpoints=("host-a", "host-b"))

        def side_effect(method, url, **kwargs):
            if "host-a" in url:
                return FakeResponse(307)
            return FakeResponse(200)

        with mock.patch.object(
            client.rest_client.pool_manager, "request", side_effect=side_effect
        ):
            host = client._ensure_active_host()
        assert host == "http://host-b/v2/api"
        assert client.current_active_host == "host-b"

    def test_no_active_raises(self):
        client = make_client(endpoints=("host-a", "host-b"))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.return_value = FakeResponse(307)
            with pytest.raises(ActivePassiveNoActiveHost) as exc_info:
                client._ensure_active_host()
        assert exc_info.value.endpoints == ["host-a", "host-b"]
        assert exc_info.value.failures is None

    def test_multiple_active_raises(self):
        client = make_client(endpoints=("host-a", "host-b"))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.return_value = FakeResponse(200)
            with pytest.raises(ActivePassiveMultipleActives) as exc_info:
                client._ensure_active_host()
        assert exc_info.value.endpoints == ["host-a", "host-b"]
        assert exc_info.value.active_hosts == ["host-a", "host-b"]

    def test_probe_error_recorded(self):
        client = make_client(endpoints=("host-a",))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.side_effect = Exception("connection refused")
            with pytest.raises(ApiException) as exc_info:
                client._ensure_active_host()
            assert "connection refused" in str(exc_info.value)
            assert exc_info.value.endpoints == ["host-a"]
            assert exc_info.value.failures == ["host-a: connection refused"]

    def test_probe_uses_configured_timeout(self):
        client = make_client(endpoints=("host-a",), probe_timeout=12)
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            def probe_side_effect(method, url, **kwargs):
                if "host-a" in url:
                    return FakeResponse(200)
                return FakeResponse(307)

            mock_req.side_effect = probe_side_effect
            client._ensure_active_host()

        timeout = mock_req.call_args[1]["timeout"]
        assert timeout.total == 12


class TestRequestRouting(object):
    def test_request_uses_active_host(self):
        client = make_client(endpoints=("host-a",))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            def probe_side_effect(method, url, **kwargs):
                if "host-a" in url:
                    return FakeResponse(200)
                return FakeResponse(307)

            mock_req.side_effect = probe_side_effect
            client._ensure_active_host()

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.return_value = ("ok", 200, {})
            client.call_api("/test", "GET")

        assert client.configuration.host == "http://host-a/v2/api"
        assert client.current_active_host == "host-a"
        assert mock_call.call_count == 1

    def test_request_disables_redirect_explicitly(self):
        client = make_client(endpoints=("host-a",))
        calls = []

        def request_side_effect(method, url, **kwargs):
            calls.append((method, url, kwargs))
            return FakeResponse(200)

        with mock.patch.object(
            client.rest_client.pool_manager,
            "request",
            side_effect=request_side_effect,
        ):
            client.request("GET", "http://host-a/v2/api/test")

        assert calls[0][2]["redirect"] is False
        assert calls[1][2]["redirect"] is False

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
        client = make_client(endpoints=("host-a", "host-b"))

        probe_calls = []

        def first_probe_side_effect(method, url, **kwargs):
            probe_calls.append(url)
            if "host-a" in url:
                return FakeResponse(200)
            return FakeResponse(307)

        with mock.patch.object(
            client.rest_client.pool_manager, "request", side_effect=first_probe_side_effect
        ):
            # First discover caches host-a
            client._ensure_active_host()

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

            with mock.patch.object(
                client.rest_client.pool_manager,
                "request",
                side_effect=second_probe_side_effect,
            ):
                result = client.call_api("/test", "GET")

        assert result == ("ok", 200, {})
        assert call_count[0] == 2

    def test_second_307_raises_retry_exhausted(self):
        client = make_client(endpoints=("host-a", "host-b"))

        def first_probe_side_effect(method, url, **kwargs):
            if "host-a" in url:
                return FakeResponse(200)
            return FakeResponse(307)

        with mock.patch.object(
            client.rest_client.pool_manager, "request", side_effect=first_probe_side_effect
        ):
            client._ensure_active_host()

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

            with mock.patch.object(
                client.rest_client.pool_manager,
                "request",
                side_effect=second_probe_side_effect,
            ):
                with pytest.raises(ActivePassiveRetryExhausted):
                    client.call_api("/test", "GET")

        assert call_count[0] == 2

    def test_manual_failover_on_307(self):
        client = make_client(
            endpoints=("host-a", "host-b"),
            failover_strategy=FailoverStrategy.MANUAL_FAILOVER,
        )

        def probe_side_effect(method, url, **kwargs):
            if "host-a" in url:
                return FakeResponse(200)
            return FakeResponse(307)

        with mock.patch.object(
            client.rest_client.pool_manager,
            "request",
            side_effect=probe_side_effect,
        ):
            client._ensure_active_host()

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.side_effect = ApiException(status=307, reason="switch")
            with pytest.raises(ActivePassiveFailoverRequired) as exc_info:
                client.call_api("/test", "GET")
        assert exc_info.value.host == "host-a"
        assert exc_info.value.endpoints == ["host-a", "host-b"]
        assert exc_info.value.strategy == FailoverStrategy.MANUAL_FAILOVER

    def test_always_probe_strategy(self):
        client = make_client(
            endpoints=("host-a",),
            failover_strategy=FailoverStrategy.ALWAYS_PROBE,
        )
        probe_count = [0]

        def probe_side_effect(method, url, **kwargs):
            probe_count[0] += 1
            return FakeResponse(200)

        with mock.patch.object(
            client.rest_client.pool_manager, "request", side_effect=probe_side_effect
        ):
            with mock.patch(
                "cloudtower.api_client.ApiClient._ApiClient__call_api"
            ) as mock_call:
                mock_call.return_value = ("ok", 200, {})
                client.call_api("/test", "GET")
                client.call_api("/test", "GET")

        assert probe_count[0] == 2

    def test_always_probe_307_requires_manual_retry(self):
        client = make_client(
            endpoints=("host-a",),
            failover_strategy=FailoverStrategy.ALWAYS_PROBE,
        )

        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.return_value = FakeResponse(200)
            with mock.patch(
                "cloudtower.api_client.ApiClient._ApiClient__call_api"
            ) as mock_call:
                mock_call.side_effect = ApiException(status=307, reason="switch")
                with pytest.raises(ActivePassiveFailoverRequired):
                    client.call_api("/test", "GET")

        assert mock_call.call_count == 1

    def test_explicit_host_bypasses_active_passive(self):
        client = make_client(endpoints=("host-a",))
        with mock.patch.object(
            client, "_ensure_active_host",
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
        assert client.current_active_host is None

    def test_recognizable_error_keeps_cache(self):
        client = make_client(endpoints=("host-a",))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.return_value = FakeResponse(200)
            client._ensure_active_host()

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

        assert client.current_active_host == "host-a"

    def test_unrecognized_error_clears_cache(self):
        client = make_client(endpoints=("host-a",))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.return_value = FakeResponse(200)
            client._ensure_active_host()

        assert client.current_active_host == "host-a"

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.side_effect = ApiException(status=502, reason="bad gateway")
            with pytest.raises(ApiException):
                client.call_api("/test", "GET")

        assert client.current_active_host is None


class TestAsync(object):
    def test_async_request(self):
        client = make_client(endpoints=("host-a",))
        with mock.patch.object(
            client.rest_client.pool_manager, "request"
        ) as mock_req:
            mock_req.return_value = FakeResponse(200)
            client._ensure_active_host()

        with mock.patch(
            "cloudtower.api_client.ApiClient._ApiClient__call_api"
        ) as mock_call:
            mock_call.return_value = ("ok", 200, {})
            future = client.call_api("/test", "GET", async_req=True)
            result = future.get(timeout=5)

        assert result == ("ok", 200, {})
