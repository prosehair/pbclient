# Parameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** | can be empty/blank, but not null | 

## Example

```python
from pbclient.models.parameter import Parameter

# TODO update the JSON string below
json = "{}"
# create an instance of Parameter from a JSON string
parameter_instance = Parameter.from_json(json)
# print the JSON string representation of the object
print(Parameter.to_json())

# convert the object into a dict
parameter_dict = parameter_instance.to_dict()
# create an instance of Parameter from a dict
parameter_form_dict = parameter.from_dict(parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


