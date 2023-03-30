# CustomsItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**h_s_tariff_code** | **str** |  | [optional] 
**net_cost_method** | **str** |  | [optional] 
**origin_country_code** | **str** |  | 
**origin_state_province** | **str** |  | [optional] 
**preference_criterion** | **str** |  | [optional] 
**producer_address** | [**Address**](Address.md) |  | [optional] 
**producer_determination** | **str** |  | [optional] 
**producer_id** | **str** |  | [optional] 
**quantity** | **int** |  | 
**quantity_uom** | **str** |  | [optional] 
**unit_price** | **float** |  | 
**unit_weight** | [**ParcelWeight**](ParcelWeight.md) |  | 

## Example

```python
from pbclient.models.customs_item import CustomsItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsItem from a JSON string
customs_item_instance = CustomsItem.from_json(json)
# print the JSON string representation of the object
print CustomsItem.to_json()

# convert the object into a dict
customs_item_dict = customs_item_instance.to_dict()
# create an instance of CustomsItem from a dict
customs_item_form_dict = customs_item.from_dict(customs_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


