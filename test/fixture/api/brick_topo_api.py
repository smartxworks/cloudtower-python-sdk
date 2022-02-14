import pytest

import test.fixture.client
from cloudtower.api.brick_topo_api import BrickTopoApi

@pytest.fixture(scope="session")
def brick_topo_api(client):
    return BrickTopoApi(client)
