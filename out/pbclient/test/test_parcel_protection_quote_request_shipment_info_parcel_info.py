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
from pbclient.models.parcel_protection_quote_request_shipment_info_parcel_info import ParcelProtectionQuoteRequestShipmentInfoParcelInfo  # noqa: E501
from pbclient.rest import ApiException

class TestParcelProtectionQuoteRequestShipmentInfoParcelInfo(unittest.TestCase):
    """ParcelProtectionQuoteRequestShipmentInfoParcelInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionQuoteRequestShipmentInfoParcelInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParcelProtectionQuoteRequestShipmentInfoParcelInfo`
        """
        model = pbclient.models.parcel_protection_quote_request_shipment_info_parcel_info.ParcelProtectionQuoteRequestShipmentInfoParcelInfo()  # noqa: E501
        if include_optional :
            return ParcelProtectionQuoteRequestShipmentInfoParcelInfo(
                commodity_list = [
                    pbclient.models.parcel_protection_quote_request_shipment_info_parcel_info_commodity_list_inner.ParcelProtectionQuoteRequest_shipmentInfo_parcelInfo_commodityList_inner(
                        category_path = '', 
                        item_code = '', 
                        name = '', 
                        url = '', )
                    ]
            )
        else :
            return ParcelProtectionQuoteRequestShipmentInfoParcelInfo(
                commodity_list = [
                    pbclient.models.parcel_protection_quote_request_shipment_info_parcel_info_commodity_list_inner.ParcelProtectionQuoteRequest_shipmentInfo_parcelInfo_commodityList_inner(
                        category_path = '', 
                        item_code = '', 
                        name = '', 
                        url = '', )
                    ],
        )
        """

    def testParcelProtectionQuoteRequestShipmentInfoParcelInfo(self):
        """Test ParcelProtectionQuoteRequestShipmentInfoParcelInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
