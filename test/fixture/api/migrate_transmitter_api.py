import pytest

import test.fixture.client
from cloudtower.api.migrate_transmitter_api import MigrateTransmitterApi

@pytest.fixture(scope="session")
def migrate_transmitter_api(client):
    return MigrateTransmitterApi(client)
