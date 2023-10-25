# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.6
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class CarrierPayment(BaseModel):
    """
    CarrierPayment
    """
    account_number: Optional[StrictStr] = Field(None, alias="accountNumber")
    country_code: Optional[StrictStr] = Field(None, alias="countryCode")
    party: StrictStr = Field(...)
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    type_of_charge: StrictStr = Field(..., alias="typeOfCharge")
    __properties = ["accountNumber", "countryCode", "party", "postalCode", "typeOfCharge"]

    @validator('party')
    def party_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('BILL_RECEIVER', 'BILL_SENDER', 'BILL_THIRD_PARTY', 'BILL_RECEIVER_CONTRACT'):
            raise ValueError("must be one of enum values ('BILL_RECEIVER', 'BILL_SENDER', 'BILL_THIRD_PARTY', 'BILL_RECEIVER_CONTRACT')")
        return value

    @validator('type_of_charge')
    def type_of_charge_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('TRANSPORTATION_CHARGES', 'DUTIES_AND_TAXES', 'ALL_CHARGES'):
            raise ValueError("must be one of enum values ('TRANSPORTATION_CHARGES', 'DUTIES_AND_TAXES', 'ALL_CHARGES')")
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
    def from_json(cls, json_str: str) -> CarrierPayment:
        """Create an instance of CarrierPayment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CarrierPayment:
        """Create an instance of CarrierPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CarrierPayment.parse_obj(obj)

        _obj = CarrierPayment.parse_obj({
            "account_number": obj.get("accountNumber"),
            "country_code": obj.get("countryCode"),
            "party": obj.get("party"),
            "postal_code": obj.get("postalCode"),
            "type_of_charge": obj.get("typeOfCharge")
        })
        return _obj


