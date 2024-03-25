# SchedulePickup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_address** | [**Address**](Address.md) |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**pickup_summary** | [**List[SchedulePickupPickupSummaryInner]**](SchedulePickupPickupSummaryInner.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**package_location** | **str** |  | [optional] 
**special_instructions** | **str** |  | [optional] 

## Example

```python
from pbclient.models.schedule_pickup import SchedulePickup

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickup from a JSON string
schedule_pickup_instance = SchedulePickup.from_json(json)
# print the JSON string representation of the object
print(SchedulePickup.to_json())

# convert the object into a dict
schedule_pickup_dict = schedule_pickup_instance.to_dict()
# create an instance of SchedulePickup from a dict
schedule_pickup_form_dict = schedule_pickup.from_dict(schedule_pickup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


