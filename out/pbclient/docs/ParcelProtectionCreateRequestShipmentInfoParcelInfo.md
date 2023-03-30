# ParcelProtectionCreateRequestShipmentInfoParcelInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commodity_list** | [**List[ParcelProtectionCreateRequestShipmentInfoParcelInfoCommodityListInner]**](ParcelProtectionCreateRequestShipmentInfoParcelInfoCommodityListInner.md) |  | [optional] 

## Example

```python
from pbclient.models.parcel_protection_create_request_shipment_info_parcel_info import ParcelProtectionCreateRequestShipmentInfoParcelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelProtectionCreateRequestShipmentInfoParcelInfo from a JSON string
parcel_protection_create_request_shipment_info_parcel_info_instance = ParcelProtectionCreateRequestShipmentInfoParcelInfo.from_json(json)
# print the JSON string representation of the object
print ParcelProtectionCreateRequestShipmentInfoParcelInfo.to_json()

# convert the object into a dict
parcel_protection_create_request_shipment_info_parcel_info_dict = parcel_protection_create_request_shipment_info_parcel_info_instance.to_dict()
# create an instance of ParcelProtectionCreateRequestShipmentInfoParcelInfo from a dict
parcel_protection_create_request_shipment_info_parcel_info_form_dict = parcel_protection_create_request_shipment_info_parcel_info.from_dict(parcel_protection_create_request_shipment_info_parcel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


