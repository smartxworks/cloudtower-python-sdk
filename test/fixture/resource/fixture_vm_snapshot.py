import pytest
import time
from cloudtower.models import (
    VmSnapshotCreationParams,
    VmSnapshotCreationParamsData,
    VmSnapshotDeletionParams,
    VmSnapshotWhereInput
)


@pytest.fixture(scope="function")
def vm_snapshot(stopped_vm, vm_snapshot_api, wait_task):
    create_param = VmSnapshotCreationParams(
        data=[
            VmSnapshotCreationParamsData(
                vm_id=stopped_vm.id,
                name="tower-python-sdk-test-vm-snapshot"+str(int(time.time()))
            ),
        ]
    )

    create_result = vm_snapshot_api.create_vm_snapshot(
        vm_snapshot_creation_params=create_param
    )
    wait_task(create_result[0].task_id)
    yield create_result[0].data

    delete_params = VmSnapshotDeletionParams(
        where=VmSnapshotWhereInput(
            id=create_result[0].data.id
        )
    )
    delete_result = vm_snapshot_api.delete_vm_snapshot(
        vm_snapshot_deletion_params=delete_params
    )
    wait_task(delete_result[0].task_id)
