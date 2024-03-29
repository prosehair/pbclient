# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 2.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pbclient.models.cross_border_quotes_request_basket_items_inner_attributes_inner import CrossBorderQuotesRequestBasketItemsInnerAttributesInner
from pbclient.models.cross_border_quotes_request_basket_items_inner_categories_inner import CrossBorderQuotesRequestBasketItemsInnerCategoriesInner
from pbclient.models.cross_border_quotes_request_basket_items_inner_identifiers_inner import CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner
from pbclient.models.cross_border_quotes_request_basket_items_inner_item_dimension import CrossBorderQuotesRequestBasketItemsInnerItemDimension
from pbclient.models.cross_border_quotes_request_basket_items_inner_pricing import CrossBorderQuotesRequestBasketItemsInnerPricing
from pbclient.models.cross_border_quotes_request_basket_items_inner_unit_weight import CrossBorderQuotesRequestBasketItemsInnerUnitWeight
from typing import Optional, Set
from typing_extensions import Self

class CrossBorderQuotesRequestBasketItemsInner(BaseModel):
    """
    CrossBorderQuotesRequestBasketItemsInner
    """ # noqa: E501
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    categories: Optional[List[CrossBorderQuotesRequestBasketItemsInnerCategoriesInner]] = None
    description: Optional[StrictStr] = None
    long_description: Optional[StrictStr] = Field(default=None, alias="longDescription")
    unit_weight: Optional[CrossBorderQuotesRequestBasketItemsInnerUnitWeight] = Field(default=None, alias="unitWeight")
    item_dimension: Optional[CrossBorderQuotesRequestBasketItemsInnerItemDimension] = Field(default=None, alias="itemDimension")
    url: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = None
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unitPrice")
    origin_country_code: Optional[StrictStr] = Field(default=None, alias="originCountryCode")
    parent_identifier: Optional[StrictStr] = Field(default=None, alias="parentIdentifier")
    child_identifier: Optional[StrictStr] = Field(default=None, alias="childIdentifier")
    kit: Optional[StrictStr] = None
    kit_identifier: Optional[StrictStr] = Field(default=None, alias="kitIdentifier")
    kit_quantity: Optional[StrictStr] = Field(default=None, alias="kitQuantity")
    manufacturer: Optional[StrictStr] = None
    brand: Optional[StrictStr] = None
    eccn: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    pricing: Optional[CrossBorderQuotesRequestBasketItemsInnerPricing] = None
    h_s_tariff_code: Optional[StrictStr] = Field(default=None, alias="hSTariffCode")
    h_s_tariff_code_country: Optional[StrictStr] = Field(default=None, alias="hSTariffCodeCountry")
    identifiers: Optional[List[CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner]] = None
    image_urls: Optional[List[StrictStr]] = Field(default=None, alias="imageUrls")
    ships_alone: Optional[StrictBool] = Field(default=None, alias="shipsAlone")
    attributes: Optional[List[CrossBorderQuotesRequestBasketItemsInnerAttributesInner]] = None
    hazmats: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["itemId", "categories", "description", "longDescription", "unitWeight", "itemDimension", "url", "quantity", "unitPrice", "originCountryCode", "parentIdentifier", "childIdentifier", "kit", "kitIdentifier", "kitQuantity", "manufacturer", "brand", "eccn", "enabled", "pricing", "hSTariffCode", "hSTariffCodeCountry", "identifiers", "imageUrls", "shipsAlone", "attributes", "hazmats"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CrossBorderQuotesRequestBasketItemsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CrossBorderQuotesRequestBasketItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemId": obj.get("itemId"),
            "categories": [CrossBorderQuotesRequestBasketItemsInnerCategoriesInner.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
            "description": obj.get("description"),
            "longDescription": obj.get("longDescription"),
            "unitWeight": CrossBorderQuotesRequestBasketItemsInnerUnitWeight.from_dict(obj["unitWeight"]) if obj.get("unitWeight") is not None else None,
            "itemDimension": CrossBorderQuotesRequestBasketItemsInnerItemDimension.from_dict(obj["itemDimension"]) if obj.get("itemDimension") is not None else None,
            "url": obj.get("url"),
            "quantity": obj.get("quantity"),
            "unitPrice": obj.get("unitPrice"),
            "originCountryCode": obj.get("originCountryCode"),
            "parentIdentifier": obj.get("parentIdentifier"),
            "childIdentifier": obj.get("childIdentifier"),
            "kit": obj.get("kit"),
            "kitIdentifier": obj.get("kitIdentifier"),
            "kitQuantity": obj.get("kitQuantity"),
            "manufacturer": obj.get("manufacturer"),
            "brand": obj.get("brand"),
            "eccn": obj.get("eccn"),
            "enabled": obj.get("enabled"),
            "pricing": CrossBorderQuotesRequestBasketItemsInnerPricing.from_dict(obj["pricing"]) if obj.get("pricing") is not None else None,
            "hSTariffCode": obj.get("hSTariffCode"),
            "hSTariffCodeCountry": obj.get("hSTariffCodeCountry"),
            "identifiers": [CrossBorderQuotesRequestBasketItemsInnerIdentifiersInner.from_dict(_item) for _item in obj["identifiers"]] if obj.get("identifiers") is not None else None,
            "imageUrls": obj.get("imageUrls"),
            "shipsAlone": obj.get("shipsAlone"),
            "attributes": [CrossBorderQuotesRequestBasketItemsInnerAttributesInner.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "hazmats": obj.get("hazmats")
        })
        return _obj


