# RadioActivityDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criticality_safety_index** | **float** |  | [optional] 
**radio_active_parcel_dimension** | [**RadioActiveParcelDimension**](RadioActiveParcelDimension.md) |  | [optional] 
**surface_reading** | **float** |  | [optional] 
**transport_index** | **float** |  | [optional] 

## Example

```python
from pbclient.models.radio_activity_detail import RadioActivityDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RadioActivityDetail from a JSON string
radio_activity_detail_instance = RadioActivityDetail.from_json(json)
# print the JSON string representation of the object
print RadioActivityDetail.to_json()

# convert the object into a dict
radio_activity_detail_dict = radio_activity_detail_instance.to_dict()
# create an instance of RadioActivityDetail from a dict
radio_activity_detail_form_dict = radio_activity_detail.from_dict(radio_activity_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


