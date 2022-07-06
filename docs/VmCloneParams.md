# VmCloneParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_vm_id** | **str** |  | 
**max_bandwidth_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**max_bandwidth** | **int** |  | [optional] 
**max_iops_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**max_iops** | **int** |  | [optional] 
**io_policy** | [**VmDiskIoPolicy**](VmDiskIoPolicy.md) |  | [optional] 
**vcpu** | **int** |  | [optional] 
**status** | [**VmStatus**](VmStatus.md) |  | [optional] 
**firmware** | [**VmFirmware**](VmFirmware.md) |  | [optional] 
**ha** | **bool** |  | [optional] 
**vm_nics** | [**list[VmNicParams]**](VmNicParams.md) |  | [optional] 
**vm_disks** | [**VmDiskParams**](VmDiskParams.md) |  | [optional] 
**memory** | **int** |  | [optional] 
**cpu_cores** | **int** |  | [optional] 
**cpu_sockets** | **int** |  | [optional] 
**guest_os_type** | [**VmGuestsOperationSystem**](VmGuestsOperationSystem.md) |  | [optional] 
**folder_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**host_id** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


