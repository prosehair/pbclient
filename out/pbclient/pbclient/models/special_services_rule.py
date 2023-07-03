# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from pbclient.models.prerequisite_rules import PrerequisiteRules
from pbclient.models.services_parameter_rule import ServicesParameterRule
from pbclient.models.special_service_codes import SpecialServiceCodes

class SpecialServicesRule(BaseModel):
    """
    SpecialServicesRule
    """
    special_service_id: Optional[SpecialServiceCodes] = Field(None, alias="specialServiceId")
    branded_name: Optional[StrictStr] = Field(None, alias="brandedName")
    category_id: Optional[StrictStr] = Field(None, alias="categoryId")
    category_name: Optional[StrictStr] = Field(None, alias="categoryName")
    trackable: Optional[StrictBool] = None
    input_parameter_rules: Optional[conlist(ServicesParameterRule)] = Field(None, alias="inputParameterRules")
    prerequisite_rules: Optional[conlist(PrerequisiteRules)] = Field(None, alias="prerequisiteRules")
    incompatible_special_services: Optional[SpecialServiceCodes] = Field(None, alias="incompatibleSpecialServices")
    __properties = ["specialServiceId", "brandedName", "categoryId", "categoryName", "trackable", "inputParameterRules", "prerequisiteRules", "incompatibleSpecialServices"]

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
    def from_json(cls, json_str: str) -> SpecialServicesRule:
        """Create an instance of SpecialServicesRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in input_parameter_rules (list)
        _items = []
        if self.input_parameter_rules:
            for _item in self.input_parameter_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inputParameterRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in prerequisite_rules (list)
        _items = []
        if self.prerequisite_rules:
            for _item in self.prerequisite_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['prerequisiteRules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpecialServicesRule:
        """Create an instance of SpecialServicesRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpecialServicesRule.parse_obj(obj)

        _obj = SpecialServicesRule.parse_obj({
            "special_service_id": obj.get("specialServiceId"),
            "branded_name": obj.get("brandedName"),
            "category_id": obj.get("categoryId"),
            "category_name": obj.get("categoryName"),
            "trackable": obj.get("trackable"),
            "input_parameter_rules": [ServicesParameterRule.from_dict(_item) for _item in obj.get("inputParameterRules")] if obj.get("inputParameterRules") is not None else None,
            "prerequisite_rules": [PrerequisiteRules.from_dict(_item) for _item in obj.get("prerequisiteRules")] if obj.get("prerequisiteRules") is not None else None,
            "incompatible_special_services": obj.get("incompatibleSpecialServices")
        })
        return _obj

