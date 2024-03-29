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
from pbclient.models.special_service import SpecialService  # noqa: E501
from pbclient.rest import ApiException

class TestSpecialService(unittest.TestCase):
    """SpecialService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SpecialService
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpecialService`
        """
        model = pbclient.models.special_service.SpecialService()  # noqa: E501
        if include_optional :
            return SpecialService(
                fee = 1.337, 
                input_parameters = [
                    pbclient.models.parameter.Parameter(
                        name = '', 
                        value = '', )
                    ], 
                special_service_id = ''
            )
        else :
            return SpecialService(
                special_service_id = '',
        )
        """

    def testSpecialService(self):
        """Test SpecialService"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
