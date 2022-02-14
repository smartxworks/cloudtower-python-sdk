import pytest
import time

from cloudtower.models import (
    GetVmPlacementGroupsRequestBody,
    GetVmPlacementGroupsConnectionRequestBody,
    VmPlacementGroupWhereInput,
    VmPlacementGroupCreationParams,
    VmPlacementGroupUpdationParams,
    VmPlacementGroupUpdationParamsData,
    VmPlacementGroupDeletionParams,
    VmVmPolicy
)


class TestVmPlacementGroup:

    def test_get_vm_placement_group(self, vm_placement_group_api):
        vm_placement_group_api.get_vm_placement_groups(
            get_vm_placement_groups_request_body=GetVmPlacementGroupsRequestBody())
        vm_placement_group_api.get_vm_placement_groups_connection(
            get_vm_placement_groups_connection_request_body=GetVmPlacementGroupsConnectionRequestBody())
        assert 0 is 0

    def test_create_update_and_delete_vm_placement_group(self, default_cluster, vm_placement_group_api, wait_task):
        create_param = [
            VmPlacementGroupCreationParams(
                cluster_id=default_cluster.id,
                name="tower-python-sdk-test-vm-placement-group"+str(int(time.time())),
                vm_vm_policy=VmVmPolicy.PREFER_SAME,
                vm_vm_policy_enabled=True,
                vm_host_prefer_policy=False,
                vm_host_must_enabled=False,
                vm_host_prefer_enabled=False,
                enabled=True,
            )
        ]

        create_result = vm_placement_group_api.create_vm_placement_group(
            vm_placement_group_creation_params=create_param)
        assert create_result is not None
        wait_task(create_result[0].task_id)

        update_params = VmPlacementGroupUpdationParams(
            where=VmPlacementGroupWhereInput(
                id=create_result[0].data.id
            ),
            data=VmPlacementGroupUpdationParamsData(
                description="vm_placement_group_updation_test"
            )
        )
        update_result = vm_placement_group_api.update_vm_placement_group(
            vm_placement_group_updation_params=update_params,
        )
        assert update_result is not None
        wait_task(update_result[0].task_id)

        delete_params = VmPlacementGroupDeletionParams(
            where=VmPlacementGroupWhereInput(
                id=create_result[0].data.id
            )
        )
        delete_result = vm_placement_group_api.delete_vm_placement_group(
            vm_placement_group_deletion_params=delete_params
        )
        assert delete_result is not None
        wait_task(delete_result[0].task_id)
