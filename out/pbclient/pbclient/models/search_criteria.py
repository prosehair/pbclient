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
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class SearchCriteria(BaseModel):
    """
    SearchCriteria
    """
    developer_id: Optional[StrictStr] = Field(None, alias="developerId")
    from_date: Optional[StrictStr] = Field(None, alias="fromDate")
    to_date: Optional[StrictStr] = Field(None, alias="toDate")
    __properties = ["developerId", "fromDate", "toDate"]

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
    def from_json(cls, json_str: str) -> SearchCriteria:
        """Create an instance of SearchCriteria from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SearchCriteria:
        """Create an instance of SearchCriteria from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SearchCriteria.parse_obj(obj)

        _obj = SearchCriteria.parse_obj({
            "developer_id": obj.get("developerId"),
            "from_date": obj.get("fromDate"),
            "to_date": obj.get("toDate")
        })
        return _obj

