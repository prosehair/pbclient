# pbclient.PickupApi

All URIs are relative to *https://api-sandbox.pitneybowes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pickup**](PickupApi.md#cancel_pickup) | **POST** /shippingservices/v1/pickups/{pickupId}/cancel | Cancel Pickup
[**get_pickupschedule**](PickupApi.md#get_pickupschedule) | **POST** /shippingservices/v1/pickups/schedule | Address validation


# **cancel_pickup**
> CancelPickup200Response cancel_pickup(x_pb_transaction_id, pickup_id, x_pb_unified_error_structure=x_pb_unified_error_structure)

Cancel Pickup

This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import pbclient
from pbclient.models.cancel_pickup200_response import CancelPickup200Response
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
    api_instance = pbclient.PickupApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique identifier for the transaction, up to 25 characters
    pickup_id = 'pickup_id_example' # str | A unique identifier for the transaction, up to 25 characters
    x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Cancel Pickup
        api_response = api_instance.cancel_pickup(x_pb_transaction_id, pickup_id, x_pb_unified_error_structure=x_pb_unified_error_structure)
        print("The response of PickupApi->cancel_pickup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->cancel_pickup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| A unique identifier for the transaction, up to 25 characters | 
 **pickup_id** | **str**| A unique identifier for the transaction, up to 25 characters | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**CancelPickup200Response**](CancelPickup200Response.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pickupschedule**
> SchedulePickupResponse get_pickupschedule(x_pb_transaction_id, schedule_pickup, x_pb_unified_error_structure=x_pb_unified_error_structure)

Address validation

This operation schedules a USPS package pickup from a residential or commercial location and provides a pickup confirmation number.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
import time
import os
import pbclient
from pbclient.models.schedule_pickup import SchedulePickup
from pbclient.models.schedule_pickup_response import SchedulePickupResponse
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
    api_instance = pbclient.PickupApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | A unique identifier for the transaction, up to 25 characters
    schedule_pickup = pbclient.SchedulePickup() # SchedulePickup | Schedule Pickup request.
    x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Address validation
        api_response = api_instance.get_pickupschedule(x_pb_transaction_id, schedule_pickup, x_pb_unified_error_structure=x_pb_unified_error_structure)
        print("The response of PickupApi->get_pickupschedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PickupApi->get_pickupschedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| A unique identifier for the transaction, up to 25 characters | 
 **schedule_pickup** | [**SchedulePickup**](SchedulePickup.md)| Schedule Pickup request. | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**SchedulePickupResponse**](SchedulePickupResponse.md)

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

