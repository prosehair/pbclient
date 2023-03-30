# HazmatDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_details** | [**BatteryDetails**](BatteryDetails.md) |  | [optional] 
**commodity_type** | **str** |  | [optional] 
**container_count** | **int** |  | [optional] 
**container_details** | [**List[ContainerDetails]**](ContainerDetails.md) |  | [optional] 
**emergency_contact_number** | **str** |  | [optional] 
**hazmat_document_type** | **str** |  | [optional] 
**identical_containers** | **bool** |  | [optional] 
**offeror** | **str** |  | [optional] 
**packaging_option** | **str** |  | [optional] 
**signatory** | [**Signatory**](Signatory.md) |  | [optional] 

## Example

```python
from pbclient.models.hazmat_details import HazmatDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HazmatDetails from a JSON string
hazmat_details_instance = HazmatDetails.from_json(json)
# print the JSON string representation of the object
print HazmatDetails.to_json()

# convert the object into a dict
hazmat_details_dict = hazmat_details_instance.to_dict()
# create an instance of HazmatDetails from a dict
hazmat_details_form_dict = hazmat_details.from_dict(hazmat_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


