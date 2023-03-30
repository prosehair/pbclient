# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictFloat, StrictStr
from pbclient.models.parcel_dimension import ParcelDimension
from pbclient.models.parcel_weight import ParcelWeight

class Parcel(BaseModel):
    """
    Parcel
    """
    dimension: Optional[ParcelDimension] = None
    weight: Optional[ParcelWeight] = None
    value_of_goods: Optional[StrictFloat] = Field(None, alias="valueOfGoods")
    currency_code: Optional[StrictStr] = Field(None, alias="currencyCode", description="Currency code as per [IOS 4217](https://en.wikipedia.org/wiki/ISO_4217)")
    __properties = ["dimension", "weight", "valueOfGoods", "currencyCode"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Parcel:
        """Create an instance of Parcel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dimension
        if self.dimension:
            _dict['dimension'] = self.dimension.to_dict()
        # override the default output from pydantic by calling `to_dict()` of weight
        if self.weight:
            _dict['weight'] = self.weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Parcel:
        """Create an instance of Parcel from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Parcel.parse_obj(obj)

        _obj = Parcel.parse_obj({
            "dimension": ParcelDimension.from_dict(obj.get("dimension")) if obj.get("dimension") is not None else None,
            "weight": ParcelWeight.from_dict(obj.get("weight")) if obj.get("weight") is not None else None,
            "value_of_goods": obj.get("valueOfGoods"),
            "currency_code": obj.get("currencyCode")
        })
        return _obj

