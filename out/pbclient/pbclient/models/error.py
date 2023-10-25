# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.9
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class Error(BaseModel):
    """
    Error messages sent back to the caller
    """
    additional_info: Optional[StrictStr] = Field(None, alias="additionalInfo", description="additionalInfo")
    error_code: Optional[StrictStr] = Field(None, alias="errorCode", description="errorCode")
    message: Optional[StrictStr] = Field(None, description="message")
    more_info: Optional[StrictStr] = Field(None, alias="moreInfo", description="moreInfo")
    parameters: Optional[conlist(StrictStr)] = Field(None, description="parameters")
    __properties = ["additionalInfo", "errorCode", "message", "moreInfo", "parameters"]

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
    def from_json(cls, json_str: str) -> Error:
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Error:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Error.parse_obj(obj)

        _obj = Error.parse_obj({
            "additional_info": obj.get("additionalInfo"),
            "error_code": obj.get("errorCode"),
            "message": obj.get("message"),
            "more_info": obj.get("moreInfo"),
            "parameters": obj.get("parameters")
        })
        return _obj


