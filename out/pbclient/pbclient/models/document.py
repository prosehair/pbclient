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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from pbclient.models.customer_data import CustomerData
from pbclient.models.doc_tab_item import DocTabItem
from pbclient.models.document_page import DocumentPage
from typing import Optional, Set
from typing_extensions import Self

class Document(BaseModel):
    """
    Document
    """ # noqa: E501
    content_type: Optional[StrictStr] = Field(default=None, alias="contentType")
    contents: Optional[StrictStr] = None
    customer_data: Optional[CustomerData] = Field(default=None, alias="customerData")
    doc_tab: Optional[List[DocTabItem]] = Field(default=None, alias="docTab")
    file_format: Optional[StrictStr] = Field(default=None, alias="fileFormat")
    pages: Optional[List[DocumentPage]] = None
    print_dialog_option: Optional[StrictStr] = Field(default=None, alias="printDialogOption")
    resolution: Optional[StrictStr] = None
    size: Optional[StrictStr] = None
    type: StrictStr
    __properties: ClassVar[List[str]] = ["contentType", "contents", "customerData", "docTab", "fileFormat", "pages", "printDialogOption", "resolution", "size", "type"]

    @field_validator('content_type')
    def content_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['URL', 'BASE64']):
            raise ValueError("must be one of enum values ('URL', 'BASE64')")
        return value

    @field_validator('file_format')
    def file_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PDF', 'PNG', 'GIF', 'ZPL', 'ZPL2']):
            raise ValueError("must be one of enum values ('PDF', 'PNG', 'GIF', 'ZPL', 'ZPL2')")
        return value

    @field_validator('print_dialog_option')
    def print_dialog_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NO_PRINT_DIALOG', 'EMBED_PRINT_DIALOG']):
            raise ValueError("must be one of enum values ('NO_PRINT_DIALOG', 'EMBED_PRINT_DIALOG')")
        return value

    @field_validator('resolution')
    def resolution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DPI_300', 'DPI_203', 'DPI_150']):
            raise ValueError("must be one of enum values ('DPI_300', 'DPI_203', 'DPI_150')")
        return value

    @field_validator('size')
    def size_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DOC_2X7', 'DOC_4X1', 'DOC_4X3', 'DOC_4X6', 'DOC_4X8', 'DOC_6X4', 'DOC_8X11', 'DOC_9X4', 'DOC_4X5', 'DOC_8_5X5_5']):
            raise ValueError("must be one of enum values ('DOC_2X7', 'DOC_4X1', 'DOC_4X3', 'DOC_4X6', 'DOC_4X8', 'DOC_6X4', 'DOC_8X11', 'DOC_9X4', 'DOC_4X5', 'DOC_8_5X5_5')")
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
        """Create an instance of Document from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of customer_data
        if self.customer_data:
            _dict['customerData'] = self.customer_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in doc_tab (list)
        _items = []
        if self.doc_tab:
            for _item in self.doc_tab:
                if _item:
                    _items.append(_item.to_dict())
            _dict['docTab'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pages (list)
        _items = []
        if self.pages:
            for _item in self.pages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contentType": obj.get("contentType"),
            "contents": obj.get("contents"),
            "customerData": CustomerData.from_dict(obj["customerData"]) if obj.get("customerData") is not None else None,
            "docTab": [DocTabItem.from_dict(_item) for _item in obj["docTab"]] if obj.get("docTab") is not None else None,
            "fileFormat": obj.get("fileFormat"),
            "pages": [DocumentPage.from_dict(_item) for _item in obj["pages"]] if obj.get("pages") is not None else None,
            "printDialogOption": obj.get("printDialogOption"),
            "resolution": obj.get("resolution"),
            "size": obj.get("size"),
            "type": obj.get("type")
        })
        return _obj


