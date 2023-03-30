# CrossBorderQuotesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_currency** | **str** | The currency to return the quote in. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR | 
**basket_currency** | **str** | The default currency of the basket. Use three uppercase letters, per the ISO currency code (ISO 4217). For example- USD, CAD, or EUR | 
**from_address** | [**Address**](Address.md) |  | [optional] 
**to_address** | [**Address**](Address.md) |  | 
**basket_items** | [**List[CrossBorderQuotesRequestBasketItemsInner]**](CrossBorderQuotesRequestBasketItemsInner.md) | The items in the buyer&#39;s shopping basket. | 
**rates** | [**List[CrossBorderQuotesRequestRatesInner]**](CrossBorderQuotesRequestRatesInner.md) | Specifies the carrier, service, parcel, and other information. In a response, this field also contains the service charges. Importatn- In a request, the rates array can contain only one rates object. | 
**shipment_options** | [**List[CarrierFacilityResponseCarrierFacilityOptionsInner]**](CarrierFacilityResponseCarrierFacilityOptionsInner.md) |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_request import CrossBorderQuotesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesRequest from a JSON string
cross_border_quotes_request_instance = CrossBorderQuotesRequest.from_json(json)
# print the JSON string representation of the object
print CrossBorderQuotesRequest.to_json()

# convert the object into a dict
cross_border_quotes_request_dict = cross_border_quotes_request_instance.to_dict()
# create an instance of CrossBorderQuotesRequest from a dict
cross_border_quotes_request_form_dict = cross_border_quotes_request.from_dict(cross_border_quotes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


