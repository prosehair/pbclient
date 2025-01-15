# CrossBorderQuotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote** | [**List[CrossBorderQuotesResponseQuoteInner]**](CrossBorderQuotesResponseQuoteInner.md) |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_response import CrossBorderQuotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesResponse from a JSON string
cross_border_quotes_response_instance = CrossBorderQuotesResponse.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesResponse.to_json())

# convert the object into a dict
cross_border_quotes_response_dict = cross_border_quotes_response_instance.to_dict()
# create an instance of CrossBorderQuotesResponse from a dict
cross_border_quotes_response_form_dict = cross_border_quotes_response.from_dict(cross_border_quotes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


