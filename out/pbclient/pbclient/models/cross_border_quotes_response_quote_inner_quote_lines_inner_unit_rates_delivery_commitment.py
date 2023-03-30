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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment(BaseModel):
    """
    CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment
    """
    min_estimated_number_of_days: Optional[StrictInt] = Field(None, alias="minEstimatedNumberOfDays")
    max_estimated_number_of_days: Optional[StrictInt] = Field(None, alias="maxEstimatedNumberOfDays")
    __properties = ["minEstimatedNumberOfDays", "maxEstimatedNumberOfDays"]

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
    def from_json(cls, json_str: str) -> CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment.parse_obj(obj)

        _obj = CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment.parse_obj({
            "min_estimated_number_of_days": obj.get("minEstimatedNumberOfDays"),
            "max_estimated_number_of_days": obj.get("maxEstimatedNumberOfDays")
        })
        return _obj

