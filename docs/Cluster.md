# Cluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_highest_version** | **str** |  | [optional] 
**applications** | [**list[NestedApplication]**](NestedApplication.md) |  | [optional] 
**architecture** | [**Architecture**](Architecture.md) |  | 
**auto_converge** | **bool** |  | [optional] 
**connect_state** | [**ConnectState**](ConnectState.md) |  | 
**consistency_groups** | [**list[NestedConsistencyGroup]**](NestedConsistencyGroup.md) |  | [optional] 
**current_cpu_model** | **str** |  | [optional] 
**datacenters** | [**list[NestedDatacenter]**](NestedDatacenter.md) |  | [optional] 
**disconnected_date** | **str** |  | [optional] 
**disconnected_reason** | [**ClusterConnectorErrorCode**](ClusterConnectorErrorCode.md) |  | [optional] 
**dns** | **list[str]** |  | 
**entity_async_status** | [**EntityAsyncStatus**](EntityAsyncStatus.md) |  | [optional] 
**everoute_cluster** | [**NestedEverouteCluster**](NestedEverouteCluster.md) |  | [optional] 
**failure_data_space** | **int** |  | [optional] 
**has_metrox** | **bool** |  | [optional] 
**host_num** | **int** |  | [optional] 
**hosts** | [**list[NestedHost]**](NestedHost.md) |  | [optional] 
**hypervisor** | [**Hypervisor**](Hypervisor.md) |  | [optional] 
**id** | **str** |  | 
**ip** | **str** |  | 
**is_all_flash** | **bool** |  | [optional] 
**iscsi_vip** | **str** |  | [optional] 
**labels** | [**list[NestedLabel]**](NestedLabel.md) |  | [optional] 
**license_expire_date** | **str** |  | [optional] 
**license_serial** | **str** |  | [optional] 
**license_sign_date** | **str** |  | [optional] 
**license_type** | [**LicenseType**](LicenseType.md) |  | [optional] 
**local_id** | **str** |  | [optional] 
**maintenance_end_date** | **str** |  | [optional] 
**maintenance_start_date** | **str** |  | [optional] 
**management_vip** | **str** |  | [optional] 
**max_chunk_num** | **int** |  | [optional] 
**max_physical_data_capacity** | **int** |  | [optional] 
**max_physical_data_capacity_per_node** | **int** |  | [optional] 
**metro_availability_checklist** | [**NestedMetroAvailabilityChecklist**](NestedMetroAvailabilityChecklist.md) |  | [optional] 
**mgt_gateway** | **str** |  | [optional] 
**mgt_netmask** | **str** |  | [optional] 
**migration_data_size** | **int** |  | [optional] 
**migration_speed** | **int** |  | [optional] 
**name** | **str** |  | 
**ntp_mode** | [**NtpMode**](NtpMode.md) |  | [optional] 
**ntp_servers** | **list[str]** |  | 
**nvme_over_rdma_enabled** | **bool** |  | [optional] 
**nvme_over_tcp_enabled** | **bool** |  | [optional] 
**nvmf_enabled** | **bool** |  | [optional] 
**pmem_enabled** | **bool** |  | [optional] 
**provisioned_cpu_cores** | **int** |  | [optional] 
**provisioned_cpu_cores_for_active_vm** | **int** |  | [optional] 
**provisioned_for_active_vm_ratio** | **float** |  | [optional] 
**provisioned_memory_bytes** | **int** |  | [optional] 
**provisioned_ratio** | **float** |  | [optional] 
**rdma_enabled** | **bool** |  | [optional] 
**recommended_cpu_models** | **list[str]** |  | 
**recover_data_size** | **int** |  | [optional] 
**recover_speed** | **int** |  | [optional] 
**reserved_cpu_cores_for_system_service** | **int** |  | [optional] 
**running_vm_num** | **int** |  | [optional] 
**settings** | [**NestedClusterSettings**](NestedClusterSettings.md) |  | [optional] 
**software_edition** | [**SoftwareEdition**](SoftwareEdition.md) |  | [optional] 
**stopped_vm_num** | **int** |  | [optional] 
**stretch** | **bool** |  | [optional] 
**suspended_vm_num** | **int** |  | [optional] 
**total_cache_capacity** | **int** |  | [optional] 
**total_cpu_cores** | **int** |  | [optional] 
**total_cpu_hz** | **int** |  | [optional] 
**total_cpu_models** | **list[str]** |  | 
**total_cpu_sockets** | **int** |  | [optional] 
**total_data_capacity** | **int** |  | [optional] 
**total_memory_bytes** | **int** |  | [optional] 
**type** | [**ClusterType**](ClusterType.md) |  | 
**upgrade_tool_version** | **str** |  | [optional] 
**used_cpu_hz** | **float** |  | [optional] 
**used_data_space** | **int** |  | [optional] 
**used_memory_bytes** | **float** |  | [optional] 
**valid_data_space** | **int** |  | [optional] 
**vcenter_account** | [**NestedVcenterAccount**](NestedVcenterAccount.md) |  | [optional] 
**vdses** | [**list[NestedVds]**](NestedVds.md) |  | [optional] 
**version** | **str** |  | 
**vhost_enabled** | **bool** |  | [optional] 
**vm_folders** | [**list[NestedVmFolder]**](NestedVmFolder.md) |  | [optional] 
**vm_num** | **int** |  | [optional] 
**vm_templates** | [**list[NestedVmTemplate]**](NestedVmTemplate.md) |  | [optional] 
**vms** | [**list[NestedVm]**](NestedVm.md) |  | [optional] 
**witness** | [**NestedWitness**](NestedWitness.md) |  | [optional] 
**zones** | [**list[NestedZone]**](NestedZone.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


