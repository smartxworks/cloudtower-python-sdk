import pytest

import test.fixture.client
from cloudtower.api.backup_restore_execution_api import BackupRestoreExecutionApi

@pytest.fixture(scope="session")
def backup_restore_execution_api(self, client):
    return BackupRestoreExecutionApi(client)
