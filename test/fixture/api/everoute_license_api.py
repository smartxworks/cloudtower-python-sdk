import pytest

import test.fixture.client
from cloudtower.api.everoute_license_api import EverouteLicenseApi

@pytest.fixture(scope="session")
def everoute_license_api(client):
    return EverouteLicenseApi(client)
