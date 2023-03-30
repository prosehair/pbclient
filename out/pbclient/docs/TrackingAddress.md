# TrackingAddress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_or_province** | **str** |  | [optional] 
**postal_code** | **int** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from pbclient.models.tracking_address import TrackingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingAddress from a JSON string
tracking_address_instance = TrackingAddress.from_json(json)
# print the JSON string representation of the object
print TrackingAddress.to_json()

# convert the object into a dict
tracking_address_dict = tracking_address_instance.to_dict()
# create an instance of TrackingAddress from a dict
tracking_address_form_dict = tracking_address.from_dict(tracking_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


