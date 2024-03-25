# PageRealTransactionDetailReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[RealTransactionDetailReport]**](RealTransactionDetailReport.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**search_criteria** | [**SearchCriteria**](SearchCriteria.md) |  | [optional] 

## Example

```python
from pbclient.models.page_real_transaction_detail_report import PageRealTransactionDetailReport

# TODO update the JSON string below
json = "{}"
# create an instance of PageRealTransactionDetailReport from a JSON string
page_real_transaction_detail_report_instance = PageRealTransactionDetailReport.from_json(json)
# print the JSON string representation of the object
print(PageRealTransactionDetailReport.to_json())

# convert the object into a dict
page_real_transaction_detail_report_dict = page_real_transaction_detail_report_instance.to_dict()
# create an instance of PageRealTransactionDetailReport from a dict
page_real_transaction_detail_report_form_dict = page_real_transaction_detail_report.from_dict(page_real_transaction_detail_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


