import pytest

import test.fixture.client
from cloudtower_python_sdk.api.log_collection_api import LogCollectionApi

@pytest.fixture(scope="session")
def log_collection_api(client):
    return LogCollectionApi(client)
