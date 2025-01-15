# CrossBorderQuotesRequestBasketItemsInnerPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **int** |  | [optional] 
**cod_price** | [**List[CrossBorderQuotesRequestBasketItemsInnerPricingCodPriceInner]**](CrossBorderQuotesRequestBasketItemsInnerPricingCodPriceInner.md) |  | [optional] 
**dutiable_value** | **int** |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_request_basket_items_inner_pricing import CrossBorderQuotesRequestBasketItemsInnerPricing

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesRequestBasketItemsInnerPricing from a JSON string
cross_border_quotes_request_basket_items_inner_pricing_instance = CrossBorderQuotesRequestBasketItemsInnerPricing.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesRequestBasketItemsInnerPricing.to_json())

# convert the object into a dict
cross_border_quotes_request_basket_items_inner_pricing_dict = cross_border_quotes_request_basket_items_inner_pricing_instance.to_dict()
# create an instance of CrossBorderQuotesRequestBasketItemsInnerPricing from a dict
cross_border_quotes_request_basket_items_inner_pricing_form_dict = cross_border_quotes_request_basket_items_inner_pricing.from_dict(cross_border_quotes_request_basket_items_inner_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


