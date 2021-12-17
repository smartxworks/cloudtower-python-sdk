import pytest

import test.fixture.client
from cloudtower_python_sdk.api.datacenter_api import DatacenterApi

@pytest.fixture(scope="session")
def datacenter_api(client):
    return DatacenterApi(client)
