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



from pydantic import BaseModel, Field, StrictStr

class SchedulePickupPickupSummaryInnerTotalWeight(BaseModel):
    """
    SchedulePickupPickupSummaryInnerTotalWeight
    """
    unit_of_measurement: StrictStr = Field(..., alias="unitOfMeasurement")
    weight: StrictStr = Field(...)
    __properties = ["unitOfMeasurement", "weight"]

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
    def from_json(cls, json_str: str) -> SchedulePickupPickupSummaryInnerTotalWeight:
        """Create an instance of SchedulePickupPickupSummaryInnerTotalWeight from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SchedulePickupPickupSummaryInnerTotalWeight:
        """Create an instance of SchedulePickupPickupSummaryInnerTotalWeight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SchedulePickupPickupSummaryInnerTotalWeight.parse_obj(obj)

        _obj = SchedulePickupPickupSummaryInnerTotalWeight.parse_obj({
            "unit_of_measurement": obj.get("unitOfMeasurement"),
            "weight": obj.get("weight")
        })
        return _obj


