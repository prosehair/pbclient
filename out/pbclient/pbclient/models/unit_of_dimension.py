# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.7
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class UnitOfDimension(str, Enum):
    """
    UnitOfDimension
    """

    """
    allowed enum values
    """
    CM = 'CM'
    IN = 'IN'

    @classmethod
    def from_json(cls, json_str: str) -> UnitOfDimension:
        """Create an instance of UnitOfDimension from a JSON string"""
        return UnitOfDimension(json.loads(json_str))


