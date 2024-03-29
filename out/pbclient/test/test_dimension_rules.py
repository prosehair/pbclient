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
from pbclient.models.dimension_rules import DimensionRules  # noqa: E501
from pbclient.rest import ApiException

class TestDimensionRules(unittest.TestCase):
    """DimensionRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DimensionRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DimensionRules`
        """
        model = pbclient.models.dimension_rules.DimensionRules()  # noqa: E501
        if include_optional :
            return DimensionRules(
                required = True, 
                unit_of_measurement = '', 
                min_parcel_dimensions = pbclient.models.dimension_rules_min_parcel_dimensions.DimensionRules_minParcelDimensions(
                    length = 1.337, 
                    width = 1.337, 
                    height = 1.337, 
                    unit_of_measurement = '', ), 
                max_parcel_dimensions = pbclient.models.dimension_rules_max_parcel_dimensions.DimensionRules_maxParcelDimensions(
                    length = 56, 
                    width = 1.337, 
                    height = 56, 
                    unit_of_measurement = '', ), 
                min_length_plus_girth = 56, 
                max_length_plus_girth = 56
            )
        else :
            return DimensionRules(
        )
        """

    def testDimensionRules(self):
        """Test DimensionRules"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
