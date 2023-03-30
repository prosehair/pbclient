# AddressSuggestionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**suggestions** | [**AddressSuggestionResponseSuggestions**](AddressSuggestionResponseSuggestions.md) |  | [optional] 

## Example

```python
from pbclient.models.address_suggestion_response import AddressSuggestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSuggestionResponse from a JSON string
address_suggestion_response_instance = AddressSuggestionResponse.from_json(json)
# print the JSON string representation of the object
print AddressSuggestionResponse.to_json()

# convert the object into a dict
address_suggestion_response_dict = address_suggestion_response_instance.to_dict()
# create an instance of AddressSuggestionResponse from a dict
address_suggestion_response_form_dict = address_suggestion_response.from_dict(address_suggestion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


