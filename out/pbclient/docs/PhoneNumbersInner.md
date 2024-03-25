# PhoneNumbersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pbclient.models.phone_numbers_inner import PhoneNumbersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumbersInner from a JSON string
phone_numbers_inner_instance = PhoneNumbersInner.from_json(json)
# print the JSON string representation of the object
print(PhoneNumbersInner.to_json())

# convert the object into a dict
phone_numbers_inner_dict = phone_numbers_inner_instance.to_dict()
# create an instance of PhoneNumbersInner from a dict
phone_numbers_inner_form_dict = phone_numbers_inner.from_dict(phone_numbers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


