# ParcelProtectionPolicyResponseContentInnerPolicyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** |  | [optional] 
**policy_date** | **str** |  | [optional] 
**policy_status** | **str** |  | [optional] 
**claim_status** | **str** |  | [optional] 
**claim_status_update_date** | **str** |  | [optional] 
**value_of_goods** | **float** |  | [optional] 
**insurance_value** | **float** |  | [optional] 
**premium_value** | **float** |  | [optional] 
**base_premium** | **float** |  | [optional] 
**technology_fee** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**mail_class** | **str** |  | [optional] 
**mail_class_option** | **str** |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_policy_response_content_inner_policy_details import ParcelProtectionPolicyResponseContentInnerPolicyDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionPolicyResponseContentInnerPolicyDetails from a JSON string
parcel_protection_policy_response_content_inner_policy_details_instance = ParcelProtectionPolicyResponseContentInnerPolicyDetails.from_json(json)
# print the JSON string representation of the object
print(ParcelProtectionPolicyResponseContentInnerPolicyDetails.to_json())

# convert the object into a dict
parcel_protection_policy_response_content_inner_policy_details_dict = parcel_protection_policy_response_content_inner_policy_details_instance.to_dict()
# create an instance of ParcelProtectionPolicyResponseContentInnerPolicyDetails from a dict
parcel_protection_policy_response_content_inner_policy_details_form_dict = parcel_protection_policy_response_content_inner_policy_details.from_dict(parcel_protection_policy_response_content_inner_policy_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


