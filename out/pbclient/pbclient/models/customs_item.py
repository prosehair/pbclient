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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from pbclient.models.parcel_dimension import ParcelDimension
from pbclient.models.parcel_weight import ParcelWeight

class CustomsItem(BaseModel):
    """
    CustomsItem
    """
    description: StrictStr = Field(...)
    hazmat: Optional[conlist(StrictStr)] = None
    h_s_tariff_code: Optional[StrictStr] = Field(None, alias="hSTariffCode")
    h_s_tariff_code_country: Optional[StrictStr] = Field(None, alias="hSTariffCodeCountry")
    item_dimension: Optional[ParcelDimension] = Field(None, alias="itemDimension")
    item_id: StrictStr = Field(..., alias="itemId")
    manufacturer: Optional[StrictStr] = None
    origin_country_code: Optional[StrictStr] = Field(None, alias="originCountryCode")
    quantity: StrictInt = Field(...)
    unit_price: Union[StrictFloat, StrictInt] = Field(..., alias="unitPrice")
    unit_weight: Optional[ParcelWeight] = Field(None, alias="unitWeight")
    url: StrictStr = Field(...)
    __properties = ["description", "hazmat", "hSTariffCode", "hSTariffCodeCountry", "itemDimension", "itemId", "manufacturer", "originCountryCode", "quantity", "unitPrice", "unitWeight", "url"]

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
    def from_json(cls, json_str: str) -> CustomsItem:
        """Create an instance of CustomsItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of item_dimension
        if self.item_dimension:
            _dict['itemDimension'] = self.item_dimension.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_weight
        if self.unit_weight:
            _dict['unitWeight'] = self.unit_weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomsItem:
        """Create an instance of CustomsItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomsItem.parse_obj(obj)

        _obj = CustomsItem.parse_obj({
            "description": obj.get("description"),
            "hazmat": obj.get("hazmat"),
            "h_s_tariff_code": obj.get("hSTariffCode"),
            "h_s_tariff_code_country": obj.get("hSTariffCodeCountry"),
            "item_dimension": ParcelDimension.from_dict(obj.get("itemDimension")) if obj.get("itemDimension") is not None else None,
            "item_id": obj.get("itemId"),
            "manufacturer": obj.get("manufacturer"),
            "origin_country_code": obj.get("originCountryCode"),
            "quantity": obj.get("quantity"),
            "unit_price": obj.get("unitPrice"),
            "unit_weight": ParcelWeight.from_dict(obj.get("unitWeight")) if obj.get("unitWeight") is not None else None,
            "url": obj.get("url")
        })
        return _obj


