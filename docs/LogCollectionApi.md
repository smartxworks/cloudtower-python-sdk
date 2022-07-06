# cloudtower.LogCollectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_collection**](LogCollectionApi.md#create_log_collection) | **POST** /create-log-collection | 
[**delete_log_collection**](LogCollectionApi.md#delete_log_collection) | **POST** /delete-log-collection | 
[**force_stop_log_collection**](LogCollectionApi.md#force_stop_log_collection) | **POST** /force-stop-log-collection | 
[**get_log_collections**](LogCollectionApi.md#get_log_collections) | **POST** /get-log-collections | 
[**get_log_collections_connection**](LogCollectionApi.md#get_log_collections_connection) | **POST** /get-log-collections-connection | 


# **create_log_collection**
> list[WithTaskLogCollection] create_log_collection(log_collection_creation_params)



### Example

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


# Enter a context with an instance of the API client
with cloudtower.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.LogCollectionApi(api_client)
    log_collection_creation_params = [cloudtower.LogCollectionCreationParams()] # list[LogCollectionCreationParams] | 

    try:
        api_response = api_instance.create_log_collection(log_collection_creation_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogCollectionApi->create_log_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_collection_creation_params** | [**list[LogCollectionCreationParams]**](LogCollectionCreationParams.md)|  | 

### Return type

[**list[WithTaskLogCollection]**](WithTaskLogCollection.md)

### Authorization

No authorization required

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

# **delete_log_collection**
> list[WithTaskDeleteLogCollection] delete_log_collection(log_collection_deletion_params)



### Example

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


# Enter a context with an instance of the API client
with cloudtower.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.LogCollectionApi(api_client)
    log_collection_deletion_params = cloudtower.LogCollectionDeletionParams() # LogCollectionDeletionParams | 

    try:
        api_response = api_instance.delete_log_collection(log_collection_deletion_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogCollectionApi->delete_log_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_collection_deletion_params** | [**LogCollectionDeletionParams**](LogCollectionDeletionParams.md)|  | 

### Return type

[**list[WithTaskDeleteLogCollection]**](WithTaskDeleteLogCollection.md)

### Authorization

No authorization required

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

# **force_stop_log_collection**
> list[WithTaskLogCollection] force_stop_log_collection(force_stop_log_collection_params)



### Example

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


# Enter a context with an instance of the API client
with cloudtower.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cloudtower.LogCollectionApi(api_client)
    force_stop_log_collection_params = cloudtower.ForceStopLogCollectionParams() # ForceStopLogCollectionParams | 

    try:
        api_response = api_instance.force_stop_log_collection(force_stop_log_collection_params)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogCollectionApi->force_stop_log_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_stop_log_collection_params** | [**ForceStopLogCollectionParams**](ForceStopLogCollectionParams.md)|  | 

### Return type

[**list[WithTaskLogCollection]**](WithTaskLogCollection.md)

### Authorization

No authorization required

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

# **get_log_collections**
> list[LogCollection] get_log_collections(get_log_collections_request_body, content_language=content_language)



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
    api_instance = cloudtower.LogCollectionApi(api_client)
    get_log_collections_request_body = cloudtower.GetLogCollectionsRequestBody() # GetLogCollectionsRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_log_collections(get_log_collections_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogCollectionApi->get_log_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_log_collections_request_body** | [**GetLogCollectionsRequestBody**](GetLogCollectionsRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[LogCollection]**](LogCollection.md)

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

# **get_log_collections_connection**
> LogCollectionConnection get_log_collections_connection(get_log_collections_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.LogCollectionApi(api_client)
    get_log_collections_connection_request_body = cloudtower.GetLogCollectionsConnectionRequestBody() # GetLogCollectionsConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_log_collections_connection(get_log_collections_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogCollectionApi->get_log_collections_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_log_collections_connection_request_body** | [**GetLogCollectionsConnectionRequestBody**](GetLogCollectionsConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**LogCollectionConnection**](LogCollectionConnection.md)

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

