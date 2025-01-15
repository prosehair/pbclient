# TrackingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_count** | **int** |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_date** | **date** |  | [optional] 
**updated_time** | **str** |  | [optional] 
**ship_date** | **date** |  | [optional] 
**ship_time** | **str** |  | [optional] 
**ship_time_offset** | **str** |  | [optional] 
**estimated_delivery_date** | **date** |  | [optional] 
**estimated_delivery_time** | **str** |  | [optional] 
**estimated_delivery_time_offset** | **str** |  | [optional] 
**delivery_date** | **date** |  | [optional] 
**delivery_time** | **str** |  | [optional] 
**delivery_time_offset** | **str** |  | [optional] 
**delivery_location** | **str** |  | [optional] 
**delivery_location_description** | **str** |  | [optional] 
**signed_by** | **str** |  | [optional] 
**weight** | **str** |  | [optional] 
**weight_oum** | **str** |  | [optional] 
**reattempt_date** | **date** |  | [optional] 
**reattempt_time** | **str** |  | [optional] 
**destination_address** | [**TrackingAddress**](TrackingAddress.md) |  | [optional] 
**sender_address** | [**TrackingAddress**](TrackingAddress.md) |  | [optional] 
**current_status** | [**EventObject**](EventObject.md) |  | [optional] 
**scan_details_list** | [**List[EventObject]**](EventObject.md) |  | [optional] 

## Example

```python
from pbclient.models.tracking_response import TrackingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingResponse from a JSON string
tracking_response_instance = TrackingResponse.from_json(json)
# print the JSON string representation of the object
print(TrackingResponse.to_json())

# convert the object into a dict
tracking_response_dict = tracking_response_instance.to_dict()
# create an instance of TrackingResponse from a dict
tracking_response_form_dict = tracking_response.from_dict(tracking_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


