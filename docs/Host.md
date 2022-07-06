# Host


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_ip** | **str** |  | [optional] 
**allocatable_memory_bytes** | **int** |  | 
**chunk_id** | **str** |  | 
**cluster** | [**NestedCluster**](NestedCluster.md) |  | 
**compatible_cpu_models** | **list[str]** |  | 
**cpu_brand** | **str** |  | 
**cpu_fan_speed** | **list[float]** |  | 
**cpu_fan_speed_unit** | [**CpuFanSpeedUnit**](CpuFanSpeedUnit.md) |  | [optional] 
**cpu_hz_per_core** | **int** |  | 
**cpu_model** | **str** |  | 
**cpu_temperature_celsius** | **list[int]** |  | 
**cpu_vendor** | **str** |  | [optional] 
**data_ip** | **str** |  | [optional] 
**disks** | [**list[NestedDisk]**](NestedDisk.md) |  | [optional] 
**failure_data_space** | **int** |  | 
**hdd_data_capacity** | **int** |  | 
**hdd_disk_count** | **int** |  | 
**hypervisor_ip** | **str** |  | [optional] 
**id** | **str** |  | 
**ipmi** | [**NestedIpmi**](NestedIpmi.md) |  | [optional] 
**is_os_in_raid1** | **bool** |  | [optional] 
**labels** | [**list[NestedLabel]**](NestedLabel.md) |  | [optional] 
**local_id** | **str** |  | 
**lsm_cap_disk_safe_umount** | **bool** |  | 
**management_ip** | **str** |  | 
**model** | **str** |  | 
**name** | **str** |  | 
**nested_virtualization** | **bool** |  | 
**nic_count** | **int** |  | 
**nics** | [**list[NestedNic]**](NestedNic.md) |  | [optional] 
**node_topo_local_id** | **str** |  | [optional] 
**os_memory_bytes** | **int** |  | 
**os_version** | **str** |  | [optional] 
**pmem_dimm_capacity** | **int** |  | 
**pmem_dimm_count** | **int** |  | 
**pmem_dimms** | [**list[NestedPmemDimm]**](NestedPmemDimm.md) |  | [optional] 
**pmem_disk_count** | **int** |  | 
**provisioned_cpu_cores** | **int** |  | 
**provisioned_memory_bytes** | **int** |  | 
**running_pause_vm_memory_bytes** | **int** |  | 
**running_vm_num** | **int** |  | [optional] 
**scvm_cpu** | **int** |  | [optional] 
**scvm_memory** | **int** |  | [optional] 
**scvm_name** | **str** |  | [optional] 
**serial** | **str** |  | [optional] 
**ssd_data_capacity** | **int** |  | 
**ssd_disk_count** | **int** |  | 
**state** | [**HostState**](HostState.md) |  | 
**status** | [**HostStatus**](HostStatus.md) |  | 
**stopped_vm_num** | **int** |  | [optional] 
**suspended_vm_num** | **int** |  | [optional] 
**total_cache_capacity** | **int** |  | [optional] 
**total_cpu_cores** | **int** |  | 
**total_cpu_hz** | **int** |  | 
**total_cpu_sockets** | **int** |  | [optional] 
**total_data_capacity** | **int** |  | 
**total_memory_bytes** | **int** |  | 
**usb_devices** | [**list[NestedUsbDevice]**](NestedUsbDevice.md) |  | [optional] 
**used_cpu_hz** | **float** |  | [optional] 
**used_data_space** | **int** |  | 
**used_memory_bytes** | **float** |  | [optional] 
**vm_num** | **int** |  | [optional] 
**vmotion_ip** | **str** |  | [optional] 
**vms** | [**list[NestedVm]**](NestedVm.md) |  | [optional] 
**vsphere_esxi_account** | [**NestedVsphereEsxiAccount**](NestedVsphereEsxiAccount.md) |  | [optional] 
**with_faster_ssd_as_cache** | **bool** |  | [optional] 
**zone** | [**NestedZone**](NestedZone.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


