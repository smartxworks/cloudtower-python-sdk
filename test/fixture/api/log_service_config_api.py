import pytest

import test.fixture.client
from cloudtower.api.log_service_config_api import LogServiceConfigApi

@pytest.fixture(scope="session")
def log_service_config_api(self, client):
    return LogServiceConfigApi(client)
