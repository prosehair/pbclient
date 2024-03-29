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
from pbclient.models.tracking_response_scan_details_list_inner import TrackingResponseScanDetailsListInner  # noqa: E501
from pbclient.rest import ApiException

class TestTrackingResponseScanDetailsListInner(unittest.TestCase):
    """TrackingResponseScanDetailsListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TrackingResponseScanDetailsListInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackingResponseScanDetailsListInner`
        """
        model = pbclient.models.tracking_response_scan_details_list_inner.TrackingResponseScanDetailsListInner()  # noqa: E501
        if include_optional :
            return TrackingResponseScanDetailsListInner(
                event_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                event_time = '', 
                event_city = '', 
                event_state_or_province = '', 
                postal_code = 56, 
                country = '', 
                scan_type = '', 
                scan_description = '', 
                package_status = ''
            )
        else :
            return TrackingResponseScanDetailsListInner(
        )
        """

    def testTrackingResponseScanDetailsListInner(self):
        """Test TrackingResponseScanDetailsListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
