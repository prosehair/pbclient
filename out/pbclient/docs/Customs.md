# Customs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customs_info** | [**CustomsInfo**](CustomsInfo.md) |  | [optional] 
**customs_items** | [**List[CustomsItem]**](CustomsItem.md) |  | [optional] 

## Example

```python
from pbclient.models.customs import Customs

# TODO update the JSON string below
json = "{}"
# create an instance of Customs from a JSON string
customs_instance = Customs.from_json(json)
# print the JSON string representation of the object
print Customs.to_json()

# convert the object into a dict
customs_dict = customs_instance.to_dict()
# create an instance of Customs from a dict
customs_form_dict = customs.from_dict(customs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


