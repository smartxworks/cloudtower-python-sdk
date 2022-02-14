import pytest

import test.fixture.client
from cloudtower.api.default_api import DefaultApi

@pytest.fixture(scope="session")
def default_api(client):
    return DefaultApi(client)
