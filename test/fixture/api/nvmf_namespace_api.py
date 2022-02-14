import pytest

import test.fixture.client
from cloudtower.api.nvmf_namespace_api import NvmfNamespaceApi

@pytest.fixture(scope="session")
def nvmf_namespace_api(client):
    return NvmfNamespaceApi(client)
