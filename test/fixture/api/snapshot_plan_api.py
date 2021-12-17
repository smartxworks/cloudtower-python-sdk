import pytest

import test.fixture.client
from cloudtower_python_sdk.api.snapshot_plan_api import SnapshotPlanApi

@pytest.fixture(scope="session")
def snapshot_plan_api(client):
    return SnapshotPlanApi(client)
