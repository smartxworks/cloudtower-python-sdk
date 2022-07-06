# IscsiTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bps** | **int** |  | [optional] 
**bps_max** | **int** |  | [optional] 
**bps_max_length** | **int** |  | [optional] 
**bps_rd** | **int** |  | [optional] 
**bps_rd_max** | **int** |  | [optional] 
**bps_rd_max_length** | **int** |  | [optional] 
**bps_wr** | **int** |  | [optional] 
**bps_wr_max** | **int** |  | [optional] 
**bps_wr_max_length** | **int** |  | [optional] 
**chap_enabled** | **bool** |  | 
**chap_name** | **str** |  | [optional] 
**chap_secret** | **str** |  | [optional] 
**cluster** | [**NestedCluster**](NestedCluster.md) |  | 
**description** | **str** |  | 
**entity_async_status** | [**EntityAsyncStatus**](EntityAsyncStatus.md) |  | [optional] 
**external_use** | **bool** |  | 
**id** | **str** |  | 
**initiator_chaps** | [**list[NestedInitiatorChap]**](NestedInitiatorChap.md) |  | [optional] 
**internal** | **bool** |  | 
**io_size** | **int** |  | [optional] 
**iops** | **int** |  | [optional] 
**iops_max** | **int** |  | [optional] 
**iops_max_length** | **int** |  | [optional] 
**iops_rd** | **int** |  | [optional] 
**iops_rd_max** | **int** |  | [optional] 
**iops_rd_max_length** | **int** |  | [optional] 
**iops_wr** | **int** |  | [optional] 
**iops_wr_max** | **int** |  | [optional] 
**iops_wr_max_length** | **int** |  | [optional] 
**ip_whitelist** | **str** |  | 
**iqn_name** | **str** |  | 
**iqn_whitelist** | **str** |  | 
**labels** | [**list[NestedLabel]**](NestedLabel.md) |  | [optional] 
**local_id** | **str** |  | 
**luns** | [**list[NestedIscsiLun]**](NestedIscsiLun.md) |  | [optional] 
**name** | **str** |  | 
**replica_num** | **int** |  | 
**stripe_num** | **int** |  | 
**stripe_size** | **int** |  | 
**thin_provision** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


