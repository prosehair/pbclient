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
from pbclient.models.container_manifest_response import ContainerManifestResponse  # noqa: E501
from pbclient.rest import ApiException

class TestContainerManifestResponse(unittest.TestCase):
    """ContainerManifestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContainerManifestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContainerManifestResponse`
        """
        model = pbclient.models.container_manifest_response.ContainerManifestResponse()  # noqa: E501
        if include_optional :
            return ContainerManifestResponse(
                data = pbclient.models.container_manifest_response_data.ContainerManifestResponse_data(
                    pb_container_id = '', 
                    label_data = '', )
            )
        else :
            return ContainerManifestResponse(
        )
        """

    def testContainerManifestResponse(self):
        """Test ContainerManifestResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
