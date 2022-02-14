import pytest

import test.fixture.client
from cloudtower.api.iscsi_connection_api import IscsiConnectionApi

@pytest.fixture(scope="session")
def iscsi_connection_api(client):
    return IscsiConnectionApi(client)
