# RealTransactionDetailReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_reason** | **str** |  | [optional] 
**credit_card_fee** | **float** |  | [optional] 
**custom_message1** | **str** |  | [optional] 
**custom_message2** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**destination_address** | **str** |  | [optional] 
**destination_country** | **str** |  | [optional] 
**destination_zip** | **str** |  | [optional] 
**developer_id** | **str** |  | [optional] 
**developer_name** | **str** |  | [optional] 
**developer_postage_payment_account_balance** | **float** |  | [optional] 
**developer_postage_payment_method** | **str** |  | [optional] 
**developer_rate_amount** | **float** |  | [optional] 
**developer_rate_plan** | **str** |  | [optional] 
**dimensional_weight_oz** | **float** |  | [optional] 
**external_id** | **str** |  | [optional] 
**international_country_price_group** | **str** |  | [optional] 
**label_fee** | **str** |  | [optional] 
**mail_class** | **str** |  | [optional] 
**merchant_id** | **str** |  | [optional] 
**merchant_name** | **str** |  | [optional] 
**merchant_postage_account_payment_method** | **str** |  | [optional] 
**merchant_rate** | **float** |  | [optional] 
**merchant_rate_plan** | **str** |  | [optional] 
**meter_number** | **str** |  | [optional] 
**origin_zip** | **str** |  | [optional] 
**origination_address** | **str** |  | [optional] 
**package_height_in_inches** | **float** |  | [optional] 
**package_length_in_inches** | **float** |  | [optional] 
**package_type** | **str** |  | [optional] 
**package_type_indicator** | **str** |  | [optional] 
**package_width_in_inches** | **float** |  | [optional] 
**parcel_tracking_number** | **str** |  | [optional] 
**postage_deposit_amount** | **float** |  | [optional] 
**print_status** | **str** |  | [optional] 
**references** | [**List[Parameter]**](Parameter.md) |  | [optional] 
**refund_denial_reason** | **str** |  | [optional] 
**refund_requestor** | **str** |  | [optional] 
**refund_status** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**shipper_postage_payment_account_balance** | **float** |  | [optional] 
**special_services** | [**List[SpecialService]**](SpecialService.md) |  | [optional] 
**status** | **str** |  | [optional] 
**transaction_date_time** | **datetime** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**value_of_goods** | **float** |  | [optional] 
**weight_in_ounces** | **int** |  | [optional] 
**zone** | **str** |  | [optional] 

## Example

```python
from pbclient.models.real_transaction_detail_report import RealTransactionDetailReport

# TODO update the JSON string below
json = "{}"
# create an instance of RealTransactionDetailReport from a JSON string
real_transaction_detail_report_instance = RealTransactionDetailReport.from_json(json)
# print the JSON string representation of the object
print(RealTransactionDetailReport.to_json())

# convert the object into a dict
real_transaction_detail_report_dict = real_transaction_detail_report_instance.to_dict()
# create an instance of RealTransactionDetailReport from a dict
real_transaction_detail_report_form_dict = real_transaction_detail_report.from_dict(real_transaction_detail_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


