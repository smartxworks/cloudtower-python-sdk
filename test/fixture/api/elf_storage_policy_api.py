import pytest

import test.fixture.client
from cloudtower.api.elf_storage_policy_api import ElfStoragePolicyApi

@pytest.fixture(scope="session")
def elf_storage_policy_api(client):
    return ElfStoragePolicyApi(client)
