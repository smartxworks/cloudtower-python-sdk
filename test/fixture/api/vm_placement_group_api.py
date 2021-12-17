import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vm_placement_group_api import VmPlacementGroupApi

@pytest.fixture(scope="session")
def vm_placement_group_api(client):
    return VmPlacementGroupApi(client)
