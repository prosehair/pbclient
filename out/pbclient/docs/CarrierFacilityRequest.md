# CarrierFacilityRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CarrierFacilityRequestAddress**](CarrierFacilityRequestAddress.md) |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**carrier_facility_options** | [**List[CarrierFacilityResponseCarrierFacilityOptionsInner]**](CarrierFacilityResponseCarrierFacilityOptionsInner.md) |  | [optional] 

## Example

```python
from pbclient.models.carrier_facility_request import CarrierFacilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierFacilityRequest from a JSON string
carrier_facility_request_instance = CarrierFacilityRequest.from_json(json)
# print the JSON string representation of the object
print CarrierFacilityRequest.to_json()

# convert the object into a dict
carrier_facility_request_dict = carrier_facility_request_instance.to_dict()
# create an instance of CarrierFacilityRequest from a dict
carrier_facility_request_form_dict = carrier_facility_request.from_dict(carrier_facility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


