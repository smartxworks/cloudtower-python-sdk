import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vds_api import VdsApi

@pytest.fixture(scope="session")
def vds_api(client):
    return VdsApi(client)
