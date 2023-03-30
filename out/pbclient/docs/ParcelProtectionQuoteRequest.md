# ParcelProtectionQuoteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_protection_account_id** | **str** |  | [optional] 
**parcel_protection_program_id** | **str** |  | [optional] 
**shipment_info** | [**ParcelProtectionQuoteRequestShipmentInfo**](ParcelProtectionQuoteRequestShipmentInfo.md) |  | 

## Example

```python
from pbclient.models.parcel_protection_quote_request import ParcelProtectionQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionQuoteRequest from a JSON string
parcel_protection_quote_request_instance = ParcelProtectionQuoteRequest.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionQuoteRequest.to_json()

# convert the object into a dict
parcel_protection_quote_request_dict = parcel_protection_quote_request_instance.to_dict()
# create an instance of ParcelProtectionQuoteRequest from a dict
parcel_protection_quote_request_form_dict = parcel_protection_quote_request.from_dict(parcel_protection_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


