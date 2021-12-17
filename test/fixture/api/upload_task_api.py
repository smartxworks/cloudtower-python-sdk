import pytest

import test.fixture.client
from cloudtower_python_sdk.api.upload_task_api import UploadTaskApi

@pytest.fixture(scope="session")
def upload_task_api(client):
    return UploadTaskApi(client)
