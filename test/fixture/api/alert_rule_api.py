import pytest

import test.fixture.client
from cloudtower.api.alert_rule_api import AlertRuleApi

@pytest.fixture(scope="session")
def alert_rule_api(client):
    return AlertRuleApi(client)
