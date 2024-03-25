# BatteryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_material** | **str** |  | [optional] 
**battery_packaging** | **str** |  | [optional] 
**regulatory** | **str** |  | [optional] 

## Example

```python
from pbclient.models.battery_details import BatteryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BatteryDetails from a JSON string
battery_details_instance = BatteryDetails.from_json(json)
# print the JSON string representation of the object
print(BatteryDetails.to_json())

# convert the object into a dict
battery_details_dict = battery_details_instance.to_dict()
# create an instance of BatteryDetails from a dict
battery_details_form_dict = battery_details.from_dict(battery_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


