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
from pbclient.models.cross_border_quotes_request_basket_items_inner_pricing import CrossBorderQuotesRequestBasketItemsInnerPricing  # noqa: E501
from pbclient.rest import ApiException

class TestCrossBorderQuotesRequestBasketItemsInnerPricing(unittest.TestCase):
    """CrossBorderQuotesRequestBasketItemsInnerPricing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesRequestBasketItemsInnerPricing
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrossBorderQuotesRequestBasketItemsInnerPricing`
        """
        model = pbclient.models.cross_border_quotes_request_basket_items_inner_pricing.CrossBorderQuotesRequestBasketItemsInnerPricing()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesRequestBasketItemsInnerPricing(
                price = 56, 
                cod_price = [
                    pbclient.models.cross_border_quotes_request_basket_items_inner_pricing_cod_price_inner.CrossBorderQuotesRequest_basketItems_inner_pricing_codPrice_inner(
                        price = 56, 
                        cod = '', 
                        includes_duty = True, 
                        includes_taxes = True, )
                    ], 
                dutiable_value = 56
            )
        else :
            return CrossBorderQuotesRequestBasketItemsInnerPricing(
        )
        """

    def testCrossBorderQuotesRequestBasketItemsInnerPricing(self):
        """Test CrossBorderQuotesRequestBasketItemsInnerPricing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
