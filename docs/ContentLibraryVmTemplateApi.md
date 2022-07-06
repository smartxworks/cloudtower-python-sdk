# cloudtower.ContentLibraryVmTemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_content_library_vm_template_from_vm**](ContentLibraryVmTemplateApi.md#clone_content_library_vm_template_from_vm) | **POST** /clone-content-library-vm-template-from-vm | 
[**convert_content_library_vm_template_from_vm**](ContentLibraryVmTemplateApi.md#convert_content_library_vm_template_from_vm) | **POST** /convert-content-library-vm-template-from-vm | 
[**delete_content_library_vm_template**](ContentLibraryVmTemplateApi.md#delete_content_library_vm_template) | **POST** /delete-content-library-vm-template | 
[**distribute_content_library_vmtemplate_clusters**](ContentLibraryVmTemplateApi.md#distribute_content_library_vmtemplate_clusters) | **POST** /distribute-content-library-vm-template-clusters | 
[**get_content_library_vm_templates**](ContentLibraryVmTemplateApi.md#get_content_library_vm_templates) | **POST** /get-content-library-vm-templates | 
[**get_content_library_vm_templates_connection**](ContentLibraryVmTemplateApi.md#get_content_library_vm_templates_connection) | **POST** /get-content-library-vm-templates-connection | 
[**remove_content_library_vm_template_clusters**](ContentLibraryVmTemplateApi.md#remove_content_library_vm_template_clusters) | **POST** /remove-content-library-vm-template-clusters | 
[**update_content_library_vm_template**](ContentLibraryVmTemplateApi.md#update_content_library_vm_template) | **POST** /update-content-library-vm-template | 


# **clone_content_library_vm_template_from_vm**
> list[WithTaskContentLibraryVmTemplate] clone_content_library_vm_template_from_vm(content_library_vm_template_creation_params, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    content_library_vm_template_creation_params = [cloudtower.ContentLibraryVmTemplateCreationParams()] # list[ContentLibraryVmTemplateCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.clone_content_library_vm_template_from_vm(content_library_vm_template_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->clone_content_library_vm_template_from_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_library_vm_template_creation_params** | [**list[ContentLibraryVmTemplateCreationParams]**](ContentLibraryVmTemplateCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskContentLibraryVmTemplate]**](WithTaskContentLibraryVmTemplate.md)

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

# **convert_content_library_vm_template_from_vm**
> list[WithTaskContentLibraryVmTemplate] convert_content_library_vm_template_from_vm(content_library_vm_template_creation_params, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    content_library_vm_template_creation_params = [cloudtower.ContentLibraryVmTemplateCreationParams()] # list[ContentLibraryVmTemplateCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.convert_content_library_vm_template_from_vm(content_library_vm_template_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->convert_content_library_vm_template_from_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_library_vm_template_creation_params** | [**list[ContentLibraryVmTemplateCreationParams]**](ContentLibraryVmTemplateCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskContentLibraryVmTemplate]**](WithTaskContentLibraryVmTemplate.md)

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

# **delete_content_library_vm_template**
> list[WithTaskDeleteContentLibraryVmTemplate] delete_content_library_vm_template(content_library_vm_template_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    content_library_vm_template_deletion_params = cloudtower.ContentLibraryVmTemplateDeletionParams() # ContentLibraryVmTemplateDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_content_library_vm_template(content_library_vm_template_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->delete_content_library_vm_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_library_vm_template_deletion_params** | [**ContentLibraryVmTemplateDeletionParams**](ContentLibraryVmTemplateDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteContentLibraryVmTemplate]**](WithTaskDeleteContentLibraryVmTemplate.md)

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

# **distribute_content_library_vmtemplate_clusters**
> list[WithTaskContentLibraryVmTemplate] distribute_content_library_vmtemplate_clusters(content_library_vm_template_updation_cluster_params, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    content_library_vm_template_updation_cluster_params = cloudtower.ContentLibraryVmTemplateUpdationClusterParams() # ContentLibraryVmTemplateUpdationClusterParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.distribute_content_library_vmtemplate_clusters(content_library_vm_template_updation_cluster_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->distribute_content_library_vmtemplate_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_library_vm_template_updation_cluster_params** | [**ContentLibraryVmTemplateUpdationClusterParams**](ContentLibraryVmTemplateUpdationClusterParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskContentLibraryVmTemplate]**](WithTaskContentLibraryVmTemplate.md)

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

# **get_content_library_vm_templates**
> list[ContentLibraryVmTemplate] get_content_library_vm_templates(get_content_library_vm_templates_request_body, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    get_content_library_vm_templates_request_body = cloudtower.GetContentLibraryVmTemplatesRequestBody() # GetContentLibraryVmTemplatesRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_content_library_vm_templates(get_content_library_vm_templates_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->get_content_library_vm_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_content_library_vm_templates_request_body** | [**GetContentLibraryVmTemplatesRequestBody**](GetContentLibraryVmTemplatesRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[ContentLibraryVmTemplate]**](ContentLibraryVmTemplate.md)

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

# **get_content_library_vm_templates_connection**
> ContentLibraryVmTemplateConnection get_content_library_vm_templates_connection(get_content_library_vm_templates_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    get_content_library_vm_templates_connection_request_body = cloudtower.GetContentLibraryVmTemplatesConnectionRequestBody() # GetContentLibraryVmTemplatesConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_content_library_vm_templates_connection(get_content_library_vm_templates_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->get_content_library_vm_templates_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_content_library_vm_templates_connection_request_body** | [**GetContentLibraryVmTemplatesConnectionRequestBody**](GetContentLibraryVmTemplatesConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**ContentLibraryVmTemplateConnection**](ContentLibraryVmTemplateConnection.md)

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

# **remove_content_library_vm_template_clusters**
> list[WithTaskContentLibraryVmTemplate] remove_content_library_vm_template_clusters(content_library_vm_template_updation_cluster_params, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    content_library_vm_template_updation_cluster_params = cloudtower.ContentLibraryVmTemplateUpdationClusterParams() # ContentLibraryVmTemplateUpdationClusterParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.remove_content_library_vm_template_clusters(content_library_vm_template_updation_cluster_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->remove_content_library_vm_template_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_library_vm_template_updation_cluster_params** | [**ContentLibraryVmTemplateUpdationClusterParams**](ContentLibraryVmTemplateUpdationClusterParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskContentLibraryVmTemplate]**](WithTaskContentLibraryVmTemplate.md)

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

# **update_content_library_vm_template**
> list[WithTaskContentLibraryVmTemplate] update_content_library_vm_template(content_library_vm_template_updation_params, content_language=content_language)



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
    api_instance = cloudtower.ContentLibraryVmTemplateApi(api_client)
    content_library_vm_template_updation_params = cloudtower.ContentLibraryVmTemplateUpdationParams() # ContentLibraryVmTemplateUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_content_library_vm_template(content_library_vm_template_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentLibraryVmTemplateApi->update_content_library_vm_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_library_vm_template_updation_params** | [**ContentLibraryVmTemplateUpdationParams**](ContentLibraryVmTemplateUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskContentLibraryVmTemplate]**](WithTaskContentLibraryVmTemplate.md)

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

