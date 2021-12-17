import pytest

import test.fixture.client
from cloudtower_python_sdk.api.nic_api import NicApi

@pytest.fixture(scope="session")
def nic_api(client):
    return NicApi(client)
