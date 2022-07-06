# VmTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clock_offset** | [**VmClockOffset**](VmClockOffset.md) |  | 
**cloud_init_supported** | **bool** |  | 
**cluster** | [**NestedCluster**](NestedCluster.md) |  | 
**content_library_vm_template** | [**NestedContentLibraryVmTemplate**](NestedContentLibraryVmTemplate.md) |  | [optional] 
**cpu** | [**NestedCpu**](NestedCpu.md) |  | 
**cpu_model** | **str** |  | 
**description** | **str** |  | 
**entity_async_status** | [**EntityAsyncStatus**](EntityAsyncStatus.md) |  | [optional] 
**firmware** | [**VmFirmware**](VmFirmware.md) |  | 
**ha** | **bool** |  | 
**id** | **str** |  | 
**io_policy** | [**VmDiskIoPolicy**](VmDiskIoPolicy.md) |  | [optional] 
**labels** | [**list[NestedLabel]**](NestedLabel.md) |  | [optional] 
**local_created_at** | **str** |  | [optional] 
**local_id** | **str** |  | 
**max_bandwidth** | **int** |  | [optional] 
**max_bandwidth_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**max_iops** | **int** |  | [optional] 
**max_iops_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**memory** | **int** |  | 
**name** | **str** |  | 
**size** | **int** |  | 
**vcpu** | **int** |  | 
**video_type** | **str** |  | [optional] 
**vm_disks** | [**list[NestedFrozenDisks]**](NestedFrozenDisks.md) |  | [optional] 
**vm_nics** | [**list[NestedTemplateNic]**](NestedTemplateNic.md) |  | [optional] 
**win_opt** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


