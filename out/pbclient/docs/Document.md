# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 
**customer_data** | [**CustomerData**](CustomerData.md) |  | [optional] 
**doc_tab** | [**List[DocTabItem]**](DocTabItem.md) |  | [optional] 
**file_format** | **str** |  | [optional] 
**pages** | [**List[DocumentPage]**](DocumentPage.md) |  | [optional] 
**print_dialog_option** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from pbclient.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


