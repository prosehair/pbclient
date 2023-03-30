# ParcelProtectionPolicyResponseContentInnerShipperInfoAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**street3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_policy_response_content_inner_shipper_info_address import ParcelProtectionPolicyResponseContentInnerShipperInfoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfoAddress from a JSON string
parcel_protection_policy_response_content_inner_shipper_info_address_instance = ParcelProtectionPolicyResponseContentInnerShipperInfoAddress.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionPolicyResponseContentInnerShipperInfoAddress.to_json()

# convert the object into a dict
parcel_protection_policy_response_content_inner_shipper_info_address_dict = parcel_protection_policy_response_content_inner_shipper_info_address_instance.to_dict()
# create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfoAddress from a dict
parcel_protection_policy_response_content_inner_shipper_info_address_form_dict = parcel_protection_policy_response_content_inner_shipper_info_address.from_dict(parcel_protection_policy_response_content_inner_shipper_info_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


