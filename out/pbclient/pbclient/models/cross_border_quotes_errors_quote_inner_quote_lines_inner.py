# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.8
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from pbclient.models.cross_border_quotes_errors_quote_inner_quote_lines_inner_unit_errors_inner import CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner

class CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner(BaseModel):
    """
    CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner
    """
    line_id: Optional[StrictStr] = Field(None, alias="lineId")
    merchant_com_ref_id: Optional[StrictStr] = Field(None, alias="merchantComRefId")
    quantity: Optional[StrictInt] = None
    unit_errors: Optional[conlist(CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner)] = Field(None, alias="unitErrors")
    __properties = ["lineId", "merchantComRefId", "quantity", "unitErrors"]

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
    def from_json(cls, json_str: str) -> CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner:
        """Create an instance of CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in unit_errors (list)
        _items = []
        if self.unit_errors:
            for _item in self.unit_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['unitErrors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner:
        """Create an instance of CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner.parse_obj(obj)

        _obj = CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner.parse_obj({
            "line_id": obj.get("lineId"),
            "merchant_com_ref_id": obj.get("merchantComRefId"),
            "quantity": obj.get("quantity"),
            "unit_errors": [CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner.from_dict(_item) for _item in obj.get("unitErrors")] if obj.get("unitErrors") is not None else None
        })
        return _obj


