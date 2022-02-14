import pytest

import test.fixture.client
from cloudtower.api.pmem_dimm_api import PmemDimmApi

@pytest.fixture(scope="session")
def pmem_dimm_api(client):
    return PmemDimmApi(client)
