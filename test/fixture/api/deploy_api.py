import pytest

import test.fixture.client
from cloudtower_python_sdk.api.deploy_api import DeployApi

@pytest.fixture(scope="session")
def deploy_api(client):
    return DeployApi(client)
