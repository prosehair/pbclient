# RadioNuclideDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemical_form** | **str** |  | [optional] 
**expected_package_reportable_quantity** | **bool** |  | [optional] 
**physical_form** | **str** |  | [optional] 
**radio_nuclide** | **str** |  | [optional] 
**radio_nuclide_activity_uom** | **str** |  | [optional] 
**radio_nuclide_activity_value** | **float** |  | [optional] 

## Example

```python
from pbclient.models.radio_nuclide_detail import RadioNuclideDetail

# TODO update the JSON string below
json = "{}"
# create an instance of RadioNuclideDetail from a JSON string
radio_nuclide_detail_instance = RadioNuclideDetail.from_json(json)
# print the JSON string representation of the object
print RadioNuclideDetail.to_json()

# convert the object into a dict
radio_nuclide_detail_dict = radio_nuclide_detail_instance.to_dict()
# create an instance of RadioNuclideDetail from a dict
radio_nuclide_detail_form_dict = radio_nuclide_detail.from_dict(radio_nuclide_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


