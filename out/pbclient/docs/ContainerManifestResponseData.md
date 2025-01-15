# ContainerManifestResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pb_container_id** | **str** |  | [optional] 
**label_data** | **str** |  | [optional] 

## Example

```python
from pbclient.models.container_manifest_response_data import ContainerManifestResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerManifestResponseData from a JSON string
container_manifest_response_data_instance = ContainerManifestResponseData.from_json(json)
# print the JSON string representation of the object
print(ContainerManifestResponseData.to_json())

# convert the object into a dict
container_manifest_response_data_dict = container_manifest_response_data_instance.to_dict()
# create an instance of ContainerManifestResponseData from a dict
container_manifest_response_data_form_dict = container_manifest_response_data.from_dict(container_manifest_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


