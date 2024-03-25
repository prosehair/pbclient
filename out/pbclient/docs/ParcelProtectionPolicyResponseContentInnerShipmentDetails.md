# ParcelProtectionPolicyResponseContentInnerShipmentDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_date** | **str** |  | [optional] 
**shipment_transaction_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**parcel_tracking_number** | **str** |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**amount** | **str** |  | [optional] 
**package_length** | **str** |  | [optional] 
**package_width** | **str** |  | [optional] 
**package_height** | **str** |  | [optional] 
**weight** | **str** |  | [optional] 
**zone** | **str** |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_policy_response_content_inner_shipment_details import ParcelProtectionPolicyResponseContentInnerShipmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionPolicyResponseContentInnerShipmentDetails from a JSON string
parcel_protection_policy_response_content_inner_shipment_details_instance = ParcelProtectionPolicyResponseContentInnerShipmentDetails.from_json(json)
# print the JSON string representation of the object
print(ParcelProtectionPolicyResponseContentInnerShipmentDetails.to_json())

# convert the object into a dict
parcel_protection_policy_response_content_inner_shipment_details_dict = parcel_protection_policy_response_content_inner_shipment_details_instance.to_dict()
# create an instance of ParcelProtectionPolicyResponseContentInnerShipmentDetails from a dict
parcel_protection_policy_response_content_inner_shipment_details_form_dict = parcel_protection_policy_response_content_inner_shipment_details.from_dict(parcel_protection_policy_response_content_inner_shipment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


