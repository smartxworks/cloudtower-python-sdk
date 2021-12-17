import pytest

import test.fixture.client
from cloudtower_python_sdk.api.system_audit_log_api import SystemAuditLogApi

@pytest.fixture(scope="session")
def system_audit_log_api(client):
    return SystemAuditLogApi(client)
