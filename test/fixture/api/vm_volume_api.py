import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vm_volume_api import VmVolumeApi

@pytest.fixture(scope="session")
def vm_volume_api(client):
    return VmVolumeApi(client)
