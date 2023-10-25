# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.11
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
from pbclient.models.carrier import Carrier
from pbclient.models.delivery_commitment import DeliveryCommitment
from pbclient.models.discount import Discount
from pbclient.models.parcel_type import ParcelType
from pbclient.models.parcel_weight import ParcelWeight
from pbclient.models.rate_destination_zone import RateDestinationZone
from pbclient.models.services import Services
from pbclient.models.special_service import SpecialService
from pbclient.models.surcharge import Surcharge
from pbclient.models.tax import Tax

class Rate(BaseModel):
    """
    Rate
    """
    alternate_base_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="alternateBaseCharge")
    alternate_total_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="alternateTotalCharge")
    base_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="baseCharge")
    base_charge_taxes: Optional[conlist(Tax)] = Field(None, alias="baseChargeTaxes")
    carrier: Carrier = Field(...)
    currency_code: Optional[StrictStr] = Field(None, alias="currencyCode", description="ISO-4217")
    delivery_commitment: Optional[DeliveryCommitment] = Field(None, alias="deliveryCommitment")
    destination_zone: Optional[RateDestinationZone] = Field(None, alias="destinationZone")
    dimensional_weight: Optional[ParcelWeight] = Field(None, alias="dimensionalWeight")
    discounts: Optional[conlist(Discount)] = None
    induction_postal_code: Optional[StrictStr] = Field(None, alias="inductionPostalCode")
    parcel_type: ParcelType = Field(..., alias="parcelType")
    rate_type_id: Optional[StrictStr] = Field(None, alias="rateTypeId")
    service_id: Optional[Services] = Field(None, alias="serviceId")
    special_services: Optional[conlist(SpecialService)] = Field(None, alias="specialServices")
    surcharges: Optional[conlist(Surcharge)] = None
    total_carrier_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalCarrierCharge")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalTaxAmount")
    __properties = ["alternateBaseCharge", "alternateTotalCharge", "baseCharge", "baseChargeTaxes", "carrier", "currencyCode", "deliveryCommitment", "destinationZone", "dimensionalWeight", "discounts", "inductionPostalCode", "parcelType", "rateTypeId", "serviceId", "specialServices", "surcharges", "totalCarrierCharge", "totalTaxAmount"]

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
    def from_json(cls, json_str: str) -> Rate:
        """Create an instance of Rate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in base_charge_taxes (list)
        _items = []
        if self.base_charge_taxes:
            for _item in self.base_charge_taxes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['baseChargeTaxes'] = _items
        # override the default output from pydantic by calling `to_dict()` of delivery_commitment
        if self.delivery_commitment:
            _dict['deliveryCommitment'] = self.delivery_commitment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_zone
        if self.destination_zone:
            _dict['destinationZone'] = self.destination_zone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimensional_weight
        if self.dimensional_weight:
            _dict['dimensionalWeight'] = self.dimensional_weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in discounts (list)
        _items = []
        if self.discounts:
            for _item in self.discounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['discounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in special_services (list)
        _items = []
        if self.special_services:
            for _item in self.special_services:
                if _item:
                    _items.append(_item.to_dict())
            _dict['specialServices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in surcharges (list)
        _items = []
        if self.surcharges:
            for _item in self.surcharges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['surcharges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Rate:
        """Create an instance of Rate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Rate.parse_obj(obj)

        _obj = Rate.parse_obj({
            "alternate_base_charge": obj.get("alternateBaseCharge"),
            "alternate_total_charge": obj.get("alternateTotalCharge"),
            "base_charge": obj.get("baseCharge"),
            "base_charge_taxes": [Tax.from_dict(_item) for _item in obj.get("baseChargeTaxes")] if obj.get("baseChargeTaxes") is not None else None,
            "carrier": obj.get("carrier"),
            "currency_code": obj.get("currencyCode"),
            "delivery_commitment": DeliveryCommitment.from_dict(obj.get("deliveryCommitment")) if obj.get("deliveryCommitment") is not None else None,
            "destination_zone": RateDestinationZone.from_dict(obj.get("destinationZone")) if obj.get("destinationZone") is not None else None,
            "dimensional_weight": ParcelWeight.from_dict(obj.get("dimensionalWeight")) if obj.get("dimensionalWeight") is not None else None,
            "discounts": [Discount.from_dict(_item) for _item in obj.get("discounts")] if obj.get("discounts") is not None else None,
            "induction_postal_code": obj.get("inductionPostalCode"),
            "parcel_type": obj.get("parcelType"),
            "rate_type_id": obj.get("rateTypeId"),
            "service_id": obj.get("serviceId"),
            "special_services": [SpecialService.from_dict(_item) for _item in obj.get("specialServices")] if obj.get("specialServices") is not None else None,
            "surcharges": [Surcharge.from_dict(_item) for _item in obj.get("surcharges")] if obj.get("surcharges") is not None else None,
            "total_carrier_charge": obj.get("totalCarrierCharge"),
            "total_tax_amount": obj.get("totalTaxAmount")
        })
        return _obj


