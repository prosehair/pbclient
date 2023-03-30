# InfectiousSubstanceContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**person_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 

## Example

```python
from pbclient.models.infectious_substance_contact import InfectiousSubstanceContact

# TODO update the JSON string below
json = "{}"
# create an instance of InfectiousSubstanceContact from a JSON string
infectious_substance_contact_instance = InfectiousSubstanceContact.from_json(json)
# print the JSON string representation of the object
print InfectiousSubstanceContact.to_json()

# convert the object into a dict
infectious_substance_contact_dict = infectious_substance_contact_instance.to_dict()
# create an instance of InfectiousSubstanceContact from a dict
infectious_substance_contact_form_dict = infectious_substance_contact.from_dict(infectious_substance_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


