# RadioActiveParcelDimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uom** | **str** | unit of measurement | [optional] 
**height** | **float** |  | [optional] 
**length** | **float** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from pbclient.models.radio_active_parcel_dimension import RadioActiveParcelDimension

# TODO update the JSON string below
json = "{}"
# create an instance of RadioActiveParcelDimension from a JSON string
radio_active_parcel_dimension_instance = RadioActiveParcelDimension.from_json(json)
# print the JSON string representation of the object
print(RadioActiveParcelDimension.to_json())

# convert the object into a dict
radio_active_parcel_dimension_dict = radio_active_parcel_dimension_instance.to_dict()
# create an instance of RadioActiveParcelDimension from a dict
radio_active_parcel_dimension_form_dict = radio_active_parcel_dimension.from_dict(radio_active_parcel_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


