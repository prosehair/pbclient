# ParcelDimension


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**unit_of_measurement** | [**UnitOfDimension**](UnitOfDimension.md) |  | [optional] 
**irregular_parcel_girth** | **float** |  | [optional] 

## Example

```python
from pbclient.models.parcel_dimension import ParcelDimension

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelDimension from a JSON string
parcel_dimension_instance = ParcelDimension.from_json(json)
# print the JSON string representation of the object
print ParcelDimension.to_json()

# convert the object into a dict
parcel_dimension_dict = parcel_dimension_instance.to_dict()
# create an instance of ParcelDimension from a dict
parcel_dimension_form_dict = parcel_dimension.from_dict(parcel_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


