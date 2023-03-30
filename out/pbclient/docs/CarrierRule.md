# CarrierRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | [**Services**](Services.md) |  | [optional] 
**branded_name** | **str** |  | [optional] 
**parcel_type_rules** | [**List[ParcelTypeRules]**](ParcelTypeRules.md) |  | [optional] 
**parameters** | **List[str]** |  | [optional] 

## Example

```python
from pbclient.models.carrier_rule import CarrierRule

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierRule from a JSON string
carrier_rule_instance = CarrierRule.from_json(json)
# print the JSON string representation of the object
print CarrierRule.to_json()

# convert the object into a dict
carrier_rule_dict = carrier_rule_instance.to_dict()
# create an instance of CarrierRule from a dict
carrier_rule_form_dict = carrier_rule.from_dict(carrier_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


