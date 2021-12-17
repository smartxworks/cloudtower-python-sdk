import pytest

import test.fixture.client
from cloudtower_python_sdk.api.everoute_package_api import EveroutePackageApi

@pytest.fixture(scope="session")
def everoute_package_api(client):
    return EveroutePackageApi(client)
