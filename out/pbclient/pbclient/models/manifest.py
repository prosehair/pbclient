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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from pbclient.models.address import Address
from pbclient.models.carrier import Carrier
from pbclient.models.document import Document
from pbclient.models.parameter import Parameter

class Manifest(BaseModel):
    """
    Manifest
    """
    carrier: Carrier = Field(...)
    documents: Optional[conlist(Document)] = None
    from_address: Optional[Address] = Field(None, alias="fromAddress")
    induction_postal_code: Optional[StrictStr] = Field(None, alias="inductionPostalCode")
    manifest_id: Optional[StrictStr] = Field(None, alias="manifestId")
    manifest_tracking_number: Optional[StrictStr] = Field(None, alias="manifestTrackingNumber")
    parameters: Optional[conlist(Parameter)] = None
    parcel_tracking_numbers: Optional[conlist(StrictStr)] = Field(None, alias="parcelTrackingNumbers")
    submission_date: StrictStr = Field(..., alias="submissionDate")
    __properties = ["carrier", "documents", "fromAddress", "inductionPostalCode", "manifestId", "manifestTrackingNumber", "parameters", "parcelTrackingNumbers", "submissionDate"]

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
    def from_json(cls, json_str: str) -> Manifest:
        """Create an instance of Manifest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item in self.documents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of from_address
        if self.from_address:
            _dict['fromAddress'] = self.from_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Manifest:
        """Create an instance of Manifest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Manifest.parse_obj(obj)

        _obj = Manifest.parse_obj({
            "carrier": obj.get("carrier"),
            "documents": [Document.from_dict(_item) for _item in obj.get("documents")] if obj.get("documents") is not None else None,
            "from_address": Address.from_dict(obj.get("fromAddress")) if obj.get("fromAddress") is not None else None,
            "induction_postal_code": obj.get("inductionPostalCode"),
            "manifest_id": obj.get("manifestId"),
            "manifest_tracking_number": obj.get("manifestTrackingNumber"),
            "parameters": [Parameter.from_dict(_item) for _item in obj.get("parameters")] if obj.get("parameters") is not None else None,
            "parcel_tracking_numbers": obj.get("parcelTrackingNumbers"),
            "submission_date": obj.get("submissionDate")
        })
        return _obj


