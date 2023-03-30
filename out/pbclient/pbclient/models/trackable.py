# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from inspect import getfullargspec
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

