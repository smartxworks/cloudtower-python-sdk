import pytest

import test.fixture.client
from cloudtower.api.deploy_api import DeployApi

@pytest.fixture(scope="session")
def deploy_api(client):
    return DeployApi(client)
