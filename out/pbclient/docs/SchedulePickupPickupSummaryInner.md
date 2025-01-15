# SchedulePickupPickupSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**total_weight** | [**SchedulePickupPickupSummaryInnerTotalWeight**](SchedulePickupPickupSummaryInnerTotalWeight.md) |  | [optional] 

## Example

```python
from pbclient.models.schedule_pickup_pickup_summary_inner import SchedulePickupPickupSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupPickupSummaryInner from a JSON string
schedule_pickup_pickup_summary_inner_instance = SchedulePickupPickupSummaryInner.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupPickupSummaryInner.to_json())

# convert the object into a dict
schedule_pickup_pickup_summary_inner_dict = schedule_pickup_pickup_summary_inner_instance.to_dict()
# create an instance of SchedulePickupPickupSummaryInner from a dict
schedule_pickup_pickup_summary_inner_form_dict = schedule_pickup_pickup_summary_inner.from_dict(schedule_pickup_pickup_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


