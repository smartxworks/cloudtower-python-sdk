import time

from cloudtower.models import (
    GetIscsiConnectionsRequestBody
)


class TestIscsiConnection:
    def test_get_iscsi_connections(self, iscsi_connection_api):
        iscsi_connection_api.get_iscsi_connections(
            get_iscsi_connections_request_body=GetIscsiConnectionsRequestBody()
        )
        assert 0 is 0
