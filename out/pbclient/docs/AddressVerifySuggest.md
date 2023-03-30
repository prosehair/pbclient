# AddressVerifySuggest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from pbclient.models.address_verify_suggest import AddressVerifySuggest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressVerifySuggest from a JSON string
address_verify_suggest_instance = AddressVerifySuggest.from_json(json)
# print the JSON string representation of the object
print AddressVerifySuggest.to_json()

# convert the object into a dict
address_verify_suggest_dict = address_verify_suggest_instance.to_dict()
# create an instance of AddressVerifySuggest from a dict
address_verify_suggest_form_dict = address_verify_suggest.from_dict(address_verify_suggest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


