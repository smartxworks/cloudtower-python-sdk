import pytest

import test.fixture.client
from cloudtower.api.vm_nic_api import VmNicApi

@pytest.fixture(scope="session")
def vm_nic_api(client):
    return VmNicApi(client)
