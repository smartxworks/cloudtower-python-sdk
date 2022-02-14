import pytest

import test.fixture.client
from cloudtower.api.vcenter_account_api import VcenterAccountApi

@pytest.fixture(scope="session")
def vcenter_account_api(client):
    return VcenterAccountApi(client)
