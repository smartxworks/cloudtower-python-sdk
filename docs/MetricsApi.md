# cloudtower.MetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_metrics**](MetricsApi.md#get_cluster_metrics) | **POST** /get-cluster-metrics | 
[**get_disk_metrics**](MetricsApi.md#get_disk_metrics) | **POST** /get-disk-metrics | 
[**get_host_metrics**](MetricsApi.md#get_host_metrics) | **POST** /get-host-metrics | 
[**get_host_network_metrics**](MetricsApi.md#get_host_network_metrics) | **POST** /get-host-network-metrics | 
[**get_host_servicek_metrics**](MetricsApi.md#get_host_servicek_metrics) | **POST** /get-host-service-metrics | 
[**get_lun_metrics**](MetricsApi.md#get_lun_metrics) | **POST** /get-lun-metrics | 
[**get_nvmf_namespace_metrics**](MetricsApi.md#get_nvmf_namespace_metrics) | **POST** /get-nvmf-namespace-metrics | 
[**get_scvm_disk_metrics**](MetricsApi.md#get_scvm_disk_metrics) | **POST** /get-scvm-disk-metrics | 
[**get_scvm_metrics**](MetricsApi.md#get_scvm_metrics) | **POST** /get-scvm-metrics | 
[**get_scvm_network_metrics**](MetricsApi.md#get_scvm_network_metrics) | **POST** /get-scvm-network-metrics | 
[**get_scvm_servicek_metrics**](MetricsApi.md#get_scvm_servicek_metrics) | **POST** /get-scvm-service-metrics | 
[**get_top_nvm_volume_metrics**](MetricsApi.md#get_top_nvm_volume_metrics) | **POST** /get-top-n-metrics-in-clusters | 
[**get_vm_metrics**](MetricsApi.md#get_vm_metrics) | **POST** /get-vm-metrics | 
[**get_vm_net_work_metrics**](MetricsApi.md#get_vm_net_work_metrics) | **POST** /get-vm-network-metrics | 
[**get_vm_volume_metrics**](MetricsApi.md#get_vm_volume_metrics) | **POST** /get-vm-volume-metrics | 
[**get_witness_metrics**](MetricsApi.md#get_witness_metrics) | **POST** /get-witness-metrics | 
[**get_zone_metrics**](MetricsApi.md#get_zone_metrics) | **POST** /get-zone-metrics | 


# **get_cluster_metrics**
> list[WithTaskMetric] get_cluster_metrics(get_cluster_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_cluster_metric_input = cloudtower.GetClusterMetricInput() # GetClusterMetricInput | 

    try:
        api_response = api_instance.get_cluster_metrics(get_cluster_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_cluster_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cluster_metric_input** | [**GetClusterMetricInput**](GetClusterMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disk_metrics**
> list[WithTaskMetric] get_disk_metrics(get_disk_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_disk_metric_input = cloudtower.GetDiskMetricInput() # GetDiskMetricInput | 

    try:
        api_response = api_instance.get_disk_metrics(get_disk_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_disk_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_disk_metric_input** | [**GetDiskMetricInput**](GetDiskMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_metrics**
> list[WithTaskMetric] get_host_metrics(get_host_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_host_metric_input = cloudtower.GetHostMetricInput() # GetHostMetricInput | 

    try:
        api_response = api_instance.get_host_metrics(get_host_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_host_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_host_metric_input** | [**GetHostMetricInput**](GetHostMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_network_metrics**
> list[WithTaskMetric] get_host_network_metrics(get_host_network_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_host_network_metric_input = cloudtower.GetHostNetworkMetricInput() # GetHostNetworkMetricInput | 

    try:
        api_response = api_instance.get_host_network_metrics(get_host_network_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_host_network_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_host_network_metric_input** | [**GetHostNetworkMetricInput**](GetHostNetworkMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_servicek_metrics**
> list[WithTaskMetric] get_host_servicek_metrics(get_host_service_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_host_service_metric_input = cloudtower.GetHostServiceMetricInput() # GetHostServiceMetricInput | 

    try:
        api_response = api_instance.get_host_servicek_metrics(get_host_service_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_host_servicek_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_host_service_metric_input** | [**GetHostServiceMetricInput**](GetHostServiceMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lun_metrics**
> list[WithTaskMetric] get_lun_metrics(get_lun_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_lun_metric_input = cloudtower.GetLunMetricInput() # GetLunMetricInput | 

    try:
        api_response = api_instance.get_lun_metrics(get_lun_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_lun_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_lun_metric_input** | [**GetLunMetricInput**](GetLunMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nvmf_namespace_metrics**
> list[WithTaskMetric] get_nvmf_namespace_metrics(get_nvmf_namespace_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_nvmf_namespace_metric_input = cloudtower.GetNvmfNamespaceMetricInput() # GetNvmfNamespaceMetricInput | 

    try:
        api_response = api_instance.get_nvmf_namespace_metrics(get_nvmf_namespace_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_nvmf_namespace_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nvmf_namespace_metric_input** | [**GetNvmfNamespaceMetricInput**](GetNvmfNamespaceMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scvm_disk_metrics**
> list[WithTaskMetric] get_scvm_disk_metrics(get_scvm_disk_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_scvm_disk_metric_input = cloudtower.GetSCVMDiskMetricInput() # GetSCVMDiskMetricInput | 

    try:
        api_response = api_instance.get_scvm_disk_metrics(get_scvm_disk_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_scvm_disk_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_scvm_disk_metric_input** | [**GetSCVMDiskMetricInput**](GetSCVMDiskMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scvm_metrics**
> list[WithTaskMetric] get_scvm_metrics(get_scvm_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_scvm_metric_input = cloudtower.GetScvmMetricInput() # GetScvmMetricInput | 

    try:
        api_response = api_instance.get_scvm_metrics(get_scvm_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_scvm_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_scvm_metric_input** | [**GetScvmMetricInput**](GetScvmMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scvm_network_metrics**
> list[WithTaskMetric] get_scvm_network_metrics(get_scvm_network_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_scvm_network_input = cloudtower.GetScvmNetworkInput() # GetScvmNetworkInput | 

    try:
        api_response = api_instance.get_scvm_network_metrics(get_scvm_network_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_scvm_network_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_scvm_network_input** | [**GetScvmNetworkInput**](GetScvmNetworkInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scvm_servicek_metrics**
> list[WithTaskMetric] get_scvm_servicek_metrics(get_scvm_service_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_scvm_service_metric_input = cloudtower.GetScvmServiceMetricInput() # GetScvmServiceMetricInput | 

    try:
        api_response = api_instance.get_scvm_servicek_metrics(get_scvm_service_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_scvm_servicek_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_scvm_service_metric_input** | [**GetScvmServiceMetricInput**](GetScvmServiceMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_nvm_volume_metrics**
> list[WithTaskMetric] get_top_nvm_volume_metrics(get_top_n_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_top_n_metric_input = cloudtower.GetTopNMetricInput() # GetTopNMetricInput | 

    try:
        api_response = api_instance.get_top_nvm_volume_metrics(get_top_n_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_top_nvm_volume_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_top_n_metric_input** | [**GetTopNMetricInput**](GetTopNMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm_metrics**
> list[WithTaskMetric] get_vm_metrics(get_vm_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_vm_metric_input = cloudtower.GetVmMetricInput() # GetVmMetricInput | 

    try:
        api_response = api_instance.get_vm_metrics(get_vm_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_vm_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vm_metric_input** | [**GetVmMetricInput**](GetVmMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm_net_work_metrics**
> list[WithTaskMetric] get_vm_net_work_metrics(get_vm_net_work_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_vm_net_work_metric_input = cloudtower.GetVmNetWorkMetricInput() # GetVmNetWorkMetricInput | 

    try:
        api_response = api_instance.get_vm_net_work_metrics(get_vm_net_work_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_vm_net_work_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vm_net_work_metric_input** | [**GetVmNetWorkMetricInput**](GetVmNetWorkMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm_volume_metrics**
> list[WithTaskMetric] get_vm_volume_metrics(get_vm_volume_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_vm_volume_metric_input = cloudtower.GetVmVolumeMetricInput() # GetVmVolumeMetricInput | 

    try:
        api_response = api_instance.get_vm_volume_metrics(get_vm_volume_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_vm_volume_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_vm_volume_metric_input** | [**GetVmVolumeMetricInput**](GetVmVolumeMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_witness_metrics**
> list[WithTaskMetric] get_witness_metrics(get_witness_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_witness_metric_input = cloudtower.GetWitnessMetricInput() # GetWitnessMetricInput | 

    try:
        api_response = api_instance.get_witness_metrics(get_witness_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_witness_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_witness_metric_input** | [**GetWitnessMetricInput**](GetWitnessMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_metrics**
> list[WithTaskMetric] get_zone_metrics(get_zone_metric_input)



### Example

* Api Key Authentication (Authorization):
```python
from __future__ import print_function
import time
import cloudtower
from cloudtower.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudtower.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with cloudtower.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.MetricsApi(api_client)
    get_zone_metric_input = cloudtower.GetZoneMetricInput() # GetZoneMetricInput | 

    try:
        api_response = api_instance.get_zone_metrics(get_zone_metric_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_zone_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_zone_metric_input** | [**GetZoneMetricInput**](GetZoneMetricInput.md)|  | 

### Return type

[**list[WithTaskMetric]**](WithTaskMetric.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad request |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

