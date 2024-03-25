# CrossBorderQuotesRequestBasketItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | [optional] 
**categories** | [**List[CrossBorderQuotesRequestBasketItemsInnerCategoriesInner]**](CrossBorderQuotesRequestBasketItemsInnerCategoriesInner.md) |  | [optional] 
**description** | **str** |  | [optional] 
**long_description** | **str** |  | [optional] 
**unit_weight** | [**CrossBorderQuotesRequestBasketItemsInnerUnitWeight**](CrossBorderQuotesRequestBasketItemsInnerUnitWeight.md) |  | [optional] 
**item_dimension** | [**CrossBorderQuotesRequestBasketItemsInnerItemDimension**](CrossBorderQuotesRequestBasketItemsInnerItemDimension.md) |  | [optional] 
**url** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_price** | **float** |  | [optional] 
**origin_country_code** | **str** |  | [optional] 
**parent_identifier** | **str** |  | [optional] 
**child_identifier** | **str** |  | [optional] 
**kit** | **str** |  | [optional] 
**kit_identifier** | **str** |  | [optional] 
**kit_quantity** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**eccn** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**pricing** | [**CrossBorderQuotesRequestBasketItemsInnerPricing**](CrossBorderQuotesRequestBasketItemsInnerPricing.md) |  | [optional] 
**h_s_tariff_code** | **str** |  | [optional] 
**h_s_tariff_code_country** | **str** |  | [optional] 
**identifiers** | [**List[CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner]**](CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner.md) |  | [optional] 
**image_urls** | **List[str]** |  | [optional] 
**ships_alone** | **bool** |  | [optional] 
**attributes** | [**List[CrossBorderQuotesRequestBasketItemsInnerAttributesInner]**](CrossBorderQuotesRequestBasketItemsInnerAttributesInner.md) |  | [optional] 
**hazmats** | **List[str]** |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_request_basket_items_inner import CrossBorderQuotesRequestBasketItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesRequestBasketItemsInner from a JSON string
cross_border_quotes_request_basket_items_inner_instance = CrossBorderQuotesRequestBasketItemsInner.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesRequestBasketItemsInner.to_json())

# convert the object into a dict
cross_border_quotes_request_basket_items_inner_dict = cross_border_quotes_request_basket_items_inner_instance.to_dict()
# create an instance of CrossBorderQuotesRequestBasketItemsInner from a dict
cross_border_quotes_request_basket_items_inner_form_dict = cross_border_quotes_request_basket_items_inner.from_dict(cross_border_quotes_request_basket_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


