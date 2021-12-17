import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vm_disk_api import VmDiskApi

@pytest.fixture(scope="session")
def vm_disk_api(client):
    return VmDiskApi(client)
