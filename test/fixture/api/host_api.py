import pytest

import test.fixture.client
from cloudtower.api.host_api import HostApi

@pytest.fixture(scope="session")
def host_api(client):
    return HostApi(client)
