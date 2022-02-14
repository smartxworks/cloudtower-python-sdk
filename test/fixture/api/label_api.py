import pytest

import test.fixture.client
from cloudtower.api.label_api import LabelApi

@pytest.fixture(scope="session")
def label_api(client):
    return LabelApi(client)
