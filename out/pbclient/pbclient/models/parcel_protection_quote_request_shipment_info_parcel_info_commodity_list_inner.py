# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.10
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner(BaseModel):
    """
    ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner
    """
    category_path: StrictStr = Field(..., alias="categoryPath")
    item_code: StrictStr = Field(..., alias="itemCode")
    name: StrictStr = Field(...)
    url: StrictStr = Field(...)
    __properties = ["categoryPath", "itemCode", "name", "url"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner.parse_obj(obj)

        _obj = ParcelProtectionQuoteRequestShipmentInfoParcelInfoCommodityListInner.parse_obj({
            "category_path": obj.get("categoryPath"),
            "item_code": obj.get("itemCode"),
            "name": obj.get("name"),
            "url": obj.get("url")
        })
        return _obj


