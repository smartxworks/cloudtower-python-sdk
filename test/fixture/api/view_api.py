import pytest

import test.fixture.client
from cloudtower_python_sdk.api.view_api import ViewApi

@pytest.fixture(scope="session")
def view_api(client):
    return ViewApi(client)
