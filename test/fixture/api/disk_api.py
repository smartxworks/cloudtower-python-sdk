import pytest

import test.fixture.client
from cloudtower.api.disk_api import DiskApi

@pytest.fixture(scope="session")
def disk_api(client):
    return DiskApi(client)
