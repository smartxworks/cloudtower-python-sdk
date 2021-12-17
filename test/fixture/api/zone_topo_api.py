import pytest

import test.fixture.client
from cloudtower_python_sdk.api.zone_topo_api import ZoneTopoApi

@pytest.fixture(scope="session")
def zone_topo_api(client):
    return ZoneTopoApi(client)
