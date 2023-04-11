# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from pbclient.models.carrier import Carrier
from pbclient.models.event_object import EventObject
from pbclient.models.tracking_address import TrackingAddress

class TrackingResponse(BaseModel):
    """
    TrackingResponse
    """
    package_count: Optional[StrictInt] = Field(None, alias="packageCount")
    carrier: Optional[Carrier] = None
    tracking_number: Optional[StrictStr] = Field(None, alias="trackingNumber")
    reference_number: Optional[StrictStr] = Field(None, alias="referenceNumber")
    status: Optional[StrictStr] = None
    updated_date: Optional[date] = Field(None, alias="updatedDate")
    updated_time: Optional[StrictStr] = Field(None, alias="updatedTime")
    ship_date: Optional[date] = Field(None, alias="shipDate")
    ship_time: Optional[StrictStr] = Field(None, alias="shipTime")
    ship_time_offset: Optional[StrictStr] = Field(None, alias="shipTimeOffset")
    estimated_delivery_date: Optional[date] = Field(None, alias="estimatedDeliveryDate")
    estimated_delivery_time: Optional[StrictStr] = Field(None, alias="estimatedDeliveryTime")
    estimated_delivery_time_offset: Optional[StrictStr] = Field(None, alias="estimatedDeliveryTimeOffset")
    delivery_date: Optional[date] = Field(None, alias="deliveryDate")
    delivery_time: Optional[StrictStr] = Field(None, alias="deliveryTime")
    delivery_time_offset: Optional[StrictStr] = Field(None, alias="deliveryTimeOffset")
    delivery_location: Optional[StrictStr] = Field(None, alias="deliveryLocation")
    delivery_location_description: Optional[StrictStr] = Field(None, alias="deliveryLocationDescription")
    signed_by: Optional[StrictStr] = Field(None, alias="signedBy")
    weight: Optional[StrictInt] = None
    weight_oum: Optional[StrictStr] = Field(None, alias="weightOUM")
    reattempt_date: Optional[date] = Field(None, alias="reattemptDate")
    reattempt_time: Optional[StrictStr] = Field(None, alias="reattemptTime")
    destination_address: Optional[TrackingAddress] = Field(None, alias="destinationAddress")
    sender_address: Optional[TrackingAddress] = Field(None, alias="senderAddress")
    current_status: Optional[EventObject] = Field(None, alias="currentStatus")
    scan_details_list: Optional[conlist(EventObject)] = Field(None, alias="scanDetailsList")
    __properties = ["packageCount", "carrier", "trackingNumber", "referenceNumber", "status", "updatedDate", "updatedTime", "shipDate", "shipTime", "shipTimeOffset", "estimatedDeliveryDate", "estimatedDeliveryTime", "estimatedDeliveryTimeOffset", "deliveryDate", "deliveryTime", "deliveryTimeOffset", "deliveryLocation", "deliveryLocationDescription", "signedBy", "weight", "weightOUM", "reattemptDate", "reattemptTime", "destinationAddress", "senderAddress", "currentStatus", "scanDetailsList"]

    @validator('status')
    def status_validate_enum(cls, v):
        if v is None:
            return v
        if v not in ('Acceptance', 'Delivered', 'DeliveryAttempt', 'Exception', 'InTransit', 'Manifest', 'OutForDelivery', 'PickedUp', 'PickupMissed', 'ReadyForPickup', 'ReturnToSender'):
            raise ValueError("must be one of enum values ('Acceptance', 'Delivered', 'DeliveryAttempt', 'Exception', 'InTransit', 'Manifest', 'OutForDelivery', 'PickedUp', 'PickupMissed', 'ReadyForPickup', 'ReturnToSender')")
        return v

    @validator('weight_oum')
    def weight_oum_validate_enum(cls, v):
        if v is None:
            return v
        if v not in ('lb', 'LBS', 'Pounds', 'KGS'):
            raise ValueError("must be one of enum values ('lb', 'LBS', 'Pounds', 'KGS')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TrackingResponse:
        """Create an instance of TrackingResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of destination_address
        if self.destination_address:
            _dict['destinationAddress'] = self.destination_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender_address
        if self.sender_address:
            _dict['senderAddress'] = self.sender_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_status
        if self.current_status:
            _dict['currentStatus'] = self.current_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in scan_details_list (list)
        _items = []
        if self.scan_details_list:
            for _item in self.scan_details_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scanDetailsList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackingResponse:
        """Create an instance of TrackingResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TrackingResponse.parse_obj(obj)

        _obj = TrackingResponse.parse_obj({
            "package_count": obj.get("packageCount"),
            "carrier": obj.get("carrier"),
            "tracking_number": obj.get("trackingNumber"),
            "reference_number": obj.get("referenceNumber"),
            "status": obj.get("status"),
            "updated_date": obj.get("updatedDate"),
            "updated_time": obj.get("updatedTime"),
            "ship_date": obj.get("shipDate"),
            "ship_time": obj.get("shipTime"),
            "ship_time_offset": obj.get("shipTimeOffset"),
            "estimated_delivery_date": obj.get("estimatedDeliveryDate"),
            "estimated_delivery_time": obj.get("estimatedDeliveryTime"),
            "estimated_delivery_time_offset": obj.get("estimatedDeliveryTimeOffset"),
            "delivery_date": obj.get("deliveryDate"),
            "delivery_time": obj.get("deliveryTime"),
            "delivery_time_offset": obj.get("deliveryTimeOffset"),
            "delivery_location": obj.get("deliveryLocation"),
            "delivery_location_description": obj.get("deliveryLocationDescription"),
            "signed_by": obj.get("signedBy"),
            "weight": obj.get("weight"),
            "weight_oum": obj.get("weightOUM"),
            "reattempt_date": obj.get("reattemptDate"),
            "reattempt_time": obj.get("reattemptTime"),
            "destination_address": TrackingAddress.from_dict(obj.get("destinationAddress")) if obj.get("destinationAddress") is not None else None,
            "sender_address": TrackingAddress.from_dict(obj.get("senderAddress")) if obj.get("senderAddress") is not None else None,
            "current_status": EventObject.from_dict(obj.get("currentStatus")) if obj.get("currentStatus") is not None else None,
            "scan_details_list": [EventObject.from_dict(_item) for _item in obj.get("scanDetailsList")] if obj.get("scanDetailsList") is not None else None
        })
        return _obj

