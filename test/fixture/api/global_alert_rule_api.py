import pytest

import test.fixture.client
from cloudtower_python_sdk.api.global_alert_rule_api import GlobalAlertRuleApi

@pytest.fixture(scope="session")
def global_alert_rule_api(client):
    return GlobalAlertRuleApi(client)
