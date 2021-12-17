import pytest

import test.fixture.client
from cloudtower_python_sdk.api.nfs_export_api import NfsExportApi

@pytest.fixture(scope="session")
def nfs_export_api(client):
    return NfsExportApi(client)
