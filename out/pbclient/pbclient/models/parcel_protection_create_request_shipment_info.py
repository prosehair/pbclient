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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from pbclient.models.carrier import Carrier
from pbclient.models.parcel_protection_create_request_shipment_info_consignee_info import ParcelProtectionCreateRequestShipmentInfoConsigneeInfo
from pbclient.models.parcel_protection_create_request_shipment_info_parcel_info import ParcelProtectionCreateRequestShipmentInfoParcelInfo
from pbclient.models.parcel_protection_create_request_shipment_info_shipper_info import ParcelProtectionCreateRequestShipmentInfoShipperInfo

class ParcelProtectionCreateRequestShipmentInfo(BaseModel):
    """
    ParcelProtectionCreateRequestShipmentInfo
    """
    tracking_number: Optional[StrictStr] = Field(None, alias="trackingNumber")
    carrier: Optional[Carrier] = None
    service_id: Optional[StrictStr] = Field(None, alias="serviceId")
    insurance_coverage_value: Optional[StrictInt] = Field(None, alias="insuranceCoverageValue")
    insurance_coverage_value_currency: Optional[StrictStr] = Field(None, alias="insuranceCoverageValueCurrency")
    parcel_info: Optional[ParcelProtectionCreateRequestShipmentInfoParcelInfo] = Field(None, alias="parcelInfo")
    shipper_info: Optional[ParcelProtectionCreateRequestShipmentInfoShipperInfo] = Field(None, alias="shipperInfo")
    consignee_info: Optional[ParcelProtectionCreateRequestShipmentInfoConsigneeInfo] = Field(None, alias="consigneeInfo")
    __properties = ["trackingNumber", "carrier", "serviceId", "insuranceCoverageValue", "insuranceCoverageValueCurrency", "parcelInfo", "shipperInfo", "consigneeInfo"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionCreateRequestShipmentInfo:
        """Create an instance of ParcelProtectionCreateRequestShipmentInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parcel_info
        if self.parcel_info:
            _dict['parcelInfo'] = self.parcel_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipper_info
        if self.shipper_info:
            _dict['shipperInfo'] = self.shipper_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of consignee_info
        if self.consignee_info:
            _dict['consigneeInfo'] = self.consignee_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionCreateRequestShipmentInfo:
        """Create an instance of ParcelProtectionCreateRequestShipmentInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionCreateRequestShipmentInfo.parse_obj(obj)

        _obj = ParcelProtectionCreateRequestShipmentInfo.parse_obj({
            "tracking_number": obj.get("trackingNumber"),
            "carrier": obj.get("carrier"),
            "service_id": obj.get("serviceId"),
            "insurance_coverage_value": obj.get("insuranceCoverageValue"),
            "insurance_coverage_value_currency": obj.get("insuranceCoverageValueCurrency"),
            "parcel_info": ParcelProtectionCreateRequestShipmentInfoParcelInfo.from_dict(obj.get("parcelInfo")) if obj.get("parcelInfo") is not None else None,
            "shipper_info": ParcelProtectionCreateRequestShipmentInfoShipperInfo.from_dict(obj.get("shipperInfo")) if obj.get("shipperInfo") is not None else None,
            "consignee_info": ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.from_dict(obj.get("consigneeInfo")) if obj.get("consigneeInfo") is not None else None
        })
        return _obj


