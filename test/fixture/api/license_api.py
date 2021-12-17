import pytest

import test.fixture.client
from cloudtower_python_sdk.api.license_api import LicenseApi

@pytest.fixture(scope="session")
def license_api(client):
    return LicenseApi(client)
