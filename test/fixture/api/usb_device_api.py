import pytest

import test.fixture.client
from cloudtower.api.usb_device_api import UsbDeviceApi

@pytest.fixture(scope="session")
def usb_device_api(client):
    return UsbDeviceApi(client)
