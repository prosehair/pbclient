# CancelShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_initiator** | **str** |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**error_messages** | [**List[Errors]**](Errors.md) |  | [optional] 
**parcel_tracking_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_carrier_charge** | **float** |  | [optional] 

## Example

```python
from pbclient.models.cancel_shipment import CancelShipment

# TODO update the JSON string below
json = "{}"
# create an instance of CancelShipment from a JSON string
cancel_shipment_instance = CancelShipment.from_json(json)
# print the JSON string representation of the object
print(CancelShipment.to_json())

# convert the object into a dict
cancel_shipment_dict = cancel_shipment_instance.to_dict()
# create an instance of CancelShipment from a dict
cancel_shipment_form_dict = cancel_shipment.from_dict(cancel_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


