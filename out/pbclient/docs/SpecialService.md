# SpecialService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** |  | [optional] 
**input_parameters** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**special_service_id** | **str** |  | 

## Example

```python
from pbclient.models.special_service import SpecialService

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialService from a JSON string
special_service_instance = SpecialService.from_json(json)
# print the JSON string representation of the object
print SpecialService.to_json()

# convert the object into a dict
special_service_dict = special_service_instance.to_dict()
# create an instance of SpecialService from a dict
special_service_form_dict = special_service.from_dict(special_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


