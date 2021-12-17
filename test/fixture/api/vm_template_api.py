import pytest

import test.fixture.client
from cloudtower_python_sdk.api.vm_template_api import VmTemplateApi

@pytest.fixture(scope="session")
def vm_template_api(client):
    return VmTemplateApi(client)
