import pytest

import test.fixture.client
from cloudtower.api.content_library_image_api import ContentLibraryImageApi

@pytest.fixture(scope="session")
def content_library_image_api(client):
    return ContentLibraryImageApi(client)
