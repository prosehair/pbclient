# Manifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**Carrier**](Carrier.md) |  | 
**documents** | [**List[Document]**](Document.md) |  | [optional] 
**from_address** | [**Address**](Address.md) |  | [optional] 
**induction_postal_code** | **str** |  | [optional] 
**manifest_id** | **str** |  | [optional] 
**manifest_tracking_number** | **str** |  | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**parcel_tracking_numbers** | **List[str]** |  | [optional] 
**submission_date** | **str** |  | 

## Example

```python
from pbclient.models.manifest import Manifest

# TODO update the JSON string below
json = "{}"
# create an instance of Manifest from a JSON string
manifest_instance = Manifest.from_json(json)
# print the JSON string representation of the object
print(Manifest.to_json())

# convert the object into a dict
manifest_dict = manifest_instance.to_dict()
# create an instance of Manifest from a dict
manifest_form_dict = manifest.from_dict(manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


