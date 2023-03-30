# AddTrackingEventsReferencesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_type** | **str** |  | [optional] 
**reference_value** | **str** |  | [optional] 
**events** | [**List[AddTrackingEventsReferencesInnerEventsInner]**](AddTrackingEventsReferencesInnerEventsInner.md) |  | [optional] 

## Example

```python
from pbclient.models.add_tracking_events_references_inner import AddTrackingEventsReferencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddTrackingEventsReferencesInner from a JSON string
add_tracking_events_references_inner_instance = AddTrackingEventsReferencesInner.from_json(json)
# print the JSON string representation of the object
print AddTrackingEventsReferencesInner.to_json()

# convert the object into a dict
add_tracking_events_references_inner_dict = add_tracking_events_references_inner_instance.to_dict()
# create an instance of AddTrackingEventsReferencesInner from a dict
add_tracking_events_references_inner_form_dict = add_tracking_events_references_inner.from_dict(add_tracking_events_references_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


