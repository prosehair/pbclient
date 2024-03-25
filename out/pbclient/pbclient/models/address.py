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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address
    """ # noqa: E501
    address_lines: Optional[List[StrictStr]] = Field(default=None, alias="addressLines")
    carrier_route: Optional[StrictStr] = Field(default=None, alias="carrierRoute")
    city_town: Optional[StrictStr] = Field(default=None, alias="cityTown")
    company: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = Field(default=None, description="2-character country code (ISO-3166-1 alpha-2)", alias="countryCode")
    delivery_point: Optional[StrictStr] = Field(default=None, alias="deliveryPoint")
    email: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    residential: Optional[StrictBool] = None
    state_province: Optional[StrictStr] = Field(default=None, alias="stateProvince")
    status: Optional[StrictStr] = None
    tax_id: Optional[StrictStr] = Field(default=None, alias="taxId")
    tax_id_type: Optional[StrictStr] = Field(default=None, alias="taxIdType")
    __properties: ClassVar[List[str]] = ["addressLines", "carrierRoute", "cityTown", "company", "countryCode", "deliveryPoint", "email", "name", "phone", "postalCode", "residential", "stateProvince", "status", "taxId", "taxIdType"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PARSED', 'VALIDATED_CHANGED', 'VALIDATED_AND_NOT_CHANGED', 'NOT_CHANGED']):
            raise ValueError("must be one of enum values ('PARSED', 'VALIDATED_CHANGED', 'VALIDATED_AND_NOT_CHANGED', 'NOT_CHANGED')")
        return value

    @field_validator('tax_id_type')
    def tax_id_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EIN', 'GST', 'VAT', 'RFC', 'EORI']):
            raise ValueError("must be one of enum values ('EIN', 'GST', 'VAT', 'RFC', 'EORI')")
        return value

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
        """Create an instance of Address from a JSON string"""
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
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressLines": obj.get("addressLines"),
            "carrierRoute": obj.get("carrierRoute"),
            "cityTown": obj.get("cityTown"),
            "company": obj.get("company"),
            "countryCode": obj.get("countryCode"),
            "deliveryPoint": obj.get("deliveryPoint"),
            "email": obj.get("email"),
            "name": obj.get("name"),
            "phone": obj.get("phone"),
            "postalCode": obj.get("postalCode"),
            "residential": obj.get("residential"),
            "stateProvince": obj.get("stateProvince"),
            "status": obj.get("status"),
            "taxId": obj.get("taxId"),
            "taxIdType": obj.get("taxIdType")
        })
        return _obj


