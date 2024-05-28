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



from pydantic import BaseModel, Field
from pbclient.models.parcel_protection_quote_request_shipment_info_shipper_info_address import ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress

class ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo(BaseModel):
    """
    ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo
    """
    address: ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress = Field(...)
    __properties = ["address"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo.parse_obj(obj)

        _obj = ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo.parse_obj({
            "address": ParcelProtectionQuoteRequestShipmentInfoShipperInfoAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None
        })
        return _obj


