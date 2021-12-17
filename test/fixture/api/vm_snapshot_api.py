import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vm_snapshot_api import VmSnapshotApi

@pytest.fixture(scope="session")
def vm_snapshot_api(client):
    return VmSnapshotApi(client)
