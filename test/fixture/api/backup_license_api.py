import pytest

import test.fixture.client
from cloudtower.api.backup_license_api import BackupLicenseApi

@pytest.fixture(scope="session")
def backup_license_api(self, client):
    return BackupLicenseApi(client)
