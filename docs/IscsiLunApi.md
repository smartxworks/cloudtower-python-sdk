# cloudtower.IscsiLunApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_iscsi_lun_from_snapshot**](IscsiLunApi.md#clone_iscsi_lun_from_snapshot) | **POST** /clone-iscsi-lun-from-snapshot | 
[**create_iscsi_lun**](IscsiLunApi.md#create_iscsi_lun) | **POST** /create-iscsi-lun | 
[**delete_iscsi_lun**](IscsiLunApi.md#delete_iscsi_lun) | **POST** /delete-iscsi-lun | 
[**get_iscsi_luns**](IscsiLunApi.md#get_iscsi_luns) | **POST** /get-iscsi-luns | 
[**get_iscsi_luns_connection**](IscsiLunApi.md#get_iscsi_luns_connection) | **POST** /get-iscsi-luns-connection | 
[**rollback_iscsi_lun_from_snapshot**](IscsiLunApi.md#rollback_iscsi_lun_from_snapshot) | **POST** /rollback-iscsi-lun-from-snapshot | 
[**update_iscsi_lun**](IscsiLunApi.md#update_iscsi_lun) | **POST** /update-iscsi-lun | 


# **clone_iscsi_lun_from_snapshot**
> list[WithTaskIscsiLun] clone_iscsi_lun_from_snapshot(iscsi_lun_clone_params, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunApi(api_client)
    iscsi_lun_clone_params = [cloudtower.IscsiLunCloneParams()] # list[IscsiLunCloneParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.clone_iscsi_lun_from_snapshot(iscsi_lun_clone_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunApi->clone_iscsi_lun_from_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iscsi_lun_clone_params** | [**list[IscsiLunCloneParams]**](IscsiLunCloneParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskIscsiLun]**](WithTaskIscsiLun.md)

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

# **create_iscsi_lun**
> list[WithTaskIscsiLun] create_iscsi_lun(iscsi_lun_creation_params, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunApi(api_client)
    iscsi_lun_creation_params = [cloudtower.IscsiLunCreationParams()] # list[IscsiLunCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.create_iscsi_lun(iscsi_lun_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunApi->create_iscsi_lun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iscsi_lun_creation_params** | [**list[IscsiLunCreationParams]**](IscsiLunCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskIscsiLun]**](WithTaskIscsiLun.md)

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

# **delete_iscsi_lun**
> list[WithTaskDeleteIscsiLun] delete_iscsi_lun(iscsi_lun_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunApi(api_client)
    iscsi_lun_deletion_params = cloudtower.IscsiLunDeletionParams() # IscsiLunDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_iscsi_lun(iscsi_lun_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunApi->delete_iscsi_lun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iscsi_lun_deletion_params** | [**IscsiLunDeletionParams**](IscsiLunDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteIscsiLun]**](WithTaskDeleteIscsiLun.md)

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

# **get_iscsi_luns**
> list[IscsiLun] get_iscsi_luns(get_iscsi_luns_request_body, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunApi(api_client)
    get_iscsi_luns_request_body = cloudtower.GetIscsiLunsRequestBody() # GetIscsiLunsRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_iscsi_luns(get_iscsi_luns_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunApi->get_iscsi_luns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_iscsi_luns_request_body** | [**GetIscsiLunsRequestBody**](GetIscsiLunsRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[IscsiLun]**](IscsiLun.md)

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

# **get_iscsi_luns_connection**
> IscsiLunConnection get_iscsi_luns_connection(get_iscsi_luns_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunApi(api_client)
    get_iscsi_luns_connection_request_body = cloudtower.GetIscsiLunsConnectionRequestBody() # GetIscsiLunsConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_iscsi_luns_connection(get_iscsi_luns_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunApi->get_iscsi_luns_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_iscsi_luns_connection_request_body** | [**GetIscsiLunsConnectionRequestBody**](GetIscsiLunsConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**IscsiLunConnection**](IscsiLunConnection.md)

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

# **rollback_iscsi_lun_from_snapshot**
> list[WithTaskIscsiLun] rollback_iscsi_lun_from_snapshot(iscsi_lun_rollback_params, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunApi(api_client)
    iscsi_lun_rollback_params = [cloudtower.IscsiLunRollbackParams()] # list[IscsiLunRollbackParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.rollback_iscsi_lun_from_snapshot(iscsi_lun_rollback_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunApi->rollback_iscsi_lun_from_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iscsi_lun_rollback_params** | [**list[IscsiLunRollbackParams]**](IscsiLunRollbackParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskIscsiLun]**](WithTaskIscsiLun.md)

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

# **update_iscsi_lun**
> list[WithTaskIscsiLun] update_iscsi_lun(iscsi_lun_updation_params, content_language=content_language)



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
    api_instance = cloudtower.IscsiLunApi(api_client)
    iscsi_lun_updation_params = cloudtower.IscsiLunUpdationParams() # IscsiLunUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_iscsi_lun(iscsi_lun_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IscsiLunApi->update_iscsi_lun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iscsi_lun_updation_params** | [**IscsiLunUpdationParams**](IscsiLunUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskIscsiLun]**](WithTaskIscsiLun.md)

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

