# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import absolute_import

import unittest
import datetime

import pbclient
from pbclient.models.dimension_rules_max_parcel_dimensions import DimensionRulesMaxParcelDimensions  # noqa: E501
from pbclient.rest import ApiException

class TestDimensionRulesMaxParcelDimensions(unittest.TestCase):
    """DimensionRulesMaxParcelDimensions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DimensionRulesMaxParcelDimensions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionRulesMaxParcelDimensions`
        """
        model = pbclient.models.dimension_rules_max_parcel_dimensions.DimensionRulesMaxParcelDimensions()  # noqa: E501
        if include_optional :
            return DimensionRulesMaxParcelDimensions(
                length = 56, 
                width = 1.337, 
                height = 56, 
                unit_of_measurement = ''
            )
        else :
            return DimensionRulesMaxParcelDimensions(
        )
        """

    def testDimensionRulesMaxParcelDimensions(self):
        """Test DimensionRulesMaxParcelDimensions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
