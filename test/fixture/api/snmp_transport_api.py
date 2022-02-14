import pytest

import test.fixture.client
from cloudtower.api.snmp_transport_api import SnmpTransportApi

@pytest.fixture(scope="session")
def snmp_transport_api(client):
    return SnmpTransportApi(client)
