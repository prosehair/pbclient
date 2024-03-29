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
from pbclient.models.additional_address import AdditionalAddress  # noqa: E501
from pbclient.rest import ApiException

class TestAdditionalAddress(unittest.TestCase):
    """AdditionalAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdditionalAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdditionalAddress`
        """
        model = pbclient.models.additional_address.AdditionalAddress()  # noqa: E501
        if include_optional :
            return AdditionalAddress(
                address = pbclient.models.address.Address(
                    address_lines = [
                        ''
                        ], 
                    carrier_route = '', 
                    city_town = '', 
                    company = '', 
                    country_code = '', 
                    delivery_point = '', 
                    email = '', 
                    name = '', 
                    phone = '', 
                    postal_code = '', 
                    residential = True, 
                    state_province = '', 
                    status = 'PARSED', 
                    tax_id = '', 
                    tax_id_type = 'EIN', ), 
                address_type = 'HOLD'
            )
        else :
            return AdditionalAddress(
                address = pbclient.models.address.Address(
                    address_lines = [
                        ''
                        ], 
                    carrier_route = '', 
                    city_town = '', 
                    company = '', 
                    country_code = '', 
                    delivery_point = '', 
                    email = '', 
                    name = '', 
                    phone = '', 
                    postal_code = '', 
                    residential = True, 
                    state_province = '', 
                    status = 'PARSED', 
                    tax_id = '', 
                    tax_id_type = 'EIN', ),
                address_type = 'HOLD',
        )
        """

    def testAdditionalAddress(self):
        """Test AdditionalAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
