# VoidParcelProtectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_id** | **str** |  | [optional] 
**parcel_protection_account_id** | **str** | Parcel Protection account ID, if applicable. | [optional] 

## Example

```python
from pbclient.models.void_parcel_protection_request import VoidParcelProtectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidParcelProtectionRequest from a JSON string
void_parcel_protection_request_instance = VoidParcelProtectionRequest.from_json(json)
# print the JSON string representation of the object
print(VoidParcelProtectionRequest.to_json())

# convert the object into a dict
void_parcel_protection_request_dict = void_parcel_protection_request_instance.to_dict()
# create an instance of VoidParcelProtectionRequest from a dict
void_parcel_protection_request_form_dict = void_parcel_protection_request.from_dict(void_parcel_protection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


