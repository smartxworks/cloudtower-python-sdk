import pytest

import test.fixture.client
from cloudtower.api.graph_api import GraphApi

@pytest.fixture(scope="session")
def graph_api(client):
    return GraphApi(client)
