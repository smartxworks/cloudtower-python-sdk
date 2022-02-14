import pytest

import test.fixture.client
from cloudtower.api.alert_notifier_api import AlertNotifierApi

@pytest.fixture(scope="session")
def alert_notifier_api(client):
    return AlertNotifierApi(client)
