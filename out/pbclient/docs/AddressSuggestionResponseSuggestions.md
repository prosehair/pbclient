# AddressSuggestionResponseSuggestions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestion_type** | **str** |  | [optional] 
**address** | [**List[Address]**](Address.md) |  | [optional] 

## Example

```python
from pbclient.models.address_suggestion_response_suggestions import AddressSuggestionResponseSuggestions

# TODO update the JSON string below
json = "{}"
# create an instance of AddressSuggestionResponseSuggestions from a JSON string
address_suggestion_response_suggestions_instance = AddressSuggestionResponseSuggestions.from_json(json)
# print the JSON string representation of the object
print AddressSuggestionResponseSuggestions.to_json()

# convert the object into a dict
address_suggestion_response_suggestions_dict = address_suggestion_response_suggestions_instance.to_dict()
# create an instance of AddressSuggestionResponseSuggestions from a dict
address_suggestion_response_suggestions_form_dict = address_suggestion_response_suggestions.from_dict(address_suggestion_response_suggestions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


