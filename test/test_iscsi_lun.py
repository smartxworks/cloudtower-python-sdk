import time
from cloudtower.models import (
    IscsiLunCreationParams,
    IscsiLunWhereInput,
    IscsiLunUpdationParams,
    IscsiLunDeletionParams,
    IscsiLunDeletionParamsData,
    GetIscsiLunsRequestBody,
    GetIscsiLunsConnectionRequestBody
)


class TestIscsiLun:
    def test_get_iscsi_lun(self, iscsi_lun_api):
        iscsi_lun_api.get_iscsi_luns(
            get_iscsi_luns_request_body=GetIscsiLunsRequestBody()
        )
        iscsi_lun_api.get_iscsi_luns_connection(
            get_iscsi_luns_connection_request_body=GetIscsiLunsConnectionRequestBody()
        )
        assert 0 is 0

    def test_create_update_and_delete_iscsi_lun(self, iscsi_lun_api, iscsi_target, wait_task):
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
        assert create_result is not None
        wait_task(create_result[0].task_id)

        update_param = IscsiLunUpdationParams(
            where=IscsiLunWhereInput(
                id=create_result[0].data.id
            ),
            data={
                "name": "tower-python-sdk-test-iscsi-lun-updated"+str(int(time.time()))
            }
        )
        update_result = iscsi_lun_api.update_iscsi_lun(
            iscsi_lun_updation_params=update_param
        )
        assert update_result is not None
        wait_task(update_result[0].task_id)

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
