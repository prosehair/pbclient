# ParcelProtectionPolicyResponseSortInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**var_property** | **str** |  | [optional] 
**ignore_case** | **bool** |  | [optional] 
**null_handling** | **str** |  | [optional] 
**descending** | **bool** |  | [optional] 
**ascending** | **bool** |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_policy_response_sort_inner import ParcelProtectionPolicyResponseSortInner

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionPolicyResponseSortInner from a JSON string
parcel_protection_policy_response_sort_inner_instance = ParcelProtectionPolicyResponseSortInner.from_json(json)
# print the JSON string representation of the object
print(ParcelProtectionPolicyResponseSortInner.to_json())

# convert the object into a dict
parcel_protection_policy_response_sort_inner_dict = parcel_protection_policy_response_sort_inner_instance.to_dict()
# create an instance of ParcelProtectionPolicyResponseSortInner from a dict
parcel_protection_policy_response_sort_inner_form_dict = parcel_protection_policy_response_sort_inner.from_dict(parcel_protection_policy_response_sort_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


