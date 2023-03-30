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
from pbclient.models.parcel import Parcel  # noqa: E501
from pbclient.rest import ApiException

class TestParcel(unittest.TestCase):
    """Parcel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Parcel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Parcel`
        """
        model = pbclient.models.parcel.Parcel()  # noqa: E501
        if include_optional :
            return Parcel(
                dimension = pbclient.models.parcel_dimension.ParcelDimension(
                    length = 1.337, 
                    height = 1.337, 
                    width = 1.337, 
                    unit_of_measurement = 'CM', 
                    irregular_parcel_girth = 1.337, ), 
                weight = pbclient.models.parcel_weight.ParcelWeight(
                    unit_of_measurement = 'GM', ), 
                value_of_goods = 1.337, 
                currency_code = ''
            )
        else :
            return Parcel(
        )
        """

    def testParcel(self):
        """Test Parcel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
