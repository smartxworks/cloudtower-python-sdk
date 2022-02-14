import pytest

import test.fixture.client
from cloudtower.api.zone_api import ZoneApi

@pytest.fixture(scope="session")
def zone_api(client):
    return ZoneApi(client)
