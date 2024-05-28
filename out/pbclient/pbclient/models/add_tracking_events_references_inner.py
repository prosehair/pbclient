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
from pbclient.models.add_tracking_events_references_inner_events_inner import AddTrackingEventsReferencesInnerEventsInner

class AddTrackingEventsReferencesInner(BaseModel):
    """
    AddTrackingEventsReferencesInner
    """
    reference_type: Optional[StrictStr] = Field(None, alias="referenceType")
    reference_value: Optional[StrictStr] = Field(None, alias="referenceValue")
    events: Optional[conlist(AddTrackingEventsReferencesInnerEventsInner)] = None
    __properties = ["referenceType", "referenceValue", "events"]

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
    def from_json(cls, json_str: str) -> AddTrackingEventsReferencesInner:
        """Create an instance of AddTrackingEventsReferencesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddTrackingEventsReferencesInner:
        """Create an instance of AddTrackingEventsReferencesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddTrackingEventsReferencesInner.parse_obj(obj)

        _obj = AddTrackingEventsReferencesInner.parse_obj({
            "reference_type": obj.get("referenceType"),
            "reference_value": obj.get("referenceValue"),
            "events": [AddTrackingEventsReferencesInnerEventsInner.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None
        })
        return _obj


