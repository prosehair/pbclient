# ContainerManifestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ContainerManifestResponseData**](ContainerManifestResponseData.md) |  | [optional] 

## Example

```python
from pbclient.models.container_manifest_response import ContainerManifestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerManifestResponse from a JSON string
container_manifest_response_instance = ContainerManifestResponse.from_json(json)
# print the JSON string representation of the object
print(ContainerManifestResponse.to_json())

# convert the object into a dict
container_manifest_response_dict = container_manifest_response_instance.to_dict()
# create an instance of ContainerManifestResponse from a dict
container_manifest_response_form_dict = container_manifest_response.from_dict(container_manifest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


