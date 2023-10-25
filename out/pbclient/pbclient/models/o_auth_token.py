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

class OAuthToken(BaseModel):
    """
    OAuthToken
    """
    access_token: Optional[StrictStr] = None
    token_type: Optional[StrictStr] = Field(None, alias="tokenType")
    issued_at: Optional[StrictStr] = Field(None, alias="issuedAt")
    expires_in: Optional[StrictStr] = Field(None, alias="expiresIn")
    client_id: Optional[StrictStr] = Field(None, alias="clientID")
    org: Optional[StrictStr] = None
    __properties = ["access_token", "tokenType", "issuedAt", "expiresIn", "clientID", "org"]

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
    def from_json(cls, json_str: str) -> OAuthToken:
        """Create an instance of OAuthToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OAuthToken:
        """Create an instance of OAuthToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuthToken.parse_obj(obj)

        _obj = OAuthToken.parse_obj({
            "access_token": obj.get("access_token"),
            "token_type": obj.get("tokenType"),
            "issued_at": obj.get("issuedAt"),
            "expires_in": obj.get("expiresIn"),
            "client_id": obj.get("clientID"),
            "org": obj.get("org")
        })
        return _obj


