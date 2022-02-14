import pytest

import test.fixture.client
from cloudtower.api.elf_data_store_api import ElfDataStoreApi

@pytest.fixture(scope="session")
def elf_data_store_api(client):
    return ElfDataStoreApi(client)
