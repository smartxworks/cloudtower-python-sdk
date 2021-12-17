import pytest

import test.fixture.client
from cloudtower_python_sdk.api.disk_api import DiskApi

@pytest.fixture(scope="session")
def disk_api(client):
    return DiskApi(client)
