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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from pbclient.models.carrier import Carrier
from pbclient.models.errors import Errors

class CancelShipment(BaseModel):
    """
    CancelShipment
    """
    cancel_initiator: Optional[StrictStr] = Field(None, alias="cancelInitiator")
    carrier: Optional[Carrier] = None
    error_messages: Optional[conlist(Errors)] = Field(None, alias="errorMessages")
    parcel_tracking_number: Optional[StrictStr] = Field(None, alias="parcelTrackingNumber")
    status: Optional[StrictStr] = None
    total_carrier_charge: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalCarrierCharge")
    __properties = ["cancelInitiator", "carrier", "errorMessages", "parcelTrackingNumber", "status", "totalCarrierCharge"]

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
    def from_json(cls, json_str: str) -> CancelShipment:
        """Create an instance of CancelShipment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in error_messages (list)
        _items = []
        if self.error_messages:
            for _item in self.error_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errorMessages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CancelShipment:
        """Create an instance of CancelShipment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CancelShipment.parse_obj(obj)

        _obj = CancelShipment.parse_obj({
            "cancel_initiator": obj.get("cancelInitiator"),
            "carrier": obj.get("carrier"),
            "error_messages": [Errors.from_dict(_item) for _item in obj.get("errorMessages")] if obj.get("errorMessages") is not None else None,
            "parcel_tracking_number": obj.get("parcelTrackingNumber"),
            "status": obj.get("status"),
            "total_carrier_charge": obj.get("totalCarrierCharge")
        })
        return _obj


