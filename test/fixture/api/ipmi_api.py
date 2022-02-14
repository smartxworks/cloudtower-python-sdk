import pytest

import test.fixture.client
from cloudtower.api.ipmi_api import IpmiApi

@pytest.fixture(scope="session")
def ipmi_api(client):
    return IpmiApi(client)
