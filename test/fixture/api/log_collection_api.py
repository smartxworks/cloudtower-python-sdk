import pytest

import test.fixture.client
from cloudtower.api.log_collection_api import LogCollectionApi

@pytest.fixture(scope="session")
def log_collection_api(client):
    return LogCollectionApi(client)
