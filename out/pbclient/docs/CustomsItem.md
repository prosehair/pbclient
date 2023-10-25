# CustomsItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**hazmat** | **List[str]** |  | [optional] 
**h_s_tariff_code** | **str** |  | [optional] 
**h_s_tariff_code_country** | **str** |  | [optional] 
**item_dimension** | [**ParcelDimension**](ParcelDimension.md) |  | [optional] 
**item_id** | **str** |  | 
**manufacturer** | **str** |  | [optional] 
**origin_country_code** | **str** |  | [optional] 
**quantity** | **int** |  | 
**unit_price** | **float** |  | 
**unit_weight** | [**ParcelWeight**](ParcelWeight.md) |  | [optional] 
**url** | **str** |  | [optional] 

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


