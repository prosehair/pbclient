# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_unit_rates_delivery_commitment import CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment

class CrossBorderQuotesResponseQuoteInnerTotalRates(BaseModel):
    """
    CrossBorderQuotesResponseQuoteInnerTotalRates
    """
    service_id: Optional[StrictStr] = Field(None, alias="serviceId")
    base_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="baseCharge")
    delivery_commitment: Optional[CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment] = Field(None, alias="deliveryCommitment")
    total_carrier_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalCarrierCharge")
    total_duty_amount: Optional[StrictInt] = Field(None, alias="totalDutyAmount")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalTaxAmount")
    __properties = ["serviceId", "baseCharge", "deliveryCommitment", "totalCarrierCharge", "totalDutyAmount", "totalTaxAmount"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CrossBorderQuotesResponseQuoteInnerTotalRates:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerTotalRates from a JSON string"""
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
    def from_dict(cls, obj: dict) -> CrossBorderQuotesResponseQuoteInnerTotalRates:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerTotalRates from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CrossBorderQuotesResponseQuoteInnerTotalRates.parse_obj(obj)

        _obj = CrossBorderQuotesResponseQuoteInnerTotalRates.parse_obj({
            "service_id": obj.get("serviceId"),
            "base_charge": obj.get("baseCharge"),
            "delivery_commitment": CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment.from_dict(obj.get("deliveryCommitment")) if obj.get("deliveryCommitment") is not None else None,
            "total_carrier_charge": obj.get("totalCarrierCharge"),
            "total_duty_amount": obj.get("totalDutyAmount"),
            "total_tax_amount": obj.get("totalTaxAmount")
        })
        return _obj

