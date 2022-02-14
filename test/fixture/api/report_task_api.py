import pytest

import test.fixture.client
from cloudtower.api.report_task_api import ReportTaskApi

@pytest.fixture(scope="session")
def report_task_api(client):
    return ReportTaskApi(client)
