import pytest

import test.fixture.client
from cloudtower.api.rack_topo_api import RackTopoApi

@pytest.fixture(scope="session")
def rack_topo_api(client):
    return RackTopoApi(client)
