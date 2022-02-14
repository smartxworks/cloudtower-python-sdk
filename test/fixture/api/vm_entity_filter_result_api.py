import pytest

import test.fixture.client
from cloudtower.api.vm_entity_filter_result_api import VmEntityFilterResultApi

@pytest.fixture(scope="session")
def vm_entity_filter_result_api(client):
    return VmEntityFilterResultApi(client)
