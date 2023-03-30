# CrossBorderQuotesErrorsQuoteInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_currency** | **str** |  | [optional] 
**quote_lines** | [**List[CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner]**](CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner.md) |  | [optional] 
**errors** | [**CrossBorderQuotesErrorsQuoteInnerErrors**](CrossBorderQuotesErrorsQuoteInnerErrors.md) |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_errors_quote_inner import CrossBorderQuotesErrorsQuoteInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesErrorsQuoteInner from a JSON string
cross_border_quotes_errors_quote_inner_instance = CrossBorderQuotesErrorsQuoteInner.from_json(json)
# print the JSON string representation of the object
print CrossBorderQuotesErrorsQuoteInner.to_json()

# convert the object into a dict
cross_border_quotes_errors_quote_inner_dict = cross_border_quotes_errors_quote_inner_instance.to_dict()
# create an instance of CrossBorderQuotesErrorsQuoteInner from a dict
cross_border_quotes_errors_quote_inner_form_dict = cross_border_quotes_errors_quote_inner.from_dict(cross_border_quotes_errors_quote_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


