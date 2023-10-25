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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class Discount(BaseModel):
    """
    Discount
    """
    discount_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="discountAmount")
    name: Optional[StrictStr] = None
    __properties = ["discountAmount", "name"]

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
    def from_json(cls, json_str: str) -> Discount:
        """Create an instance of Discount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Discount:
        """Create an instance of Discount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Discount.parse_obj(obj)

        _obj = Discount.parse_obj({
            "discount_amount": obj.get("discountAmount"),
            "name": obj.get("name")
        })
        return _obj


