# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.14
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist

class ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress(BaseModel):
    """
    ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress
    """
    address_lines: conlist(StrictStr) = Field(..., alias="addressLines")
    city_town: StrictStr = Field(..., alias="cityTown")
    state_province: StrictStr = Field(..., alias="stateProvince")
    postal_code: StrictStr = Field(..., alias="postalCode")
    country_code: StrictStr = Field(..., alias="countryCode")
    __properties = ["addressLines", "cityTown", "stateProvince", "postalCode", "countryCode"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress.parse_obj(obj)

        _obj = ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress.parse_obj({
            "address_lines": obj.get("addressLines"),
            "city_town": obj.get("cityTown"),
            "state_province": obj.get("stateProvince"),
            "postal_code": obj.get("postalCode"),
            "country_code": obj.get("countryCode")
        })
        return _obj


