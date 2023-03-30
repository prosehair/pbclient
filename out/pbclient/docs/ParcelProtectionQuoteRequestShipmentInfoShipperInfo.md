# ParcelProtectionQuoteRequestShipmentInfoShipperInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper_id** | **str** |  | 
**address** | [**ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress**](ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress.md) |  | 

## Example

```python
from pbclient.models.parcel_protection_quote_request_shipment_info_shipper_info import ParcelProtectionQuoteRequestShipmentInfoShipperInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionQuoteRequestShipmentInfoShipperInfo from a JSON string
parcel_protection_quote_request_shipment_info_shipper_info_instance = ParcelProtectionQuoteRequestShipmentInfoShipperInfo.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionQuoteRequestShipmentInfoShipperInfo.to_json()

# convert the object into a dict
parcel_protection_quote_request_shipment_info_shipper_info_dict = parcel_protection_quote_request_shipment_info_shipper_info_instance.to_dict()
# create an instance of ParcelProtectionQuoteRequestShipmentInfoShipperInfo from a dict
parcel_protection_quote_request_shipment_info_shipper_info_form_dict = parcel_protection_quote_request_shipment_info_shipper_info.from_dict(parcel_protection_quote_request_shipment_info_shipper_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


