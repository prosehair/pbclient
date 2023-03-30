# ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[str]** |  | 
**city_town** | **str** |  | 
**state_province** | **str** |  | 
**postal_code** | **str** |  | 
**country_code** | **str** |  | 

## Example

```python
from pbclient.models.parcel_protection_quote_request_shipment_info_shipper_info_address import ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress from a JSON string
parcel_protection_quote_request_shipment_info_shipper_info_address_instance = ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress.to_json()

# convert the object into a dict
parcel_protection_quote_request_shipment_info_shipper_info_address_dict = parcel_protection_quote_request_shipment_info_shipper_info_address_instance.to_dict()
# create an instance of ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress from a dict
parcel_protection_quote_request_shipment_info_shipper_info_address_form_dict = parcel_protection_quote_request_shipment_info_shipper_info_address.from_dict(parcel_protection_quote_request_shipment_info_shipper_info_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


