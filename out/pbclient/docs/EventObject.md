# EventObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standardized_event_code** | **str** |  | [optional] 
**l1_code** | **str** |  | [optional] 
**l1_description** | **str** |  | [optional] 
**event_date** | **date** |  | [optional] 
**event_time** | **str** |  | [optional] 
**event_time_offset** | **str** |  | [optional] 
**tracking_url** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**location_unit** | **str** |  | [optional] 
**event_leg** | **str** |  | [optional] 
**event_type** | **str** |  | [optional] 
**scan_type** | **str** |  | [optional] 
**scan_description** | **str** |  | [optional] 
**package_status** | **str** |  | [optional] 
**l2_description** | **str** |  | [optional] 
**event_city** | **str** |  | [optional] 
**event_state_or_province** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from pbclient.models.event_object import EventObject

# TODO update the JSON string below
json = "{}"
# create an instance of EventObject from a JSON string
event_object_instance = EventObject.from_json(json)
# print the JSON string representation of the object
print EventObject.to_json()

# convert the object into a dict
event_object_dict = event_object_instance.to_dict()
# create an instance of EventObject from a dict
event_object_form_dict = event_object.from_dict(event_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


