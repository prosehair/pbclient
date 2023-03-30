# AdditionalAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | 
**address_type** | **str** |  | 

## Example

```python
from pbclient.models.additional_address import AdditionalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalAddress from a JSON string
additional_address_instance = AdditionalAddress.from_json(json)
# print the JSON string representation of the object
print AdditionalAddress.to_json()

# convert the object into a dict
additional_address_dict = additional_address_instance.to_dict()
# create an instance of AdditionalAddress from a dict
additional_address_form_dict = additional_address.from_dict(additional_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


