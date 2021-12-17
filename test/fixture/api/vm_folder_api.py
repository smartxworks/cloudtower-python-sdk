import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vm_folder_api import VmFolderApi

@pytest.fixture(scope="session")
def vm_folder_api(client):
    return VmFolderApi(client)
