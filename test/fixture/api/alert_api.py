import pytest

import test.fixture.client
from cloudtower_python_sdk.api.alert_api import AlertApi

@pytest.fixture(scope="session")
def alert_api(client):
    return AlertApi(client)
