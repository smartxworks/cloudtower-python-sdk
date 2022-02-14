import pytest

import test.fixture.client
from cloudtower.api.cluster_api import ClusterApi

@pytest.fixture(scope="session")
def cluster_api(client):
    return ClusterApi(client)
