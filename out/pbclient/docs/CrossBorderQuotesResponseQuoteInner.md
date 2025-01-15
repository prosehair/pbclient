# CrossBorderQuotesResponseQuoteInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_currency** | **str** |  | [optional] 
**quote_lines** | [**List[CrossBorderQuotesResponseQuoteInnerQuoteLinesInner]**](CrossBorderQuotesResponseQuoteInnerQuoteLinesInner.md) |  | [optional] 
**total_price** | **float** |  | [optional] 
**total_rates** | [**CrossBorderQuotesResponseQuoteInnerTotalRates**](CrossBorderQuotesResponseQuoteInnerTotalRates.md) |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_response_quote_inner import CrossBorderQuotesResponseQuoteInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesResponseQuoteInner from a JSON string
cross_border_quotes_response_quote_inner_instance = CrossBorderQuotesResponseQuoteInner.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesResponseQuoteInner.to_json())

# convert the object into a dict
cross_border_quotes_response_quote_inner_dict = cross_border_quotes_response_quote_inner_instance.to_dict()
# create an instance of CrossBorderQuotesResponseQuoteInner from a dict
cross_border_quotes_response_quote_inner_form_dict = cross_border_quotes_response_quote_inner.from_dict(cross_border_quotes_response_quote_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


