# SearchCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developer_id** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**to_date** | **str** |  | [optional] 

## Example

```python
from pbclient.models.search_criteria import SearchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCriteria from a JSON string
search_criteria_instance = SearchCriteria.from_json(json)
# print the JSON string representation of the object
print(SearchCriteria.to_json())

# convert the object into a dict
search_criteria_dict = search_criteria_instance.to_dict()
# create an instance of SearchCriteria from a dict
search_criteria_form_dict = search_criteria.from_dict(search_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


