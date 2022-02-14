import pytest

import test.fixture.client
from cloudtower.api.snmp_trap_receiver_api import SnmpTrapReceiverApi

@pytest.fixture(scope="session")
def snmp_trap_receiver_api(client):
    return SnmpTrapReceiverApi(client)
