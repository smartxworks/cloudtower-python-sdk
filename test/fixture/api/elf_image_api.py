import pytest

import test.fixture.client
from cloudtower.api.elf_image_api import ElfImageApi

@pytest.fixture(scope="session")
def elf_image_api(client):
    return ElfImageApi(client)
