import pytest

import test.fixture.client
from cloudtower.api.datacenter_api import DatacenterApi

@pytest.fixture(scope="session")
def datacenter_api(client):
    return DatacenterApi(client)
