import pytest

import test.fixture.client
from cloudtower_python_sdk.api.security_policy_api import SecurityPolicyApi

@pytest.fixture(scope="session")
def security_policy_api(client):
    return SecurityPolicyApi(client)
