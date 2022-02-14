import pytest

import test.fixture.client
from cloudtower.api.witness_api import WitnessApi

@pytest.fixture(scope="session")
def witness_api(client):
    return WitnessApi(client)
