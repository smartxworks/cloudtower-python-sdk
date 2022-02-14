import pytest

import test.fixture.client
from cloudtower.api.entity_filter_api import EntityFilterApi

@pytest.fixture(scope="session")
def entity_filter_api(client):
    return EntityFilterApi(client)
