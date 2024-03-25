# CrossBorderQuotesRequestRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from pbclient.models.cross_border_quotes_request_rates_inner import CrossBorderQuotesRequestRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossBorderQuotesRequestRatesInner from a JSON string
cross_border_quotes_request_rates_inner_instance = CrossBorderQuotesRequestRatesInner.from_json(json)
# print the JSON string representation of the object
print(CrossBorderQuotesRequestRatesInner.to_json())

# convert the object into a dict
cross_border_quotes_request_rates_inner_dict = cross_border_quotes_request_rates_inner_instance.to_dict()
# create an instance of CrossBorderQuotesRequestRatesInner from a dict
cross_border_quotes_request_rates_inner_form_dict = cross_border_quotes_request_rates_inner.from_dict(cross_border_quotes_request_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


