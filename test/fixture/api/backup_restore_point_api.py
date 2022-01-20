import pytest

import test.fixture.client
from cloudtower_python_sdk.api.backup_restore_point_api import BackupRestorePointApi

@pytest.fixture(scope="session")
def backup_restore_point_api(self, client):
    return BackupRestorePointApi(client)
