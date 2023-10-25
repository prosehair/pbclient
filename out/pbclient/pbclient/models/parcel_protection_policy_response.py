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
from pydantic import BaseModel, Field, StrictBool, StrictInt, conlist
from pbclient.models.parcel_protection_policy_response_content_inner import ParcelProtectionPolicyResponseContentInner
from pbclient.models.parcel_protection_policy_response_sort_inner import ParcelProtectionPolicyResponseSortInner

class ParcelProtectionPolicyResponse(BaseModel):
    """
    ParcelProtectionPolicyResponse
    """
    content: Optional[conlist(ParcelProtectionPolicyResponseContentInner)] = None
    last: Optional[StrictBool] = None
    total_elements: Optional[StrictInt] = Field(None, alias="totalElements")
    total_pages: Optional[StrictInt] = Field(None, alias="totalPages")
    first: Optional[StrictBool] = None
    number_of_elements: Optional[StrictInt] = Field(None, alias="numberOfElements")
    sort: Optional[conlist(ParcelProtectionPolicyResponseSortInner)] = None
    size: Optional[StrictInt] = None
    number: Optional[StrictInt] = None
    __properties = ["content", "last", "totalElements", "totalPages", "first", "numberOfElements", "sort", "size", "number"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionPolicyResponse:
        """Create an instance of ParcelProtectionPolicyResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in content (list)
        _items = []
        if self.content:
            for _item in self.content:
                if _item:
                    _items.append(_item.to_dict())
            _dict['content'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sort (list)
        _items = []
        if self.sort:
            for _item in self.sort:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sort'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionPolicyResponse:
        """Create an instance of ParcelProtectionPolicyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionPolicyResponse.parse_obj(obj)

        _obj = ParcelProtectionPolicyResponse.parse_obj({
            "content": [ParcelProtectionPolicyResponseContentInner.from_dict(_item) for _item in obj.get("content")] if obj.get("content") is not None else None,
            "last": obj.get("last"),
            "total_elements": obj.get("totalElements"),
            "total_pages": obj.get("totalPages"),
            "first": obj.get("first"),
            "number_of_elements": obj.get("numberOfElements"),
            "sort": [ParcelProtectionPolicyResponseSortInner.from_dict(_item) for _item in obj.get("sort")] if obj.get("sort") is not None else None,
            "size": obj.get("size"),
            "number": obj.get("number")
        })
        return _obj


