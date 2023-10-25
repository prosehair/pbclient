# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.9
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_unit_rates_delivery_commitment import CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment

class CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates(BaseModel):
    """
    CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates
    """
    line_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="linePrice")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalTaxAmount")
    total_duty_amount: Optional[StrictInt] = Field(None, alias="totalDutyAmount")
    service_id: Optional[StrictStr] = Field(None, alias="serviceId")
    base_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="baseCharge")
    delivery_commitment: Optional[CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment] = Field(None, alias="deliveryCommitment")
    total_carrier_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalCarrierCharge")
    __properties = ["linePrice", "totalTaxAmount", "totalDutyAmount", "serviceId", "baseCharge", "deliveryCommitment", "totalCarrierCharge"]

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
    def from_json(cls, json_str: str) -> CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of delivery_commitment
        if self.delivery_commitment:
            _dict['deliveryCommitment'] = self.delivery_commitment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates.parse_obj(obj)

        _obj = CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates.parse_obj({
            "line_price": obj.get("linePrice"),
            "total_tax_amount": obj.get("totalTaxAmount"),
            "total_duty_amount": obj.get("totalDutyAmount"),
            "service_id": obj.get("serviceId"),
            "base_charge": obj.get("baseCharge"),
            "delivery_commitment": CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment.from_dict(obj.get("deliveryCommitment")) if obj.get("deliveryCommitment") is not None else None,
            "total_carrier_charge": obj.get("totalCarrierCharge")
        })
        return _obj


