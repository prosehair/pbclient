# AddTrackingEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**references** | [**List[AddTrackingEventsReferencesInner]**](AddTrackingEventsReferencesInner.md) |  | [optional] 

## Example

```python
from pbclient.models.add_tracking_events import AddTrackingEvents

# TODO update the JSON string below
json = "{}"
# create an instance of AddTrackingEvents from a JSON string
add_tracking_events_instance = AddTrackingEvents.from_json(json)
# print the JSON string representation of the object
print(AddTrackingEvents.to_json())

# convert the object into a dict
add_tracking_events_dict = add_tracking_events_instance.to_dict()
# create an instance of AddTrackingEvents from a dict
add_tracking_events_form_dict = add_tracking_events.from_dict(add_tracking_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


