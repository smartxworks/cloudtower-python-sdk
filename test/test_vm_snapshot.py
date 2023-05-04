import time
from cloudtower.models import (
    GetVmSnapshotsRequestBody,
    GetVmSnapshotsConnectionRequestBody,
    VmSnapshotCreationParams,
    VmSnapshotCreationParamsData,
    VmSnapshotDeletionParams,
    VmSnapshotWhereInput,
    VmRebuildParams,
    VmDeleteParams,
    VmWhereInput,
    VmRollbackParams,
    VmRollbackParamsData
)


class TestVmSnapshot:
    def test_get_vm_snapshots(self, vm_snapshot_api):
        vm_snapshot_api.get_vm_snapshots(get_vm_snapshots_request_body=GetVmSnapshotsRequestBody())
        vm_snapshot_api.get_vm_snapshots_connection(
            get_vm_snapshots_connection_request_body=GetVmSnapshotsConnectionRequestBody())
        assert 0 is 0

    def test_create_and_delete_vm_snapshot(self, stopped_vm, vm_snapshot_api, wait_task):
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
        assert create_result is not None
        wait_task(create_result[0].task_id)

        delete_params = VmSnapshotDeletionParams(
            where=VmSnapshotWhereInput(
                id=create_result[0].data.id
            )
        )
        delete_result = vm_snapshot_api.delete_vm_snapshot(
            vm_snapshot_deletion_params=delete_params
        )
        wait_task(delete_result[0].task_id)

    def test_rollback_vm(self, vm_api, vm_snapshot, stopped_vm, wait_task):
        rollback_params = VmRollbackParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmRollbackParamsData(
                snapshot_id=vm_snapshot.id
            )
        )
        rollback_result = vm_api.rollback_vm(vm_rollback_params=rollback_params)
        assert rollback_result is not None
        wait_task(rollback_result[0].task_id)
        

    def test_rebuild_vm(self, vm_api, vm_snapshot, default_cluster, wait_task):
        rebuld_params = [VmRebuildParams(
            cluster_id=default_cluster.id,
            rebuild_from_snapshot_id=vm_snapshot.id,
            name="tower-python-sdk-test-vm-rebuild"+str(int(time.time()))
        )]
        rebuild_result = vm_api.rebuild_vm(vm_rebuild_params=rebuld_params)
        assert rebuild_result is not None
        wait_task(rebuild_result[0].task_id)
        wait_task(
            vm_api.delete_vm(
                vm_delete_params=VmDeleteParams(
                    where=VmWhereInput(
                        id=rebuild_result[0].data.id
                    )
                )
            )[0].task_id
        )
