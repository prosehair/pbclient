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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class ParcelProtectionCreateResponseParcelProtectionFeesBreakup(BaseModel):
    """
    ParcelProtectionCreateResponseParcelProtectionFeesBreakup
    """
    base_premium: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="basePremium")
    technology_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="technologyFee")
    __properties = ["basePremium", "technologyFee"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionCreateResponseParcelProtectionFeesBreakup:
        """Create an instance of ParcelProtectionCreateResponseParcelProtectionFeesBreakup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionCreateResponseParcelProtectionFeesBreakup:
        """Create an instance of ParcelProtectionCreateResponseParcelProtectionFeesBreakup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionCreateResponseParcelProtectionFeesBreakup.parse_obj(obj)

        _obj = ParcelProtectionCreateResponseParcelProtectionFeesBreakup.parse_obj({
            "base_premium": obj.get("basePremium"),
            "technology_fee": obj.get("technologyFee")
        })
        return _obj


