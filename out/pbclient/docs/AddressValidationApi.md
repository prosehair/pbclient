# pbclient.AddressValidationApi

All URIs are relative to *https://api-sandbox.pitneybowes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_address**](AddressValidationApi.md#verify_address) | **POST** /shippingservices/v1/addresses/verify | Address validation
[**verify_and_suggest_address**](AddressValidationApi.md#verify_and_suggest_address) | **POST** /shippingservices/v1/addresses/verify-suggest | Address Suggestion


# **verify_address**
> Address verify_address(address, x_pb_unified_error_structure=x_pb_unified_error_structure, minimal_address_validation=minimal_address_validation)

Address validation

Address validation verifies and cleanses postal addresses within the United States to help ensure packages are rated accurately and shipments arrive at their final destinations on time.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import pbclient
from pbclient.models.address import Address
from pbclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.pitneybowes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pbclient.Configuration(
    host = "https://api-sandbox.pitneybowes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pbclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pbclient.AddressValidationApi(api_client)
    address = pbclient.Address() # Address | Address object that needs to be validated.
    x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)
    minimal_address_validation = True # bool | When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check. (optional)

    try:
        # Address validation
        api_response = api_instance.verify_address(address, x_pb_unified_error_structure=x_pb_unified_error_structure, minimal_address_validation=minimal_address_validation)
        print("The response of AddressValidationApi->verify_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressValidationApi->verify_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**Address**](Address.md)| Address object that needs to be validated. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]
 **minimal_address_validation** | **bool**| When set to true, the complete address (delivery line and last line) is validated but only the last line (city, state, and postal code) would be changed by the validation check. | [optional] 

### Return type

[**Address**](Address.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_and_suggest_address**
> AddressSuggestionResponse verify_and_suggest_address(return_suggestions, address_verify_suggest, x_pb_unified_error_structure=x_pb_unified_error_structure)

Address Suggestion

This operation returns suggested addresses. Use this if the [Address Validation API](https://shipping.pitneybowes.com/api/post-address-verify.html) call has returned an error.

### Example

* OAuth Authentication (oAuth2ClientCredentials):

```python
import pbclient
from pbclient.models.address_suggestion_response import AddressSuggestionResponse
from pbclient.models.address_verify_suggest import AddressVerifySuggest
from pbclient.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-sandbox.pitneybowes.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pbclient.Configuration(
    host = "https://api-sandbox.pitneybowes.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pbclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pbclient.AddressValidationApi(api_client)
    return_suggestions = 'true' # str | To return suggested addresses, set this to true. (default to 'true')
    address_verify_suggest = pbclient.AddressVerifySuggest() # AddressVerifySuggest | Address object that needs to be validated.
    x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Address Suggestion
        api_response = api_instance.verify_and_suggest_address(return_suggestions, address_verify_suggest, x_pb_unified_error_structure=x_pb_unified_error_structure)
        print("The response of AddressValidationApi->verify_and_suggest_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressValidationApi->verify_and_suggest_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_suggestions** | **str**| To return suggested addresses, set this to true. | [default to &#39;true&#39;]
 **address_verify_suggest** | [**AddressVerifySuggest**](AddressVerifySuggest.md)| Address object that needs to be validated. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**AddressSuggestionResponse**](AddressSuggestionResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

