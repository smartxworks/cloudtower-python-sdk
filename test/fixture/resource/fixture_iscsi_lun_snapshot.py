import pytest
import time

from cloudtower.models import (
    IscsiLunSnapshotCreationParams,
    IscsiLunSnapshotDeletionParams,
    IscsiLunSnapshotWhereInput
)


@pytest.fixture(scope="function")
def iscsi_lun_snapshot(iscsi_lun_snapshot_api, iscsi_lun, iscsi_target, wait_task):
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
    wait_task(create_result[0].task_id)
    yield create_result[0].data
    delete_param = IscsiLunSnapshotDeletionParams(
        where=IscsiLunSnapshotWhereInput(
            id=create_result[0].data.id
        )
    )
    delete_result = iscsi_lun_snapshot_api.delete_iscsi_lun_snapshot(
        delete_iscsi_lun_snapshot_params=delete_param
    )
    assert delete_result is not None
    wait_task(delete_result[0].task_id) if len(delete_result) else None
