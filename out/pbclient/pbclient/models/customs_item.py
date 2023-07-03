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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator
from pbclient.models.address import Address
from pbclient.models.parcel_weight import ParcelWeight

class CustomsItem(BaseModel):
    """
    CustomsItem
    """
    description: StrictStr = Field(...)
    h_s_tariff_code: Optional[StrictStr] = Field(None, alias="hSTariffCode")
    net_cost_method: Optional[StrictStr] = Field(None, alias="netCostMethod")
    origin_country_code: StrictStr = Field(..., alias="originCountryCode")
    origin_state_province: Optional[StrictStr] = Field(None, alias="originStateProvince")
    preference_criterion: Optional[StrictStr] = Field(None, alias="preferenceCriterion")
    producer_address: Optional[Address] = Field(None, alias="producerAddress")
    producer_determination: Optional[StrictStr] = Field(None, alias="producerDetermination")
    producer_id: Optional[StrictStr] = Field(None, alias="producerId")
    quantity: StrictInt = Field(...)
    quantity_uom: Optional[StrictStr] = Field(None, alias="quantityUOM")
    unit_price: Union[StrictFloat, StrictInt] = Field(..., alias="unitPrice")
    unit_weight: ParcelWeight = Field(..., alias="unitWeight")
    __properties = ["description", "hSTariffCode", "netCostMethod", "originCountryCode", "originStateProvince", "preferenceCriterion", "producerAddress", "producerDetermination", "producerId", "quantity", "quantityUOM", "unitPrice", "unitWeight"]

    @validator('net_cost_method')
    def net_cost_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NO_NET_COST', 'NET_COST'):
            raise ValueError("must be one of enum values ('NO_NET_COST', 'NET_COST')")
        return value

    @validator('preference_criterion')
    def preference_criterion_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('A', 'B', 'C', 'D', 'E', 'F'):
            raise ValueError("must be one of enum values ('A', 'B', 'C', 'D', 'E', 'F')")
        return value

    @validator('producer_determination')
    def producer_determination_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NO_1', 'NO_2', 'NO_3', 'PD_YES'):
            raise ValueError("must be one of enum values ('NO_1', 'NO_2', 'NO_3', 'PD_YES')")
        return value

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
        # override the default output from pydantic by calling `to_dict()` of producer_address
        if self.producer_address:
            _dict['producerAddress'] = self.producer_address.to_dict()
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
            "h_s_tariff_code": obj.get("hSTariffCode"),
            "net_cost_method": obj.get("netCostMethod"),
            "origin_country_code": obj.get("originCountryCode"),
            "origin_state_province": obj.get("originStateProvince"),
            "preference_criterion": obj.get("preferenceCriterion"),
            "producer_address": Address.from_dict(obj.get("producerAddress")) if obj.get("producerAddress") is not None else None,
            "producer_determination": obj.get("producerDetermination"),
            "producer_id": obj.get("producerId"),
            "quantity": obj.get("quantity"),
            "quantity_uom": obj.get("quantityUOM"),
            "unit_price": obj.get("unitPrice"),
            "unit_weight": ParcelWeight.from_dict(obj.get("unitWeight")) if obj.get("unitWeight") is not None else None
        })
        return _obj

