from cloudtower.models import GetVmDisksConnectionRequestBody, GetVmDisksRequestBody, VmDiskWhereInput


class TestVmDisk:

    def test_get_vm_disks(self, vm_disk_api):
        vm_disk_api.get_vm_disks(get_vm_disks_request_body=GetVmDisksRequestBody(
            # FIXME: remove the filter after data clear is done
            where=VmDiskWhereInput(
                _not=[
                    VmDiskWhereInput(
                        vm=None
                    )
                ]
            )
        ))
        vm_disk_api.get_vm_disks_connection(
            get_vm_disks_connection_request_body=GetVmDisksConnectionRequestBody())
        assert 0 is 0
