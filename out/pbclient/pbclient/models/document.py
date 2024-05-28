# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.14
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from pbclient.models.customer_data import CustomerData
from pbclient.models.doc_tab_item import DocTabItem
from pbclient.models.document_page import DocumentPage

class Document(BaseModel):
    """
    Document
    """
    content_type: Optional[StrictStr] = Field(None, alias="contentType")
    contents: Optional[StrictStr] = None
    customer_data: Optional[CustomerData] = Field(None, alias="customerData")
    doc_tab: Optional[conlist(DocTabItem)] = Field(None, alias="docTab")
    file_format: Optional[StrictStr] = Field(None, alias="fileFormat")
    pages: Optional[conlist(DocumentPage)] = None
    print_dialog_option: Optional[StrictStr] = Field(None, alias="printDialogOption")
    resolution: Optional[StrictStr] = None
    size: Optional[StrictStr] = None
    type: StrictStr = Field(...)
    __properties = ["contentType", "contents", "customerData", "docTab", "fileFormat", "pages", "printDialogOption", "resolution", "size", "type"]

    @validator('content_type')
    def content_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('URL', 'BASE64'):
            raise ValueError("must be one of enum values ('URL', 'BASE64')")
        return value

    @validator('file_format')
    def file_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PDF', 'PNG', 'GIF', 'ZPL', 'ZPL2'):
            raise ValueError("must be one of enum values ('PDF', 'PNG', 'GIF', 'ZPL', 'ZPL2')")
        return value

    @validator('print_dialog_option')
    def print_dialog_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NO_PRINT_DIALOG', 'EMBED_PRINT_DIALOG'):
            raise ValueError("must be one of enum values ('NO_PRINT_DIALOG', 'EMBED_PRINT_DIALOG')")
        return value

    @validator('resolution')
    def resolution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DPI_300', 'DPI_203', 'DPI_150'):
            raise ValueError("must be one of enum values ('DPI_300', 'DPI_203', 'DPI_150')")
        return value

    @validator('size')
    def size_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DOC_2X7', 'DOC_4X1', 'DOC_4X3', 'DOC_4X6', 'DOC_4X8', 'DOC_6X4', 'DOC_8X11', 'DOC_9X4', 'DOC_4X5', 'DOC_8_5X5_5'):
            raise ValueError("must be one of enum values ('DOC_2X7', 'DOC_4X1', 'DOC_4X3', 'DOC_4X6', 'DOC_4X8', 'DOC_6X4', 'DOC_8X11', 'DOC_9X4', 'DOC_4X5', 'DOC_8_5X5_5')")
        return value

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
    def from_json(cls, json_str: str) -> Document:
        """Create an instance of Document from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
    def from_dict(cls, obj: dict) -> Document:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Document.parse_obj(obj)

        _obj = Document.parse_obj({
            "content_type": obj.get("contentType"),
            "contents": obj.get("contents"),
            "customer_data": CustomerData.from_dict(obj.get("customerData")) if obj.get("customerData") is not None else None,
            "doc_tab": [DocTabItem.from_dict(_item) for _item in obj.get("docTab")] if obj.get("docTab") is not None else None,
            "file_format": obj.get("fileFormat"),
            "pages": [DocumentPage.from_dict(_item) for _item in obj.get("pages")] if obj.get("pages") is not None else None,
            "print_dialog_option": obj.get("printDialogOption"),
            "resolution": obj.get("resolution"),
            "size": obj.get("size"),
            "type": obj.get("type")
        })
        return _obj


