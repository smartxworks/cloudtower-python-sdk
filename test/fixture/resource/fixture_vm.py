import pytest
import time

from cloudtower.models import (
    VmCreationParams,
    VmDiskParams,
    VmStatus,
    VmFirmware,
    VmWhereInput,
    GetVmsRequestBody,
    VmOperateParams,
    VmDeleteParams
)


@pytest.fixture(scope="function")
def stopped_vm(default_cluster, default_vlan, vm_api, wait_task, wait_entity_async_status):
    creation_params = [
        VmCreationParams(
            cluster_id=default_cluster.id,
            name="tower-python-sdk-test-stopped-vm" + int(time.time()).__str__(),
            ha=True,
            cpu_cores=1,
            cpu_sockets=1,
            memory=4294967296,
            vcpu=1,
            status=VmStatus.STOPPED,
            firmware=VmFirmware.BIOS,
            vm_nics=[{
                "connect_vlan_id": default_vlan.id,
                "local_id": ""
            }],
            vm_disks=VmDiskParams(
                mount_cd_roms=[{
                    "index": 1,
                    "boot": 1
                }]
            )
        )
    ]
    create_result = vm_api.create_vm(creation_params)
    create_task_id = create_result[0].task_id
    create_vm = create_result[0].data
    vm_where_input = VmWhereInput(
        id=create_vm.id
    )
    wait_task(id=create_task_id)
    yield create_vm
    vms = vm_api.get_vms(get_vms_request_body=GetVmsRequestBody(
        where=vm_where_input
    ))
    # return if the vm is already deleted in the previous operation
    if len(vms) == 0:
        return
    vm = vms[0]
    wait_entity_async_status(vm_api, 'get_vms', GetVmsRequestBody(
        where=vm_where_input
    ))
    # close vm if vm is running
    if vm.status == VmStatus.RUNNING:
        task_id = vm_api.poweroff_vm(vm_operate_params=VmOperateParams(
            where=vm_where_input
        ))[0].task_id
        wait_task(id=task_id)
    delete_result = vm_api.delete_vm(vm_delete_params=VmDeleteParams(
        where=vm_where_input
    ))
    wait_task(delete_result[0].task_id)


@pytest.fixture(scope="function")
def running_vm(default_cluster, default_vlan, vm_api, wait_task, wait_entity_async_status):
    creation_params = [
        VmCreationParams(
            cluster_id=default_cluster.id,
            name="tower-python-sdk-test-running-vm" + int(time.time()).__str__(),
            ha=True,
            cpu_cores=1,
            cpu_sockets=1,
            memory=4294967296,
            vcpu=1,
            status=VmStatus.RUNNING,
            firmware=VmFirmware.BIOS,
            vm_nics=[{
                "connect_vlan_id": default_vlan.id,
                "local_id": ""
            }],
            vm_disks=VmDiskParams(
                mount_cd_roms=[{
                    "index": 1,
                    "boot": 1
                }]
            )
        )
    ]
    create_result = vm_api.create_vm(creation_params)
    create_task_id = create_result[0].task_id
    create_vm = create_result[0].data
    vm_where_input = VmWhereInput(
        id=create_vm.id
    )
    wait_task(id=create_task_id)
    yield create_vm
    vms = vm_api.get_vms(get_vms_request_body=GetVmsRequestBody(
        where=vm_where_input
    ))
    # return if the vm is already deleted in the previous operation
    if len(vms) == 0:
        return
    vm = vms[0]
    wait_entity_async_status(vm_api, 'get_vms', GetVmsRequestBody(
        where=vm_where_input
    ))
    # close vm if vm is running
    if vm.status == VmStatus.RUNNING:
        task_id = vm_api.poweroff_vm(vm_operate_params=VmOperateParams(
            where=vm_where_input
        ))[0].task_id
        wait_task(id=task_id)
    delete_result = vm_api.delete_vm(vm_delete_params=VmDeleteParams(
        where=vm_where_input
    ))
    wait_task(delete_result[0].task_id)
