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

class ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress(BaseModel):
    """
    ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress
    """
    address_lines: Optional[conlist(StrictStr)] = Field(None, alias="addressLines")
    city_town: Optional[StrictStr] = Field(None, alias="cityTown")
    state_province: Optional[StrictStr] = Field(None, alias="stateProvince")
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    country_code: Optional[StrictStr] = Field(None, alias="countryCode")
    __properties = ["addressLines", "cityTown", "stateProvince", "postalCode", "countryCode"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress:
        """Create an instance of ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress:
        """Create an instance of ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress.parse_obj(obj)

        _obj = ParcelProtectionCreateRequestShipmentInfoShipperInfoAddress.parse_obj({
            "address_lines": obj.get("addressLines"),
            "city_town": obj.get("cityTown"),
            "state_province": obj.get("stateProvince"),
            "postal_code": obj.get("postalCode"),
            "country_code": obj.get("countryCode")
        })
        return _obj

