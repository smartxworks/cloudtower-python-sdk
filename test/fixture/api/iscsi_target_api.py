import pytest

import test.fixture.client
from cloudtower_python_sdk.api.iscsi_target_api import IscsiTargetApi

@pytest.fixture(scope="session")
def iscsi_target_api(client):
    return IscsiTargetApi(client)
