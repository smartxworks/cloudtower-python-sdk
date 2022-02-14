import pytest

import test.fixture.client
from cloudtower.api.everoute_package_api import EveroutePackageApi

@pytest.fixture(scope="session")
def everoute_package_api(client):
    return EveroutePackageApi(client)
