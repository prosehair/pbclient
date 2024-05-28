# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.13
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
from pbclient.models.real_transaction_detail_report import RealTransactionDetailReport
from pbclient.models.search_criteria import SearchCriteria

class PageRealTransactionDetailReport(BaseModel):
    """
    PageRealTransactionDetailReport
    """
    content: Optional[conlist(RealTransactionDetailReport)] = None
    first: Optional[StrictBool] = None
    last: Optional[StrictBool] = None
    number: Optional[StrictInt] = None
    number_of_elements: Optional[StrictInt] = Field(None, alias="numberOfElements")
    size: Optional[StrictInt] = None
    total_elements: Optional[StrictInt] = Field(None, alias="totalElements")
    total_pages: Optional[StrictInt] = Field(None, alias="totalPages")
    search_criteria: Optional[SearchCriteria] = Field(None, alias="searchCriteria")
    __properties = ["content", "first", "last", "number", "numberOfElements", "size", "totalElements", "totalPages", "searchCriteria"]

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
    def from_json(cls, json_str: str) -> PageRealTransactionDetailReport:
        """Create an instance of PageRealTransactionDetailReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of search_criteria
        if self.search_criteria:
            _dict['searchCriteria'] = self.search_criteria.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PageRealTransactionDetailReport:
        """Create an instance of PageRealTransactionDetailReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PageRealTransactionDetailReport.parse_obj(obj)

        _obj = PageRealTransactionDetailReport.parse_obj({
            "content": [RealTransactionDetailReport.from_dict(_item) for _item in obj.get("content")] if obj.get("content") is not None else None,
            "first": obj.get("first"),
            "last": obj.get("last"),
            "number": obj.get("number"),
            "number_of_elements": obj.get("numberOfElements"),
            "size": obj.get("size"),
            "total_elements": obj.get("totalElements"),
            "total_pages": obj.get("totalPages"),
            "search_criteria": SearchCriteria.from_dict(obj.get("searchCriteria")) if obj.get("searchCriteria") is not None else None
        })
        return _obj


