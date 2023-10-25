# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.4
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from pbclient.models.address import Address
from pbclient.models.carrier_facility_response_carrier_facility_options_inner import CarrierFacilityResponseCarrierFacilityOptionsInner
from pbclient.models.carrier_facility_response_carrier_facility_suggestions_inner_facility_hours_inner import CarrierFacilityResponseCarrierFacilitySuggestionsInnerFacilityHoursInner
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CarrierFacilityResponseCarrierFacilitySuggestionsInner(BaseModel):
    """
    CarrierFacilityResponseCarrierFacilitySuggestionsInner
    """
    address: Optional[Address] = None
    carrier_facility_attributes: Optional[List[CarrierFacilityResponseCarrierFacilityOptionsInner]] = Field(default=None, alias="carrierFacilityAttributes")
    facility_hours: Optional[List[CarrierFacilityResponseCarrierFacilitySuggestionsInnerFacilityHoursInner]] = Field(default=None, alias="facilityHours")
    facility_parking: Optional[StrictStr] = Field(default=None, alias="facilityParking")
    __properties: ClassVar[List[str]] = ["address", "carrierFacilityAttributes", "facilityHours", "facilityParking"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CarrierFacilityResponseCarrierFacilitySuggestionsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in carrier_facility_attributes (list)
        _items = []
        if self.carrier_facility_attributes:
            for _item in self.carrier_facility_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['carrierFacilityAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in facility_hours (list)
        _items = []
        if self.facility_hours:
            for _item in self.facility_hours:
                if _item:
                    _items.append(_item.to_dict())
            _dict['facilityHours'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CarrierFacilityResponseCarrierFacilitySuggestionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "carrierFacilityAttributes": [CarrierFacilityResponseCarrierFacilityOptionsInner.from_dict(_item) for _item in obj.get("carrierFacilityAttributes")] if obj.get("carrierFacilityAttributes") is not None else None,
            "facilityHours": [CarrierFacilityResponseCarrierFacilitySuggestionsInnerFacilityHoursInner.from_dict(_item) for _item in obj.get("facilityHours")] if obj.get("facilityHours") is not None else None,
            "facilityParking": obj.get("facilityParking")
        })
        return _obj


