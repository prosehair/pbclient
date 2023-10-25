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
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class UnitOfWeight(str, Enum):
    """
    UnitOfWeight
    """

    """
    allowed enum values
    """
    GM = 'GM'
    OZ = 'OZ'
    LB = 'LB'
    KG = 'KG'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UnitOfWeight from a JSON string"""
        return cls(json.loads(json_str))


