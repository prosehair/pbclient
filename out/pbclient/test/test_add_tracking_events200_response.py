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
from pbclient.models.add_tracking_events200_response import AddTrackingEvents200Response  # noqa: E501
from pbclient.rest import ApiException

class TestAddTrackingEvents200Response(unittest.TestCase):
    """AddTrackingEvents200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddTrackingEvents200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddTrackingEvents200Response`
        """
        model = pbclient.models.add_tracking_events200_response.AddTrackingEvents200Response()  # noqa: E501
        if include_optional :
            return AddTrackingEvents200Response(
                status = ''
            )
        else :
            return AddTrackingEvents200Response(
        )
        """

    def testAddTrackingEvents200Response(self):
        """Test AddTrackingEvents200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
