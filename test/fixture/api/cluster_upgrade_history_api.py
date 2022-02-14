import pytest

import test.fixture.client
from cloudtower.api.cluster_upgrade_history_api import ClusterUpgradeHistoryApi

@pytest.fixture(scope="session")
def cluster_upgrade_history_api(client):
    return ClusterUpgradeHistoryApi(client)
