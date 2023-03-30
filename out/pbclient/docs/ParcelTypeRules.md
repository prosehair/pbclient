# ParcelTypeRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_type** | [**ParcelType**](ParcelType.md) |  | [optional] 
**branded_name** | **str** |  | [optional] 
**rate_type_id** | **str** |  | [optional] 
**rate_type_branded_name** | **str** |  | [optional] 
**trackable** | [**Trackable**](Trackable.md) |  | [optional] 
**special_services_rule** | [**List[SpecialServicesRule]**](SpecialServicesRule.md) |  | [optional] 
**weight_rules** | [**List[WeightRules]**](WeightRules.md) |  | [optional] 
**dimension_rules** | [**List[DimensionRules]**](DimensionRules.md) |  | [optional] 
**suggested_trackable_special_service_id** | [**SpecialServiceCodes**](SpecialServiceCodes.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_type_rules import ParcelTypeRules

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelTypeRules from a JSON string
parcel_type_rules_instance = ParcelTypeRules.from_json(json)
# print the JSON string representation of the object
print ParcelTypeRules.to_json()

# convert the object into a dict
parcel_type_rules_dict = parcel_type_rules_instance.to_dict()
# create an instance of ParcelTypeRules from a dict
parcel_type_rules_form_dict = parcel_type_rules.from_dict(parcel_type_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


