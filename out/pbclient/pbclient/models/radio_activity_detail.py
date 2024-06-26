# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.14
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from pbclient.models.radio_active_parcel_dimension import RadioActiveParcelDimension

class RadioActivityDetail(BaseModel):
    """
    RadioActivityDetail
    """
    criticality_safety_index: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="criticalitySafetyIndex")
    radio_active_parcel_dimension: Optional[RadioActiveParcelDimension] = Field(None, alias="radioActiveParcelDimension")
    surface_reading: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="surfaceReading")
    transport_index: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="transportIndex")
    __properties = ["criticalitySafetyIndex", "radioActiveParcelDimension", "surfaceReading", "transportIndex"]

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
    def from_json(cls, json_str: str) -> RadioActivityDetail:
        """Create an instance of RadioActivityDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of radio_active_parcel_dimension
        if self.radio_active_parcel_dimension:
            _dict['radioActiveParcelDimension'] = self.radio_active_parcel_dimension.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RadioActivityDetail:
        """Create an instance of RadioActivityDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RadioActivityDetail.parse_obj(obj)

        _obj = RadioActivityDetail.parse_obj({
            "criticality_safety_index": obj.get("criticalitySafetyIndex"),
            "radio_active_parcel_dimension": RadioActiveParcelDimension.from_dict(obj.get("radioActiveParcelDimension")) if obj.get("radioActiveParcelDimension") is not None else None,
            "surface_reading": obj.get("surfaceReading"),
            "transport_index": obj.get("transportIndex")
        })
        return _obj


