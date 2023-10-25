# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.9
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

class InfectiousSubstanceContact(BaseModel):
    """
    InfectiousSubstanceContact
    """
    company_name: Optional[StrictStr] = Field(None, alias="companyName")
    contact_id: Optional[StrictStr] = Field(None, alias="contactId")
    email_address: Optional[StrictStr] = Field(None, alias="emailAddress")
    person_name: Optional[StrictStr] = Field(None, alias="personName")
    phone_number: Optional[StrictStr] = Field(None, alias="phoneNumber")
    __properties = ["companyName", "contactId", "emailAddress", "personName", "phoneNumber"]

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
    def from_json(cls, json_str: str) -> InfectiousSubstanceContact:
        """Create an instance of InfectiousSubstanceContact from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InfectiousSubstanceContact:
        """Create an instance of InfectiousSubstanceContact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InfectiousSubstanceContact.parse_obj(obj)

        _obj = InfectiousSubstanceContact.parse_obj({
            "company_name": obj.get("companyName"),
            "contact_id": obj.get("contactId"),
            "email_address": obj.get("emailAddress"),
            "person_name": obj.get("personName"),
            "phone_number": obj.get("phoneNumber")
        })
        return _obj


