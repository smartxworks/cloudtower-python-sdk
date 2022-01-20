import pytest

import test.fixture.client
from cloudtower_python_sdk.api.backup_store_repository_api import BackupStoreRepositoryApi

@pytest.fixture(scope="session")
def backup_store_repository_api(self, client):
    return BackupStoreRepositoryApi(client)
