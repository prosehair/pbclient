# ParcelProtectionQuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_protection_fees** | **float** |  | 
**parcel_protection_fees_currency_code** | **str** |  | 
**parcel_protection_fees_breakup** | [**ParcelProtectionQuoteResponseParcelProtectionFeesBreakup**](ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.md) |  | 

## Example

```python
from pbclient.models.parcel_protection_quote_response import ParcelProtectionQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionQuoteResponse from a JSON string
parcel_protection_quote_response_instance = ParcelProtectionQuoteResponse.from_json(json)
# print the JSON string representation of the object
print(ParcelProtectionQuoteResponse.to_json())

# convert the object into a dict
parcel_protection_quote_response_dict = parcel_protection_quote_response_instance.to_dict()
# create an instance of ParcelProtectionQuoteResponse from a dict
parcel_protection_quote_response_form_dict = parcel_protection_quote_response.from_dict(parcel_protection_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


