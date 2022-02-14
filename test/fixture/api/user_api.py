import pytest

import test.fixture.client
from cloudtower.api.user_api import UserApi

@pytest.fixture(scope="session")
def user_api(client):
    return UserApi(client)
