# cloudtower.IscsiLunSnapshotApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iscsi_lun_snapshot**](IscsiLunSnapshotApi.md#create_iscsi_lun_snapshot) | **POST** /create-iscsi-lun-snapshot | 
[**delete_iscsi_lun_snapshot**](IscsiLunSnapshotApi.md#delete_iscsi_lun_snapshot) | **POST** /delete-iscsi-lun-snapshot | 
[**get_iscsi_lun_snapshots**](IscsiLunSnapshotApi.md#get_iscsi_lun_snapshots) | **POST** /get-iscsi-lun-snapshots | 
[**get_iscsi_lun_snapshots_connection**](IscsiLunSnapshotApi.md#get_iscsi_lun_snapshots_connection) | **POST** /get-iscsi-lun-snapshots-connection | 


# **create_iscsi_lun_snapshot**
> list[WithTaskIscsiLunSnapshot] create_iscsi_lun_snapshot(iscsi_lun_snapshot_creation_params, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunSnapshotApi(api_client)
    iscsi_lun_snapshot_creation_params = [cloudtower.IscsiLunSnapshotCreationParams()] # list[IscsiLunSnapshotCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.create_iscsi_lun_snapshot(iscsi_lun_snapshot_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunSnapshotApi->create_iscsi_lun_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iscsi_lun_snapshot_creation_params** | [**list[IscsiLunSnapshotCreationParams]**](IscsiLunSnapshotCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskIscsiLunSnapshot]**](WithTaskIscsiLunSnapshot.md)

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

# **delete_iscsi_lun_snapshot**
> list[WithTaskDeleteIscsiLunSnapshot] delete_iscsi_lun_snapshot(iscsi_lun_snapshot_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunSnapshotApi(api_client)
    iscsi_lun_snapshot_deletion_params = cloudtower.IscsiLunSnapshotDeletionParams() # IscsiLunSnapshotDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_iscsi_lun_snapshot(iscsi_lun_snapshot_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunSnapshotApi->delete_iscsi_lun_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iscsi_lun_snapshot_deletion_params** | [**IscsiLunSnapshotDeletionParams**](IscsiLunSnapshotDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteIscsiLunSnapshot]**](WithTaskDeleteIscsiLunSnapshot.md)

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

# **get_iscsi_lun_snapshots**
> list[IscsiLunSnapshot] get_iscsi_lun_snapshots(get_iscsi_lun_snapshots_request_body, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunSnapshotApi(api_client)
    get_iscsi_lun_snapshots_request_body = cloudtower.GetIscsiLunSnapshotsRequestBody() # GetIscsiLunSnapshotsRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_iscsi_lun_snapshots(get_iscsi_lun_snapshots_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunSnapshotApi->get_iscsi_lun_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_iscsi_lun_snapshots_request_body** | [**GetIscsiLunSnapshotsRequestBody**](GetIscsiLunSnapshotsRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[IscsiLunSnapshot]**](IscsiLunSnapshot.md)

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

# **get_iscsi_lun_snapshots_connection**
> IscsiLunSnapshotConnection get_iscsi_lun_snapshots_connection(get_iscsi_lun_snapshots_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunSnapshotApi(api_client)
    get_iscsi_lun_snapshots_connection_request_body = cloudtower.GetIscsiLunSnapshotsConnectionRequestBody() # GetIscsiLunSnapshotsConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_iscsi_lun_snapshots_connection(get_iscsi_lun_snapshots_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunSnapshotApi->get_iscsi_lun_snapshots_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_iscsi_lun_snapshots_connection_request_body** | [**GetIscsiLunSnapshotsConnectionRequestBody**](GetIscsiLunSnapshotsConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**IscsiLunSnapshotConnection**](IscsiLunSnapshotConnection.md)

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

