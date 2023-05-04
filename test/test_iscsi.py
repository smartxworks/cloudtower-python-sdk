from cloudtower.models import (
    GetIscsiConnectionsConnectionRequestBody
)


class TestIscsi:
    def test_get_iscsi_connections_connection_call(self, iscsi_connection_api):
        iscsi_connection_api.get_iscsi_connections_connection(
            get_iscsi_connections_connection_request_body=GetIscsiConnectionsConnectionRequestBody()
        )
        assert 0 is 0
