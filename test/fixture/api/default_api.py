import pytest

import test.fixture.client
from cloudtower_python_sdk.api.default_api import DefaultApi

@pytest.fixture(scope="session")
def default_api(client):
    return DefaultApi(client)
