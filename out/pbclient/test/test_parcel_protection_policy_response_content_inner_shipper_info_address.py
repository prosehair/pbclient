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
from pbclient.models.parcel_protection_policy_response_content_inner_shipper_info_address import ParcelProtectionPolicyResponseContentInnerShipperInfoAddress  # noqa: E501
from pbclient.rest import ApiException

class TestParcelProtectionPolicyResponseContentInnerShipperInfoAddress(unittest.TestCase):
    """ParcelProtectionPolicyResponseContentInnerShipperInfoAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionPolicyResponseContentInnerShipperInfoAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParcelProtectionPolicyResponseContentInnerShipperInfoAddress`
        """
        model = pbclient.models.parcel_protection_policy_response_content_inner_shipper_info_address.ParcelProtectionPolicyResponseContentInnerShipperInfoAddress()  # noqa: E501
        if include_optional :
            return ParcelProtectionPolicyResponseContentInnerShipperInfoAddress(
                street1 = '', 
                street2 = '', 
                street3 = '', 
                city = '', 
                region = '', 
                country = '', 
                postal_code = ''
            )
        else :
            return ParcelProtectionPolicyResponseContentInnerShipperInfoAddress(
        )
        """

    def testParcelProtectionPolicyResponseContentInnerShipperInfoAddress(self):
        """Test ParcelProtectionPolicyResponseContentInnerShipperInfoAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
