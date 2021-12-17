import pytest

import test.fixture.client
from cloudtower_python_sdk.api.image_connector_api import ImageConnectorApi

@pytest.fixture(scope="session")
def image_connector_api(client):
    return ImageConnectorApi(client)
