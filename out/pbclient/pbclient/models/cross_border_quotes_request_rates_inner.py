# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from pbclient.models.carrier import Carrier

class CrossBorderQuotesRequestRatesInner(BaseModel):
    """
    CrossBorderQuotesRequestRatesInner
    """
    carrier: Optional[Carrier] = None
    service_id: Optional[StrictStr] = Field(None, alias="serviceId")
    __properties = ["carrier", "serviceId"]

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
    def from_json(cls, json_str: str) -> CrossBorderQuotesRequestRatesInner:
        """Create an instance of CrossBorderQuotesRequestRatesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CrossBorderQuotesRequestRatesInner:
        """Create an instance of CrossBorderQuotesRequestRatesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CrossBorderQuotesRequestRatesInner.parse_obj(obj)

        _obj = CrossBorderQuotesRequestRatesInner.parse_obj({
            "carrier": obj.get("carrier"),
            "service_id": obj.get("serviceId")
        })
        return _obj

