# SpecialServicesRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_service_id** | [**SpecialServiceCodes**](SpecialServiceCodes.md) |  | [optional] 
**branded_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**trackable** | **bool** |  | [optional] 
**input_parameter_rules** | [**List[ServicesParameterRule]**](ServicesParameterRule.md) |  | [optional] 
**prerequisite_rules** | [**List[PrerequisiteRules]**](PrerequisiteRules.md) |  | [optional] 
**incompatible_special_services** | [**SpecialServiceCodes**](SpecialServiceCodes.md) |  | [optional] 

## Example

```python
from pbclient.models.special_services_rule import SpecialServicesRule

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialServicesRule from a JSON string
special_services_rule_instance = SpecialServicesRule.from_json(json)
# print the JSON string representation of the object
print(SpecialServicesRule.to_json())

# convert the object into a dict
special_services_rule_dict = special_services_rule_instance.to_dict()
# create an instance of SpecialServicesRule from a dict
special_services_rule_form_dict = special_services_rule.from_dict(special_services_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


