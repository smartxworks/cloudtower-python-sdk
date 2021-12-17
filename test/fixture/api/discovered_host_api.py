import pytest

import test.fixture.client
from cloudtower_python_sdk.api.discovered_host_api import DiscoveredHostApi

@pytest.fixture(scope="session")
def discovered_host_api(client):
    return DiscoveredHostApi(client)
