import pytest

import test.fixture.client
from cloudtower_python_sdk.api.migrate_transmitter_api import MigrateTransmitterApi

@pytest.fixture(scope="session")
def migrate_transmitter_api(client):
    return MigrateTransmitterApi(client)
