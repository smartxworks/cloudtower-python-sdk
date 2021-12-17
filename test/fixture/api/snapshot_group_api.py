import pytest

import test.fixture.client
from cloudtower_python_sdk.api.snapshot_group_api import SnapshotGroupApi

@pytest.fixture(scope="session")
def snapshot_group_api(client):
    return SnapshotGroupApi(client)
