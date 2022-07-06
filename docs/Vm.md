# Vm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clock_offset** | [**VmClockOffset**](VmClockOffset.md) |  | 
**cloud_init_supported** | **bool** |  | [optional] 
**cluster** | [**NestedCluster**](NestedCluster.md) |  | [optional] 
**cpu** | [**NestedCpu**](NestedCpu.md) |  | 
**cpu_model** | **str** |  | 
**cpu_usage** | **float** |  | [optional] 
**deleted_at** | **str** |  | [optional] 
**description** | **str** |  | 
**dns_servers** | **str** |  | [optional] 
**entity_filter_results** | [**list[NestedVmEntityFilterResult]**](NestedVmEntityFilterResult.md) |  | [optional] 
**entity_async_status** | [**EntityAsyncStatus**](EntityAsyncStatus.md) |  | [optional] 
**firmware** | [**VmFirmware**](VmFirmware.md) |  | 
**folder** | [**NestedVmFolder**](NestedVmFolder.md) |  | [optional] 
**guest_cpu_model** | **str** |  | [optional] 
**guest_os_type** | [**VmGuestsOperationSystem**](VmGuestsOperationSystem.md) |  | [optional] 
**guest_size_usage** | **float** |  | [optional] 
**guest_used_size** | **int** |  | [optional] 
**ha** | **bool** |  | 
**host** | [**NestedHost**](NestedHost.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**id** | **str** |  | 
**in_recycle_bin** | **bool** |  | 
**internal** | **bool** |  | 
**io_policy** | [**VmDiskIoPolicy**](VmDiskIoPolicy.md) |  | [optional] 
**ips** | **str** |  | 
**isolation_policy** | [**NestedIsolationPolicy**](NestedIsolationPolicy.md) |  | [optional] 
**kernel_info** | **str** |  | [optional] 
**labels** | [**list[NestedLabel]**](NestedLabel.md) |  | [optional] 
**last_shutdown_time** | **str** |  | [optional] 
**local_created_at** | **str** |  | [optional] 
**local_id** | **str** |  | 
**logical_size_bytes** | **int** |  | [optional] 
**max_bandwidth** | **int** |  | [optional] 
**max_bandwidth_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**max_iops** | **int** |  | [optional] 
**max_iops_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**memory** | **int** |  | 
**memory_usage** | **float** |  | [optional] 
**name** | **str** |  | 
**nested_virtualization** | **bool** |  | 
**node_ip** | **str** |  | 
**original_name** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**out_uninstall_usb** | **list[str]** |  | 
**protected** | **bool** |  | 
**provisioned_size** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**snapshot_plan** | [**NestedSnapshotPlan**](NestedSnapshotPlan.md) |  | [optional] 
**snapshots** | [**list[NestedVmSnapshot]**](NestedVmSnapshot.md) |  | [optional] 
**status** | [**VmStatus**](VmStatus.md) |  | 
**unique_size** | **int** |  | [optional] 
**usb_devices** | [**list[NestedUsbDevice]**](NestedUsbDevice.md) |  | [optional] 
**vcpu** | **int** |  | 
**video_type** | [**VmVideoType**](VmVideoType.md) |  | [optional] 
**vm_disks** | [**list[NestedVmDisk]**](NestedVmDisk.md) |  | [optional] 
**vm_nics** | [**list[NestedVmNic]**](NestedVmNic.md) |  | [optional] 
**vm_placement_group** | [**list[NestedVmPlacementGroup]**](NestedVmPlacementGroup.md) |  | [optional] 
**vm_tools_status** | [**VmToolsStatus**](VmToolsStatus.md) |  | 
**vm_tools_version** | **str** |  | [optional] 
**vm_usage** | [**VmUsage**](VmUsage.md) |  | [optional] 
**win_opt** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


