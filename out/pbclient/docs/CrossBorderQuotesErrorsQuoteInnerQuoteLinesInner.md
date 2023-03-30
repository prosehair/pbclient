# CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **str** |  | [optional] 
**merchant_com_ref_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_errors** | [**List[CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner]**](CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner.md) |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_errors_quote_inner_quote_lines_inner import CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner from a JSON string
cross_border_quotes_errors_quote_inner_quote_lines_inner_instance = CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner.from_json(json)
# print the JSON string representation of the object
print CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner.to_json()

# convert the object into a dict
cross_border_quotes_errors_quote_inner_quote_lines_inner_dict = cross_border_quotes_errors_quote_inner_quote_lines_inner_instance.to_dict()
# create an instance of CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner from a dict
cross_border_quotes_errors_quote_inner_quote_lines_inner_form_dict = cross_border_quotes_errors_quote_inner_quote_lines_inner.from_dict(cross_border_quotes_errors_quote_inner_quote_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


