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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from pbclient.models.battery_details import BatteryDetails
from pbclient.models.container_details import ContainerDetails
from pbclient.models.signatory import Signatory

class HazmatDetails(BaseModel):
    """
    HazmatDetails
    """
    battery_details: Optional[BatteryDetails] = Field(None, alias="batteryDetails")
    commodity_type: Optional[StrictStr] = Field(None, alias="commodityType")
    container_count: Optional[StrictInt] = Field(None, alias="containerCount")
    container_details: Optional[conlist(ContainerDetails)] = Field(None, alias="containerDetails")
    emergency_contact_number: Optional[StrictStr] = Field(None, alias="emergencyContactNumber")
    hazmat_document_type: Optional[StrictStr] = Field(None, alias="hazmatDocumentType")
    identical_containers: Optional[StrictBool] = Field(None, alias="identicalContainers")
    offeror: Optional[StrictStr] = None
    packaging_option: Optional[StrictStr] = Field(None, alias="packagingOption")
    signatory: Optional[Signatory] = None
    __properties = ["batteryDetails", "commodityType", "containerCount", "containerDetails", "emergencyContactNumber", "hazmatDocumentType", "identicalContainers", "offeror", "packagingOption", "signatory"]

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
    def from_json(cls, json_str: str) -> HazmatDetails:
        """Create an instance of HazmatDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of battery_details
        if self.battery_details:
            _dict['batteryDetails'] = self.battery_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in container_details (list)
        _items = []
        if self.container_details:
            for _item in self.container_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['containerDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of signatory
        if self.signatory:
            _dict['signatory'] = self.signatory.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HazmatDetails:
        """Create an instance of HazmatDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HazmatDetails.parse_obj(obj)

        _obj = HazmatDetails.parse_obj({
            "battery_details": BatteryDetails.from_dict(obj.get("batteryDetails")) if obj.get("batteryDetails") is not None else None,
            "commodity_type": obj.get("commodityType"),
            "container_count": obj.get("containerCount"),
            "container_details": [ContainerDetails.from_dict(_item) for _item in obj.get("containerDetails")] if obj.get("containerDetails") is not None else None,
            "emergency_contact_number": obj.get("emergencyContactNumber"),
            "hazmat_document_type": obj.get("hazmatDocumentType"),
            "identical_containers": obj.get("identicalContainers"),
            "offeror": obj.get("offeror"),
            "packaging_option": obj.get("packagingOption"),
            "signatory": Signatory.from_dict(obj.get("signatory")) if obj.get("signatory") is not None else None
        })
        return _obj


