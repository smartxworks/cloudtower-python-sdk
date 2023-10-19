import pytest
import time

from cloudtower.models import (
    VmCreationParams,
    VmStatus,
    VmFirmware,
    VmDiskParams,
    VmUpdateParams,
    VmWhereInput,
    VmOperateParams,
    VmUpdateParamsData,
    GetVmsRequestBody,
    VmCloneParams,
    VmStartParams,
    VmMigrateParams,
    VmStartParamsData,
    GetHostsRequestBody,
    HostWhereInput,
    ClusterWhereInput,
    GetVmsConnectionRequestBody,
    VmAddCdRomParams,
    VmAddCdRomParamsData,
    GetVmDisksRequestBody,
    VmDiskWhereInput,
    VmRemoveCdRomParams,
    VmRemoveCdRomParamsData,
    VmAddDiskParams,
    VmAddDiskParamsData,
    VmAddDiskParamsDataVmDisks,
    Bus,
    VmVolumeElfStoragePolicyType,
    VmUpdateDiskParams,
    VmUpdateDiskParamsData,
    VmRemoveDiskParams,
    VmRemoveDiskParamsData,
    VmAddNicParams,
    VmAddNicParamsData,
    VmUpdateNicParams,
    VmUpdateNicParamsData,
    VmRemoveNicParams,
    VmRemoveNicParamsData,
    VmDeleteParams
)


