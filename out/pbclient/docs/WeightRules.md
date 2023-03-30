# WeightRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** |  | [optional] 
**unit_of_measurement** | **str** |  | [optional] 
**min_weight** | **float** |  | [optional] 
**max_weight** | **float** |  | [optional] 

## Example

```python
from pbclient.models.weight_rules import WeightRules

# TODO update the JSON string below
json = "{}"
# create an instance of WeightRules from a JSON string
weight_rules_instance = WeightRules.from_json(json)
# print the JSON string representation of the object
print WeightRules.to_json()

# convert the object into a dict
weight_rules_dict = weight_rules_instance.to_dict()
# create an instance of WeightRules from a dict
weight_rules_form_dict = weight_rules.from_dict(weight_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


