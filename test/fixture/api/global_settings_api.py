import pytest

import test.fixture.client
from cloudtower.api.global_settings_api import GlobalSettingsApi

@pytest.fixture(scope="session")
def global_settings_api(client):
    return GlobalSettingsApi(client)
