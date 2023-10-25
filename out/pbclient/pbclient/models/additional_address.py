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



from pydantic import BaseModel, Field, StrictStr, validator
from pbclient.models.address import Address

class AdditionalAddress(BaseModel):
    """
    AdditionalAddress
    """
    address: Address = Field(...)
    address_type: StrictStr = Field(..., alias="addressType")
    __properties = ["address", "addressType"]

    @validator('address_type')
    def address_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('HOLD', 'BROKER', 'THIRD_PARTY', 'PICKUP', 'EXPORTER'):
            raise ValueError("must be one of enum values ('HOLD', 'BROKER', 'THIRD_PARTY', 'PICKUP', 'EXPORTER')")
        return value

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
    def from_json(cls, json_str: str) -> AdditionalAddress:
        """Create an instance of AdditionalAddress from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AdditionalAddress:
        """Create an instance of AdditionalAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdditionalAddress.parse_obj(obj)

        _obj = AdditionalAddress.parse_obj({
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "address_type": obj.get("addressType")
        })
        return _obj


