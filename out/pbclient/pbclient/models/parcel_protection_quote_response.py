# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.5
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from pbclient.models.parcel_protection_quote_response_parcel_protection_fees_breakup import ParcelProtectionQuoteResponseParcelProtectionFeesBreakup
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ParcelProtectionQuoteResponse(BaseModel):
    """
    ParcelProtectionQuoteResponse
    """
    parcel_protection_fees: Union[StrictFloat, StrictInt] = Field(alias="parcelProtectionFees")
    parcel_protection_fees_currency_code: StrictStr = Field(alias="parcelProtectionFeesCurrencyCode")
    parcel_protection_fees_breakup: ParcelProtectionQuoteResponseParcelProtectionFeesBreakup = Field(alias="parcelProtectionFeesBreakup")
    __properties: ClassVar[List[str]] = ["parcelProtectionFees", "parcelProtectionFeesCurrencyCode", "parcelProtectionFeesBreakup"]

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
        """Create an instance of ParcelProtectionQuoteResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parcel_protection_fees_breakup
        if self.parcel_protection_fees_breakup:
            _dict['parcelProtectionFeesBreakup'] = self.parcel_protection_fees_breakup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ParcelProtectionQuoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parcelProtectionFees": obj.get("parcelProtectionFees"),
            "parcelProtectionFeesCurrencyCode": obj.get("parcelProtectionFeesCurrencyCode"),
            "parcelProtectionFeesBreakup": ParcelProtectionQuoteResponseParcelProtectionFeesBreakup.from_dict(obj.get("parcelProtectionFeesBreakup")) if obj.get("parcelProtectionFeesBreakup") is not None else None
        })
        return _obj


