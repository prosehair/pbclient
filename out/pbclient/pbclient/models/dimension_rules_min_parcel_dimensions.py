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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class DimensionRulesMinParcelDimensions(BaseModel):
    """
    DimensionRulesMinParcelDimensions
    """
    length: Optional[Union[StrictFloat, StrictInt]] = None
    width: Optional[Union[StrictFloat, StrictInt]] = None
    height: Optional[Union[StrictFloat, StrictInt]] = None
    unit_of_measurement: Optional[StrictStr] = Field(None, alias="unitOfMeasurement")
    __properties = ["length", "width", "height", "unitOfMeasurement"]

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
    def from_json(cls, json_str: str) -> DimensionRulesMinParcelDimensions:
        """Create an instance of DimensionRulesMinParcelDimensions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DimensionRulesMinParcelDimensions:
        """Create an instance of DimensionRulesMinParcelDimensions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DimensionRulesMinParcelDimensions.parse_obj(obj)

        _obj = DimensionRulesMinParcelDimensions.parse_obj({
            "length": obj.get("length"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "unit_of_measurement": obj.get("unitOfMeasurement")
        })
        return _obj


