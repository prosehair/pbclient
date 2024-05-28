# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.13
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from pbclient.models.address import Address
from pbclient.models.carrier import Carrier
from pbclient.models.schedule_pickup_pickup_summary_inner import SchedulePickupPickupSummaryInner

class SchedulePickupResponse(BaseModel):
    """
    SchedulePickupResponse
    """
    pickup_address: Optional[Address] = Field(None, alias="pickupAddress")
    carrier: Optional[Carrier] = None
    pickup_summary: Optional[conlist(SchedulePickupPickupSummaryInner)] = Field(None, alias="pickupSummary")
    reference: Optional[StrictStr] = None
    package_location: Optional[StrictStr] = Field(None, alias="packageLocation")
    special_instructions: Optional[StrictStr] = Field(None, alias="specialInstructions")
    pickup_date_time: Optional[StrictStr] = Field(None, alias="pickupDateTime")
    pickup_confirmation_number: Optional[StrictStr] = Field(None, alias="pickupConfirmationNumber")
    pickup_id: Optional[StrictStr] = Field(None, alias="pickupId")
    __properties = ["pickupAddress", "carrier", "pickupSummary", "reference", "packageLocation", "specialInstructions", "pickupDateTime", "pickupConfirmationNumber", "pickupId"]

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
    def from_json(cls, json_str: str) -> SchedulePickupResponse:
        """Create an instance of SchedulePickupResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pickup_address
        if self.pickup_address:
            _dict['pickupAddress'] = self.pickup_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pickup_summary (list)
        _items = []
        if self.pickup_summary:
            for _item in self.pickup_summary:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pickupSummary'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SchedulePickupResponse:
        """Create an instance of SchedulePickupResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SchedulePickupResponse.parse_obj(obj)

        _obj = SchedulePickupResponse.parse_obj({
            "pickup_address": Address.from_dict(obj.get("pickupAddress")) if obj.get("pickupAddress") is not None else None,
            "carrier": obj.get("carrier"),
            "pickup_summary": [SchedulePickupPickupSummaryInner.from_dict(_item) for _item in obj.get("pickupSummary")] if obj.get("pickupSummary") is not None else None,
            "reference": obj.get("reference"),
            "package_location": obj.get("packageLocation"),
            "special_instructions": obj.get("specialInstructions"),
            "pickup_date_time": obj.get("pickupDateTime"),
            "pickup_confirmation_number": obj.get("pickupConfirmationNumber"),
            "pickup_id": obj.get("pickupId")
        })
        return _obj


