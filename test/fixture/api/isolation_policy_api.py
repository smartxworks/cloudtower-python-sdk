import pytest

import test.fixture.client
from cloudtower_python_sdk.api.isolation_policy_api import IsolationPolicyApi

@pytest.fixture(scope="session")
def isolation_policy_api(client):
    return IsolationPolicyApi(client)
