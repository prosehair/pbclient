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
import json
from enum import Enum
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


