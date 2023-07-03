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
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, conlist
from pbclient.models.add_tracking_events_references_inner import AddTrackingEventsReferencesInner
from pbclient.models.carrier import Carrier

class AddTrackingEvents(BaseModel):
    """
    AddTrackingEvents
    """
    carrier: Optional[Carrier] = None
    references: Optional[conlist(AddTrackingEventsReferencesInner)] = None
    __properties = ["carrier", "references"]

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
    def from_json(cls, json_str: str) -> AddTrackingEvents:
        """Create an instance of AddTrackingEvents from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in references (list)
        _items = []
        if self.references:
            for _item in self.references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['references'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddTrackingEvents:
        """Create an instance of AddTrackingEvents from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddTrackingEvents.parse_obj(obj)

        _obj = AddTrackingEvents.parse_obj({
            "carrier": obj.get("carrier"),
            "references": [AddTrackingEventsReferencesInner.from_dict(_item) for _item in obj.get("references")] if obj.get("references") is not None else None
        })
        return _obj

