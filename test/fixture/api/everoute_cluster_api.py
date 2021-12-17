import pytest

import test.fixture.client
from cloudtower_python_sdk.api.everoute_cluster_api import EverouteClusterApi

@pytest.fixture(scope="session")
def everoute_cluster_api(client):
    return EverouteClusterApi(client)
