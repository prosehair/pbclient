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

import pbclient
from pbclient.api.rate_parcels_api import RateParcelsApi  # noqa: E501
from pbclient.rest import ApiException


class TestRateParcelsApi(unittest.TestCase):
    """RateParcelsApi unit test stubs"""

    def setUp(self):
        self.api = pbclient.api.rate_parcels_api.RateParcelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rate_parcel(self):
        """Test case for rate_parcel

        Use this operation to rate a parcel before you print and purchase a shipment label. You can rate a parcel for multiple services and multiple parcel types with a single API request.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
