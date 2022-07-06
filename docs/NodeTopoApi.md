# cloudtower.NodeTopoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_topoes**](NodeTopoApi.md#get_node_topoes) | **POST** /get-node-topoes | 
[**get_node_topoes_connection**](NodeTopoApi.md#get_node_topoes_connection) | **POST** /get-node-topoes-connection | 
[**update_node_topo**](NodeTopoApi.md#update_node_topo) | **POST** /move-node-topo | 


# **get_node_topoes**
> list[NodeTopo] get_node_topoes(get_node_topoes_request_body, content_language=content_language)



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
    api_instance = cloudtower.NodeTopoApi(api_client)
    get_node_topoes_request_body = cloudtower.GetNodeTopoesRequestBody() # GetNodeTopoesRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_node_topoes(get_node_topoes_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeTopoApi->get_node_topoes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_node_topoes_request_body** | [**GetNodeTopoesRequestBody**](GetNodeTopoesRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[NodeTopo]**](NodeTopo.md)

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

# **get_node_topoes_connection**
> NodeTopoConnection get_node_topoes_connection(get_node_topoes_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.NodeTopoApi(api_client)
    get_node_topoes_connection_request_body = cloudtower.GetNodeTopoesConnectionRequestBody() # GetNodeTopoesConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_node_topoes_connection(get_node_topoes_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeTopoApi->get_node_topoes_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_node_topoes_connection_request_body** | [**GetNodeTopoesConnectionRequestBody**](GetNodeTopoesConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**NodeTopoConnection**](NodeTopoConnection.md)

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

# **update_node_topo**
> list[WithTaskNodeTopo] update_node_topo(node_top_updation_param, content_language=content_language)



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
    api_instance = cloudtower.NodeTopoApi(api_client)
    node_top_updation_param = [cloudtower.NodeTopUpdationParam()] # list[NodeTopUpdationParam] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_node_topo(node_top_updation_param, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeTopoApi->update_node_topo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_top_updation_param** | [**list[NodeTopUpdationParam]**](NodeTopUpdationParam.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskNodeTopo]**](WithTaskNodeTopo.md)

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

