# cloudtower.ConsistencyGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consistency_group**](ConsistencyGroupApi.md#create_consistency_group) | **POST** /create-consistency-group | 
[**delete_consistency_group**](ConsistencyGroupApi.md#delete_consistency_group) | **POST** /delete-consistency-group | 
[**get_consistency_groups**](ConsistencyGroupApi.md#get_consistency_groups) | **POST** /get-consistency-groups | 
[**get_consistency_groups_connection**](ConsistencyGroupApi.md#get_consistency_groups_connection) | **POST** /get-consistency-groups-connection | 
[**update_consistency_group**](ConsistencyGroupApi.md#update_consistency_group) | **POST** /update-consistency-group | 


# **create_consistency_group**
> list[WithTaskConsistencyGroup] create_consistency_group(consistency_group_creation_params, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupApi(api_client)
    consistency_group_creation_params = [cloudtower.ConsistencyGroupCreationParams()] # list[ConsistencyGroupCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.create_consistency_group(consistency_group_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupApi->create_consistency_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consistency_group_creation_params** | [**list[ConsistencyGroupCreationParams]**](ConsistencyGroupCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskConsistencyGroup]**](WithTaskConsistencyGroup.md)

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

# **delete_consistency_group**
> list[WithTaskDeleteConsistencyGroup] delete_consistency_group(consistency_group_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupApi(api_client)
    consistency_group_deletion_params = cloudtower.ConsistencyGroupDeletionParams() # ConsistencyGroupDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_consistency_group(consistency_group_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupApi->delete_consistency_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consistency_group_deletion_params** | [**ConsistencyGroupDeletionParams**](ConsistencyGroupDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteConsistencyGroup]**](WithTaskDeleteConsistencyGroup.md)

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

# **get_consistency_groups**
> list[ConsistencyGroup] get_consistency_groups(get_consistency_groups_request_body, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupApi(api_client)
    get_consistency_groups_request_body = cloudtower.GetConsistencyGroupsRequestBody() # GetConsistencyGroupsRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_consistency_groups(get_consistency_groups_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupApi->get_consistency_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_consistency_groups_request_body** | [**GetConsistencyGroupsRequestBody**](GetConsistencyGroupsRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[ConsistencyGroup]**](ConsistencyGroup.md)

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

# **get_consistency_groups_connection**
> ConsistencyGroupConnection get_consistency_groups_connection(get_consistency_groups_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupApi(api_client)
    get_consistency_groups_connection_request_body = cloudtower.GetConsistencyGroupsConnectionRequestBody() # GetConsistencyGroupsConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_consistency_groups_connection(get_consistency_groups_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupApi->get_consistency_groups_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_consistency_groups_connection_request_body** | [**GetConsistencyGroupsConnectionRequestBody**](GetConsistencyGroupsConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**ConsistencyGroupConnection**](ConsistencyGroupConnection.md)

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

# **update_consistency_group**
> list[WithTaskConsistencyGroup] update_consistency_group(consistency_group_updation_params, content_language=content_language)



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
    api_instance = cloudtower.ConsistencyGroupApi(api_client)
    consistency_group_updation_params = cloudtower.ConsistencyGroupUpdationParams() # ConsistencyGroupUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_consistency_group(consistency_group_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConsistencyGroupApi->update_consistency_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consistency_group_updation_params** | [**ConsistencyGroupUpdationParams**](ConsistencyGroupUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskConsistencyGroup]**](WithTaskConsistencyGroup.md)

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

