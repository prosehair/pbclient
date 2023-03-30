# ParcelProtectionCreateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**parcel_protection_reference_id** | **str** |  | [optional] 
**parcel_protection_date** | **str** |  | [optional] 
**parcel_protection_fees** | **float** |  | [optional] 
**parcel_protection_fees_currency_code** | **str** |  | [optional] 
**parcel_protection_fees_breakup** | [**ParcelProtectionCreateResponseParcelProtectionFeesBreakup**](ParcelProtectionCreateResponseParcelProtectionFeesBreakup.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_create_response import ParcelProtectionCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionCreateResponse from a JSON string
parcel_protection_create_response_instance = ParcelProtectionCreateResponse.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionCreateResponse.to_json()

# convert the object into a dict
parcel_protection_create_response_dict = parcel_protection_create_response_instance.to_dict()
# create an instance of ParcelProtectionCreateResponse from a dict
parcel_protection_create_response_form_dict = parcel_protection_create_response.from_dict(parcel_protection_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


