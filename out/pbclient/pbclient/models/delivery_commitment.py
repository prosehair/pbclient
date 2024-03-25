# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 2.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DeliveryCommitment(BaseModel):
    """
    DeliveryCommitment
    """ # noqa: E501
    additional_details: Optional[StrictStr] = Field(default=None, alias="additionalDetails")
    estimated_delivery_date_time: Optional[StrictStr] = Field(default=None, alias="estimatedDeliveryDateTime")
    guarantee: Optional[StrictStr] = None
    max_estimated_number_of_days: Optional[StrictStr] = Field(default=None, alias="maxEstimatedNumberOfDays")
    min_estimated_number_of_days: Optional[StrictStr] = Field(default=None, alias="minEstimatedNumberOfDays")
    __properties: ClassVar[List[str]] = ["additionalDetails", "estimatedDeliveryDateTime", "guarantee", "maxEstimatedNumberOfDays", "minEstimatedNumberOfDays"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DeliveryCommitment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeliveryCommitment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "additionalDetails": obj.get("additionalDetails"),
            "estimatedDeliveryDateTime": obj.get("estimatedDeliveryDateTime"),
            "guarantee": obj.get("guarantee"),
            "maxEstimatedNumberOfDays": obj.get("maxEstimatedNumberOfDays"),
            "minEstimatedNumberOfDays": obj.get("minEstimatedNumberOfDays")
        })
        return _obj


