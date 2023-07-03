# pbclient.AuthenticationApi

All URIs are relative to *https://api-sandbox.pitneybowes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token**](AuthenticationApi.md#oauth_token) | **POST** /oauth/token | OAuth Authentication


# **oauth_token**
> OAuthToken oauth_token(authorization, content_type=content_type, grant_type=grant_type)

OAuth Authentication

This API call generates the OAuth token based on the Base64-encoded value of the API key and secret associated with your PB Shipping APIs developer account. The token expires after 10 hours, after which you must create a new one.

### Example

```python
import time
import os
import pbclient
from pbclient.models.o_auth_token import OAuthToken
from pbclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.pitneybowes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pbclient.Configuration(
    host = "https://api-sandbox.pitneybowes.com"
)


# Enter a context with an instance of the API client
with pbclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pbclient.AuthenticationApi(api_client)
    authorization = 'authorization_example' # str | Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: <API_key>:<API_secret> Pass the encoded value using Basic authentication: Basic <encoded-value>
    content_type = 'application/x-www-form-urlencoded' # str | This mentions the content type getting passed in body of request. (optional) (default to 'application/x-www-form-urlencoded')
    grant_type = 'client_credentials' # str |  (optional) (default to 'client_credentials')

    try:
        # OAuth Authentication
        api_response = api_instance.oauth_token(authorization, content_type=content_type, grant_type=grant_type)
        print("The response of AuthenticationApi->oauth_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->oauth_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Use Basic authentication to pass the Base64-encoded value of your developer account’s API key and secret. Encode the key and secret in the following format. Be sure to include the colon between the key and secret: &lt;API_key&gt;:&lt;API_secret&gt; Pass the encoded value using Basic authentication: Basic &lt;encoded-value&gt; | 
 **content_type** | **str**| This mentions the content type getting passed in body of request. | [optional] [default to &#39;application/x-www-form-urlencoded&#39;]
 **grant_type** | **str**|  | [optional] [default to &#39;client_credentials&#39;]

### Return type

[**OAuthToken**](OAuthToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

