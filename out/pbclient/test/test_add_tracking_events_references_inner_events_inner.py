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
from pbclient.models.add_tracking_events_references_inner_events_inner import AddTrackingEventsReferencesInnerEventsInner  # noqa: E501
from pbclient.rest import ApiException

class TestAddTrackingEventsReferencesInnerEventsInner(unittest.TestCase):
    """AddTrackingEventsReferencesInnerEventsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddTrackingEventsReferencesInnerEventsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddTrackingEventsReferencesInnerEventsInner`
        """
        model = pbclient.models.add_tracking_events_references_inner_events_inner.AddTrackingEventsReferencesInnerEventsInner()  # noqa: E501
        if include_optional :
            return AddTrackingEventsReferencesInnerEventsInner(
                event_code = '', 
                carrier_event_code = '', 
                event_date = '', 
                event_time = '', 
                event_time_offset = '', 
                event_city = '', 
                event_state_or_province = '', 
                postal_code = '', 
                country = ''
            )
        else :
            return AddTrackingEventsReferencesInnerEventsInner(
        )
        """

    def testAddTrackingEventsReferencesInnerEventsInner(self):
        """Test AddTrackingEventsReferencesInnerEventsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
