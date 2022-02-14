import time
import pytest
from cloudtower.models import (
    IscsiLunCreationParams,
    IscsiLunDeletionParams,
    IscsiLunDeletionParamsData,
    IscsiLunWhereInput
)


@pytest.fixture(scope="function")
def iscsi_lun(iscsi_lun_api, iscsi_target, wait_task):
    create_param = [
        IscsiLunCreationParams(
            iscsi_target_id=iscsi_target.id,
            name="tower-python-sdk-test-iscsi-lun"+str(int(time.time())),
            replica_num=2,
            assigned_size=30.0 * 1024 * 1024 * 1024
        )
    ]
    create_result = iscsi_lun_api.create_iscsi_lun(
        iscsi_lun_creation_params=create_param
    )
    wait_task(create_result[0].task_id)
    yield create_result[0].data

    delete_param = IscsiLunDeletionParams(
        where=IscsiLunWhereInput(
            id=create_result[0].data.id
        ),
        data=IscsiLunDeletionParamsData(
            remove_snapshot=True
        )
    )
    delete_result = iscsi_lun_api.delete_iscsi_lun(
        iscsi_lun_deletion_params=delete_param
    )
    assert delete_result is not None
    wait_task(delete_result[0].task_id)
