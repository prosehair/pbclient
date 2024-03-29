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
from pbclient.models.parcel_protection_quote_request_shipment_info import ParcelProtectionQuoteRequestShipmentInfo
from typing import Optional, Set
from typing_extensions import Self

class ParcelProtectionQuoteRequest(BaseModel):
    """
    ParcelProtectionQuoteRequest
    """ # noqa: E501
    parcel_protection_account_id: Optional[StrictStr] = Field(default=None, alias="parcelProtectionAccountID")
    parcel_protection_program_id: Optional[StrictStr] = Field(default=None, alias="parcelProtectionProgramID")
    shipment_info: ParcelProtectionQuoteRequestShipmentInfo = Field(alias="shipmentInfo")
    __properties: ClassVar[List[str]] = ["parcelProtectionAccountID", "parcelProtectionProgramID", "shipmentInfo"]

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
        """Create an instance of ParcelProtectionQuoteRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shipment_info
        if self.shipment_info:
            _dict['shipmentInfo'] = self.shipment_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParcelProtectionQuoteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parcelProtectionAccountID": obj.get("parcelProtectionAccountID"),
            "parcelProtectionProgramID": obj.get("parcelProtectionProgramID"),
            "shipmentInfo": ParcelProtectionQuoteRequestShipmentInfo.from_dict(obj["shipmentInfo"]) if obj.get("shipmentInfo") is not None else None
        })
        return _obj


