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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from pbclient.models.unit_of_dimension import UnitOfDimension

class ParcelDimension(BaseModel):
    """
    ParcelDimension
    """
    length: Optional[Union[StrictFloat, StrictInt]] = None
    height: Optional[Union[StrictFloat, StrictInt]] = None
    width: Optional[Union[StrictFloat, StrictInt]] = None
    unit_of_measurement: Optional[UnitOfDimension] = Field(None, alias="unitOfMeasurement")
    irregular_parcel_girth: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="irregularParcelGirth")
    __properties = ["length", "height", "width", "unitOfMeasurement", "irregularParcelGirth"]

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
    def from_json(cls, json_str: str) -> ParcelDimension:
        """Create an instance of ParcelDimension from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelDimension:
        """Create an instance of ParcelDimension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelDimension.parse_obj(obj)

        _obj = ParcelDimension.parse_obj({
            "length": obj.get("length"),
            "height": obj.get("height"),
            "width": obj.get("width"),
            "unit_of_measurement": obj.get("unitOfMeasurement"),
            "irregular_parcel_girth": obj.get("irregularParcelGirth")
        })
        return _obj

