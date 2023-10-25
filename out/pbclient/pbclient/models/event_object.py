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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class EventObject(BaseModel):
    """
    EventObject
    """
    standardized_event_code: Optional[StrictStr] = Field(None, alias="standardizedEventCode")
    l1_code: Optional[StrictStr] = Field(None, alias="l1Code")
    l1_description: Optional[StrictStr] = Field(None, alias="l1Description")
    event_date: Optional[date] = Field(None, alias="eventDate")
    event_time: Optional[StrictStr] = Field(None, alias="eventTime")
    event_time_offset: Optional[StrictStr] = Field(None, alias="eventTimeOffset")
    tracking_url: Optional[StrictStr] = Field(None, alias="trackingUrl")
    latitude: Optional[StrictStr] = None
    longitude: Optional[StrictStr] = None
    location_unit: Optional[StrictStr] = Field(None, alias="locationUnit")
    event_leg: Optional[StrictStr] = Field(None, alias="eventLeg")
    event_type: Optional[StrictStr] = Field(None, alias="eventType")
    scan_type: Optional[StrictStr] = Field(None, alias="scanType")
    scan_description: Optional[StrictStr] = Field(None, alias="scanDescription")
    package_status: Optional[StrictStr] = Field(None, alias="packageStatus")
    l2_description: Optional[StrictStr] = Field(None, alias="l2Description")
    event_city: Optional[StrictStr] = Field(None, alias="eventCity")
    event_state_or_province: Optional[StrictStr] = Field(None, alias="eventStateOrProvince")
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    country: Optional[StrictStr] = None
    __properties = ["standardizedEventCode", "l1Code", "l1Description", "eventDate", "eventTime", "eventTimeOffset", "trackingUrl", "latitude", "longitude", "locationUnit", "eventLeg", "eventType", "scanType", "scanDescription", "packageStatus", "l2Description", "eventCity", "eventStateOrProvince", "postalCode", "country"]

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
    def from_json(cls, json_str: str) -> EventObject:
        """Create an instance of EventObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventObject:
        """Create an instance of EventObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventObject.parse_obj(obj)

        _obj = EventObject.parse_obj({
            "standardized_event_code": obj.get("standardizedEventCode"),
            "l1_code": obj.get("l1Code"),
            "l1_description": obj.get("l1Description"),
            "event_date": obj.get("eventDate"),
            "event_time": obj.get("eventTime"),
            "event_time_offset": obj.get("eventTimeOffset"),
            "tracking_url": obj.get("trackingUrl"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "location_unit": obj.get("locationUnit"),
            "event_leg": obj.get("eventLeg"),
            "event_type": obj.get("eventType"),
            "scan_type": obj.get("scanType"),
            "scan_description": obj.get("scanDescription"),
            "package_status": obj.get("packageStatus"),
            "l2_description": obj.get("l2Description"),
            "event_city": obj.get("eventCity"),
            "event_state_or_province": obj.get("eventStateOrProvince"),
            "postal_code": obj.get("postalCode"),
            "country": obj.get("country")
        })
        return _obj


