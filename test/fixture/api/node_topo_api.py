import pytest

import test.fixture.client
from cloudtower_python_sdk.api.node_topo_api import NodeTopoApi

@pytest.fixture(scope="session")
def node_topo_api(client):
    return NodeTopoApi(client)
