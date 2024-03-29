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
from pbclient.models.parcel_protection_create_request_shipment_info_shipper_info import ParcelProtectionCreateRequestShipmentInfoShipperInfo  # noqa: E501
from pbclient.rest import ApiException

class TestParcelProtectionCreateRequestShipmentInfoShipperInfo(unittest.TestCase):
    """ParcelProtectionCreateRequestShipmentInfoShipperInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionCreateRequestShipmentInfoShipperInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParcelProtectionCreateRequestShipmentInfoShipperInfo`
        """
        model = pbclient.models.parcel_protection_create_request_shipment_info_shipper_info.ParcelProtectionCreateRequestShipmentInfoShipperInfo()  # noqa: E501
        if include_optional :
            return ParcelProtectionCreateRequestShipmentInfoShipperInfo(
                shipper_id = '', 
                address = pbclient.models.parcel_protection_create_request_shipment_info_shipper_info_address.ParcelProtectionCreateRequest_shipmentInfo_shipperInfo_address(
                    address_lines = [
                        ''
                        ], 
                    city_town = '', 
                    state_province = '', 
                    postal_code = '', 
                    country_code = '', ), 
                company_name = '', 
                family_name = '', 
                given_name = '', 
                middle_name = '', 
                email = '', 
                phone_numbers = [
                    pbclient.models.phone_numbers_inner.PhoneNumbers_inner(
                        number = '', 
                        type = '', )
                    ]
            )
        else :
            return ParcelProtectionCreateRequestShipmentInfoShipperInfo(
        )
        """

    def testParcelProtectionCreateRequestShipmentInfoShipperInfo(self):
        """Test ParcelProtectionCreateRequestShipmentInfoShipperInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
