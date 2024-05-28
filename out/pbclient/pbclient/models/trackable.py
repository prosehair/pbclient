# coding: utf-8

"""
    Shipping API

    Shipping API Sample.

    The version of the OpenAPI document: 1.0.13
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Trackable(str, Enum):
    """
    * TRACKABLE - Item is trackable by default. * NON_TRACKABLE - Item is not trackable. * REQUIRES_TRACKABLE_SPECIAL_SERVICE - Item is trackable if special service is requested. 
    """

    """
    allowed enum values
    """
    TRACKABLE = 'TRACKABLE'
    NON_TRACKABLE = 'NON_TRACKABLE'
    REQUIRES_TRACKABLE_SPECIAL_SERVICE = 'REQUIRES_TRACKABLE_SPECIAL_SERVICE'

    @classmethod
    def from_json(cls, json_str: str) -> Trackable:
        """Create an instance of Trackable from a JSON string"""
        return Trackable(json.loads(json_str))


