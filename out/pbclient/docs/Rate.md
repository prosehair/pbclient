# Rate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_base_charge** | **float** |  | [optional] 
**alternate_total_charge** | **float** |  | [optional] 
**base_charge** | **float** |  | [optional] 
**base_charge_taxes** | [**List[Tax]**](Tax.md) |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | 
**currency_code** | **str** | ISO-4217 | [optional] 
**delivery_commitment** | [**DeliveryCommitment**](DeliveryCommitment.md) |  | [optional] 
**destination_zone** | [**RateDestinationZone**](RateDestinationZone.md) |  | [optional] 
**dimensional_weight** | [**ParcelWeight**](ParcelWeight.md) |  | [optional] 
**discounts** | [**List[Discount]**](Discount.md) |  | [optional] 
**induction_postal_code** | **str** |  | [optional] 
**parcel_type** | [**ParcelType**](ParcelType.md) |  | 
**rate_type_id** | **str** |  | [optional] 
**service_id** | [**Services**](Services.md) |  | [optional] 
**special_services** | [**List[SpecialService]**](SpecialService.md) |  | [optional] 
**surcharges** | [**List[Surcharge]**](Surcharge.md) |  | [optional] 
**total_carrier_charge** | **float** |  | [optional] 
**total_tax_amount** | **float** |  | [optional] 

## Example

```python
from pbclient.models.rate import Rate

# TODO update the JSON string below
json = "{}"
# create an instance of Rate from a JSON string
rate_instance = Rate.from_json(json)
# print the JSON string representation of the object
print Rate.to_json()

# convert the object into a dict
rate_dict = rate_instance.to_dict()
# create an instance of Rate from a dict
rate_form_dict = rate.from_dict(rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


