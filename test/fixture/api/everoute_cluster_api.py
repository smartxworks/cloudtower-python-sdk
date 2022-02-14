import pytest

import test.fixture.client
from cloudtower.api.everoute_cluster_api import EverouteClusterApi

@pytest.fixture(scope="session")
def everoute_cluster_api(client):
    return EverouteClusterApi(client)
