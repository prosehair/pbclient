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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from pbclient.models.parcel_type_rules import ParcelTypeRules
from pbclient.models.services import Services

class CarrierRule(BaseModel):
    """
    CarrierRule
    """
    service_id: Optional[Services] = Field(None, alias="serviceId")
    branded_name: Optional[StrictStr] = Field(None, alias="brandedName")
    parcel_type_rules: Optional[conlist(ParcelTypeRules)] = Field(None, alias="parcelTypeRules")
    parameters: Optional[conlist(StrictStr)] = None
    __properties = ["serviceId", "brandedName", "parcelTypeRules", "parameters"]

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
    def from_json(cls, json_str: str) -> CarrierRule:
        """Create an instance of CarrierRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in parcel_type_rules (list)
        _items = []
        if self.parcel_type_rules:
            for _item in self.parcel_type_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parcelTypeRules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CarrierRule:
        """Create an instance of CarrierRule from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CarrierRule.parse_obj(obj)

        _obj = CarrierRule.parse_obj({
            "service_id": obj.get("serviceId"),
            "branded_name": obj.get("brandedName"),
            "parcel_type_rules": [ParcelTypeRules.from_dict(_item) for _item in obj.get("parcelTypeRules")] if obj.get("parcelTypeRules") is not None else None,
            "parameters": obj.get("parameters")
        })
        return _obj

