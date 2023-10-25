# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.11
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from pbclient.models.parameter import Parameter
from pbclient.models.special_service import SpecialService

class RealTransactionDetailReport(BaseModel):
    """
    RealTransactionDetailReport
    """
    adjustment_reason: Optional[StrictStr] = Field(None, alias="adjustmentReason")
    credit_card_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="creditCardFee")
    custom_message1: Optional[StrictStr] = Field(None, alias="customMessage1")
    custom_message2: Optional[StrictStr] = Field(None, alias="customMessage2")
    description: Optional[StrictStr] = None
    destination_address: Optional[StrictStr] = Field(None, alias="destinationAddress")
    destination_country: Optional[StrictStr] = Field(None, alias="destinationCountry")
    destination_zip: Optional[StrictStr] = Field(None, alias="destinationZip")
    developer_id: Optional[StrictStr] = Field(None, alias="developerId")
    developer_name: Optional[StrictStr] = Field(None, alias="developerName")
    developer_postage_payment_account_balance: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="developerPostagePaymentAccountBalance")
    developer_postage_payment_method: Optional[StrictStr] = Field(None, alias="developerPostagePaymentMethod")
    developer_rate_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="developerRateAmount")
    developer_rate_plan: Optional[StrictStr] = Field(None, alias="developerRatePlan")
    dimensional_weight_oz: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="dimensionalWeightOz")
    external_id: Optional[StrictStr] = Field(None, alias="externalId")
    international_country_price_group: Optional[StrictStr] = Field(None, alias="internationalCountryPriceGroup")
    label_fee: Optional[StrictStr] = Field(None, alias="labelFee")
    mail_class: Optional[StrictStr] = Field(None, alias="mailClass")
    merchant_id: Optional[StrictStr] = Field(None, alias="merchantId")
    merchant_name: Optional[StrictStr] = Field(None, alias="merchantName")
    merchant_postage_account_payment_method: Optional[StrictStr] = Field(None, alias="merchantPostageAccountPaymentMethod")
    merchant_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="merchantRate")
    merchant_rate_plan: Optional[StrictStr] = Field(None, alias="merchantRatePlan")
    meter_number: Optional[StrictStr] = Field(None, alias="meterNumber")
    origin_zip: Optional[StrictStr] = Field(None, alias="originZip")
    origination_address: Optional[StrictStr] = Field(None, alias="originationAddress")
    package_height_in_inches: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="packageHeightInInches")
    package_length_in_inches: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="packageLengthInInches")
    package_type: Optional[StrictStr] = Field(None, alias="packageType")
    package_type_indicator: Optional[StrictStr] = Field(None, alias="packageTypeIndicator")
    package_width_in_inches: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="packageWidthInInches")
    parcel_tracking_number: Optional[StrictStr] = Field(None, alias="parcelTrackingNumber")
    postage_deposit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="postageDepositAmount")
    print_status: Optional[StrictStr] = Field(None, alias="printStatus")
    references: Optional[conlist(Parameter)] = None
    refund_denial_reason: Optional[StrictStr] = Field(None, alias="refundDenialReason")
    refund_requestor: Optional[StrictStr] = Field(None, alias="refundRequestor")
    refund_status: Optional[StrictStr] = Field(None, alias="refundStatus")
    shipment_id: Optional[StrictStr] = Field(None, alias="shipmentId")
    shipper_postage_payment_account_balance: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="shipperPostagePaymentAccountBalance")
    special_services: Optional[conlist(SpecialService)] = Field(None, alias="specialServices")
    status: Optional[StrictStr] = None
    transaction_date_time: Optional[datetime] = Field(None, alias="transactionDateTime")
    transaction_id: Optional[StrictStr] = Field(None, alias="transactionId")
    transaction_type: Optional[StrictStr] = Field(None, alias="transactionType")
    value_of_goods: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="valueOfGoods")
    weight_in_ounces: Optional[StrictInt] = Field(None, alias="weightInOunces")
    zone: Optional[StrictStr] = None
    __properties = ["adjustmentReason", "creditCardFee", "customMessage1", "customMessage2", "description", "destinationAddress", "destinationCountry", "destinationZip", "developerId", "developerName", "developerPostagePaymentAccountBalance", "developerPostagePaymentMethod", "developerRateAmount", "developerRatePlan", "dimensionalWeightOz", "externalId", "internationalCountryPriceGroup", "labelFee", "mailClass", "merchantId", "merchantName", "merchantPostageAccountPaymentMethod", "merchantRate", "merchantRatePlan", "meterNumber", "originZip", "originationAddress", "packageHeightInInches", "packageLengthInInches", "packageType", "packageTypeIndicator", "packageWidthInInches", "parcelTrackingNumber", "postageDepositAmount", "printStatus", "references", "refundDenialReason", "refundRequestor", "refundStatus", "shipmentId", "shipperPostagePaymentAccountBalance", "specialServices", "status", "transactionDateTime", "transactionId", "transactionType", "valueOfGoods", "weightInOunces", "zone"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RealTransactionDetailReport:
        """Create an instance of RealTransactionDetailReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in references (list)
        _items = []
        if self.references:
            for _item in self.references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['references'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in special_services (list)
        _items = []
        if self.special_services:
            for _item in self.special_services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specialServices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RealTransactionDetailReport:
        """Create an instance of RealTransactionDetailReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RealTransactionDetailReport.parse_obj(obj)

        _obj = RealTransactionDetailReport.parse_obj({
            "adjustment_reason": obj.get("adjustmentReason"),
            "credit_card_fee": obj.get("creditCardFee"),
            "custom_message1": obj.get("customMessage1"),
            "custom_message2": obj.get("customMessage2"),
            "description": obj.get("description"),
            "destination_address": obj.get("destinationAddress"),
            "destination_country": obj.get("destinationCountry"),
            "destination_zip": obj.get("destinationZip"),
            "developer_id": obj.get("developerId"),
            "developer_name": obj.get("developerName"),
            "developer_postage_payment_account_balance": obj.get("developerPostagePaymentAccountBalance"),
            "developer_postage_payment_method": obj.get("developerPostagePaymentMethod"),
            "developer_rate_amount": obj.get("developerRateAmount"),
            "developer_rate_plan": obj.get("developerRatePlan"),
            "dimensional_weight_oz": obj.get("dimensionalWeightOz"),
            "external_id": obj.get("externalId"),
            "international_country_price_group": obj.get("internationalCountryPriceGroup"),
            "label_fee": obj.get("labelFee"),
            "mail_class": obj.get("mailClass"),
            "merchant_id": obj.get("merchantId"),
            "merchant_name": obj.get("merchantName"),
            "merchant_postage_account_payment_method": obj.get("merchantPostageAccountPaymentMethod"),
            "merchant_rate": obj.get("merchantRate"),
            "merchant_rate_plan": obj.get("merchantRatePlan"),
            "meter_number": obj.get("meterNumber"),
            "origin_zip": obj.get("originZip"),
            "origination_address": obj.get("originationAddress"),
            "package_height_in_inches": obj.get("packageHeightInInches"),
            "package_length_in_inches": obj.get("packageLengthInInches"),
            "package_type": obj.get("packageType"),
            "package_type_indicator": obj.get("packageTypeIndicator"),
            "package_width_in_inches": obj.get("packageWidthInInches"),
            "parcel_tracking_number": obj.get("parcelTrackingNumber"),
            "postage_deposit_amount": obj.get("postageDepositAmount"),
            "print_status": obj.get("printStatus"),
            "references": [Parameter.from_dict(_item) for _item in obj.get("references")] if obj.get("references") is not None else None,
            "refund_denial_reason": obj.get("refundDenialReason"),
            "refund_requestor": obj.get("refundRequestor"),
            "refund_status": obj.get("refundStatus"),
            "shipment_id": obj.get("shipmentId"),
            "shipper_postage_payment_account_balance": obj.get("shipperPostagePaymentAccountBalance"),
            "special_services": [SpecialService.from_dict(_item) for _item in obj.get("specialServices")] if obj.get("specialServices") is not None else None,
            "status": obj.get("status"),
            "transaction_date_time": obj.get("transactionDateTime"),
            "transaction_id": obj.get("transactionId"),
            "transaction_type": obj.get("transactionType"),
            "value_of_goods": obj.get("valueOfGoods"),
            "weight_in_ounces": obj.get("weightInOunces"),
            "zone": obj.get("zone")
        })
        return _obj


