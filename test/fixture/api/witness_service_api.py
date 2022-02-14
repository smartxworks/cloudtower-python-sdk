import pytest

import test.fixture.client
from cloudtower.api.witness_service_api import WitnessServiceApi

@pytest.fixture(scope="session")
def witness_service_api(client):
    return WitnessServiceApi(client)
