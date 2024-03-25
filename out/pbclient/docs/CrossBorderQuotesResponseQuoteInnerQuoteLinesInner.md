# CrossBorderQuotesResponseQuoteInnerQuoteLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**quote_line_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_rates** | [**CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates**](CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates.md) |  | [optional] 
**line_rates** | [**CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates**](CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates.md) |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner import CrossBorderQuotesResponseQuoteInnerQuoteLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInner from a JSON string
cross_border_quotes_response_quote_inner_quote_lines_inner_instance = CrossBorderQuotesResponseQuoteInnerQuoteLinesInner.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesResponseQuoteInnerQuoteLinesInner.to_json())

# convert the object into a dict
cross_border_quotes_response_quote_inner_quote_lines_inner_dict = cross_border_quotes_response_quote_inner_quote_lines_inner_instance.to_dict()
# create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInner from a dict
cross_border_quotes_response_quote_inner_quote_lines_inner_form_dict = cross_border_quotes_response_quote_inner_quote_lines_inner.from_dict(cross_border_quotes_response_quote_inner_quote_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


