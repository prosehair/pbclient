# pbclient.ContainerApi

All URIs are relative to *https://api-sandbox.pitneybowes.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_containerized_parcels_labels**](ContainerApi.md#get_containerized_parcels_labels) | **POST** /shippingservices/v1/container-manifest | Create Container Manifest Label


# **get_containerized_parcels_labels**
> ContainerManifestResponse get_containerized_parcels_labels(x_pb_transaction_id, manifest, x_pb_unified_error_structure=x_pb_unified_error_structure)

Create Container Manifest Label

This operation prints a label for the shipment of containerized parcels destined for a Pitney Bowes warehouse facility from the client location.

### Example

* OAuth Authentication (oAuth2ClientCredentials):
```python
from __future__ import print_function
import time
import os
import pbclient
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
    api_instance = pbclient.ContainerApi(api_client)
    x_pb_transaction_id = 'x_pb_transaction_id_example' # str | Required. A unique identifier for the transaction, up to 25 characters.
    manifest = {"carrier":"Newgistics","containerType":"Carton","parcelTrackingNumbers":["9205500000000000000000","9206600000000000000000"],"documents":[{"resolution":"DPI_203","size":"DOC_4X4","fileFormat":"PDF"}],"parameters":[{"name":"CLIENT_CONTAINER_ID","value":"AB12345678"},{"name":"SHIPMENT_REFERENCE_NUMBER","value":"CD12345678"},{"name":"CLIENT_FACILITY_ID","value":"7777"},{"name":"CARRIER_GATEWAY_FACILITY_ID","value":"1234"},{"name":"CARRIER_FACILITY_ID","value":"4321"},{"name":"PRINT_CUSTOM_MESSAGE_1","value":"Container: AB12345678, Shipment: CD12345678"},{"name":"current_container","value":"1"},{"name":"total_container_count","value":"2"},{"name":"client_Id","value":"NGST"}]} # Manifest | manifest
    x_pb_unified_error_structure = True # bool | Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. (optional) (default to True)

    try:
        # Create Container Manifest Label
        api_response = api_instance.get_containerized_parcels_labels(x_pb_transaction_id, manifest, x_pb_unified_error_structure=x_pb_unified_error_structure)
        print("The response of ContainerApi->get_containerized_parcels_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerApi->get_containerized_parcels_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pb_transaction_id** | **str**| Required. A unique identifier for the transaction, up to 25 characters. | 
 **manifest** | [**Manifest**](Manifest.md)| manifest | 
 **x_pb_unified_error_structure** | **bool**| Set this to true to use the standard [error object](https://shipping.pitneybowes.com/reference/error-object.html#standard-error-object) if an error occurs. | [optional] [default to True]

### Return type

[**ContainerManifestResponse**](ContainerManifestResponse.md)

### Authorization

[oAuth2ClientCredentials](../README.md#oAuth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

