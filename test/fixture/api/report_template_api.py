import pytest

import test.fixture.client
from cloudtower.api.report_template_api import ReportTemplateApi

@pytest.fixture(scope="session")
def report_template_api(client):
    return ReportTemplateApi(client)
