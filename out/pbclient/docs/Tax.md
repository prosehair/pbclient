# Tax


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tax_amount** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 

## Example

```python
from pbclient.models.tax import Tax

# TODO update the JSON string below
json = "{}"
# create an instance of Tax from a JSON string
tax_instance = Tax.from_json(json)
# print the JSON string representation of the object
print(Tax.to_json())

# convert the object into a dict
tax_dict = tax_instance.to_dict()
# create an instance of Tax from a dict
tax_form_dict = tax.from_dict(tax_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


