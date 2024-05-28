# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.14
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, conlist
from pbclient.models.cross_border_quotes_errors_quote_inner_errors_errors_inner import CrossBorderQuotesErrorsQuoteInnerErrorsErrorsInner

class CrossBorderQuotesErrorsQuoteInnerErrors(BaseModel):
    """
    CrossBorderQuotesErrorsQuoteInnerErrors
    """
    errors: Optional[conlist(CrossBorderQuotesErrorsQuoteInnerErrorsErrorsInner)] = None
    __properties = ["errors"]

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
    def from_json(cls, json_str: str) -> CrossBorderQuotesErrorsQuoteInnerErrors:
        """Create an instance of CrossBorderQuotesErrorsQuoteInnerErrors from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CrossBorderQuotesErrorsQuoteInnerErrors:
        """Create an instance of CrossBorderQuotesErrorsQuoteInnerErrors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CrossBorderQuotesErrorsQuoteInnerErrors.parse_obj(obj)

        _obj = CrossBorderQuotesErrorsQuoteInnerErrors.parse_obj({
            "errors": [CrossBorderQuotesErrorsQuoteInnerErrorsErrorsInner.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None
        })
        return _obj


