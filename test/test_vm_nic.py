from cloudtower.models import (
    GetVmNicsRequestBody,
    GetVmNicsConnectionRequestBody,
    VmNicWhereInput,
    VmWhereInput
)


class TestVmNic:
    def test_get_vm_nics(self, vm_nic_api):
        vm_nic_api.get_vm_nics(
            get_vm_nics_request_body=GetVmNicsRequestBody(
                where=VmNicWhereInput(
                    _not=VmNicWhereInput(
                        vm=None
                    )
                )
            )
        )
        vm_nic_api.get_vm_nics_connection(
            get_vm_nics_connection_request_body=GetVmNicsConnectionRequestBody())
        assert 0 is 0
