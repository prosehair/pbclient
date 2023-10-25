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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from pbclient.models.cross_border_quotes_request_basket_items_inner_attributes_inner import CrossBorderQuotesRequestBasketItemsInnerAttributesInner
from pbclient.models.cross_border_quotes_request_basket_items_inner_categories_inner import CrossBorderQuotesRequestBasketItemsInnerCategoriesInner
from pbclient.models.cross_border_quotes_request_basket_items_inner_identifiers_inner import CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner
from pbclient.models.cross_border_quotes_request_basket_items_inner_item_dimension import CrossBorderQuotesRequestBasketItemsInnerItemDimension
from pbclient.models.cross_border_quotes_request_basket_items_inner_pricing import CrossBorderQuotesRequestBasketItemsInnerPricing
from pbclient.models.cross_border_quotes_request_basket_items_inner_unit_weight import CrossBorderQuotesRequestBasketItemsInnerUnitWeight

class CrossBorderQuotesRequestBasketItemsInner(BaseModel):
    """
    CrossBorderQuotesRequestBasketItemsInner
    """
    item_id: Optional[StrictStr] = Field(None, alias="itemId")
    categories: Optional[conlist(CrossBorderQuotesRequestBasketItemsInnerCategoriesInner)] = None
    description: Optional[StrictStr] = None
    long_description: Optional[StrictStr] = Field(None, alias="longDescription")
    unit_weight: Optional[CrossBorderQuotesRequestBasketItemsInnerUnitWeight] = Field(None, alias="unitWeight")
    item_dimension: Optional[CrossBorderQuotesRequestBasketItemsInnerItemDimension] = Field(None, alias="itemDimension")
    url: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = None
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="unitPrice")
    origin_country_code: Optional[StrictStr] = Field(None, alias="originCountryCode")
    parent_identifier: Optional[StrictStr] = Field(None, alias="parentIdentifier")
    child_identifier: Optional[StrictStr] = Field(None, alias="childIdentifier")
    kit: Optional[StrictStr] = None
    kit_identifier: Optional[StrictStr] = Field(None, alias="kitIdentifier")
    kit_quantity: Optional[StrictStr] = Field(None, alias="kitQuantity")
    manufacturer: Optional[StrictStr] = None
    brand: Optional[StrictStr] = None
    eccn: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    pricing: Optional[CrossBorderQuotesRequestBasketItemsInnerPricing] = None
    h_s_tariff_code: Optional[StrictStr] = Field(None, alias="hSTariffCode")
    h_s_tariff_code_country: Optional[StrictStr] = Field(None, alias="hSTariffCodeCountry")
    identifiers: Optional[conlist(CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner)] = None
    image_urls: Optional[conlist(StrictStr)] = Field(None, alias="imageUrls")
    ships_alone: Optional[StrictBool] = Field(None, alias="shipsAlone")
    attributes: Optional[conlist(CrossBorderQuotesRequestBasketItemsInnerAttributesInner)] = None
    hazmats: Optional[conlist(StrictStr)] = None
    __properties = ["itemId", "categories", "description", "longDescription", "unitWeight", "itemDimension", "url", "quantity", "unitPrice", "originCountryCode", "parentIdentifier", "childIdentifier", "kit", "kitIdentifier", "kitQuantity", "manufacturer", "brand", "eccn", "enabled", "pricing", "hSTariffCode", "hSTariffCodeCountry", "identifiers", "imageUrls", "shipsAlone", "attributes", "hazmats"]

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
    def from_json(cls, json_str: str) -> CrossBorderQuotesRequestBasketItemsInner:
        """Create an instance of CrossBorderQuotesRequestBasketItemsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of unit_weight
        if self.unit_weight:
            _dict['unitWeight'] = self.unit_weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item_dimension
        if self.item_dimension:
            _dict['itemDimension'] = self.item_dimension.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in identifiers (list)
        _items = []
        if self.identifiers:
            for _item in self.identifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CrossBorderQuotesRequestBasketItemsInner:
        """Create an instance of CrossBorderQuotesRequestBasketItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CrossBorderQuotesRequestBasketItemsInner.parse_obj(obj)

        _obj = CrossBorderQuotesRequestBasketItemsInner.parse_obj({
            "item_id": obj.get("itemId"),
            "categories": [CrossBorderQuotesRequestBasketItemsInnerCategoriesInner.from_dict(_item) for _item in obj.get("categories")] if obj.get("categories") is not None else None,
            "description": obj.get("description"),
            "long_description": obj.get("longDescription"),
            "unit_weight": CrossBorderQuotesRequestBasketItemsInnerUnitWeight.from_dict(obj.get("unitWeight")) if obj.get("unitWeight") is not None else None,
            "item_dimension": CrossBorderQuotesRequestBasketItemsInnerItemDimension.from_dict(obj.get("itemDimension")) if obj.get("itemDimension") is not None else None,
            "url": obj.get("url"),
            "quantity": obj.get("quantity"),
            "unit_price": obj.get("unitPrice"),
            "origin_country_code": obj.get("originCountryCode"),
            "parent_identifier": obj.get("parentIdentifier"),
            "child_identifier": obj.get("childIdentifier"),
            "kit": obj.get("kit"),
            "kit_identifier": obj.get("kitIdentifier"),
            "kit_quantity": obj.get("kitQuantity"),
            "manufacturer": obj.get("manufacturer"),
            "brand": obj.get("brand"),
            "eccn": obj.get("eccn"),
            "enabled": obj.get("enabled"),
            "pricing": CrossBorderQuotesRequestBasketItemsInnerPricing.from_dict(obj.get("pricing")) if obj.get("pricing") is not None else None,
            "h_s_tariff_code": obj.get("hSTariffCode"),
            "h_s_tariff_code_country": obj.get("hSTariffCodeCountry"),
            "identifiers": [CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner.from_dict(_item) for _item in obj.get("identifiers")] if obj.get("identifiers") is not None else None,
            "image_urls": obj.get("imageUrls"),
            "ships_alone": obj.get("shipsAlone"),
            "attributes": [CrossBorderQuotesRequestBasketItemsInnerAttributesInner.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None,
            "hazmats": obj.get("hazmats")
        })
        return _obj


