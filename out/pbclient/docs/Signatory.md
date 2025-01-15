# Signatory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**place** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from pbclient.models.signatory import Signatory

# TODO update the JSON string below
json = "{}"
# create an instance of Signatory from a JSON string
signatory_instance = Signatory.from_json(json)
# print the JSON string representation of the object
print(Signatory.to_json())

# convert the object into a dict
signatory_dict = signatory_instance.to_dict()
# create an instance of Signatory from a dict
signatory_form_dict = signatory.from_dict(signatory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


