# ParcelProtectionPolicyResponseContentInnerShipperInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_number1** | **str** |  | [optional] 
**phone_number2** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**address** | [**ParcelProtectionPolicyResponseContentInnerShipperInfoAddress**](ParcelProtectionPolicyResponseContentInnerShipperInfoAddress.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_policy_response_content_inner_shipper_info import ParcelProtectionPolicyResponseContentInnerShipperInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfo from a JSON string
parcel_protection_policy_response_content_inner_shipper_info_instance = ParcelProtectionPolicyResponseContentInnerShipperInfo.from_json(json)
# print the JSON string representation of the object
print(ParcelProtectionPolicyResponseContentInnerShipperInfo.to_json())

# convert the object into a dict
parcel_protection_policy_response_content_inner_shipper_info_dict = parcel_protection_policy_response_content_inner_shipper_info_instance.to_dict()
# create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfo from a dict
parcel_protection_policy_response_content_inner_shipper_info_form_dict = parcel_protection_policy_response_content_inner_shipper_info.from_dict(parcel_protection_policy_response_content_inner_shipper_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


