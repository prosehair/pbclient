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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator

class Address(BaseModel):
    """
    Address
    """
    address_lines: Optional[conlist(StrictStr)] = Field(None, alias="addressLines")
    carrier_route: Optional[StrictStr] = Field(None, alias="carrierRoute")
    city_town: Optional[StrictStr] = Field(None, alias="cityTown")
    company: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = Field(None, alias="countryCode", description="2-character country code (ISO-3166-1 alpha-2)")
    delivery_point: Optional[StrictStr] = Field(None, alias="deliveryPoint")
    email: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    residential: Optional[StrictBool] = None
    state_province: Optional[StrictStr] = Field(None, alias="stateProvince")
    status: Optional[StrictStr] = None
    tax_id: Optional[StrictStr] = Field(None, alias="taxId")
    tax_id_type: Optional[StrictStr] = Field(None, alias="taxIdType")
    __properties = ["addressLines", "carrierRoute", "cityTown", "company", "countryCode", "deliveryPoint", "email", "name", "phone", "postalCode", "residential", "stateProvince", "status", "taxId", "taxIdType"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARSED', 'VALIDATED_CHANGED', 'VALIDATED_AND_NOT_CHANGED', 'NOT_CHANGED'):
            raise ValueError("must be one of enum values ('PARSED', 'VALIDATED_CHANGED', 'VALIDATED_AND_NOT_CHANGED', 'NOT_CHANGED')")
        return value

    @validator('tax_id_type')
    def tax_id_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EIN', 'GST', 'VAT', 'RFC', 'EORI'):
            raise ValueError("must be one of enum values ('EIN', 'GST', 'VAT', 'RFC', 'EORI')")
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
    def from_json(cls, json_str: str) -> Address:
        """Create an instance of Address from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Address:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Address.parse_obj(obj)

        _obj = Address.parse_obj({
            "address_lines": obj.get("addressLines"),
            "carrier_route": obj.get("carrierRoute"),
            "city_town": obj.get("cityTown"),
            "company": obj.get("company"),
            "country_code": obj.get("countryCode"),
            "delivery_point": obj.get("deliveryPoint"),
            "email": obj.get("email"),
            "name": obj.get("name"),
            "phone": obj.get("phone"),
            "postal_code": obj.get("postalCode"),
            "residential": obj.get("residential"),
            "state_province": obj.get("stateProvince"),
            "status": obj.get("status"),
            "tax_id": obj.get("taxId"),
            "tax_id_type": obj.get("taxIdType")
        })
        return _obj


