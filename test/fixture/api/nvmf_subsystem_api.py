import pytest

import test.fixture.client
from cloudtower.api.nvmf_subsystem_api import NvmfSubsystemApi

@pytest.fixture(scope="session")
def nvmf_subsystem_api(client):
    return NvmfSubsystemApi(client)
