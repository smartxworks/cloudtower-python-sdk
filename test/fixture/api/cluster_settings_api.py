import pytest

import test.fixture.client
from cloudtower.api.cluster_settings_api import ClusterSettingsApi

@pytest.fixture(scope="session")
def cluster_settings_api(client):
    return ClusterSettingsApi(client)
