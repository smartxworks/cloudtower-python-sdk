import pytest

import test.fixture.client
from cloudtower.api.vm_api import VmApi

@pytest.fixture(scope="session")
def vm_api(client):
    return VmApi(client)
