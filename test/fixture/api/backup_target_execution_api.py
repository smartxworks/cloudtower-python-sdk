import pytest

import test.fixture.client
from cloudtower.api.backup_target_execution_api import BackupTargetExecutionApi

@pytest.fixture(scope="session")
def backup_target_execution_api(self, client):
    return BackupTargetExecutionApi(client)
