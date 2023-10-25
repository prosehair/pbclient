# CustomsInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eelpfc** | **str** |  | [optional] 
**blanket_end_date** | **str** | format: YYYY-MM-DD | [optional] 
**blanket_start_date** | **str** | format: YYYY-MM-DD | [optional] 
**certificate_number** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**currency_code** | **str** | ISO-4217 | 
**customs_declared_value** | **str** |  | [optional] 
**declaration_statement** | **str** |  | [optional] 
**freight_charge** | **float** |  | [optional] 
**from_customs_reference** | **str** |  | [optional] 
**handling_costs** | **float** |  | [optional] 
**importer_customs_reference** | **str** |  | [optional] 
**insured_amount** | **float** |  | [optional] 
**insured_number** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**license_number** | **str** |  | [optional] 
**other_charge** | **float** |  | [optional] 
**other_description** | **str** |  | [optional] 
**other_type** | **str** |  | [optional] 
**packing_costs** | **float** |  | [optional] 
**producer_specification** | **str** |  | [optional] 
**reason_for_export** | **str** |  | [optional] 
**reason_for_export_explanation** | **str** |  | [optional] 
**sdr_value** | **float** |  | [optional] 
**shipping_document_type** | **str** |  | [optional] 
**signature_contact** | [**Address**](Address.md) |  | [optional] 
**terms_of_sale** | **str** |  | [optional] 

## Example

```python
from pbclient.models.customs_info import CustomsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustomsInfo from a JSON string
customs_info_instance = CustomsInfo.from_json(json)
# print the JSON string representation of the object
print CustomsInfo.to_json()

# convert the object into a dict
customs_info_dict = customs_info_instance.to_dict()
# create an instance of CustomsInfo from a dict
customs_info_form_dict = customs_info.from_dict(customs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


