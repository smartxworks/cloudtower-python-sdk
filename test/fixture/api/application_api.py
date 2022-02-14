import pytest

import test.fixture.client
from cloudtower.api.application_api import ApplicationApi

@pytest.fixture(scope="session")
def application_api(client):
    return ApplicationApi(client)
