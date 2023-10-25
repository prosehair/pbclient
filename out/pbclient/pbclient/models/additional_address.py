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



from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from pbclient.models.address import Address
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AdditionalAddress(BaseModel):
    """
    AdditionalAddress
    """
    address: Address
    address_type: StrictStr = Field(alias="addressType")
    __properties: ClassVar[List[str]] = ["address", "addressType"]

    @field_validator('address_type')
    def address_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('HOLD', 'BROKER', 'THIRD_PARTY', 'PICKUP', 'EXPORTER'):
            raise ValueError("must be one of enum values ('HOLD', 'BROKER', 'THIRD_PARTY', 'PICKUP', 'EXPORTER')")
        return value

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
        """Create an instance of AdditionalAddress from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of AdditionalAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "addressType": obj.get("addressType")
        })
        return _obj


