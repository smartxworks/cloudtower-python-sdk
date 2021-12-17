import pytest

import test.fixture.client
from cloudtower_python_sdk.api.user_audit_log_api import UserAuditLogApi

@pytest.fixture(scope="session")
def user_audit_log_api(client):
    return UserAuditLogApi(client)
