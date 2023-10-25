# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.7
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from pbclient.models.address import Address

class AddressVerifySuggest(BaseModel):
    """
    AddressVerifySuggest
    """
    address: Optional[Address] = None
    __properties = ["address"]

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
    def from_json(cls, json_str: str) -> AddressVerifySuggest:
        """Create an instance of AddressVerifySuggest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddressVerifySuggest:
        """Create an instance of AddressVerifySuggest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddressVerifySuggest.parse_obj(obj)

        _obj = AddressVerifySuggest.parse_obj({
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None
        })
        return _obj


