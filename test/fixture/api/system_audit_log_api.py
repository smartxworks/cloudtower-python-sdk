import pytest

import test.fixture.client
from cloudtower.api.system_audit_log_api import SystemAuditLogApi

@pytest.fixture(scope="session")
def system_audit_log_api(client):
    return SystemAuditLogApi(client)