class TestVm:

    def test_get_vm(self, vm_api):
        vm_api.get_vms(get_vms_request_body=GetVmsRequestBody())
        vm_api.get_vms_connection(get_vms_connection_request_body=GetVmsConnectionRequestBody())
        assert 0 is 0

    def test_create_and_delete_vm(self, vm_api, default_cluster, default_vlan, wait_task):
        creation_params = [
            VmCreationParams(
                cluster_id=default_cluster.id,
                name="tower-python-sdk-test-create-vm" + int(time.time()).__str__(),
                ha=True,
                cpu_cores=1,
                cpu_sockets=1,
                memory=4294967296,
                vcpu=1,
                status=VmStatus.STOPPED,
                firmware=VmFirmware.BIOS,
                vm_nics=[{
                    "connect_vlan_id": default_vlan.id,
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
        assert create_result is not None
        create_task_id = create_result[0].task_id
        create_vm = create_result[0].data
        wait_task(id=create_task_id)
        updation_params = VmUpdateParams(
            data=VmUpdateParamsData(
                description="tower-python-sdk-test-update-description"
            ),
            where=VmWhereInput(
                id=create_vm.id
            )
        )
        update_result = vm_api.update_vm(updation_params)
        assert update_result is not None
        update_task_id = update_result[0].task_id
        update_vm = update_result[0].data
        wait_task(id=update_task_id)
        deletion_params = VmOperateParams(
            where=VmWhereInput(
                id=create_vm.id
            )
        )
        delete_result = vm_api.delete_vm(vm_delete_params=deletion_params)
        delete_task_id = delete_result[0].task_id
        wait_task(id=delete_task_id)
        assert 0 is 0

    def test_clone_vm(self, vm_api, stopped_vm, default_cluster, wait_task):
        clone_result = vm_api.clone_vm(vm_clone_params=[VmCloneParams(
            src_vm_id=stopped_vm.id,
            cluster_id=default_cluster.id,
            name="tower-python-sdk-test-cloned-vm"+str(int(time.time()))
        )])
        assert clone_result is not None
        wait_task(clone_result[0].task_id)
        wait_task(
            vm_api.delete_vm(
                vm_delete_params=VmDeleteParams(
                    where=VmWhereInput(
                        id=clone_result[0].data.id
                    )
                )
            )[0].task_id)
        assert 0 is 0

    def test_start_vm(self, vm_api, stopped_vm, wait_task):
        start_params = VmStartParams(
            where=VmWhereInput(
                id=stopped_vm.id
            )
        )
        start_result = vm_api.start_vm(vm_start_params=start_params)
        assert start_result is not None
        wait_task(start_result[0].task_id)

    def test_migrate_vm(self, host_api, vm_api, default_cluster, stopped_vm, wait_task):
        host = host_api.get_hosts(get_hosts_request_body=GetHostsRequestBody(
            where=HostWhereInput(
                id_not=stopped_vm.host.id if stopped_vm.host is not None else None,
                cluster=ClusterWhereInput(
                    id=default_cluster.id
                )
            )
        ))[0]
        migrate_params = VmMigrateParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmStartParamsData(
                host_id=host.id
            )
        )
        migrate_result = vm_api.migrate_vm(vm_migrate_params=migrate_params)
        assert migrate_result is not None
        wait_task(migrate_result[0].task_id)
        wait_task(
            vm_api.delete_vm(vm_delete_params=VmOperateParams(
                where=VmWhereInput(
                    id=migrate_result[0].data.id
                )
            ))[0].task_id
        )

    def test_restart_vm(self, vm_api, running_vm, wait_task):
        restart_param = VmOperateParams(
            where=VmWhereInput(
                id=running_vm.id
            )
        )
        restart_result = vm_api.restart_vm(vm_operate_params=restart_param)
        assert restart_result is not None
        wait_task(restart_result[0].task_id)

    def test_force_restart_vm(self, vm_api, running_vm, wait_task):
        force_restart_param = VmOperateParams(
            where=VmWhereInput(
                id=running_vm.id
            )
        )
        force_restart_result = vm_api.force_restart_vm(vm_operate_params=force_restart_param)
        assert force_restart_result is not None
        wait_task(force_restart_result[0].task_id)

    def test_suspend_resume_vm(self, vm_api, running_vm, wait_task):
        operate_param = VmOperateParams(
            where=VmWhereInput(
                id=running_vm.id
            )
        )
        suspend_result = vm_api.suspend_vm(vm_operate_params=operate_param)
        assert suspend_result is not None
        wait_task(suspend_result[0].task_id)
        resume_result = vm_api.resume_vm(vm_operate_params=operate_param)
        assert resume_result is not None
        wait_task(resume_result[0].task_id)

    @pytest.mark.skip(reason="we cannot shutdown a vm without system installed")
    def test_shudown_vm(self, vm_api, running_vm, wait_task):
        shutdown_param = VmOperateParams(
            where=VmWhereInput(
                id=running_vm.id
            )
        )
        shutdown_result = vm_api.shut_down_vm(vm_operate_params=shutdown_param)
        assert shutdown_result is not None
        wait_task(shutdown_result[0].task_id)

    def test_poweroff_vm(self, vm_api, running_vm, wait_task):
        force_shutdown_param = VmOperateParams(
            where=VmWhereInput(
                id=running_vm.id
            )
        )
        force_shutdown_result = vm_api.poweroff_vm(vm_operate_params=force_shutdown_param)
        assert force_shutdown_result is not None
        wait_task(force_shutdown_result[0].task_id)

    def test_add_and_remove_vm_cd_rom(self, vm_api, vm_disk_api, stopped_vm, wait_task):
        add_cd_rom_param = VmAddCdRomParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmAddCdRomParamsData(
                vm_cd_roms=[
                    {
                        "boot": 2,
                        "index": 2
                    }
                ]
            )
        )
        add_cd_rom_result = vm_api.add_vm_cd_rom(vm_add_cd_rom_params=add_cd_rom_param)
        assert add_cd_rom_result is not None
        wait_task(add_cd_rom_result[0].task_id)
        vm_disk = vm_disk_api.get_vm_disks(
            get_vm_disks_request_body=GetVmDisksRequestBody(
                where=VmDiskWhereInput(
                    boot=2,
                    vm=VmWhereInput(
                        id=stopped_vm.id
                    )
                )
            )
        )[0]
        remove_cd_rom_param = VmRemoveCdRomParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmRemoveCdRomParamsData(
                cd_rom_ids=[
                    vm_disk.id
                ]
            )
        )
        remove_cd_rom_result = vm_api.remove_vm_cd_rom(vm_remove_cd_rom_params=remove_cd_rom_param)
        assert remove_cd_rom_result is not None
        wait_task(remove_cd_rom_result[0].task_id)

    def test_add_update_and_remove_vm_disk(self, vm_api, stopped_vm, wait_task):
        add_vm_disk_param = VmAddDiskParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmAddDiskParamsData(
                vm_disks=VmAddDiskParamsDataVmDisks(
                    mount_new_create_disks=[
                        {
                            "bus": Bus.IDE,
                            "boot": 2,
                            "vm_volume": {
                                "elf_storage_policy": VmVolumeElfStoragePolicyType._2_THIN_PROVISION,
                                "name": "tower-python-sdk-vm-operate-disk-volume" + str(int(time.time())),
                                "size": 1073741824
                            }
                        }
                    ]
                )
            )
        )
        add_vm_disk_result = vm_api.add_vm_disk(vm_add_disk_params=add_vm_disk_param)
        assert add_vm_disk_result is not None
        wait_task(add_vm_disk_result[0].task_id)

        update_vm_disk_params = VmUpdateDiskParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmUpdateDiskParamsData(
                bus=Bus.SCSI,
                vm_disk_id=add_vm_disk_result[0].data.vm_disks[0].id,
            )
        )
        update_vm_disk_result = vm_api.update_vm_disk(vm_update_disk_params=update_vm_disk_params)
        assert update_vm_disk_result is not None
        wait_task(update_vm_disk_result[0].task_id)
        remove_vm_disk_params = VmRemoveDiskParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmRemoveDiskParamsData(
                disk_ids=[
                    add_vm_disk_result[0].data.vm_disks[0].id
                ]
            )
        )
        remove_vm_disk_result = vm_api.remove_vm_disk(vm_remove_disk_params=remove_vm_disk_params)
        assert remove_vm_disk_result is not None
        wait_task(remove_vm_disk_result[0].task_id)

    def test_add_update_and_remove_vm_nic(self, vm_api, default_vlan, stopped_vm, wait_task):
        add_vm_nic_param = VmAddNicParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmAddNicParamsData(
                vm_nics=[
                    {
                        "connect_vlan_id": default_vlan.id
                    }
                ]
            )
        )
        add_vm_nic_result = vm_api.add_vm_nic(vm_add_nic_params=add_vm_nic_param)
        assert add_vm_nic_result is not None
        wait_task(add_vm_nic_result[0].task_id)

        update_vm_nic_param = VmUpdateNicParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmUpdateNicParamsData(
                nic_index=0,
                enabled=False
            )
        )
        update_vm_nic_result = vm_api.update_vm_nic(vm_update_nic_params=update_vm_nic_param)
        assert update_vm_nic_result is not None
        wait_task(update_vm_nic_result[0].task_id)

        remove_vm_nic_param = VmRemoveNicParams(
            where=VmWhereInput(
                id=stopped_vm.id
            ),
            data=VmRemoveNicParamsData(
                nic_index=[0]
            )
        )

        remove_vm_nic_result = vm_api.remove_vm_nic(vm_remove_nic_params=remove_vm_nic_param)
        assert remove_vm_nic_result is not None
        wait_task(remove_vm_nic_result[0].task_id)

    def test_move_to_and_recover_from_recycle_bin(self, vm_api, stopped_vm, open_recycle_bin_if_close, wait_task):
        open_recycle_bin_if_close()
        move_to_recycle_bin_result = vm_api.move_vm_to_recycle_bin(
            vm_operate_params=VmOperateParams(
                where=VmWhereInput(
                    id=stopped_vm.id
                )
            )
        )
        assert move_to_recycle_bin_result is not None
        wait_task(move_to_recycle_bin_result[0].task_id)
        recover_from_recycle_bin_result = vm_api.recover_vm_from_recycle_bin(
            vm_operate_params=VmOperateParams(
                where=VmWhereInput(
                    id=stopped_vm.id
                )
            )
        )
        assert recover_from_recycle_bin_result is not None
        wait_task(recover_from_recycle_bin_result[0].task_id)
