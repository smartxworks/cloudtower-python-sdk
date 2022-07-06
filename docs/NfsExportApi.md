# cloudtower.NfsExportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nfs_export**](NfsExportApi.md#create_nfs_export) | **POST** /create-nfs-export | 
[**delete_nfs_export**](NfsExportApi.md#delete_nfs_export) | **POST** /delete-nfs-export | 
[**get_nfs_exports**](NfsExportApi.md#get_nfs_exports) | **POST** /get-nfs-exports | 
[**get_nfs_exports_connection**](NfsExportApi.md#get_nfs_exports_connection) | **POST** /get-nfs-exports-connection | 
[**update_nfs_export**](NfsExportApi.md#update_nfs_export) | **POST** /update-nfs-export | 


# **create_nfs_export**
> list[WithTaskNfsExport] create_nfs_export(nfs_export_creation_params, content_language=content_language)



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
    api_instance = cloudtower.NfsExportApi(api_client)
    nfs_export_creation_params = [cloudtower.NfsExportCreationParams()] # list[NfsExportCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.create_nfs_export(nfs_export_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NfsExportApi->create_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export_creation_params** | [**list[NfsExportCreationParams]**](NfsExportCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskNfsExport]**](WithTaskNfsExport.md)

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

# **delete_nfs_export**
> list[WithTaskDeleteNfsExport] delete_nfs_export(nfs_export_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.NfsExportApi(api_client)
    nfs_export_deletion_params = cloudtower.NfsExportDeletionParams() # NfsExportDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_nfs_export(nfs_export_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NfsExportApi->delete_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export_deletion_params** | [**NfsExportDeletionParams**](NfsExportDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteNfsExport]**](WithTaskDeleteNfsExport.md)

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

# **get_nfs_exports**
> list[NfsExport] get_nfs_exports(get_nfs_exports_request_body, content_language=content_language)



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
    api_instance = cloudtower.NfsExportApi(api_client)
    get_nfs_exports_request_body = cloudtower.GetNfsExportsRequestBody() # GetNfsExportsRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_nfs_exports(get_nfs_exports_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NfsExportApi->get_nfs_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nfs_exports_request_body** | [**GetNfsExportsRequestBody**](GetNfsExportsRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[NfsExport]**](NfsExport.md)

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

# **get_nfs_exports_connection**
> NfsExportConnection get_nfs_exports_connection(get_nfs_exports_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.NfsExportApi(api_client)
    get_nfs_exports_connection_request_body = cloudtower.GetNfsExportsConnectionRequestBody() # GetNfsExportsConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_nfs_exports_connection(get_nfs_exports_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NfsExportApi->get_nfs_exports_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_nfs_exports_connection_request_body** | [**GetNfsExportsConnectionRequestBody**](GetNfsExportsConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**NfsExportConnection**](NfsExportConnection.md)

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

# **update_nfs_export**
> list[WithTaskNfsExport] update_nfs_export(nfs_export_updation_params, content_language=content_language)



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
    api_instance = cloudtower.NfsExportApi(api_client)
    nfs_export_updation_params = cloudtower.NfsExportUpdationParams() # NfsExportUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_nfs_export(nfs_export_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NfsExportApi->update_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export_updation_params** | [**NfsExportUpdationParams**](NfsExportUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskNfsExport]**](WithTaskNfsExport.md)

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

