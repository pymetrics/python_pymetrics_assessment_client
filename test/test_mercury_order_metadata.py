# coding: utf-8

"""
    pymetrics API

    ### This is pymetrics's public API. The API can be used to get information on candidates as part of a job application workflow, or for employee career pathing and development. The typical use case for this is to support an externally initiated assessment for a candidate job application. This is often done \"inline\" with the candidate's application, or asynchronously after the candidate submits their application. This data can then be used for career pathing and employee development in subsequent stages.  The expected sequence of API calls is: * `Generate OAuth Token` with the OAuth Client ID and Secret you've been provided * `Get Assessment Configurations` to determine which configured assessment templates are available * `Create Assessment Order` for a selected Assessment and candidate job application * `Get Assessment Order` to receive the recommendation results and reports, once they are available  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.mercury_order_metadata import MercuryOrderMetadata  # noqa: E501
from openapi_client.rest import ApiException

class TestMercuryOrderMetadata(unittest.TestCase):
    """MercuryOrderMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MercuryOrderMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.mercury_order_metadata.MercuryOrderMetadata()  # noqa: E501
        if include_optional :
            return MercuryOrderMetadata(
                id = '', 
                status = 'Rejected', 
                assessment_id = '', 
                implementation_id = ''
            )
        else :
            return MercuryOrderMetadata(
                id = '',
                status = 'Rejected',
                assessment_id = '',
                implementation_id = '',
        )

    def testMercuryOrderMetadata(self):
        """Test MercuryOrderMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()