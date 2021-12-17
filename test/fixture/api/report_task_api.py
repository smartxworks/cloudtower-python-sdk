import pytest

import test.fixture.client
from cloudtower_python_sdk.api.report_task_api import ReportTaskApi

@pytest.fixture(scope="session")
def report_task_api(client):
    return ReportTaskApi(client)
