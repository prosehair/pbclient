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
from pbclient.models.radio_nuclide_detail import RadioNuclideDetail  # noqa: E501
from pbclient.rest import ApiException

class TestRadioNuclideDetail(unittest.TestCase):
    """RadioNuclideDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RadioNuclideDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RadioNuclideDetail`
        """
        model = pbclient.models.radio_nuclide_detail.RadioNuclideDetail()  # noqa: E501
        if include_optional :
            return RadioNuclideDetail(
                chemical_form = '', 
                expected_package_reportable_quantity = True, 
                physical_form = '', 
                radio_nuclide = '', 
                radio_nuclide_activity_uom = '', 
                radio_nuclide_activity_value = 1.337
            )
        else :
            return RadioNuclideDetail(
        )
        """

    def testRadioNuclideDetail(self):
        """Test RadioNuclideDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
