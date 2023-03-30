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
from pbclient.models.cross_border_quotes_request_basket_items_inner import CrossBorderQuotesRequestBasketItemsInner  # noqa: E501
from pbclient.rest import ApiException

class TestCrossBorderQuotesRequestBasketItemsInner(unittest.TestCase):
    """CrossBorderQuotesRequestBasketItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CrossBorderQuotesRequestBasketItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CrossBorderQuotesRequestBasketItemsInner`
        """
        model = pbclient.models.cross_border_quotes_request_basket_items_inner.CrossBorderQuotesRequestBasketItemsInner()  # noqa: E501
        if include_optional :
            return CrossBorderQuotesRequestBasketItemsInner(
                item_id = '', 
                categories = [
                    pbclient.models.cross_border_quotes_request_basket_items_inner_categories_inner.CrossBorderQuotesRequest_basketItems_inner_categories_inner(
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
                        url = '', )
                    ], 
                description = '', 
                long_description = '', 
                unit_weight = pbclient.models.cross_border_quotes_request_basket_items_inner_unit_weight.CrossBorderQuotesRequest_basketItems_inner_unitWeight(
                    weight = 56, 
                    unit_of_measurement = '', ), 
                item_dimension = pbclient.models.cross_border_quotes_request_basket_items_inner_item_dimension.CrossBorderQuotesRequest_basketItems_inner_itemDimension(
                    length = 56, 
                    height = 1.337, 
                    width = 56, 
                    unit_of_measurement = '', ), 
                url = '', 
                quantity = 56, 
                unit_price = 1.337, 
                origin_country_code = '', 
                parent_identifier = '', 
                child_identifier = '', 
                kit = '', 
                kit_identifier = '', 
                kit_quantity = '', 
                manufacturer = '', 
                brand = '', 
                eccn = '', 
                enabled = True, 
                pricing = pbclient.models.cross_border_quotes_request_basket_items_inner_pricing.CrossBorderQuotesRequest_basketItems_inner_pricing(
                    price = 56, 
                    cod_price = [
                        pbclient.models.cross_border_quotes_request_basket_items_inner_pricing_cod_price_inner.CrossBorderQuotesRequest_basketItems_inner_pricing_codPrice_inner(
                            price = 56, 
                            cod = '', 
                            includes_duty = True, 
                            includes_taxes = True, )
                        ], 
                    dutiable_value = 56, ), 
                h_s_tariff_code = '', 
                h_s_tariff_code_country = '', 
                identifiers = [
                    pbclient.models.cross_border_quotes_request_basket_items_inner_identifiers_inner.CrossBorderQuotesRequest_basketItems_inner_identifiers_inner(
                        number = '', 
                        source = '', )
                    ], 
                image_urls = [
                    ''
                    ], 
                ships_alone = True, 
                attributes = [
                    pbclient.models.cross_border_quotes_request_basket_items_inner_attributes_inner.CrossBorderQuotesRequest_basketItems_inner_attributes_inner(
                        type = '', 
                        name = '', 
                        value = '', )
                    ], 
                hazmats = [
                    ''
                    ]
            )
        else :
            return CrossBorderQuotesRequestBasketItemsInner(
        )
        """

    def testCrossBorderQuotesRequestBasketItemsInner(self):
        """Test CrossBorderQuotesRequestBasketItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
