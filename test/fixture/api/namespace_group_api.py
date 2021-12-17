import pytest

import test.fixture.client
from cloudtower_python_sdk.api.namespace_group_api import NamespaceGroupApi

@pytest.fixture(scope="session")
def namespace_group_api(client):
    return NamespaceGroupApi(client)
