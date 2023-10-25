# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.8
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from pbclient.models.parcel_protection_policy_response_content_inner_shipper_info_address import ParcelProtectionPolicyResponseContentInnerShipperInfoAddress

class ParcelProtectionPolicyResponseContentInnerShipperInfo(BaseModel):
    """
    ParcelProtectionPolicyResponseContentInnerShipperInfo
    """
    shipper_id: Optional[StrictStr] = Field(None, alias="shipperID")
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    middle_name: Optional[StrictStr] = Field(None, alias="middleName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    company: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone_number1: Optional[StrictStr] = Field(None, alias="phoneNumber1")
    phone_number2: Optional[StrictStr] = Field(None, alias="phoneNumber2")
    fax_number: Optional[StrictStr] = Field(None, alias="faxNumber")
    address: Optional[ParcelProtectionPolicyResponseContentInnerShipperInfoAddress] = None
    __properties = ["shipperID", "firstName", "middleName", "lastName", "company", "email", "phoneNumber1", "phoneNumber2", "faxNumber", "address"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionPolicyResponseContentInnerShipperInfo:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfo from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ParcelProtectionPolicyResponseContentInnerShipperInfo:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionPolicyResponseContentInnerShipperInfo.parse_obj(obj)

        _obj = ParcelProtectionPolicyResponseContentInnerShipperInfo.parse_obj({
            "shipper_id": obj.get("shipperID"),
            "first_name": obj.get("firstName"),
            "middle_name": obj.get("middleName"),
            "last_name": obj.get("lastName"),
            "company": obj.get("company"),
            "email": obj.get("email"),
            "phone_number1": obj.get("phoneNumber1"),
            "phone_number2": obj.get("phoneNumber2"),
            "fax_number": obj.get("faxNumber"),
            "address": ParcelProtectionPolicyResponseContentInnerShipperInfoAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None
        })
        return _obj


