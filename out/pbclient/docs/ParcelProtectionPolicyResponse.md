# ParcelProtectionPolicyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[ParcelProtectionPolicyResponseContentInner]**](ParcelProtectionPolicyResponseContentInner.md) |  | [optional] 
**last** | **bool** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**List[ParcelProtectionPolicyResponseSortInner]**](ParcelProtectionPolicyResponseSortInner.md) |  | [optional] 
**size** | **int** |  | [optional] 
**number** | **int** |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_policy_response import ParcelProtectionPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionPolicyResponse from a JSON string
parcel_protection_policy_response_instance = ParcelProtectionPolicyResponse.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionPolicyResponse.to_json()

# convert the object into a dict
parcel_protection_policy_response_dict = parcel_protection_policy_response_instance.to_dict()
# create an instance of ParcelProtectionPolicyResponse from a dict
parcel_protection_policy_response_form_dict = parcel_protection_policy_response.from_dict(parcel_protection_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


