# CommodityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cargo_air_craft** | **bool** |  | [optional] 
**hazard_class** | **str** |  | [optional] 
**infectious_substance_contact** | [**InfectiousSubstanceContact**](InfectiousSubstanceContact.md) |  | [optional] 
**inner_receptacles_quantity** | **int** |  | [optional] 
**inner_receptacles_quantity_uom** | **str** |  | [optional] 
**packaging_group** | **str** |  | [optional] 
**packaging_instructions** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**proper_shipping_name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**quantity_uom** | **str** |  | [optional] 
**radio_activity_detail** | [**RadioActivityDetail**](RadioActivityDetail.md) |  | [optional] 
**radio_nuclide_detail** | [**RadioNuclideDetail**](RadioNuclideDetail.md) |  | [optional] 
**reportable_quantity** | **bool** |  | [optional] 
**technical_name** | **str** |  | [optional] 
**un_id** | **str** |  | [optional] 

## Example

```python
from pbclient.models.commodity_info import CommodityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommodityInfo from a JSON string
commodity_info_instance = CommodityInfo.from_json(json)
# print the JSON string representation of the object
print(CommodityInfo.to_json())

# convert the object into a dict
commodity_info_dict = commodity_info_instance.to_dict()
# create an instance of CommodityInfo from a dict
commodity_info_form_dict = commodity_info.from_dict(commodity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


