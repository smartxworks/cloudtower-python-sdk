import time
from cloudtower.models import (
    GetIscsiTargetsRequestBody,
    GetIscsiTargetsConnectionRequestBody,
    IscsiTargetCreationParams,
    IscsiTargetUpdationParams,
    IscsiTargetWhereInput,
    IscsiTargetCommonParams,
    IscsiTargetDeletionParams
)


class TestIscsiTarget:
    def test_get_iscsi_target(self, iscsi_target_api):
        iscsi_target_api.get_iscsi_targets(
            get_iscsi_targets_request_body=GetIscsiTargetsRequestBody()
        )
        iscsi_target_api.get_iscsi_targets_connection(
            get_iscsi_targets_connection_request_body=GetIscsiTargetsConnectionRequestBody()
        )
        assert 0 is 0

    def test_create_update_and_delete_iscsi_target(self, iscsi_target_api, default_cluster, wait_task):
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
        assert create_result is not None
        wait_task(create_result[0].task_id)
        
        update_param = IscsiTargetUpdationParams(
            where=IscsiTargetWhereInput(
                id=create_result[0].data.id
            ),
            data=IscsiTargetCommonParams(
                iops=create_result[0].data.iops,
            )
        )
        update_result = iscsi_target_api.update_iscsi_target(
            iscsi_target_updation_params=update_param
        )
        assert update_result is not None
        wait_task(update_result[0].task_id)

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
