# Disk


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_async_status** | [**EntityAsyncStatus**](EntityAsyncStatus.md) |  | [optional] 
**failure_information** | [**NestedDiskFailureInformation**](NestedDiskFailureInformation.md) |  | [optional] 
**firmware** | **str** |  | 
**function** | [**DiskFunction**](DiskFunction.md) |  | [optional] 
**health_status** | [**DiskHealthStatus**](DiskHealthStatus.md) |  | [optional] 
**healthy** | **bool** |  | 
**host** | [**NestedHost**](NestedHost.md) |  | 
**id** | **str** |  | 
**labels** | [**list[NestedLabel]**](NestedLabel.md) |  | [optional] 
**local_id** | **str** |  | 
**model** | **str** |  | 
**mounted** | **bool** |  | 
**name** | **str** |  | 
**numa_node** | **int** |  | [optional] 
**offline** | **bool** |  | 
**partitions** | [**list[NestedPartition]**](NestedPartition.md) |  | 
**path** | **str** |  | 
**persistent_memory_type** | **str** |  | [optional] 
**physical_slot_on_brick** | **int** |  | [optional] 
**pmem_dimms** | [**list[NestedPmemDimm]**](NestedPmemDimm.md) |  | [optional] 
**recommended_usage** | [**DiskUsage**](DiskUsage.md) |  | [optional] 
**remaining_life_percent** | **int** |  | [optional] 
**serial** | **str** |  | 
**size** | **int** |  | 
**type** | [**DiskType**](DiskType.md) |  | 
**usage** | [**DiskUsage**](DiskUsage.md) |  | 
**usage_status** | [**DiskUsageStatus**](DiskUsageStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


