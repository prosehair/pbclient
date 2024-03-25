# CrossBorderQuotesErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote** | [**List[CrossBorderQuotesErrorsQuoteInner]**](CrossBorderQuotesErrorsQuoteInner.md) |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_errors import CrossBorderQuotesErrors

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesErrors from a JSON string
cross_border_quotes_errors_instance = CrossBorderQuotesErrors.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesErrors.to_json())

# convert the object into a dict
cross_border_quotes_errors_dict = cross_border_quotes_errors_instance.to_dict()
# create an instance of CrossBorderQuotesErrors from a dict
cross_border_quotes_errors_form_dict = cross_border_quotes_errors.from_dict(cross_border_quotes_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


