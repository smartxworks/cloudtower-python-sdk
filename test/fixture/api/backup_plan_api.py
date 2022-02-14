import pytest

import test.fixture.client
from cloudtower.api.backup_plan_api import BackupPlanApi

@pytest.fixture(scope="session")
def backup_plan_api(self, client):
    return BackupPlanApi(client)
