# ParcelProtectionCreateRequestShipmentInfoConsigneeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**company_name** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_numbers** | [**List[PhoneNumbersInner]**](PhoneNumbersInner.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_create_request_shipment_info_consignee_info import ParcelProtectionCreateRequestShipmentInfoConsigneeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionCreateRequestShipmentInfoConsigneeInfo from a JSON string
parcel_protection_create_request_shipment_info_consignee_info_instance = ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.to_json()

# convert the object into a dict
parcel_protection_create_request_shipment_info_consignee_info_dict = parcel_protection_create_request_shipment_info_consignee_info_instance.to_dict()
# create an instance of ParcelProtectionCreateRequestShipmentInfoConsigneeInfo from a dict
parcel_protection_create_request_shipment_info_consignee_info_form_dict = parcel_protection_create_request_shipment_info_consignee_info.from_dict(parcel_protection_create_request_shipment_info_consignee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


