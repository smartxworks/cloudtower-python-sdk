# cloudtower.SnapshotPlanTaskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snapshot_plan_tasks**](SnapshotPlanTaskApi.md#get_snapshot_plan_tasks) | **POST** /get-snapshot-plan-tasks | 
[**get_snapshot_plan_tasks_connection**](SnapshotPlanTaskApi.md#get_snapshot_plan_tasks_connection) | **POST** /get-snapshot-plan-tasks-connection | 


# **get_snapshot_plan_tasks**
> list[SnapshotPlanTask] get_snapshot_plan_tasks(get_snapshot_plan_tasks_request_body, content_language=content_language)



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
    api_instance = cloudtower.SnapshotPlanTaskApi(api_client)
    get_snapshot_plan_tasks_request_body = cloudtower.GetSnapshotPlanTasksRequestBody() # GetSnapshotPlanTasksRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_snapshot_plan_tasks(get_snapshot_plan_tasks_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotPlanTaskApi->get_snapshot_plan_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_snapshot_plan_tasks_request_body** | [**GetSnapshotPlanTasksRequestBody**](GetSnapshotPlanTasksRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[SnapshotPlanTask]**](SnapshotPlanTask.md)

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

# **get_snapshot_plan_tasks_connection**
> SnapshotPlanTaskConnection get_snapshot_plan_tasks_connection(get_snapshot_plan_tasks_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.SnapshotPlanTaskApi(api_client)
    get_snapshot_plan_tasks_connection_request_body = cloudtower.GetSnapshotPlanTasksConnectionRequestBody() # GetSnapshotPlanTasksConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_snapshot_plan_tasks_connection(get_snapshot_plan_tasks_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnapshotPlanTaskApi->get_snapshot_plan_tasks_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_snapshot_plan_tasks_connection_request_body** | [**GetSnapshotPlanTasksConnectionRequestBody**](GetSnapshotPlanTasksConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**SnapshotPlanTaskConnection**](SnapshotPlanTaskConnection.md)

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

