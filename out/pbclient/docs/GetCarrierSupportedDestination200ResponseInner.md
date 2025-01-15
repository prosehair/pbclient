# GetCarrierSupportedDestination200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 

## Example

```python
from pbclient.models.get_carrier_supported_destination200_response_inner import GetCarrierSupportedDestination200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCarrierSupportedDestination200ResponseInner from a JSON string
get_carrier_supported_destination200_response_inner_instance = GetCarrierSupportedDestination200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetCarrierSupportedDestination200ResponseInner.to_json())

# convert the object into a dict
get_carrier_supported_destination200_response_inner_dict = get_carrier_supported_destination200_response_inner_instance.to_dict()
# create an instance of GetCarrierSupportedDestination200ResponseInner from a dict
get_carrier_supported_destination200_response_inner_form_dict = get_carrier_supported_destination200_response_inner.from_dict(get_carrier_supported_destination200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


