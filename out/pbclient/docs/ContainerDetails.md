# ContainerDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commodity_info** | [**List[CommodityInfo]**](CommodityInfo.md) |  | [optional] 
**container_type** | **str** |  | [optional] 
**packaging_type** | **str** |  | [optional] 

## Example

```python
from pbclient.models.container_details import ContainerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerDetails from a JSON string
container_details_instance = ContainerDetails.from_json(json)
# print the JSON string representation of the object
print(ContainerDetails.to_json())

# convert the object into a dict
container_details_dict = container_details_instance.to_dict()
# create an instance of ContainerDetails from a dict
container_details_form_dict = container_details.from_dict(container_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


