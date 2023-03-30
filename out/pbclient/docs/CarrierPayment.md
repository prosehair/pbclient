# CarrierPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**party** | **str** |  | 
**postal_code** | **str** |  | [optional] 
**type_of_charge** | **str** |  | 

## Example

```python
from pbclient.models.carrier_payment import CarrierPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CarrierPayment from a JSON string
carrier_payment_instance = CarrierPayment.from_json(json)
# print the JSON string representation of the object
print CarrierPayment.to_json()

# convert the object into a dict
carrier_payment_dict = carrier_payment_instance.to_dict()
# create an instance of CarrierPayment from a dict
carrier_payment_form_dict = carrier_payment.from_dict(carrier_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


