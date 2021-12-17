import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vsphere_esxi_account_api import VsphereEsxiAccountApi

@pytest.fixture(scope="session")
def vsphere_esxi_account_api(client):
    return VsphereEsxiAccountApi(client)
