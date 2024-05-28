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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from pbclient.models.additional_address import AdditionalAddress
from pbclient.models.address import Address
from pbclient.models.carrier_payment import CarrierPayment
from pbclient.models.customs import Customs
from pbclient.models.document import Document
from pbclient.models.hazmat_details import HazmatDetails
from pbclient.models.parameter import Parameter
from pbclient.models.parcel import Parcel
from pbclient.models.rate import Rate

class Shipment(BaseModel):
    """
    Shipment
    """
    additional_addresses: Optional[conlist(AdditionalAddress)] = Field(None, alias="additionalAddresses")
    alt_return_address: Optional[Address] = Field(None, alias="altReturnAddress")
    carrier_payments: Optional[conlist(CarrierPayment)] = Field(None, alias="carrierPayments")
    customs: Optional[Customs] = None
    documents: Optional[conlist(Document)] = None
    from_address: Address = Field(..., alias="fromAddress")
    hazmat_details: Optional[HazmatDetails] = Field(None, alias="hazmatDetails")
    parcel: Parcel = Field(...)
    parcel_tracking_number: Optional[StrictStr] = Field(None, alias="parcelTrackingNumber")
    rates: conlist(Rate) = Field(...)
    references: Optional[conlist(Parameter)] = None
    shipment_id: Optional[StrictStr] = Field(None, alias="shipmentId")
    shipment_options: Optional[conlist(Parameter)] = Field(None, alias="shipmentOptions")
    shipment_type: Optional[StrictStr] = Field(None, alias="shipmentType")
    sold_to_address: Optional[Address] = Field(None, alias="soldToAddress")
    to_address: Address = Field(..., alias="toAddress")
    __properties = ["additionalAddresses", "altReturnAddress", "carrierPayments", "customs", "documents", "fromAddress", "hazmatDetails", "parcel", "parcelTrackingNumber", "rates", "references", "shipmentId", "shipmentOptions", "shipmentType", "soldToAddress", "toAddress"]

    @validator('shipment_type')
    def shipment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('OUTBOUND', 'RETURN'):
            raise ValueError("must be one of enum values ('OUTBOUND', 'RETURN')")
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
    def from_json(cls, json_str: str) -> Shipment:
        """Create an instance of Shipment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in additional_addresses (list)
        _items = []
        if self.additional_addresses:
            for _item in self.additional_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAddresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of alt_return_address
        if self.alt_return_address:
            _dict['altReturnAddress'] = self.alt_return_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in carrier_payments (list)
        _items = []
        if self.carrier_payments:
            for _item in self.carrier_payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['carrierPayments'] = _items
        # override the default output from pydantic by calling `to_dict()` of customs
        if self.customs:
            _dict['customs'] = self.customs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item in self.documents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of from_address
        if self.from_address:
            _dict['fromAddress'] = self.from_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hazmat_details
        if self.hazmat_details:
            _dict['hazmatDetails'] = self.hazmat_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parcel
        if self.parcel:
            _dict['parcel'] = self.parcel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rates (list)
        _items = []
        if self.rates:
            for _item in self.rates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in references (list)
        _items = []
        if self.references:
            for _item in self.references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['references'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipment_options (list)
        _items = []
        if self.shipment_options:
            for _item in self.shipment_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipmentOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of sold_to_address
        if self.sold_to_address:
            _dict['soldToAddress'] = self.sold_to_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_address
        if self.to_address:
            _dict['toAddress'] = self.to_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Shipment:
        """Create an instance of Shipment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Shipment.parse_obj(obj)

        _obj = Shipment.parse_obj({
            "additional_addresses": [AdditionalAddress.from_dict(_item) for _item in obj.get("additionalAddresses")] if obj.get("additionalAddresses") is not None else None,
            "alt_return_address": Address.from_dict(obj.get("altReturnAddress")) if obj.get("altReturnAddress") is not None else None,
            "carrier_payments": [CarrierPayment.from_dict(_item) for _item in obj.get("carrierPayments")] if obj.get("carrierPayments") is not None else None,
            "customs": Customs.from_dict(obj.get("customs")) if obj.get("customs") is not None else None,
            "documents": [Document.from_dict(_item) for _item in obj.get("documents")] if obj.get("documents") is not None else None,
            "from_address": Address.from_dict(obj.get("fromAddress")) if obj.get("fromAddress") is not None else None,
            "hazmat_details": HazmatDetails.from_dict(obj.get("hazmatDetails")) if obj.get("hazmatDetails") is not None else None,
            "parcel": Parcel.from_dict(obj.get("parcel")) if obj.get("parcel") is not None else None,
            "parcel_tracking_number": obj.get("parcelTrackingNumber"),
            "rates": [Rate.from_dict(_item) for _item in obj.get("rates")] if obj.get("rates") is not None else None,
            "references": [Parameter.from_dict(_item) for _item in obj.get("references")] if obj.get("references") is not None else None,
            "shipment_id": obj.get("shipmentId"),
            "shipment_options": [Parameter.from_dict(_item) for _item in obj.get("shipmentOptions")] if obj.get("shipmentOptions") is not None else None,
            "shipment_type": obj.get("shipmentType"),
            "sold_to_address": Address.from_dict(obj.get("soldToAddress")) if obj.get("soldToAddress") is not None else None,
            "to_address": Address.from_dict(obj.get("toAddress")) if obj.get("toAddress") is not None else None
        })
        return _obj


