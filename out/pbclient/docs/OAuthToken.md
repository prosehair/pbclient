# OAuthToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**issued_at** | **str** |  | [optional] 
**expires_in** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**org** | **str** |  | [optional] 

## Example

```python
from pbclient.models.o_auth_token import OAuthToken

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthToken from a JSON string
o_auth_token_instance = OAuthToken.from_json(json)
# print the JSON string representation of the object
print OAuthToken.to_json()

# convert the object into a dict
o_auth_token_dict = o_auth_token_instance.to_dict()
# create an instance of OAuthToken from a dict
o_auth_token_form_dict = o_auth_token.from_dict(o_auth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


