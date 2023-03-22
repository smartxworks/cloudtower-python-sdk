import pytest
import time
from cloudtower.models import (
    IscsiTargetCreationParams,
    IscsiTargetDeletionParams,
    IscsiTargetWhereInput
)


@pytest.fixture(scope="function")
def iscsi_target(iscsi_target_api, default_cluster, wait_task):
    create_param = [
        IscsiTargetCreationParams(
            cluster_id=default_cluster.id,
            thin_provision=True,
            replica_num=2,
            stripe_num=4,
            stripe_size=262144.0,
            name="tower-python-sdk-test-iscsi-target"+str(int(time.time())),
        )
    ]

    create_result = iscsi_target_api.create_iscsi_target(
        iscsi_target_creation_params=create_param
    )
    wait_task(create_result[0].task_id)
    yield create_result[0].data
    delete_param = IscsiTargetDeletionParams(
        where=IscsiTargetWhereInput(
            id=create_result[0].data.id
        )
    )
    delete_result = iscsi_target_api.delete_iscsi_target(
        iscsi_target_deletion_params=delete_param
    )
    assert delete_result is not None
    wait_task(delete_result[0].task_id)
