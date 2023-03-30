# Surcharge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pbclient.models.surcharge import Surcharge

# TODO update the JSON string below
json = "{}"
# create an instance of Surcharge from a JSON string
surcharge_instance = Surcharge.from_json(json)
# print the JSON string representation of the object
print Surcharge.to_json()

# convert the object into a dict
surcharge_dict = surcharge_instance.to_dict()
# create an instance of Surcharge from a dict
surcharge_form_dict = surcharge.from_dict(surcharge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


