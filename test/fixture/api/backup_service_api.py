import pytest

import test.fixture.client
from cloudtower_python_sdk.api.backup_service_api import BackupServiceApi

@pytest.fixture(scope="session")
def backup_service_api(self, client):
    return BackupServiceApi(client)
