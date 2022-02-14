import pytest

import test.fixture.client
from cloudtower.api.consistency_group_api import ConsistencyGroupApi

@pytest.fixture(scope="session")
def consistency_group_api(client):
    return ConsistencyGroupApi(client)
