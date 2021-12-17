import pytest

import test.fixture.client
from cloudtower_python_sdk.api.host_api import HostApi

@pytest.fixture(scope="session")
def host_api(client):
    return HostApi(client)
