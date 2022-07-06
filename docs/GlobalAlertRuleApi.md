# cloudtower.GlobalAlertRuleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_alert_rules**](GlobalAlertRuleApi.md#get_global_alert_rules) | **POST** /get-global-alert-rules | 
[**get_global_alert_rules_connection**](GlobalAlertRuleApi.md#get_global_alert_rules_connection) | **POST** /get-global-alert-rules-connection | 
[**update_customize_alert_rule**](GlobalAlertRuleApi.md#update_customize_alert_rule) | **POST** /update-customize-alert-rule | 
[**update_global_alert_rule**](GlobalAlertRuleApi.md#update_global_alert_rule) | **POST** /update-global-alert-rule | 


# **get_global_alert_rules**
> list[GlobalAlertRule] get_global_alert_rules(get_global_alert_rules_request_body, content_language=content_language)



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
    api_instance = cloudtower.GlobalAlertRuleApi(api_client)
    get_global_alert_rules_request_body = cloudtower.GetGlobalAlertRulesRequestBody() # GetGlobalAlertRulesRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_global_alert_rules(get_global_alert_rules_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlobalAlertRuleApi->get_global_alert_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_global_alert_rules_request_body** | [**GetGlobalAlertRulesRequestBody**](GetGlobalAlertRulesRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[GlobalAlertRule]**](GlobalAlertRule.md)

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

# **get_global_alert_rules_connection**
> GlobalAlertRuleConnection get_global_alert_rules_connection(get_global_alert_rules_connection_request_body, content_language=content_language)



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
    api_instance = cloudtower.GlobalAlertRuleApi(api_client)
    get_global_alert_rules_connection_request_body = cloudtower.GetGlobalAlertRulesConnectionRequestBody() # GetGlobalAlertRulesConnectionRequestBody | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.get_global_alert_rules_connection(get_global_alert_rules_connection_request_body, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlobalAlertRuleApi->get_global_alert_rules_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_global_alert_rules_connection_request_body** | [**GetGlobalAlertRulesConnectionRequestBody**](GetGlobalAlertRulesConnectionRequestBody.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**GlobalAlertRuleConnection**](GlobalAlertRuleConnection.md)

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

# **update_customize_alert_rule**
> list[WithTaskGlobalAlertRule] update_customize_alert_rule(customize_alert_rule_updation_params, content_language=content_language)



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
    api_instance = cloudtower.GlobalAlertRuleApi(api_client)
    customize_alert_rule_updation_params = cloudtower.CustomizeAlertRuleUpdationParams() # CustomizeAlertRuleUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_customize_alert_rule(customize_alert_rule_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlobalAlertRuleApi->update_customize_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customize_alert_rule_updation_params** | [**CustomizeAlertRuleUpdationParams**](CustomizeAlertRuleUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskGlobalAlertRule]**](WithTaskGlobalAlertRule.md)

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

# **update_global_alert_rule**
> list[WithTaskGlobalAlertRule] update_global_alert_rule(global_alert_rule_updation_params, content_language=content_language)



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
    api_instance = cloudtower.GlobalAlertRuleApi(api_client)
    global_alert_rule_updation_params = cloudtower.GlobalAlertRuleUpdationParams() # GlobalAlertRuleUpdationParams | 
content_language = 'en-US' # str |  (optional) (default to 'en-US')

    try:
        api_response = api_instance.update_global_alert_rule(global_alert_rule_updation_params, content_language=content_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GlobalAlertRuleApi->update_global_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_alert_rule_updation_params** | [**GlobalAlertRuleUpdationParams**](GlobalAlertRuleUpdationParams.md)|  | 
 **content_language** | **str**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**list[WithTaskGlobalAlertRule]**](WithTaskGlobalAlertRule.md)

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

