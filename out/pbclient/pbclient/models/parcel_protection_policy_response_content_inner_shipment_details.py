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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from pbclient.models.carrier import Carrier

class ParcelProtectionPolicyResponseContentInnerShipmentDetails(BaseModel):
    """
    ParcelProtectionPolicyResponseContentInnerShipmentDetails
    """
    shipment_date: Optional[StrictStr] = Field(None, alias="shipmentDate")
    shipment_transaction_id: Optional[StrictStr] = Field(None, alias="shipmentTransactionId")
    shipment_id: Optional[StrictStr] = Field(None, alias="shipmentId")
    parcel_tracking_number: Optional[StrictStr] = Field(None, alias="parcelTrackingNumber")
    carrier: Optional[Carrier] = None
    amount: Optional[StrictStr] = None
    package_length: Optional[StrictStr] = Field(None, alias="packageLength")
    package_width: Optional[StrictStr] = Field(None, alias="packageWidth")
    package_height: Optional[StrictStr] = Field(None, alias="packageHeight")
    weight: Optional[StrictStr] = None
    zone: Optional[StrictStr] = None
    __properties = ["shipmentDate", "shipmentTransactionId", "shipmentId", "parcelTrackingNumber", "carrier", "amount", "packageLength", "packageWidth", "packageHeight", "weight", "zone"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionPolicyResponseContentInnerShipmentDetails:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipmentDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionPolicyResponseContentInnerShipmentDetails:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipmentDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionPolicyResponseContentInnerShipmentDetails.parse_obj(obj)

        _obj = ParcelProtectionPolicyResponseContentInnerShipmentDetails.parse_obj({
            "shipment_date": obj.get("shipmentDate"),
            "shipment_transaction_id": obj.get("shipmentTransactionId"),
            "shipment_id": obj.get("shipmentId"),
            "parcel_tracking_number": obj.get("parcelTrackingNumber"),
            "carrier": obj.get("carrier"),
            "amount": obj.get("amount"),
            "package_length": obj.get("packageLength"),
            "package_width": obj.get("packageWidth"),
            "package_height": obj.get("packageHeight"),
            "weight": obj.get("weight"),
            "zone": obj.get("zone")
        })
        return _obj

