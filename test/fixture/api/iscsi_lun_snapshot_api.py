import pytest

import test.fixture.client
from cloudtower.api.iscsi_lun_snapshot_api import IscsiLunSnapshotApi

@pytest.fixture(scope="session")
def iscsi_lun_snapshot_api(client):
    return IscsiLunSnapshotApi(client)
