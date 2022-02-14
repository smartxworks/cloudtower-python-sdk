import pytest
import time

from cloudtower.models import (
    VmFolderCreationParams,
    VmFolderDeletionParams,
    VmFolderWhereInput
)


@pytest.fixture(scope="function")
def vm_folder(vm_folder_api, default_cluster, wait_task):
    create_param = [
        VmFolderCreationParams(
            cluster_id=default_cluster.id,
            name="tower-python-sdk-test-vm-folder"+str(int(time.time()))
        )
    ]
    create_result = vm_folder_api.create_vm_folder(vm_folder_creation_params=create_param)
    wait_task(create_result[0].task_id)
    yield create_result[0].data
    delete_param = VmFolderDeletionParams(
        where=VmFolderWhereInput(
            id=create_result[0].data.id
        )
    )
    delete_result = vm_folder_api.delete_vm_folder(vm_folder_deletion_params=delete_param)
    wait_task(delete_result[0].task_id)
