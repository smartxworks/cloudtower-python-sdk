# cloudtower.NvmfNamespaceSnapshotApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nvmf_namespace_snapshot**](NvmfNamespaceSnapshotApi.md#create_nvmf_namespace_snapshot) | **POST** /create-nvmf-namespace-snapshot | 
[**delete_nvmf_namespace_snapshot**](NvmfNamespaceSnapshotApi.md#delete_nvmf_namespace_snapshot) | **POST** /delete-nvmf-namespace-snapshot | 
[**get_nvmf_namespace_snapshots**](NvmfNamespaceSnapshotApi.md#get_nvmf_namespace_snapshots) | **POST** /get-nvmf-namespace-snapshots | 
[**get_nvmf_namespace_snapshots_connection**](NvmfNamespaceSnapshotApi.md#get_nvmf_namespace_snapshots_connection) | **POST** /get-nvmf-namespace-snapshots-connection | 


# **create_nvmf_namespace_snapshot**
> list[WithTaskNvmfNamespaceSnapshot] create_nvmf_namespace_snapshot(nvmf_namespace_snapshot_creation_params, content_language=content_language)



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
    api_instance = cloudtower.NvmfNamespaceSnapshotApi(api_client)
    nvmf_namespace_snapshot_creation_params = [cloudtower.NvmfNamespaceSnapshotCreationParams()] # list[NvmfNamespaceSnapshotCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.create_nvmf_namespace_snapshot(nvmf_namespace_snapshot_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvmfNamespaceSnapshotApi->create_nvmf_namespace_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvmf_namespace_snapshot_creation_params** | [**list[NvmfNamespaceSnapshotCreationParams]**](NvmfNamespaceSnapshotCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskNvmfNamespaceSnapshot]**](WithTaskNvmfNamespaceSnapshot.md)

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

# **delete_nvmf_namespace_snapshot**
> list[WithTaskDeleteNvmfNamespaceSnapshot] delete_nvmf_namespace_snapshot(nvmf_namespace_snapshot_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.NvmfNamespaceSnapshotApi(api_client)
    nvmf_namespace_snapshot_deletion_params = cloudtower.NvmfNamespaceSnapshotDeletionParams() # NvmfNamespaceSnapshotDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_nvmf_namespace_snapshot(nvmf_namespace_snapshot_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvmfNamespaceSnapshotApi->delete_nvmf_namespace_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvmf_namespace_snapshot_deletion_params** | [**NvmfNamespaceSnapshotDeletionParams**](NvmfNamespaceSnapshotDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteNvmfNamespaceSnapshot]**](WithTaskDeleteNvmfNamespaceSnapshot.md)

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

# **get_nvmf_namespace_snapshots**
> list[NvmfNamespaceSnapshot] get_nvmf_namespace_snapshots(get_nvmf_namespace_snapshots_request_body, content_language=content_language)



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
    api_instance = cloudtower.NvmfNamespaceSnapshotApi(api_client)
    get_nvmf_namespace_snapshots_request_body = cloudtower.GetNvmfNamespaceSnapshotsRequestBody() # GetNvmfNamespaceSnapshotsRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_nvmf_namespace_snapshots(get_nvmf_namespace_snapshots_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvmfNamespaceSnapshotApi->get_nvmf_namespace_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nvmf_namespace_snapshots_request_body** | [**GetNvmfNamespaceSnapshotsRequestBody**](GetNvmfNamespaceSnapshotsRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[NvmfNamespaceSnapshot]**](NvmfNamespaceSnapshot.md)

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

# **get_nvmf_namespace_snapshots_connection**
> NvmfNamespaceSnapshotConnection get_nvmf_namespace_snapshots_connection(get_nvmf_namespace_snapshots_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.NvmfNamespaceSnapshotApi(api_client)
    get_nvmf_namespace_snapshots_connection_request_body = cloudtower.GetNvmfNamespaceSnapshotsConnectionRequestBody() # GetNvmfNamespaceSnapshotsConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_nvmf_namespace_snapshots_connection(get_nvmf_namespace_snapshots_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvmfNamespaceSnapshotApi->get_nvmf_namespace_snapshots_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nvmf_namespace_snapshots_connection_request_body** | [**GetNvmfNamespaceSnapshotsConnectionRequestBody**](GetNvmfNamespaceSnapshotsConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**NvmfNamespaceSnapshotConnection**](NvmfNamespaceSnapshotConnection.md)

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

