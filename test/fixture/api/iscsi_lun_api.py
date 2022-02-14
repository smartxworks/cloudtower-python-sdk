import pytest

import test.fixture.client
from cloudtower.api.iscsi_lun_api import IscsiLunApi

@pytest.fixture(scope="session")
def iscsi_lun_api(client):
    return IscsiLunApi(client)
