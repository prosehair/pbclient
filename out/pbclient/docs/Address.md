# Address


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_lines** | **List[str]** |  | [optional] 
**carrier_route** | **str** |  | [optional] 
**city_town** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**country_code** | **str** | 2-character country code (ISO-3166-1 alpha-2) | 
**delivery_point** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**residential** | **bool** |  | [optional] 
**state_province** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_id_type** | **str** |  | [optional] 

## Example

```python
from pbclient.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print Address.to_json()

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_form_dict = address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


