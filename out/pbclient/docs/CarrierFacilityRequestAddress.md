# CarrierFacilityRequestAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[str]** |  | [optional] 
**city_town** | **str** |  | [optional] 
**state_province** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 

## Example

```python
from pbclient.models.carrier_facility_request_address import CarrierFacilityRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierFacilityRequestAddress from a JSON string
carrier_facility_request_address_instance = CarrierFacilityRequestAddress.from_json(json)
# print the JSON string representation of the object
print CarrierFacilityRequestAddress.to_json()

# convert the object into a dict
carrier_facility_request_address_dict = carrier_facility_request_address_instance.to_dict()
# create an instance of CarrierFacilityRequestAddress from a dict
carrier_facility_request_address_form_dict = carrier_facility_request_address.from_dict(carrier_facility_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


