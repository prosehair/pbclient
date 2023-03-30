# ParcelProtectionCreateRequestShipmentInfoShipperInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_id** | **str** |  | [optional] 
**address** | [**ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress**](ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress.md) |  | [optional] 
**company_name** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**given_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_numbers** | [**List[PhoneNumbersInner]**](PhoneNumbersInner.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_create_request_shipment_info_shipper_info import ParcelProtectionCreateRequestShipmentInfoShipperInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionCreateRequestShipmentInfoShipperInfo from a JSON string
parcel_protection_create_request_shipment_info_shipper_info_instance = ParcelProtectionCreateRequestShipmentInfoShipperInfo.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionCreateRequestShipmentInfoShipperInfo.to_json()

# convert the object into a dict
parcel_protection_create_request_shipment_info_shipper_info_dict = parcel_protection_create_request_shipment_info_shipper_info_instance.to_dict()
# create an instance of ParcelProtectionCreateRequestShipmentInfoShipperInfo from a dict
parcel_protection_create_request_shipment_info_shipper_info_form_dict = parcel_protection_create_request_shipment_info_shipper_info.from_dict(parcel_protection_create_request_shipment_info_shipper_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


