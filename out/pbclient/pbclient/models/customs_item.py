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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pbclient.models.parcel_dimension import ParcelDimension
from pbclient.models.parcel_weight import ParcelWeight
from typing import Optional, Set
from typing_extensions import Self

class CustomsItem(BaseModel):
    """
    CustomsItem
    """ # noqa: E501
    description: StrictStr
    hazmat: Optional[List[StrictStr]] = None
    h_s_tariff_code: Optional[StrictStr] = Field(default=None, alias="hSTariffCode")
    h_s_tariff_code_country: Optional[StrictStr] = Field(default=None, alias="hSTariffCodeCountry")
    item_dimension: Optional[ParcelDimension] = Field(default=None, alias="itemDimension")
    item_id: StrictStr = Field(alias="itemId")
    manufacturer: Optional[StrictStr] = None
    origin_country_code: Optional[StrictStr] = Field(default=None, alias="originCountryCode")
    quantity: StrictInt
    unit_price: Union[StrictFloat, StrictInt] = Field(alias="unitPrice")
    unit_weight: Optional[ParcelWeight] = Field(default=None, alias="unitWeight")
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "hazmat", "hSTariffCode", "hSTariffCodeCountry", "itemDimension", "itemId", "manufacturer", "originCountryCode", "quantity", "unitPrice", "unitWeight", "url"]

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
        """Create an instance of CustomsItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of item_dimension
        if self.item_dimension:
            _dict['itemDimension'] = self.item_dimension.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_weight
        if self.unit_weight:
            _dict['unitWeight'] = self.unit_weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomsItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "hazmat": obj.get("hazmat"),
            "hSTariffCode": obj.get("hSTariffCode"),
            "hSTariffCodeCountry": obj.get("hSTariffCodeCountry"),
            "itemDimension": ParcelDimension.from_dict(obj["itemDimension"]) if obj.get("itemDimension") is not None else None,
            "itemId": obj.get("itemId"),
            "manufacturer": obj.get("manufacturer"),
            "originCountryCode": obj.get("originCountryCode"),
            "quantity": obj.get("quantity"),
            "unitPrice": obj.get("unitPrice"),
            "unitWeight": ParcelWeight.from_dict(obj["unitWeight"]) if obj.get("unitWeight") is not None else None,
            "url": obj.get("url")
        })
        return _obj


