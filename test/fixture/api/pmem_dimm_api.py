import pytest

import test.fixture.client
from cloudtower_python_sdk.api.pmem_dimm_api import PmemDimmApi

@pytest.fixture(scope="session")
def pmem_dimm_api(client):
    return PmemDimmApi(client)
