import pytest

import test.fixture.client
from cloudtower_python_sdk.api.consistency_group_snapshot_api import ConsistencyGroupSnapshotApi

@pytest.fixture(scope="session")
def consistency_group_snapshot_api(client):
    return ConsistencyGroupSnapshotApi(client)
