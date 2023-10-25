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


from typing import Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ParcelProtectionPolicyResponseContentInnerShipperInfoAddress(BaseModel):
    """
    ParcelProtectionPolicyResponseContentInnerShipperInfoAddress
    """
    street1: Optional[StrictStr] = None
    street2: Optional[StrictStr] = None
    street3: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    region: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    __properties: ClassVar[List[str]] = ["street1", "street2", "street3", "city", "region", "country", "postalCode"]

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
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfoAddress from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ParcelProtectionPolicyResponseContentInnerShipperInfoAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "street1": obj.get("street1"),
            "street2": obj.get("street2"),
            "street3": obj.get("street3"),
            "city": obj.get("city"),
            "region": obj.get("region"),
            "country": obj.get("country"),
            "postalCode": obj.get("postalCode")
        })
        return _obj


