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
from pbclient.models.parcel_protection_policy_response_content_inner import ParcelProtectionPolicyResponseContentInner  # noqa: E501
from pbclient.rest import ApiException

class TestParcelProtectionPolicyResponseContentInner(unittest.TestCase):
    """ParcelProtectionPolicyResponseContentInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionPolicyResponseContentInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParcelProtectionPolicyResponseContentInner`
        """
        model = pbclient.models.parcel_protection_policy_response_content_inner.ParcelProtectionPolicyResponseContentInner()  # noqa: E501
        if include_optional :
            return ParcelProtectionPolicyResponseContentInner(
                transaction_id = '', 
                developer_id = '', 
                subscription_acc_no = '', 
                client_transaction_id = '', 
                policy_details = pbclient.models.parcel_protection_policy_response_content_inner_policy_details.ParcelProtectionPolicyResponse_content_inner_policyDetails(
                    policy_id = '', 
                    policy_date = '', 
                    policy_status = '', 
                    claim_status = '', 
                    claim_status_update_date = '', 
                    value_of_goods = 1.337, 
                    insurance_value = 1.337, 
                    premium_value = 1.337, 
                    base_premium = 1.337, 
                    technology_fee = 1.337, 
                    currency_code = '', 
                    mail_class = '', 
                    mail_class_option = '', ), 
                shipment_details = pbclient.models.parcel_protection_policy_response_content_inner_shipment_details.ParcelProtectionPolicyResponse_content_inner_shipmentDetails(
                    shipment_date = '', 
                    shipment_transaction_id = '', 
                    shipment_id = '', 
                    parcel_tracking_number = '', 
                    carrier = 'USPS', 
                    amount = '', 
                    package_length = '', 
                    package_width = '', 
                    package_height = '', 
                    weight = '', 
                    zone = '', ), 
                shipper_info = pbclient.models.parcel_protection_policy_response_content_inner_shipper_info.ParcelProtectionPolicyResponse_content_inner_shipperInfo(
                    shipper_id = '', 
                    first_name = '', 
                    middle_name = '', 
                    last_name = '', 
                    company = '', 
                    email = '', 
                    phone_number1 = '', 
                    phone_number2 = '', 
                    fax_number = '', 
                    address = pbclient.models.parcel_protection_policy_response_content_inner_shipper_info_address.ParcelProtectionPolicyResponse_content_inner_shipperInfo_address(
                        street1 = '', 
                        street2 = '', 
                        street3 = '', 
                        city = '', 
                        region = '', 
                        country = '', 
                        postal_code = '', ), ), 
                consignee_info = pbclient.models.parcel_protection_policy_response_content_inner_shipper_info.ParcelProtectionPolicyResponse_content_inner_shipperInfo(
                    shipper_id = '', 
                    first_name = '', 
                    middle_name = '', 
                    last_name = '', 
                    company = '', 
                    email = '', 
                    phone_number1 = '', 
                    phone_number2 = '', 
                    fax_number = '', 
                    address = pbclient.models.parcel_protection_policy_response_content_inner_shipper_info_address.ParcelProtectionPolicyResponse_content_inner_shipperInfo_address(
                        street1 = '', 
                        street2 = '', 
                        street3 = '', 
                        city = '', 
                        region = '', 
                        country = '', 
                        postal_code = '', ), ), 
                created_at = '', 
                updated_at = ''
            )
        else :
            return ParcelProtectionPolicyResponseContentInner(
        )
        """

    def testParcelProtectionPolicyResponseContentInner(self):
        """Test ParcelProtectionPolicyResponseContentInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
