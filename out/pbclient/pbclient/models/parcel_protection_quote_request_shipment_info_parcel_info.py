# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from pbclient.models.parcel_protection_quote_request_shipment_info_parcel_info_commodity_list_inner import ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner

class ParcelProtectionQuoteRequestShipmentInfoParcelInfo(BaseModel):
    """
    ParcelProtectionQuoteRequestShipmentInfoParcelInfo
    """
    commodity_list: conlist(ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner) = Field(..., alias="commodityList")
    __properties = ["commodityList"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionQuoteRequestShipmentInfoParcelInfo:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoParcelInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in commodity_list (list)
        _items = []
        if self.commodity_list:
            for _item in self.commodity_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['commodityList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionQuoteRequestShipmentInfoParcelInfo:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoParcelInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionQuoteRequestShipmentInfoParcelInfo.parse_obj(obj)

        _obj = ParcelProtectionQuoteRequestShipmentInfoParcelInfo.parse_obj({
            "commodity_list": [ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner.from_dict(_item) for _item in obj.get("commodityList")] if obj.get("commodityList") is not None else None
        })
        return _obj

