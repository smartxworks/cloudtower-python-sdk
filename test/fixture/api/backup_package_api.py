import pytest

import test.fixture.client
from cloudtower.api.backup_package_api import BackupPackageApi

@pytest.fixture(scope="session")
def backup_package_api(self, client):
    return BackupPackageApi(client)
