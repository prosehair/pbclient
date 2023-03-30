# ParcelProtectionCreateRequestShipmentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_number** | **str** |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**service_id** | **str** |  | [optional] 
**insurance_coverage_value** | **int** |  | [optional] 
**insurance_coverage_value_currency** | **str** |  | [optional] 
**parcel_info** | [**ParcelProtectionCreateRequestShipmentInfoParcelInfo**](ParcelProtectionCreateRequestShipmentInfoParcelInfo.md) |  | [optional] 
**shipper_info** | [**ParcelProtectionCreateRequestShipmentInfoShipperInfo**](ParcelProtectionCreateRequestShipmentInfoShipperInfo.md) |  | [optional] 
**consignee_info** | [**ParcelProtectionCreateRequestShipmentInfoConsigneeInfo**](ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_create_request_shipment_info import ParcelProtectionCreateRequestShipmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionCreateRequestShipmentInfo from a JSON string
parcel_protection_create_request_shipment_info_instance = ParcelProtectionCreateRequestShipmentInfo.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionCreateRequestShipmentInfo.to_json()

# convert the object into a dict
parcel_protection_create_request_shipment_info_dict = parcel_protection_create_request_shipment_info_instance.to_dict()
# create an instance of ParcelProtectionCreateRequestShipmentInfo from a dict
parcel_protection_create_request_shipment_info_form_dict = parcel_protection_create_request_shipment_info.from_dict(parcel_protection_create_request_shipment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


