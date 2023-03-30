# CustomerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_details** | [**List[Parameter]**](Parameter.md) |  | [optional] 

## Example

```python
from pbclient.models.customer_data import CustomerData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerData from a JSON string
customer_data_instance = CustomerData.from_json(json)
# print the JSON string representation of the object
print CustomerData.to_json()

# convert the object into a dict
customer_data_dict = customer_data_instance.to_dict()
# create an instance of CustomerData from a dict
customer_data_form_dict = customer_data.from_dict(customer_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


