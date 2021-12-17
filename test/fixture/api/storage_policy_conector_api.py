import pytest

import test.fixture.client
from cloudtower_python_sdk.api.storage_policy_conector_api import StoragePolicyConectorApi

@pytest.fixture(scope="session")
def storage_policy_conector_api(client):
    return StoragePolicyConectorApi(client)
