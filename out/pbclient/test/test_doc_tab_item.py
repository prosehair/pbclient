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
from pbclient.models.doc_tab_item import DocTabItem  # noqa: E501
from pbclient.rest import ApiException

class TestDocTabItem(unittest.TestCase):
    """DocTabItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DocTabItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocTabItem`
        """
        model = pbclient.models.doc_tab_item.DocTabItem()  # noqa: E501
        if include_optional :
            return DocTabItem(
                display_name = '', 
                name = '', 
                value = ''
            )
        else :
            return DocTabItem(
        )
        """

    def testDocTabItem(self):
        """Test DocTabItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
