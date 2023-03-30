# TrackingResponseScanDetailsListInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_date** | **date** |  | [optional] 
**event_time** | **str** |  | [optional] 
**event_city** | **str** |  | [optional] 
**event_state_or_province** | **str** |  | [optional] 
**postal_code** | **int** |  | [optional] 
**country** | **str** |  | [optional] 
**scan_type** | **str** |  | [optional] 
**scan_description** | **str** |  | [optional] 
**package_status** | **str** |  | [optional] 

## Example

```python
from pbclient.models.tracking_response_scan_details_list_inner import TrackingResponseScanDetailsListInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrackingResponseScanDetailsListInner from a JSON string
tracking_response_scan_details_list_inner_instance = TrackingResponseScanDetailsListInner.from_json(json)
# print the JSON string representation of the object
print TrackingResponseScanDetailsListInner.to_json()

# convert the object into a dict
tracking_response_scan_details_list_inner_dict = tracking_response_scan_details_list_inner_instance.to_dict()
# create an instance of TrackingResponseScanDetailsListInner from a dict
tracking_response_scan_details_list_inner_form_dict = tracking_response_scan_details_list_inner.from_dict(tracking_response_scan_details_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


