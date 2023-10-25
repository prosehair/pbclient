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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from pbclient.models.cross_border_quotes_errors_quote_inner_quote_lines_inner_unit_errors_inner import CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner(BaseModel):
    """
    CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner
    """
    line_id: Optional[StrictStr] = Field(default=None, alias="lineId")
    merchant_com_ref_id: Optional[StrictStr] = Field(default=None, alias="merchantComRefId")
    quantity: Optional[StrictInt] = None
    unit_errors: Optional[List[CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner]] = Field(default=None, alias="unitErrors")
    __properties: ClassVar[List[str]] = ["lineId", "merchantComRefId", "quantity", "unitErrors"]

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
        """Create an instance of CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in unit_errors (list)
        _items = []
        if self.unit_errors:
            for _item in self.unit_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['unitErrors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CrossBorderQuotesErrorsQuoteInnerQuoteLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lineId": obj.get("lineId"),
            "merchantComRefId": obj.get("merchantComRefId"),
            "quantity": obj.get("quantity"),
            "unitErrors": [CrossBorderQuotesErrorsQuoteInnerQuoteLinesInnerUnitErrorsInner.from_dict(_item) for _item in obj.get("unitErrors")] if obj.get("unitErrors") is not None else None
        })
        return _obj


