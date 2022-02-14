import pytest

import test.fixture.client
from cloudtower.api.license_api import LicenseApi

@pytest.fixture(scope="session")
def license_api(client):
    return LicenseApi(client)
