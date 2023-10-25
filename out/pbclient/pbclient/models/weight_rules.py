# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.7
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

class WeightRules(BaseModel):
    """
    WeightRules
    """
    required: Optional[StrictBool] = None
    unit_of_measurement: Optional[StrictStr] = Field(None, alias="unitOfMeasurement")
    min_weight: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="minWeight")
    max_weight: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="maxWeight")
    __properties = ["required", "unitOfMeasurement", "minWeight", "maxWeight"]

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
    def from_json(cls, json_str: str) -> WeightRules:
        """Create an instance of WeightRules from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WeightRules:
        """Create an instance of WeightRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WeightRules.parse_obj(obj)

        _obj = WeightRules.parse_obj({
            "required": obj.get("required"),
            "unit_of_measurement": obj.get("unitOfMeasurement"),
            "min_weight": obj.get("minWeight"),
            "max_weight": obj.get("maxWeight")
        })
        return _obj


