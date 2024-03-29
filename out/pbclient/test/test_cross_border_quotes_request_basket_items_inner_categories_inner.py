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
from pbclient.models.cross_border_quotes_request_basket_items_inner_categories_inner import CrossBorderQuotesRequestBasketItemsInnerCategoriesInner  # noqa: E501
from pbclient.rest import ApiException

class TestCrossBorderQuotesRequestBasketItemsInnerCategoriesInner(unittest.TestCase):
    """CrossBorderQuotesRequestBasketItemsInnerCategoriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesRequestBasketItemsInnerCategoriesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrossBorderQuotesRequestBasketItemsInnerCategoriesInner`
        """
        model = pbclient.models.cross_border_quotes_request_basket_items_inner_categories_inner.CrossBorderQuotesRequestBasketItemsInnerCategoriesInner()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesRequestBasketItemsInnerCategoriesInner(
                category_code = '', 
                descriptions = [
                    pbclient.models.cross_border_quotes_request_basket_items_inner_categories_inner_descriptions_inner.CrossBorderQuotesRequest_basketItems_inner_categories_inner_descriptions_inner(
                        locale = '', 
                        name = '', 
                        parents_names = [
                            ''
                            ], )
                    ], 
                parent_category_code = '', 
                url = ''
            )
        else :
            return CrossBorderQuotesRequestBasketItemsInnerCategoriesInner(
        )
        """

    def testCrossBorderQuotesRequestBasketItemsInnerCategoriesInner(self):
        """Test CrossBorderQuotesRequestBasketItemsInnerCategoriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
