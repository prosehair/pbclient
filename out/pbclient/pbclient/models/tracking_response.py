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

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from pbclient.models.carrier import Carrier
from pbclient.models.event_object import EventObject
from pbclient.models.tracking_address import TrackingAddress
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TrackingResponse(BaseModel):
    """
    TrackingResponse
    """
    package_count: Optional[StrictInt] = Field(default=None, alias="packageCount")
    carrier: Optional[Carrier] = None
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    status: Optional[StrictStr] = None
    updated_date: Optional[date] = Field(default=None, alias="updatedDate")
    updated_time: Optional[StrictStr] = Field(default=None, alias="updatedTime")
    ship_date: Optional[date] = Field(default=None, alias="shipDate")
    ship_time: Optional[StrictStr] = Field(default=None, alias="shipTime")
    ship_time_offset: Optional[StrictStr] = Field(default=None, alias="shipTimeOffset")
    estimated_delivery_date: Optional[date] = Field(default=None, alias="estimatedDeliveryDate")
    estimated_delivery_time: Optional[StrictStr] = Field(default=None, alias="estimatedDeliveryTime")
    estimated_delivery_time_offset: Optional[StrictStr] = Field(default=None, alias="estimatedDeliveryTimeOffset")
    delivery_date: Optional[date] = Field(default=None, alias="deliveryDate")
    delivery_time: Optional[StrictStr] = Field(default=None, alias="deliveryTime")
    delivery_time_offset: Optional[StrictStr] = Field(default=None, alias="deliveryTimeOffset")
    delivery_location: Optional[StrictStr] = Field(default=None, alias="deliveryLocation")
    delivery_location_description: Optional[StrictStr] = Field(default=None, alias="deliveryLocationDescription")
    signed_by: Optional[StrictStr] = Field(default=None, alias="signedBy")
    weight: Optional[StrictStr] = None
    weight_oum: Optional[StrictStr] = Field(default=None, alias="weightOUM")
    reattempt_date: Optional[date] = Field(default=None, alias="reattemptDate")
    reattempt_time: Optional[StrictStr] = Field(default=None, alias="reattemptTime")
    destination_address: Optional[TrackingAddress] = Field(default=None, alias="destinationAddress")
    sender_address: Optional[TrackingAddress] = Field(default=None, alias="senderAddress")
    current_status: Optional[EventObject] = Field(default=None, alias="currentStatus")
    scan_details_list: Optional[List[EventObject]] = Field(default=None, alias="scanDetailsList")
    __properties: ClassVar[List[str]] = ["packageCount", "carrier", "trackingNumber", "referenceNumber", "status", "updatedDate", "updatedTime", "shipDate", "shipTime", "shipTimeOffset", "estimatedDeliveryDate", "estimatedDeliveryTime", "estimatedDeliveryTimeOffset", "deliveryDate", "deliveryTime", "deliveryTimeOffset", "deliveryLocation", "deliveryLocationDescription", "signedBy", "weight", "weightOUM", "reattemptDate", "reattemptTime", "destinationAddress", "senderAddress", "currentStatus", "scanDetailsList"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Acceptance', 'Delivered', 'DeliveryAttempt', 'Exception', 'InTransit', 'Manifest', 'OutForDelivery', 'PickedUp', 'PickupMissed', 'ReadyForPickup', 'ReturnToSender'):
            raise ValueError("must be one of enum values ('Acceptance', 'Delivered', 'DeliveryAttempt', 'Exception', 'InTransit', 'Manifest', 'OutForDelivery', 'PickedUp', 'PickupMissed', 'ReadyForPickup', 'ReturnToSender')")
        return value

    @field_validator('weight_oum')
    def weight_oum_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('lb', 'LBS', 'Pounds', 'KGS'):
            raise ValueError("must be one of enum values ('lb', 'LBS', 'Pounds', 'KGS')")
        return value

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
        """Create an instance of TrackingResponse from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of TrackingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "packageCount": obj.get("packageCount"),
            "carrier": obj.get("carrier"),
            "trackingNumber": obj.get("trackingNumber"),
            "referenceNumber": obj.get("referenceNumber"),
            "status": obj.get("status"),
            "updatedDate": obj.get("updatedDate"),
            "updatedTime": obj.get("updatedTime"),
            "shipDate": obj.get("shipDate"),
            "shipTime": obj.get("shipTime"),
            "shipTimeOffset": obj.get("shipTimeOffset"),
            "estimatedDeliveryDate": obj.get("estimatedDeliveryDate"),
            "estimatedDeliveryTime": obj.get("estimatedDeliveryTime"),
            "estimatedDeliveryTimeOffset": obj.get("estimatedDeliveryTimeOffset"),
            "deliveryDate": obj.get("deliveryDate"),
            "deliveryTime": obj.get("deliveryTime"),
            "deliveryTimeOffset": obj.get("deliveryTimeOffset"),
            "deliveryLocation": obj.get("deliveryLocation"),
            "deliveryLocationDescription": obj.get("deliveryLocationDescription"),
            "signedBy": obj.get("signedBy"),
            "weight": obj.get("weight"),
            "weightOUM": obj.get("weightOUM"),
            "reattemptDate": obj.get("reattemptDate"),
            "reattemptTime": obj.get("reattemptTime"),
            "destinationAddress": TrackingAddress.from_dict(obj.get("destinationAddress")) if obj.get("destinationAddress") is not None else None,
            "senderAddress": TrackingAddress.from_dict(obj.get("senderAddress")) if obj.get("senderAddress") is not None else None,
            "currentStatus": EventObject.from_dict(obj.get("currentStatus")) if obj.get("currentStatus") is not None else None,
            "scanDetailsList": [EventObject.from_dict(_item) for _item in obj.get("scanDetailsList")] if obj.get("scanDetailsList") is not None else None
        })
        return _obj


