import pytest

import test.fixture.client
from cloudtower_python_sdk.api.content_library_vm_template_api import ContentLibraryVmTemplateApi

@pytest.fixture(scope="session")
def content_library_vm_template_api(client):
    return ContentLibraryVmTemplateApi(client)
