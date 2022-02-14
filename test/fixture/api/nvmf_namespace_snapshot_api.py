import pytest

import test.fixture.client
from cloudtower.api.nvmf_namespace_snapshot_api import NvmfNamespaceSnapshotApi

@pytest.fixture(scope="session")
def nvmf_namespace_snapshot_api(client):
    return NvmfNamespaceSnapshotApi(client)
