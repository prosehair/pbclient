# DocTabItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from pbclient.models.doc_tab_item import DocTabItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocTabItem from a JSON string
doc_tab_item_instance = DocTabItem.from_json(json)
# print the JSON string representation of the object
print DocTabItem.to_json()

# convert the object into a dict
doc_tab_item_dict = doc_tab_item_instance.to_dict()
# create an instance of DocTabItem from a dict
doc_tab_item_form_dict = doc_tab_item.from_dict(doc_tab_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


