import pytest

import test.fixture.client
from cloudtower_python_sdk.api.iscsi_api import IscsiApi

@pytest.fixture(scope="session")
def iscsi_api(client):
    return IscsiApi(client)
