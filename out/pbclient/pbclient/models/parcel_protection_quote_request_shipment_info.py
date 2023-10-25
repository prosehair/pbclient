# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.5
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from pbclient.models.carrier import Carrier
from pbclient.models.parcel_protection_quote_request_shipment_info_consignee_info import ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo
from pbclient.models.parcel_protection_quote_request_shipment_info_parcel_info import ParcelProtectionQuoteRequestShipmentInfoParcelInfo
from pbclient.models.parcel_protection_quote_request_shipment_info_shipper_info import ParcelProtectionQuoteRequestShipmentInfoShipperInfo
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ParcelProtectionQuoteRequestShipmentInfo(BaseModel):
    """
    ParcelProtectionQuoteRequestShipmentInfo
    """
    carrier: Carrier
    service_id: StrictStr = Field(alias="serviceId")
    insurance_coverage_value: StrictInt = Field(alias="insuranceCoverageValue")
    insurance_coverage_value_currency: StrictStr = Field(alias="insuranceCoverageValueCurrency")
    parcel_info: ParcelProtectionQuoteRequestShipmentInfoParcelInfo = Field(alias="parcelInfo")
    shipper_info: ParcelProtectionQuoteRequestShipmentInfoShipperInfo = Field(alias="shipperInfo")
    consignee_info: ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo = Field(alias="consigneeInfo")
    __properties: ClassVar[List[str]] = ["carrier", "serviceId", "insuranceCoverageValue", "insuranceCoverageValueCurrency", "parcelInfo", "shipperInfo", "consigneeInfo"]

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
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfo from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ParcelProtectionQuoteRequestShipmentInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrier": obj.get("carrier"),
            "serviceId": obj.get("serviceId"),
            "insuranceCoverageValue": obj.get("insuranceCoverageValue"),
            "insuranceCoverageValueCurrency": obj.get("insuranceCoverageValueCurrency"),
            "parcelInfo": ParcelProtectionQuoteRequestShipmentInfoParcelInfo.from_dict(obj.get("parcelInfo")) if obj.get("parcelInfo") is not None else None,
            "shipperInfo": ParcelProtectionQuoteRequestShipmentInfoShipperInfo.from_dict(obj.get("shipperInfo")) if obj.get("shipperInfo") is not None else None,
            "consigneeInfo": ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo.from_dict(obj.get("consigneeInfo")) if obj.get("consigneeInfo") is not None else None
        })
        return _obj


