import pytest

import test.fixture.client
from cloudtower.api.task_api import TaskApi

@pytest.fixture(scope="session")
def task_api(client):
    return TaskApi(client)
