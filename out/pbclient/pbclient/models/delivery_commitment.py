# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.3
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

class DeliveryCommitment(BaseModel):
    """
    DeliveryCommitment
    """
    additional_details: Optional[StrictStr] = Field(None, alias="additionalDetails")
    estimated_delivery_date_time: Optional[StrictStr] = Field(None, alias="estimatedDeliveryDateTime")
    guarantee: Optional[StrictStr] = None
    max_estimated_number_of_days: Optional[StrictStr] = Field(None, alias="maxEstimatedNumberOfDays")
    min_estimated_number_of_days: Optional[StrictStr] = Field(None, alias="minEstimatedNumberOfDays")
    __properties = ["additionalDetails", "estimatedDeliveryDateTime", "guarantee", "maxEstimatedNumberOfDays", "minEstimatedNumberOfDays"]

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
    def from_json(cls, json_str: str) -> DeliveryCommitment:
        """Create an instance of DeliveryCommitment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeliveryCommitment:
        """Create an instance of DeliveryCommitment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeliveryCommitment.parse_obj(obj)

        _obj = DeliveryCommitment.parse_obj({
            "additional_details": obj.get("additionalDetails"),
            "estimated_delivery_date_time": obj.get("estimatedDeliveryDateTime"),
            "guarantee": obj.get("guarantee"),
            "max_estimated_number_of_days": obj.get("maxEstimatedNumberOfDays"),
            "min_estimated_number_of_days": obj.get("minEstimatedNumberOfDays")
        })
        return _obj

