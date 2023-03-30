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
from pbclient.models.cross_border_quotes_request_basket_items_inner_item_dimension import CrossBorderQuotesRequestBasketItemsInnerItemDimension  # noqa: E501
from pbclient.rest import ApiException

class TestCrossBorderQuotesRequestBasketItemsInnerItemDimension(unittest.TestCase):
    """CrossBorderQuotesRequestBasketItemsInnerItemDimension unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesRequestBasketItemsInnerItemDimension
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrossBorderQuotesRequestBasketItemsInnerItemDimension`
        """
        model = pbclient.models.cross_border_quotes_request_basket_items_inner_item_dimension.CrossBorderQuotesRequestBasketItemsInnerItemDimension()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesRequestBasketItemsInnerItemDimension(
                length = 56, 
                height = 1.337, 
                width = 56, 
                unit_of_measurement = ''
            )
        else :
            return CrossBorderQuotesRequestBasketItemsInnerItemDimension(
        )
        """

    def testCrossBorderQuotesRequestBasketItemsInnerItemDimension(self):
        """Test CrossBorderQuotesRequestBasketItemsInnerItemDimension"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
