# VmCreationParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_bandwidth_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**max_bandwidth** | **int** |  | [optional] 
**max_iops_policy** | [**VmDiskIoRestrictType**](VmDiskIoRestrictType.md) |  | [optional] 
**max_iops** | **int** |  | [optional] 
**io_policy** | [**VmDiskIoPolicy**](VmDiskIoPolicy.md) |  | [optional] 
**vcpu** | **int** |  | [optional] 
**status** | [**VmStatus**](VmStatus.md) |  | 
**firmware** | [**VmFirmware**](VmFirmware.md) |  | 
**ha** | **bool** |  | 
**vm_nics** | [**list[VmNicParams]**](VmNicParams.md) |  | 
**vm_disks** | [**VmDiskParams**](VmDiskParams.md) |  | 
**memory** | **int** |  | 
**cpu_cores** | **int** |  | 
**cpu_sockets** | **int** |  | 
**guest_os_type** | [**VmGuestsOperationSystem**](VmGuestsOperationSystem.md) |  | [optional] 
**folder_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**host_id** | **str** |  | [optional] 
**cluster_id** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


