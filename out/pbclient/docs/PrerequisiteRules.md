# PrerequisiteRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_service_codes** | [**SpecialServiceCodes**](SpecialServiceCodes.md) |  | [optional] 
**min_input_value** | **float** |  | [optional] 

## Example

```python
from pbclient.models.prerequisite_rules import PrerequisiteRules

# TODO update the JSON string below
json = "{}"
# create an instance of PrerequisiteRules from a JSON string
prerequisite_rules_instance = PrerequisiteRules.from_json(json)
# print the JSON string representation of the object
print(PrerequisiteRules.to_json())

# convert the object into a dict
prerequisite_rules_dict = prerequisite_rules_instance.to_dict()
# create an instance of PrerequisiteRules from a dict
prerequisite_rules_form_dict = prerequisite_rules.from_dict(prerequisite_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


