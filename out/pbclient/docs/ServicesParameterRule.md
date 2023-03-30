# ServicesParameterRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**branded_name** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**min_value** | **float** |  | [optional] 
**max_value** | **float** |  | [optional] 
**free_value** | **float** |  | [optional] 
**format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from pbclient.models.services_parameter_rule import ServicesParameterRule

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesParameterRule from a JSON string
services_parameter_rule_instance = ServicesParameterRule.from_json(json)
# print the JSON string representation of the object
print ServicesParameterRule.to_json()

# convert the object into a dict
services_parameter_rule_dict = services_parameter_rule_instance.to_dict()
# create an instance of ServicesParameterRule from a dict
services_parameter_rule_form_dict = services_parameter_rule.from_dict(services_parameter_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


