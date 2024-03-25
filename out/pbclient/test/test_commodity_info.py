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
from pbclient.models.commodity_info import CommodityInfo  # noqa: E501
from pbclient.rest import ApiException

class TestCommodityInfo(unittest.TestCase):
    """CommodityInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CommodityInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommodityInfo`
        """
        model = pbclient.models.commodity_info.CommodityInfo()  # noqa: E501
        if include_optional :
            return CommodityInfo(
                cargo_air_craft = True, 
                hazard_class = '', 
                infectious_substance_contact = pbclient.models.infectious_substance_contact.InfectiousSubstanceContact(
                    company_name = '', 
                    contact_id = '', 
                    email_address = '', 
                    person_name = '', 
                    phone_number = '', ), 
                inner_receptacles_quantity = 56, 
                inner_receptacles_quantity_uom = '', 
                packaging_group = '', 
                packaging_instructions = '', 
                percentage = 1.337, 
                proper_shipping_name = '', 
                quantity = 56, 
                quantity_uom = '', 
                radio_activity_detail = pbclient.models.radio_activity_detail.RadioActivityDetail(
                    criticality_safety_index = 1.337, 
                    radio_active_parcel_dimension = pbclient.models.radio_active_parcel_dimension.RadioActiveParcelDimension(
                        uom = 'CM', 
                        height = 1.337, 
                        length = 1.337, 
                        width = 1.337, ), 
                    surface_reading = 1.337, 
                    transport_index = 1.337, ), 
                radio_nuclide_detail = pbclient.models.radio_nuclide_detail.RadioNuclideDetail(
                    chemical_form = '', 
                    expected_package_reportable_quantity = True, 
                    physical_form = '', 
                    radio_nuclide = '', 
                    radio_nuclide_activity_uom = '', 
                    radio_nuclide_activity_value = 1.337, ), 
                reportable_quantity = True, 
                technical_name = '', 
                un_id = ''
            )
        else :
            return CommodityInfo(
        )
        """

    def testCommodityInfo(self):
        """Test CommodityInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
