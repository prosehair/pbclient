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
from pbclient.models.cross_border_quotes_response import CrossBorderQuotesResponse  # noqa: E501
from pbclient.rest import ApiException

class TestCrossBorderQuotesResponse(unittest.TestCase):
    """CrossBorderQuotesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrossBorderQuotesResponse`
        """
        model = pbclient.models.cross_border_quotes_response.CrossBorderQuotesResponse()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesResponse(
                quote = [
                    pbclient.models.cross_border_quotes_response_quote_inner.CrossBorderQuotesResponse_quote_inner(
                        quote_currency = '', 
                        quote_lines = [
                            pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner.CrossBorderQuotesResponse_quote_inner_quoteLines_inner(
                                line_id = '', 
                                item_id = '', 
                                quote_line_id = '', 
                                quantity = 56, 
                                unit_rates = pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_unit_rates.CrossBorderQuotesResponse_quote_inner_quoteLines_inner_unitRates(
                                    unit_price = 1.337, 
                                    total_tax_amount = 1.337, 
                                    total_duty_amount = 56, 
                                    service_id = '', 
                                    base_charge = 1.337, 
                                    delivery_commitment = pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_unit_rates_delivery_commitment.CrossBorderQuotesResponse_quote_inner_quoteLines_inner_unitRates_deliveryCommitment(
                                        min_estimated_number_of_days = 56, 
                                        max_estimated_number_of_days = 56, ), 
                                    total_carrier_charge = 1.337, ), 
                                line_rates = pbclient.models.cross_border_quotes_response_quote_inner_quote_lines_inner_line_rates.CrossBorderQuotesResponse_quote_inner_quoteLines_inner_lineRates(
                                    line_price = 1.337, 
                                    total_tax_amount = 1.337, 
                                    total_duty_amount = 56, 
                                    service_id = '', 
                                    base_charge = 1.337, 
                                    total_carrier_charge = 1.337, ), )
                            ], 
                        total_price = 1.337, 
                        total_rates = pbclient.models.cross_border_quotes_response_quote_inner_total_rates.CrossBorderQuotesResponse_quote_inner_totalRates(
                            service_id = '', 
                            base_charge = 1.337, 
                            total_carrier_charge = 1.337, 
                            total_duty_amount = 56, 
                            total_tax_amount = 1.337, ), )
                    ]
            )
        else :
            return CrossBorderQuotesResponse(
        )
        """

    def testCrossBorderQuotesResponse(self):
        """Test CrossBorderQuotesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
