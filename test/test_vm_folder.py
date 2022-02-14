import pytest
import time
from cloudtower.models import (
    GetVmFoldersConnectionRequestBody,
    GetVmFoldersRequestBody,
    VmFolderWhereInput,
    VmFolderCreationParams,
    VmFolderUpdationParams,
    VmFolderUpdationParamsData,
    VmFolderDeletionParams,
    VmAddFolderParams,
    VmAddFolderParamsData,
    VmWhereInput,
    VmOperateParams
)


class TestVmFolder:

    def test_get_vm_folder(self, vm_folder_api):
        vm_folder_api.get_vm_folders(get_vm_folders_request_body=GetVmFoldersRequestBody())
        vm_folder_api.get_vm_folders_connection(
            get_vm_folders_connection_request_body=GetVmFoldersConnectionRequestBody())
        assert 0 is 0

    def test_create_update_and_delete_vm_folder(self, vm_folder_api, default_cluster, wait_task):
        create_param = [
            VmFolderCreationParams(
                cluster_id=default_cluster.id,
                name="tower-python-sdk-test-vm-folder"+str(int(time.time()))
            )
        ]
        create_result = vm_folder_api.create_vm_folder(vm_folder_creation_params=create_param)
        assert create_result is not None
        wait_task(create_result[0].task_id)

        update_param = VmFolderUpdationParams(
            where=VmFolderWhereInput(
                id=create_result[0].data.id
            ),
            data=VmFolderUpdationParamsData(
                name="tower-python-sdk-test-vm-folder-updated"+str(int(time.time()))
            )
        )
        update_result = vm_folder_api.update_vm_folder(vm_folder_updation_params=update_param)
        assert update_result is not None
        wait_task(update_result[0].task_id)
        delete_param = VmFolderDeletionParams(
            where=VmFolderWhereInput(
                id=create_result[0].data.id
            )
        )
        delete_result = vm_folder_api.delete_vm_folder(vm_folder_deletion_params=delete_param)
        assert delete_result is not None
        wait_task(delete_result[0].task_id)

    def test_add_and_remove_vm_to_folder(self, vm_api, vm_folder, stopped_vm, wait_task):
        add_param = VmAddFolderParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmAddFolderParamsData(
                folder_id=vm_folder.id
            )
        )
        add_result = vm_api.add_vm_to_folder(vm_add_folder_params=add_param)
        assert add_result is not None
        wait_task(add_result[0].task_id)

        remove_param = VmOperateParams(
            where=VmWhereInput(
                id=stopped_vm.id
            )
        )
        remove_result = vm_api.remove_vm_to_folder(vm_operate_params=remove_param)
        assert remove_result is not None
        wait_task(remove_result[0].task_id)
