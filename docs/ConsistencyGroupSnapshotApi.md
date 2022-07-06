# cloudtower.ConsistencyGroupSnapshotApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consistency_group_snapshot**](ConsistencyGroupSnapshotApi.md#create_consistency_group_snapshot) | **POST** /create-consistency-snapshot-group | 
[**delete_consistency_group_snapshot**](ConsistencyGroupSnapshotApi.md#delete_consistency_group_snapshot) | **POST** /delete-consistency-snapshot-group | 
[**get_consistency_group_snapshots**](ConsistencyGroupSnapshotApi.md#get_consistency_group_snapshots) | **POST** /get-consistency-group-snapshots | 
[**get_consistency_group_snapshots_connection**](ConsistencyGroupSnapshotApi.md#get_consistency_group_snapshots_connection) | **POST** /get-consistency-group-snapshots-connection | 
[**update_consistency_group_snapshot**](ConsistencyGroupSnapshotApi.md#update_consistency_group_snapshot) | **POST** /rollback-consistency-snapshot-group | 


# **create_consistency_group_snapshot**
> list[WithTaskConsistencyGroupSnapshot] create_consistency_group_snapshot(consistency_group_snapshot_creation_params, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupSnapshotApi(api_client)
    consistency_group_snapshot_creation_params = [cloudtower.ConsistencyGroupSnapshotCreationParams()] # list[ConsistencyGroupSnapshotCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.create_consistency_group_snapshot(consistency_group_snapshot_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupSnapshotApi->create_consistency_group_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consistency_group_snapshot_creation_params** | [**list[ConsistencyGroupSnapshotCreationParams]**](ConsistencyGroupSnapshotCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskConsistencyGroupSnapshot]**](WithTaskConsistencyGroupSnapshot.md)

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

# **delete_consistency_group_snapshot**
> list[WithTaskDeleteConsistencyGroupSnapshot] delete_consistency_group_snapshot(consistency_group_snapshot_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupSnapshotApi(api_client)
    consistency_group_snapshot_deletion_params = cloudtower.ConsistencyGroupSnapshotDeletionParams() # ConsistencyGroupSnapshotDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_consistency_group_snapshot(consistency_group_snapshot_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupSnapshotApi->delete_consistency_group_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consistency_group_snapshot_deletion_params** | [**ConsistencyGroupSnapshotDeletionParams**](ConsistencyGroupSnapshotDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteConsistencyGroupSnapshot]**](WithTaskDeleteConsistencyGroupSnapshot.md)

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

# **get_consistency_group_snapshots**
> list[ConsistencyGroupSnapshot] get_consistency_group_snapshots(get_consistency_group_snapshots_request_body, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupSnapshotApi(api_client)
    get_consistency_group_snapshots_request_body = cloudtower.GetConsistencyGroupSnapshotsRequestBody() # GetConsistencyGroupSnapshotsRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_consistency_group_snapshots(get_consistency_group_snapshots_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupSnapshotApi->get_consistency_group_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_consistency_group_snapshots_request_body** | [**GetConsistencyGroupSnapshotsRequestBody**](GetConsistencyGroupSnapshotsRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[ConsistencyGroupSnapshot]**](ConsistencyGroupSnapshot.md)

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

# **get_consistency_group_snapshots_connection**
> ConsistencyGroupSnapshotConnection get_consistency_group_snapshots_connection(get_consistency_group_snapshots_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupSnapshotApi(api_client)
    get_consistency_group_snapshots_connection_request_body = cloudtower.GetConsistencyGroupSnapshotsConnectionRequestBody() # GetConsistencyGroupSnapshotsConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_consistency_group_snapshots_connection(get_consistency_group_snapshots_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupSnapshotApi->get_consistency_group_snapshots_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_consistency_group_snapshots_connection_request_body** | [**GetConsistencyGroupSnapshotsConnectionRequestBody**](GetConsistencyGroupSnapshotsConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**ConsistencyGroupSnapshotConnection**](ConsistencyGroupSnapshotConnection.md)

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

# **update_consistency_group_snapshot**
> list[WithTaskConsistencyGroupSnapshot] update_consistency_group_snapshot(consistency_group_snapshot_updation_params, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupSnapshotApi(api_client)
    consistency_group_snapshot_updation_params = cloudtower.ConsistencyGroupSnapshotUpdationParams() # ConsistencyGroupSnapshotUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_consistency_group_snapshot(consistency_group_snapshot_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupSnapshotApi->update_consistency_group_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consistency_group_snapshot_updation_params** | [**ConsistencyGroupSnapshotUpdationParams**](ConsistencyGroupSnapshotUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskConsistencyGroupSnapshot]**](WithTaskConsistencyGroupSnapshot.md)

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

