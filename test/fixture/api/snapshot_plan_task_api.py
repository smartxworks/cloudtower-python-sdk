import pytest

import test.fixture.client
from cloudtower.api.snapshot_plan_task_api import SnapshotPlanTaskApi

@pytest.fixture(scope="session")
def snapshot_plan_task_api(client):
    return SnapshotPlanTaskApi(client)
