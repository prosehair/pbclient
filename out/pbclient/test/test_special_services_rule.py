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
from pbclient.models.special_services_rule import SpecialServicesRule  # noqa: E501
from pbclient.rest import ApiException

class TestSpecialServicesRule(unittest.TestCase):
    """SpecialServicesRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SpecialServicesRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpecialServicesRule`
        """
        model = pbclient.models.special_services_rule.SpecialServicesRule()  # noqa: E501
        if include_optional :
            return SpecialServicesRule(
                special_service_id = 'ADSIG', 
                branded_name = '', 
                category_id = '', 
                category_name = '', 
                trackable = True, 
                input_parameter_rules = [
                    pbclient.models.services_parameter_rule.ServicesParameterRule(
                        name = '', 
                        branded_name = '', 
                        required = True, 
                        min_value = 1.337, 
                        max_value = 1.337, 
                        free_value = 1.337, 
                        format = '', 
                        description = '', )
                    ], 
                prerequisite_rules = [
                    pbclient.models.prerequisite_rules.PrerequisiteRules(
                        special_service_codes = 'ADSIG', 
                        min_input_value = 1.337, )
                    ], 
                incompatible_special_services = 'ADSIG'
            )
        else :
            return SpecialServicesRule(
        )
        """

    def testSpecialServicesRule(self):
        """Test SpecialServicesRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
