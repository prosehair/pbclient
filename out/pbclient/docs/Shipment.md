# Shipment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_addresses** | [**List[AdditionalAddress]**](AdditionalAddress.md) |  | [optional] 
**alt_return_address** | [**Address**](Address.md) |  | [optional] 
**carrier_payments** | [**List[CarrierPayment]**](CarrierPayment.md) |  | [optional] 
**customs** | [**Customs**](Customs.md) |  | [optional] 
**documents** | [**List[Document]**](Document.md) |  | [optional] 
**from_address** | [**Address**](Address.md) |  | 
**hazmat_details** | [**HazmatDetails**](HazmatDetails.md) |  | [optional] 
**parcel** | [**Parcel**](Parcel.md) |  | 
**parcel_tracking_number** | **str** |  | [optional] 
**rates** | [**List[Rate]**](Rate.md) |  | 
**references** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**shipment_options** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**shipment_type** | **str** |  | [optional] 
**sold_to_address** | [**Address**](Address.md) |  | [optional] 
**to_address** | [**Address**](Address.md) |  | 

## Example

```python
from pbclient.models.shipment import Shipment

# TODO update the JSON string below
json = "{}"
# create an instance of Shipment from a JSON string
shipment_instance = Shipment.from_json(json)
# print the JSON string representation of the object
print Shipment.to_json()

# convert the object into a dict
shipment_dict = shipment_instance.to_dict()
# create an instance of Shipment from a dict
shipment_form_dict = shipment.from_dict(shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


