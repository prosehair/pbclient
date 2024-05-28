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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class AddTrackingEventsReferencesInnerEventsInner(BaseModel):
    """
    AddTrackingEventsReferencesInnerEventsInner
    """
    event_code: Optional[StrictStr] = Field(None, alias="eventCode")
    carrier_event_code: Optional[StrictStr] = Field(None, alias="carrierEventCode")
    event_date: Optional[StrictStr] = Field(None, alias="eventDate")
    event_time: Optional[StrictStr] = Field(None, alias="eventTime")
    event_time_offset: Optional[StrictStr] = Field(None, alias="eventTimeOffset")
    event_city: Optional[StrictStr] = Field(None, alias="eventCity")
    event_state_or_province: Optional[StrictStr] = Field(None, alias="eventStateOrProvince")
    postal_code: Optional[StrictStr] = Field(None, alias="postalCode")
    country: Optional[StrictStr] = None
    __properties = ["eventCode", "carrierEventCode", "eventDate", "eventTime", "eventTimeOffset", "eventCity", "eventStateOrProvince", "postalCode", "country"]

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
    def from_json(cls, json_str: str) -> AddTrackingEventsReferencesInnerEventsInner:
        """Create an instance of AddTrackingEventsReferencesInnerEventsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddTrackingEventsReferencesInnerEventsInner:
        """Create an instance of AddTrackingEventsReferencesInnerEventsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddTrackingEventsReferencesInnerEventsInner.parse_obj(obj)

        _obj = AddTrackingEventsReferencesInnerEventsInner.parse_obj({
            "event_code": obj.get("eventCode"),
            "carrier_event_code": obj.get("carrierEventCode"),
            "event_date": obj.get("eventDate"),
            "event_time": obj.get("eventTime"),
            "event_time_offset": obj.get("eventTimeOffset"),
            "event_city": obj.get("eventCity"),
            "event_state_or_province": obj.get("eventStateOrProvince"),
            "postal_code": obj.get("postalCode"),
            "country": obj.get("country")
        })
        return _obj


