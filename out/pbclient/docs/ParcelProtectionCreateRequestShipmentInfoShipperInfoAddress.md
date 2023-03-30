# ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[str]** |  | [optional] 
**city_town** | **str** |  | [optional] 
**state_province** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_create_request_shipment_info_shipper_info_address import ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress from a JSON string
parcel_protection_create_request_shipment_info_shipper_info_address_instance = ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress.to_json()

# convert the object into a dict
parcel_protection_create_request_shipment_info_shipper_info_address_dict = parcel_protection_create_request_shipment_info_shipper_info_address_instance.to_dict()
# create an instance of ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress from a dict
parcel_protection_create_request_shipment_info_shipper_info_address_form_dict = parcel_protection_create_request_shipment_info_shipper_info_address.from_dict(parcel_protection_create_request_shipment_info_shipper_info_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


