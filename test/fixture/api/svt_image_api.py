import pytest

import test.fixture.client
from cloudtower.api.svt_image_api import SvtImageApi

@pytest.fixture(scope="session")
def svt_image_api(client):
    return SvtImageApi(client)
