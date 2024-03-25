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
from pbclient.models.cross_border_quotes_errors_quote_inner import CrossBorderQuotesErrorsQuoteInner  # noqa: E501
from pbclient.rest import ApiException

class TestCrossBorderQuotesErrorsQuoteInner(unittest.TestCase):
    """CrossBorderQuotesErrorsQuoteInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesErrorsQuoteInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrossBorderQuotesErrorsQuoteInner`
        """
        model = pbclient.models.cross_border_quotes_errors_quote_inner.CrossBorderQuotesErrorsQuoteInner()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesErrorsQuoteInner(
                quote_currency = '', 
                quote_lines = [
                    pbclient.models.cross_border_quotes_errors_quote_inner_quote_lines_inner.CrossBorderQuotesErrors_quote_inner_quoteLines_inner(
                        line_id = '', 
                        merchant_com_ref_id = '', 
                        quantity = 56, 
                        unit_errors = [
                            pbclient.models.cross_border_quotes_errors_quote_inner_quote_lines_inner_unit_errors_inner.CrossBorderQuotesErrors_quote_inner_quoteLines_inner_unitErrors_inner(
                                error = 56, 
                                message = '', )
                            ], )
                    ], 
                errors = pbclient.models.cross_border_quotes_errors_quote_inner_errors.CrossBorderQuotesErrors_quote_inner_errors()
            )
        else :
            return CrossBorderQuotesErrorsQuoteInner(
        )
        """

    def testCrossBorderQuotesErrorsQuoteInner(self):
        """Test CrossBorderQuotesErrorsQuoteInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
