import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vlan_api import VlanApi

@pytest.fixture(scope="session")
def vlan_api(client):
    return VlanApi(client)
