# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.6
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from pbclient.models.parcel_protection_create_response_parcel_protection_fees_breakup import ParcelProtectionCreateResponseParcelProtectionFeesBreakup

class ParcelProtectionCreateResponse(BaseModel):
    """
    ParcelProtectionCreateResponse
    """
    transaction_id: Optional[StrictStr] = Field(None, alias="transactionID")
    parcel_protection_reference_id: Optional[StrictStr] = Field(None, alias="parcelProtectionReferenceID")
    parcel_protection_date: Optional[StrictStr] = Field(None, alias="parcelProtectionDate")
    parcel_protection_fees: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="parcelProtectionFees")
    parcel_protection_fees_currency_code: Optional[StrictStr] = Field(None, alias="parcelProtectionFeesCurrencyCode")
    parcel_protection_fees_breakup: Optional[ParcelProtectionCreateResponseParcelProtectionFeesBreakup] = Field(None, alias="parcelProtectionFeesBreakup")
    __properties = ["transactionID", "parcelProtectionReferenceID", "parcelProtectionDate", "parcelProtectionFees", "parcelProtectionFeesCurrencyCode", "parcelProtectionFeesBreakup"]

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
    def from_json(cls, json_str: str) -> ParcelProtectionCreateResponse:
        """Create an instance of ParcelProtectionCreateResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parcel_protection_fees_breakup
        if self.parcel_protection_fees_breakup:
            _dict['parcelProtectionFeesBreakup'] = self.parcel_protection_fees_breakup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelProtectionCreateResponse:
        """Create an instance of ParcelProtectionCreateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParcelProtectionCreateResponse.parse_obj(obj)

        _obj = ParcelProtectionCreateResponse.parse_obj({
            "transaction_id": obj.get("transactionID"),
            "parcel_protection_reference_id": obj.get("parcelProtectionReferenceID"),
            "parcel_protection_date": obj.get("parcelProtectionDate"),
            "parcel_protection_fees": obj.get("parcelProtectionFees"),
            "parcel_protection_fees_currency_code": obj.get("parcelProtectionFeesCurrencyCode"),
            "parcel_protection_fees_breakup": ParcelProtectionCreateResponseParcelProtectionFeesBreakup.from_dict(obj.get("parcelProtectionFeesBreakup")) if obj.get("parcelProtectionFeesBreakup") is not None else None
        })
        return _obj


