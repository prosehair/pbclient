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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_unit_rates_delivery_commitment import CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment
from typing import Optional, Set
from typing_extensions import Self

class CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates(BaseModel):
    """
    CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates
    """ # noqa: E501
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unitPrice")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalTaxAmount")
    total_duty_amount: Optional[StrictInt] = Field(default=None, alias="totalDutyAmount")
    service_id: Optional[StrictStr] = Field(default=None, alias="serviceId")
    base_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="baseCharge")
    delivery_commitment: Optional[CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment] = Field(default=None, alias="deliveryCommitment")
    total_carrier_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="totalCarrierCharge")
    __properties: ClassVar[List[str]] = ["unitPrice", "totalTaxAmount", "totalDutyAmount", "serviceId", "baseCharge", "deliveryCommitment", "totalCarrierCharge"]

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
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of delivery_commitment
        if self.delivery_commitment:
            _dict['deliveryCommitment'] = self.delivery_commitment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "unitPrice": obj.get("unitPrice"),
            "totalTaxAmount": obj.get("totalTaxAmount"),
            "totalDutyAmount": obj.get("totalDutyAmount"),
            "serviceId": obj.get("serviceId"),
            "baseCharge": obj.get("baseCharge"),
            "deliveryCommitment": CrossBorderQuotesResponseQuoteInnerQuoteLinesInnerUnitRatesDeliveryCommitment.from_dict(obj["deliveryCommitment"]) if obj.get("deliveryCommitment") is not None else None,
            "totalCarrierCharge": obj.get("totalCarrierCharge")
        })
        return _obj


