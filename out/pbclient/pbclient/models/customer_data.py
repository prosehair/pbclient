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
from pydantic import BaseModel, Field, conlist
from pbclient.models.parameter import Parameter

class CustomerData(BaseModel):
    """
    CustomerData
    """
    label_details: Optional[conlist(Parameter)] = Field(None, alias="labelDetails")
    __properties = ["labelDetails"]

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
    def from_json(cls, json_str: str) -> CustomerData:
        """Create an instance of CustomerData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in label_details (list)
        _items = []
        if self.label_details:
            for _item in self.label_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labelDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomerData:
        """Create an instance of CustomerData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomerData.parse_obj(obj)

        _obj = CustomerData.parse_obj({
            "label_details": [Parameter.from_dict(_item) for _item in obj.get("labelDetails")] if obj.get("labelDetails") is not None else None
        })
        return _obj

