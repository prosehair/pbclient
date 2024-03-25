# DimensionRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** |  | [optional] 
**unit_of_measurement** | **str** |  | [optional] 
**min_parcel_dimensions** | [**DimensionRulesMinParcelDimensions**](DimensionRulesMinParcelDimensions.md) |  | [optional] 
**max_parcel_dimensions** | [**DimensionRulesMaxParcelDimensions**](DimensionRulesMaxParcelDimensions.md) |  | [optional] 
**min_length_plus_girth** | **int** |  | [optional] 
**max_length_plus_girth** | **int** |  | [optional] 

## Example

```python
from pbclient.models.dimension_rules import DimensionRules

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionRules from a JSON string
dimension_rules_instance = DimensionRules.from_json(json)
# print the JSON string representation of the object
print(DimensionRules.to_json())

# convert the object into a dict
dimension_rules_dict = dimension_rules_instance.to_dict()
# create an instance of DimensionRules from a dict
dimension_rules_form_dict = dimension_rules.from_dict(dimension_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


