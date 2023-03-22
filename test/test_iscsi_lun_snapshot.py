import time
from cloudtower.models import (
    GetIscsiLunSnapshotsRequestBody,
    GetIscsiLunSnapshotsConnectionRequestBody,
    IscsiLunSnapshotCreationParams,
    IscsiLunSnapshotDeletionParams,
    IscsiLunSnapshotWhereInput,
    IscsiLunCloneParams,
    IscsiLunRollbackParams,
    IscsiLunDeletionParams,
    IscsiLunWhereInput
)


class TestIscsiLunSnapshot:
    def test_get_iscsi_lun_snapshot(self, iscsi_lun_snapshot_api):
        iscsi_lun_snapshot_api.get_iscsi_lun_snapshots(
            get_iscsi_lun_snapshots_request_body=GetIscsiLunSnapshotsRequestBody()
        )
        iscsi_lun_snapshot_api.get_iscsi_lun_snapshots_connection(
            get_iscsi_lun_snapshots_connection_request_body=GetIscsiLunSnapshotsConnectionRequestBody()
        )
        assert 0 is 0

    def test_create_and_delete_iscsi_lun_snapshot(self, iscsi_lun_snapshot_api, iscsi_lun, iscsi_target, wait_task):
        create_param = [
            IscsiLunSnapshotCreationParams(
                iscsi_lun_id=iscsi_lun.id,
                iscsi_target_id=iscsi_target.id,
                name="tower-python-sdk-test-iscsi-lun-snapshot"+str(int(time.time())),
            )
        ]

        create_result = iscsi_lun_snapshot_api.create_iscsi_lun_snapshot(
            iscsi_lun_snapshot_creation_params=create_param
        )
        assert create_result is not None
        wait_task(create_result[0].task_id)

        delete_param = IscsiLunSnapshotDeletionParams(
            where=IscsiLunSnapshotWhereInput(
                id=create_result[0].data.id
            )
        )
        delete_result = iscsi_lun_snapshot_api.delete_iscsi_lun_snapshot(
            delete_iscsi_lun_snapshot_params=delete_param
        )
        assert delete_result is not None
        wait_task(delete_result[0].task_id)

    def test_clone_iscsi_lun_from_snapshot(self, iscsi_lun_api, iscsi_target, iscsi_lun_snapshot, wait_task):
        clone_param = [
            IscsiLunCloneParams(
                iscsi_target_id=iscsi_target.id,
                snapshot_id=iscsi_lun_snapshot.id,
            )
        ]

        clone_result = iscsi_lun_api.clone_iscsi_lun_from_snapshot(
            iscsi_lun_clone_params=clone_param
        )
        assert clone_result is not None
        wait_task(clone_result[0].task_id)

        delete_result = iscsi_lun_api.delete_iscsi_lun(
            iscsi_lun_deletion_params=IscsiLunDeletionParams(
                where=IscsiLunWhereInput(
                    id=clone_result[0].data.id
                )
            )
        )
        wait_task(delete_result[0].task_id)

    def test_rollback_iscsi_lun_from_snapshot(self, iscsi_lun_api, iscsi_lun, iscsi_lun_snapshot, wait_task):
        rollback_params = [
            IscsiLunRollbackParams(
                lun_id=iscsi_lun.id,
                snapshot_id=iscsi_lun_snapshot.id,
            )
        ]

        rollback_result = iscsi_lun_api.rollback_iscsi_lun_from_snapshot(
            iscsi_lun_rollback_params=rollback_params
        )
        assert rollback_result is not None
        wait_task(rollback_result[0].task_id)

        delete_result = iscsi_lun_api.delete_iscsi_lun(
            iscsi_lun_deletion_params=IscsiLunDeletionParams(
                where=IscsiLunWhereInput(
                    id=rollback_result[0].data.id
                )
            )
        )
        wait_task(delete_result[0].task_id)
