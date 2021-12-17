import pytest

import test.fixture.client
from cloudtower_python_sdk.api.graph_api import GraphApi

@pytest.fixture(scope="session")
def graph_api(client):
    return GraphApi(client)
