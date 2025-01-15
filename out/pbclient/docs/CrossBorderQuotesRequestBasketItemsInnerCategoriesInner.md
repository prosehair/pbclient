# CrossBorderQuotesRequestBasketItemsInnerCategoriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_code** | **str** |  | [optional] 
**descriptions** | [**List[CrossBorderQuotesRequestBasketItemsInnerCategoriesInnerDescriptionsInner]**](CrossBorderQuotesRequestBasketItemsInnerCategoriesInnerDescriptionsInner.md) |  | [optional] 
**parent_category_code** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_request_basket_items_inner_categories_inner import CrossBorderQuotesRequestBasketItemsInnerCategoriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesRequestBasketItemsInnerCategoriesInner from a JSON string
cross_border_quotes_request_basket_items_inner_categories_inner_instance = CrossBorderQuotesRequestBasketItemsInnerCategoriesInner.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesRequestBasketItemsInnerCategoriesInner.to_json())

# convert the object into a dict
cross_border_quotes_request_basket_items_inner_categories_inner_dict = cross_border_quotes_request_basket_items_inner_categories_inner_instance.to_dict()
# create an instance of CrossBorderQuotesRequestBasketItemsInnerCategoriesInner from a dict
cross_border_quotes_request_basket_items_inner_categories_inner_form_dict = cross_border_quotes_request_basket_items_inner_categories_inner.from_dict(cross_border_quotes_request_basket_items_inner_categories_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


