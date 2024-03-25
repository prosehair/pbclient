# ParcelWeight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight** | **float** |  | [optional] 
**unit_of_measurement** | [**UnitOfWeight**](UnitOfWeight.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_weight import ParcelWeight

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelWeight from a JSON string
parcel_weight_instance = ParcelWeight.from_json(json)
# print the JSON string representation of the object
print(ParcelWeight.to_json())

# convert the object into a dict
parcel_weight_dict = parcel_weight_instance.to_dict()
# create an instance of ParcelWeight from a dict
parcel_weight_form_dict = parcel_weight.from_dict(parcel_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


