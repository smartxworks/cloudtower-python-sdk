import pytest

import test.fixture.client
from cloudtower_python_sdk.api.organization_api import OrganizationApi

@pytest.fixture(scope="session")
def organization_api(client):
    return OrganizationApi(client)
