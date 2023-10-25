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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates import CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates
from pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_unit_rates import CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates

class CrossBorderQuotesResponseQuoteInnerQuoteLinesInner(BaseModel):
    """
    CrossBorderQuotesResponseQuoteInnerQuoteLinesInner
    """
    line_id: Optional[StrictStr] = Field(None, alias="lineId")
    item_id: Optional[StrictStr] = Field(None, alias="itemId")
    quote_line_id: Optional[StrictStr] = Field(None, alias="quoteLineId")
    quantity: Optional[StrictInt] = None
    unit_rates: Optional[CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates] = Field(None, alias="unitRates")
    line_rates: Optional[CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates] = Field(None, alias="lineRates")
    __properties = ["lineId", "itemId", "quoteLineId", "quantity", "unitRates", "lineRates"]

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
    def from_json(cls, json_str: str) -> CrossBorderQuotesResponseQuoteInnerQuoteLinesInner:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of unit_rates
        if self.unit_rates:
            _dict['unitRates'] = self.unit_rates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of line_rates
        if self.line_rates:
            _dict['lineRates'] = self.line_rates.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CrossBorderQuotesResponseQuoteInnerQuoteLinesInner:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CrossBorderQuotesResponseQuoteInnerQuoteLinesInner.parse_obj(obj)

        _obj = CrossBorderQuotesResponseQuoteInnerQuoteLinesInner.parse_obj({
            "line_id": obj.get("lineId"),
            "item_id": obj.get("itemId"),
            "quote_line_id": obj.get("quoteLineId"),
            "quantity": obj.get("quantity"),
            "unit_rates": CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates.from_dict(obj.get("unitRates")) if obj.get("unitRates") is not None else None,
            "line_rates": CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerLineRates.from_dict(obj.get("lineRates")) if obj.get("lineRates") is not None else None
        })
        return _obj


