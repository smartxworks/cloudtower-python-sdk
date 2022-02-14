import pytest

import test.fixture.client
from cloudtower.api.vm_folder_api import VmFolderApi

@pytest.fixture(scope="session")
def vm_folder_api(client):
    return VmFolderApi(client)
