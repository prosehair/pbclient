# CarrierFacilityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**carrier_facility_options** | [**List[CarrierFacilityResponseCarrierFacilityOptionsInner]**](CarrierFacilityResponseCarrierFacilityOptionsInner.md) |  | [optional] 
**carrier_facility_suggestions** | [**List[CarrierFacilityResponseCarrierFacilitySuggestionsInner]**](CarrierFacilityResponseCarrierFacilitySuggestionsInner.md) |  | [optional] 

## Example

```python
from pbclient.models.carrier_facility_response import CarrierFacilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierFacilityResponse from a JSON string
carrier_facility_response_instance = CarrierFacilityResponse.from_json(json)
# print the JSON string representation of the object
print CarrierFacilityResponse.to_json()

# convert the object into a dict
carrier_facility_response_dict = carrier_facility_response_instance.to_dict()
# create an instance of CarrierFacilityResponse from a dict
carrier_facility_response_form_dict = carrier_facility_response.from_dict(carrier_facility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


