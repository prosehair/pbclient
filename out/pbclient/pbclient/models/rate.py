# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.4
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
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
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Rate(BaseModel):
    """
    Rate
    """
    alternate_base_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="alternateBaseCharge")
    alternate_total_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="alternateTotalCharge")
    base_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="baseCharge")
    base_charge_taxes: Optional[List[Tax]] = Field(default=None, alias="baseChargeTaxes")
    carrier: Carrier
    currency_code: Optional[StrictStr] = Field(default=None, description="ISO-4217", alias="currencyCode")
    delivery_commitment: Optional[DeliveryCommitment] = Field(default=None, alias="deliveryCommitment")
    destination_zone: Optional[RateDestinationZone] = Field(default=None, alias="destinationZone")
    dimensional_weight: Optional[ParcelWeight] = Field(default=None, alias="dimensionalWeight")
    discounts: Optional[List[Discount]] = None
    induction_postal_code: Optional[StrictStr] = Field(default=None, alias="inductionPostalCode")
    parcel_type: ParcelType = Field(alias="parcelType")
    rate_type_id: Optional[StrictStr] = Field(default=None, alias="rateTypeId")
    service_id: Optional[Services] = Field(default=None, alias="serviceId")
    special_services: Optional[List[SpecialService]] = Field(default=None, alias="specialServices")
    surcharges: Optional[List[Surcharge]] = None
    total_carrier_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalCarrierCharge")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalTaxAmount")
    __properties: ClassVar[List[str]] = ["alternateBaseCharge", "alternateTotalCharge", "baseCharge", "baseChargeTaxes", "carrier", "currencyCode", "deliveryCommitment", "destinationZone", "dimensionalWeight", "discounts", "inductionPostalCode", "parcelType", "rateTypeId", "serviceId", "specialServices", "surcharges", "totalCarrierCharge", "totalTaxAmount"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Rate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
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
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Rate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alternateBaseCharge": obj.get("alternateBaseCharge"),
            "alternateTotalCharge": obj.get("alternateTotalCharge"),
            "baseCharge": obj.get("baseCharge"),
            "baseChargeTaxes": [Tax.from_dict(_item) for _item in obj.get("baseChargeTaxes")] if obj.get("baseChargeTaxes") is not None else None,
            "carrier": obj.get("carrier"),
            "currencyCode": obj.get("currencyCode"),
            "deliveryCommitment": DeliveryCommitment.from_dict(obj.get("deliveryCommitment")) if obj.get("deliveryCommitment") is not None else None,
            "destinationZone": RateDestinationZone.from_dict(obj.get("destinationZone")) if obj.get("destinationZone") is not None else None,
            "dimensionalWeight": ParcelWeight.from_dict(obj.get("dimensionalWeight")) if obj.get("dimensionalWeight") is not None else None,
            "discounts": [Discount.from_dict(_item) for _item in obj.get("discounts")] if obj.get("discounts") is not None else None,
            "inductionPostalCode": obj.get("inductionPostalCode"),
            "parcelType": obj.get("parcelType"),
            "rateTypeId": obj.get("rateTypeId"),
            "serviceId": obj.get("serviceId"),
            "specialServices": [SpecialService.from_dict(_item) for _item in obj.get("specialServices")] if obj.get("specialServices") is not None else None,
            "surcharges": [Surcharge.from_dict(_item) for _item in obj.get("surcharges")] if obj.get("surcharges") is not None else None,
            "totalCarrierCharge": obj.get("totalCarrierCharge"),
            "totalTaxAmount": obj.get("totalTaxAmount")
        })
        return _obj


