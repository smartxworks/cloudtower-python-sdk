import pytest

import test.fixture.client
from cloudtower.api.vsphere_esxi_account_api import VsphereEsxiAccountApi

@pytest.fixture(scope="session")
def vsphere_esxi_account_api(client):
    return VsphereEsxiAccountApi(client)
