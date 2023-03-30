# ParcelProtectionQuoteRequestShipmentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**Carrier**](Carrier.md) |  | 
**service_id** | **str** |  | 
**insurance_coverage_value** | **int** |  | 
**insurance_coverage_value_currency** | **str** |  | 
**parcel_info** | [**ParcelProtectionQuoteRequestShipmentInfoParcelInfo**](ParcelProtectionQuoteRequestShipmentInfoParcelInfo.md) |  | 
**shipper_info** | [**ParcelProtectionQuoteRequestShipmentInfoShipperInfo**](ParcelProtectionQuoteRequestShipmentInfoShipperInfo.md) |  | 
**consignee_info** | [**ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo**](ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo.md) |  | 

## Example

```python
from pbclient.models.parcel_protection_quote_request_shipment_info import ParcelProtectionQuoteRequestShipmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionQuoteRequestShipmentInfo from a JSON string
parcel_protection_quote_request_shipment_info_instance = ParcelProtectionQuoteRequestShipmentInfo.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionQuoteRequestShipmentInfo.to_json()

# convert the object into a dict
parcel_protection_quote_request_shipment_info_dict = parcel_protection_quote_request_shipment_info_instance.to_dict()
# create an instance of ParcelProtectionQuoteRequestShipmentInfo from a dict
parcel_protection_quote_request_shipment_info_form_dict = parcel_protection_quote_request_shipment_info.from_dict(parcel_protection_quote_request_shipment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


