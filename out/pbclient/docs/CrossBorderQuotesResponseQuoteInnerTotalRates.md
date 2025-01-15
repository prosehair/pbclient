# CrossBorderQuotesResponseQuoteInnerTotalRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** |  | [optional] 
**base_charge** | **float** |  | [optional] 
**delivery_commitment** | [**CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment**](CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment.md) |  | [optional] 
**total_carrier_charge** | **float** |  | [optional] 
**total_duty_amount** | **int** |  | [optional] 
**total_tax_amount** | **float** |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_response_quote_inner_total_rates import CrossBorderQuotesResponseQuoteInnerTotalRates

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesResponseQuoteInnerTotalRates from a JSON string
cross_border_quotes_response_quote_inner_total_rates_instance = CrossBorderQuotesResponseQuoteInnerTotalRates.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesResponseQuoteInnerTotalRates.to_json())

# convert the object into a dict
cross_border_quotes_response_quote_inner_total_rates_dict = cross_border_quotes_response_quote_inner_total_rates_instance.to_dict()
# create an instance of CrossBorderQuotesResponseQuoteInnerTotalRates from a dict
cross_border_quotes_response_quote_inner_total_rates_form_dict = cross_border_quotes_response_quote_inner_total_rates.from_dict(cross_border_quotes_response_quote_inner_total_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


