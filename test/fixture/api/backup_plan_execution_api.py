import pytest

import test.fixture.client
from cloudtower.api.backup_plan_execution_api import BackupPlanExecutionApi

@pytest.fixture(scope="session")
def backup_plan_execution_api(self, client):
    return BackupPlanExecutionApi(client)
