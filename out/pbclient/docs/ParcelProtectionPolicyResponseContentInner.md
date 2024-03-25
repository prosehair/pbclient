# ParcelProtectionPolicyResponseContentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**developer_id** | **str** |  | [optional] 
**subscription_acc_no** | **str** |  | [optional] 
**client_transaction_id** | **str** |  | [optional] 
**policy_details** | [**ParcelProtectionPolicyResponseContentInnerPolicyDetails**](ParcelProtectionPolicyResponseContentInnerPolicyDetails.md) |  | [optional] 
**shipment_details** | [**ParcelProtectionPolicyResponseContentInnerShipmentDetails**](ParcelProtectionPolicyResponseContentInnerShipmentDetails.md) |  | [optional] 
**shipper_info** | [**ParcelProtectionPolicyResponseContentInnerShipperInfo**](ParcelProtectionPolicyResponseContentInnerShipperInfo.md) |  | [optional] 
**consignee_info** | [**ParcelProtectionPolicyResponseContentInnerShipperInfo**](ParcelProtectionPolicyResponseContentInnerShipperInfo.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_policy_response_content_inner import ParcelProtectionPolicyResponseContentInner

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionPolicyResponseContentInner from a JSON string
parcel_protection_policy_response_content_inner_instance = ParcelProtectionPolicyResponseContentInner.from_json(json)
# print the JSON string representation of the object
print(ParcelProtectionPolicyResponseContentInner.to_json())

# convert the object into a dict
parcel_protection_policy_response_content_inner_dict = parcel_protection_policy_response_content_inner_instance.to_dict()
# create an instance of ParcelProtectionPolicyResponseContentInner from a dict
parcel_protection_policy_response_content_inner_form_dict = parcel_protection_policy_response_content_inner.from_dict(parcel_protection_policy_response_content_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


