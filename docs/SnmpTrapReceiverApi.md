# cloudtower.SnmpTrapReceiverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snmp_trap_receiver**](SnmpTrapReceiverApi.md#create_snmp_trap_receiver) | **POST** /create-snmp-trap-receiver | 
[**delete_snmp_trap_receiver**](SnmpTrapReceiverApi.md#delete_snmp_trap_receiver) | **POST** /delete-snmp-trap-receiver | 
[**get_snmp_trap_receivers**](SnmpTrapReceiverApi.md#get_snmp_trap_receivers) | **POST** /get-snmp-trap-receivers | 
[**get_snmp_trap_receivers_connection**](SnmpTrapReceiverApi.md#get_snmp_trap_receivers_connection) | **POST** /get-snmp-trap-receivers-connection | 
[**update_snmp_trap_receiver**](SnmpTrapReceiverApi.md#update_snmp_trap_receiver) | **POST** /update-snmp-trap-receiver | 


# **create_snmp_trap_receiver**
> list[WithTaskSnmpTrapReceiver] create_snmp_trap_receiver(snmp_trap_receiver_creation_params, content_language=content_language)



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
    api_instance = cloudtower.SnmpTrapReceiverApi(api_client)
    snmp_trap_receiver_creation_params = [cloudtower.SnmpTrapReceiverCreationParams()] # list[SnmpTrapReceiverCreationParams] | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.create_snmp_trap_receiver(snmp_trap_receiver_creation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnmpTrapReceiverApi->create_snmp_trap_receiver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_trap_receiver_creation_params** | [**list[SnmpTrapReceiverCreationParams]**](SnmpTrapReceiverCreationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskSnmpTrapReceiver]**](WithTaskSnmpTrapReceiver.md)

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

# **delete_snmp_trap_receiver**
> list[WithTaskDeleteSnmpTrapReceiver] delete_snmp_trap_receiver(snmp_trap_receiver_deletion_params, content_language=content_language)



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
    api_instance = cloudtower.SnmpTrapReceiverApi(api_client)
    snmp_trap_receiver_deletion_params = cloudtower.SnmpTrapReceiverDeletionParams() # SnmpTrapReceiverDeletionParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.delete_snmp_trap_receiver(snmp_trap_receiver_deletion_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnmpTrapReceiverApi->delete_snmp_trap_receiver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_trap_receiver_deletion_params** | [**SnmpTrapReceiverDeletionParams**](SnmpTrapReceiverDeletionParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskDeleteSnmpTrapReceiver]**](WithTaskDeleteSnmpTrapReceiver.md)

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

# **get_snmp_trap_receivers**
> list[SnmpTrapReceiver] get_snmp_trap_receivers(get_snmp_trap_receivers_request_body, content_language=content_language)



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
    api_instance = cloudtower.SnmpTrapReceiverApi(api_client)
    get_snmp_trap_receivers_request_body = cloudtower.GetSnmpTrapReceiversRequestBody() # GetSnmpTrapReceiversRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_snmp_trap_receivers(get_snmp_trap_receivers_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnmpTrapReceiverApi->get_snmp_trap_receivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_snmp_trap_receivers_request_body** | [**GetSnmpTrapReceiversRequestBody**](GetSnmpTrapReceiversRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[SnmpTrapReceiver]**](SnmpTrapReceiver.md)

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

# **get_snmp_trap_receivers_connection**
> SnmpTrapReceiverConnection get_snmp_trap_receivers_connection(get_snmp_trap_receivers_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.SnmpTrapReceiverApi(api_client)
    get_snmp_trap_receivers_connection_request_body = cloudtower.GetSnmpTrapReceiversConnectionRequestBody() # GetSnmpTrapReceiversConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_snmp_trap_receivers_connection(get_snmp_trap_receivers_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnmpTrapReceiverApi->get_snmp_trap_receivers_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_snmp_trap_receivers_connection_request_body** | [**GetSnmpTrapReceiversConnectionRequestBody**](GetSnmpTrapReceiversConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**SnmpTrapReceiverConnection**](SnmpTrapReceiverConnection.md)

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

# **update_snmp_trap_receiver**
> list[WithTaskSnmpTrapReceiver] update_snmp_trap_receiver(snmp_trap_receiver_updation_params, content_language=content_language)



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
    api_instance = cloudtower.SnmpTrapReceiverApi(api_client)
    snmp_trap_receiver_updation_params = cloudtower.SnmpTrapReceiverUpdationParams() # SnmpTrapReceiverUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_snmp_trap_receiver(snmp_trap_receiver_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SnmpTrapReceiverApi->update_snmp_trap_receiver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_trap_receiver_updation_params** | [**SnmpTrapReceiverUpdationParams**](SnmpTrapReceiverUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskSnmpTrapReceiver]**](WithTaskSnmpTrapReceiver.md)

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

