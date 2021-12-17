import pytest

import test.fixture.client
from cloudtower_python_sdk.api.cluster_image_api import ClusterImageApi

@pytest.fixture(scope="session")
def cluster_image_api(client):
    return ClusterImageApi(client)
