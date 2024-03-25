# Parcel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | [**ParcelDimension**](ParcelDimension.md) |  | [optional] 
**weight** | [**ParcelWeight**](ParcelWeight.md) |  | [optional] 
**value_of_goods** | **float** |  | [optional] 
**currency_code** | **str** | Currency code as per [IOS 4217](https://en.wikipedia.org/wiki/ISO_4217) | [optional] 

## Example

```python
from pbclient.models.parcel import Parcel

# TODO update the JSON string below
json = "{}"
# create an instance of Parcel from a JSON string
parcel_instance = Parcel.from_json(json)
# print the JSON string representation of the object
print(Parcel.to_json())

# convert the object into a dict
parcel_dict = parcel_instance.to_dict()
# create an instance of Parcel from a dict
parcel_form_dict = parcel.from_dict(parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


