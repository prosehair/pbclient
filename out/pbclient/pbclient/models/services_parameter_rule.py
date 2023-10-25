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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ServicesParameterRule(BaseModel):
    """
    ServicesParameterRule
    """
    name: Optional[StrictStr] = None
    branded_name: Optional[StrictStr] = Field(None, alias="brandedName")
    required: Optional[StrictBool] = None
    min_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="minValue")
    max_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="maxValue")
    free_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="freeValue")
    format: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    __properties = ["name", "brandedName", "required", "minValue", "maxValue", "freeValue", "format", "description"]

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
    def from_json(cls, json_str: str) -> ServicesParameterRule:
        """Create an instance of ServicesParameterRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServicesParameterRule:
        """Create an instance of ServicesParameterRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServicesParameterRule.parse_obj(obj)

        _obj = ServicesParameterRule.parse_obj({
            "name": obj.get("name"),
            "branded_name": obj.get("brandedName"),
            "required": obj.get("required"),
            "min_value": obj.get("minValue"),
            "max_value": obj.get("maxValue"),
            "free_value": obj.get("freeValue"),
            "format": obj.get("format"),
            "description": obj.get("description")
        })
        return _obj


