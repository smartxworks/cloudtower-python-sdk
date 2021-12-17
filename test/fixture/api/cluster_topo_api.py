import pytest

import test.fixture.client
from cloudtower_python_sdk.api.cluster_topo_api import ClusterTopoApi

@pytest.fixture(scope="session")
def cluster_topo_api(client):
    return ClusterTopoApi(client)
