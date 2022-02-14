import pytest

import test.fixture.client
from cloudtower.api.user_role_next_api import UserRoleNextApi

@pytest.fixture(scope="session")
def user_role_next_api(client):
    return UserRoleNextApi(client)
