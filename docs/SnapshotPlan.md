# SnapshotPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_delete_num** | **int** |  | 
**auto_execute_num** | **int** |  | 
**cluster** | [**NestedCluster**](NestedCluster.md) |  | 
**description** | **str** |  | 
**end_time** | **str** |  | [optional] 
**entity_async_status** | [**EntityAsyncStatus**](EntityAsyncStatus.md) |  | [optional] 
**exec_h_m** | **object** |  | [optional] 
**execute_intervals** | **list[int]** |  | 
**execute_plan_type** | [**SnapshotPlanExecuteType**](SnapshotPlanExecuteType.md) |  | 
**execution_tasks** | [**list[NestedSnapshotPlanTask]**](NestedSnapshotPlanTask.md) |  | [optional] 
**healthy** | **bool** |  | 
**id** | **str** |  | 
**last_execute_end_time** | **str** |  | [optional] 
**last_execute_status** | [**SnapshotPlanExecuteStatus**](SnapshotPlanExecuteStatus.md) |  | 
**last_execute_time** | **str** |  | [optional] 
**local_id** | **str** |  | 
**logical_size_bytes** | **int** |  | 
**manual_delete_num** | **int** |  | 
**manual_execute_num** | **int** |  | 
**mirror** | **bool** |  | 
**name** | **str** |  | 
**next_execute_time** | **str** |  | [optional] 
**object_num** | **int** |  | 
**physical_size_bytes** | **int** |  | 
**remain_snapshot_num** | **int** |  | 
**snapshot_group_num** | **int** |  | 
**start_time** | **str** |  | 
**status** | [**SnapshotPlanStatus**](SnapshotPlanStatus.md) |  | 
**vms** | [**list[NestedVm]**](NestedVm.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


