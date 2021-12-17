import pytest

import test.fixture.client
from cloudtower_python_sdk.api.nfs_inode_api import NfsInodeApi

@pytest.fixture(scope="session")
def nfs_inode_api(client):
    return NfsInodeApi(client)
