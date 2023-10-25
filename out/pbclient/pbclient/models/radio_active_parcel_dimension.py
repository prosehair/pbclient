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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class RadioActiveParcelDimension(BaseModel):
    """
    RadioActiveParcelDimension
    """
    uom: Optional[StrictStr] = Field(None, alias="UOM", description="unit of measurement")
    height: Optional[Union[StrictFloat, StrictInt]] = None
    length: Optional[Union[StrictFloat, StrictInt]] = None
    width: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["UOM", "height", "length", "width"]

    @validator('uom')
    def uom_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CM', 'IN'):
            raise ValueError("must be one of enum values ('CM', 'IN')")
        return value

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
    def from_json(cls, json_str: str) -> RadioActiveParcelDimension:
        """Create an instance of RadioActiveParcelDimension from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RadioActiveParcelDimension:
        """Create an instance of RadioActiveParcelDimension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RadioActiveParcelDimension.parse_obj(obj)

        _obj = RadioActiveParcelDimension.parse_obj({
            "uom": obj.get("UOM"),
            "height": obj.get("height"),
            "length": obj.get("length"),
            "width": obj.get("width")
        })
        return _obj


