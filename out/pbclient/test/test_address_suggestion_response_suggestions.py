# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import absolute_import

import unittest
import datetime

import pbclient
from pbclient.models.address_suggestion_response_suggestions import AddressSuggestionResponseSuggestions  # noqa: E501
from pbclient.rest import ApiException

class TestAddressSuggestionResponseSuggestions(unittest.TestCase):
    """AddressSuggestionResponseSuggestions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressSuggestionResponseSuggestions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressSuggestionResponseSuggestions`
        """
        model = pbclient.models.address_suggestion_response_suggestions.AddressSuggestionResponseSuggestions()  # noqa: E501
        if include_optional :
            return AddressSuggestionResponseSuggestions(
                suggestion_type = '', 
                address = [
                    pbclient.models.address.Address(
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
                        tax_id_type = 'EIN', )
                    ]
            )
        else :
            return AddressSuggestionResponseSuggestions(
        )
        """

    def testAddressSuggestionResponseSuggestions(self):
        """Test AddressSuggestionResponseSuggestions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
