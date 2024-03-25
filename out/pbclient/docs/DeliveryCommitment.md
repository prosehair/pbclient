# DeliveryCommitment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_details** | **str** |  | [optional] 
**estimated_delivery_date_time** | **str** |  | [optional] 
**guarantee** | **str** |  | [optional] 
**max_estimated_number_of_days** | **str** |  | [optional] 
**min_estimated_number_of_days** | **str** |  | [optional] 

## Example

```python
from pbclient.models.delivery_commitment import DeliveryCommitment

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryCommitment from a JSON string
delivery_commitment_instance = DeliveryCommitment.from_json(json)
# print the JSON string representation of the object
print(DeliveryCommitment.to_json())

# convert the object into a dict
delivery_commitment_dict = delivery_commitment_instance.to_dict()
# create an instance of DeliveryCommitment from a dict
delivery_commitment_form_dict = delivery_commitment.from_dict(delivery_commitment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


