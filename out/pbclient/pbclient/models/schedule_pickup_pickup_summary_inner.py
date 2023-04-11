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
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from pbclient.models.schedule_pickup_pickup_summary_inner_total_weight import SchedulePickupPickupSummaryInnerTotalWeight

class SchedulePickupPickupSummaryInner(BaseModel):
    """
    SchedulePickupPickupSummaryInner
    """
    service_id: Optional[StrictStr] = Field(None, alias="serviceId")
    count: Optional[StrictInt] = None
    total_weight: Optional[SchedulePickupPickupSummaryInnerTotalWeight] = Field(None, alias="totalWeight")
    __properties = ["serviceId", "count", "totalWeight"]

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
    def from_json(cls, json_str: str) -> SchedulePickupPickupSummaryInner:
        """Create an instance of SchedulePickupPickupSummaryInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of total_weight
        if self.total_weight:
            _dict['totalWeight'] = self.total_weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SchedulePickupPickupSummaryInner:
        """Create an instance of SchedulePickupPickupSummaryInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SchedulePickupPickupSummaryInner.parse_obj(obj)

        _obj = SchedulePickupPickupSummaryInner.parse_obj({
            "service_id": obj.get("serviceId"),
            "count": obj.get("count"),
            "total_weight": SchedulePickupPickupSummaryInnerTotalWeight.from_dict(obj.get("totalWeight")) if obj.get("totalWeight") is not None else None
        })
        return _obj

