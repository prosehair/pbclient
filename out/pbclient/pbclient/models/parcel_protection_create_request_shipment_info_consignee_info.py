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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from pbclient.models.address import Address
from pbclient.models.phone_numbers_inner import PhoneNumbersInner

class ParcelProtectionCreateRequestShipmentInfoConsigneeInfo(BaseModel):
    """
    ParcelProtectionCreateRequestShipmentInfoConsigneeInfo
    """
    address: Optional[Address] = None
    company_name: Optional[StrictStr] = Field(None, alias="companyName")
    family_name: Optional[StrictStr] = Field(None, alias="familyName")
    given_name: Optional[StrictStr] = Field(None, alias="givenName")
    middle_name: Optional[StrictStr] = Field(None, alias="middleName")
    email: Optional[StrictStr] = None
    phone_numbers: Optional[conlist(PhoneNumbersInner)] = Field(None, alias="phoneNumbers")
    __properties = ["address", "companyName", "familyName", "givenName", "middleName", "email", "phoneNumbers"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionCreateRequestShipmentInfoConsigneeInfo:
        """Create an instance of ParcelProtectionCreateRequestShipmentInfoConsigneeInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in phone_numbers (list)
        _items = []
        if self.phone_numbers:
            for _item in self.phone_numbers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['phoneNumbers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionCreateRequestShipmentInfoConsigneeInfo:
        """Create an instance of ParcelProtectionCreateRequestShipmentInfoConsigneeInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.parse_obj(obj)

        _obj = ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.parse_obj({
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "company_name": obj.get("companyName"),
            "family_name": obj.get("familyName"),
            "given_name": obj.get("givenName"),
            "middle_name": obj.get("middleName"),
            "email": obj.get("email"),
            "phone_numbers": [PhoneNumbersInner.from_dict(_item) for _item in obj.get("phoneNumbers")] if obj.get("phoneNumbers") is not None else None
        })
        return _obj

