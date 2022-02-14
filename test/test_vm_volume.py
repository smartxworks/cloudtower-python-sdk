import time
from cloudtower.models import (
    GetVmVolumesRequestBody,
    GetVmVolumesConnectionRequestBody,
    VmVolumeCreationParams,
    VmVolumeDeletionParams,
    VmVolumeWhereInput,
    VmVolumeElfStoragePolicyType
)


class TestVmVolume:
    def test_get_vm_volumes(self, vm_volume_api):
        vm_volume_api.get_vm_volumes(
            get_vm_volumes_request_body=GetVmVolumesRequestBody()
        )
        vm_volume_api.get_vm_volumes_connection(
            get_vm_volumes_connection_request_body=GetVmVolumesConnectionRequestBody()
        )
        assert 0 is 0

    def test_create_and_delete_vm_volume(self, vm_volume_api, default_cluster, wait_task):
        create_param = [
            VmVolumeCreationParams(
                cluster_id=default_cluster.id,
                name="tower-python-sdk-test-vm-volume"+str(int(time.time())),
                elf_storage_policy=VmVolumeElfStoragePolicyType._2_THIN_PROVISION,
                size=1024*1024*1024,
                sharing=False
            )
        ]
        create_result = vm_volume_api.create_vm_volume(
            vm_volume_creation_params=create_param
        )
        assert create_result is not None
        wait_task(create_result[0].task_id)

        delete_param = VmVolumeDeletionParams(
            where=VmVolumeWhereInput(
                id=create_result[0].data.id
            )
        )
        delete_result = vm_volume_api.delete_vm_volume_from_vm(
            vm_volume_deletion_params=delete_param
        )
        assert delete_result is not None
        wait_task(delete_result[0].task_id)
