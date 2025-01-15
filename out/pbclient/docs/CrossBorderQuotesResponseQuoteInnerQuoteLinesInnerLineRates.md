# CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_price** | **float** |  | [optional] 
**total_tax_amount** | **float** |  | [optional] 
**total_duty_amount** | **int** |  | [optional] 
**service_id** | **str** |  | [optional] 
**base_charge** | **float** |  | [optional] 
**delivery_commitment** | [**CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment**](CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment.md) |  | [optional] 
**total_carrier_charge** | **float** |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates import CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates from a JSON string
cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates_instance = CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates.to_json())

# convert the object into a dict
cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates_dict = cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates_instance.to_dict()
# create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates from a dict
cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates_form_dict = cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates.from_dict(cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


