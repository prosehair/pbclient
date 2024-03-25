# SchedulePickupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_address** | [**Address**](Address.md) |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**pickup_summary** | [**List[SchedulePickupPickupSummaryInner]**](SchedulePickupPickupSummaryInner.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**package_location** | **str** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**pickup_date_time** | **str** |  | [optional] 
**pickup_confirmation_number** | **str** |  | [optional] 
**pickup_id** | **str** |  | [optional] 

## Example

```python
from pbclient.models.schedule_pickup_response import SchedulePickupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulePickupResponse from a JSON string
schedule_pickup_response_instance = SchedulePickupResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulePickupResponse.to_json())

# convert the object into a dict
schedule_pickup_response_dict = schedule_pickup_response_instance.to_dict()
# create an instance of SchedulePickupResponse from a dict
schedule_pickup_response_form_dict = schedule_pickup_response.from_dict(schedule_pickup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


