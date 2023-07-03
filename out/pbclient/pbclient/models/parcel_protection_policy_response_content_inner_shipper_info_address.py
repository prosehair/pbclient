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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class ParcelProtectionPolicyResponseContentInnerShipperInfoAddress(BaseModel):
    """
    ParcelProtectionPolicyResponseContentInnerShipperInfoAddress
    """
    street1: Optional[StrictStr] = None
    street2: Optional[StrictStr] = None
    street3: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    region: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    __properties = ["street1", "street2", "street3", "city", "region", "country", "postalCode"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionPolicyResponseContentInnerShipperInfoAddress:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfoAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionPolicyResponseContentInnerShipperInfoAddress:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfoAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionPolicyResponseContentInnerShipperInfoAddress.parse_obj(obj)

        _obj = ParcelProtectionPolicyResponseContentInnerShipperInfoAddress.parse_obj({
            "street1": obj.get("street1"),
            "street2": obj.get("street2"),
            "street3": obj.get("street3"),
            "city": obj.get("city"),
            "region": obj.get("region"),
            "country": obj.get("country"),
            "postal_code": obj.get("postalCode")
        })
        return _obj

