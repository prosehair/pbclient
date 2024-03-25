# CarrierFacilityResponseCarrierFacilitySuggestionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**carrier_facility_attributes** | [**List[CarrierFacilityResponseCarrierFacilityOptionsInner]**](CarrierFacilityResponseCarrierFacilityOptionsInner.md) |  | [optional] 
**facility_hours** | [**List[CarrierFacilityResponseCarrierFacilitySuggestionsInnerFacilityHoursInner]**](CarrierFacilityResponseCarrierFacilitySuggestionsInnerFacilityHoursInner.md) |  | [optional] 
**facility_parking** | **str** |  | [optional] 

## Example

```python
from pbclient.models.carrier_facility_response_carrier_facility_suggestions_inner import CarrierFacilityResponseCarrierFacilitySuggestionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierFacilityResponseCarrierFacilitySuggestionsInner from a JSON string
carrier_facility_response_carrier_facility_suggestions_inner_instance = CarrierFacilityResponseCarrierFacilitySuggestionsInner.from_json(json)
# print the JSON string representation of the object
print(CarrierFacilityResponseCarrierFacilitySuggestionsInner.to_json())

# convert the object into a dict
carrier_facility_response_carrier_facility_suggestions_inner_dict = carrier_facility_response_carrier_facility_suggestions_inner_instance.to_dict()
# create an instance of CarrierFacilityResponseCarrierFacilitySuggestionsInner from a dict
carrier_facility_response_carrier_facility_suggestions_inner_form_dict = carrier_facility_response_carrier_facility_suggestions_inner.from_dict(carrier_facility_response_carrier_facility_suggestions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


