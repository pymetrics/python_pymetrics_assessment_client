# coding: utf-8

"""
    pymetrics Assessment API

    ### This is pymetrics's public API for assessments, usually as part of a job application workflow. The typical use case for this is to support an externally initiated assessment for a candidate job application. This is often done \"inline\" with the candidate's application, or asynchronously after the candidate submits their application.  The expected sequence of API calls is: * `Generate OAuth Token` with the OAuth Client ID and Secret you've been provided * `Get Assessment Configurations` to determine which configured assessment templates are available * `Create Assessment Order` for a selected Assessment and candidate job application * `Get Assessment Order` to receive the recommendation results, once they are available  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.order_request import OrderRequest  # noqa: E501
from openapi_client.rest import ApiException

class TestOrderRequest(unittest.TestCase):
    """OrderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrderRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.order_request.OrderRequest()  # noqa: E501
        if include_optional :
            return OrderRequest(
                candidate = openapi_client.models.mercury_candidate.MercuryCandidate(
                    first_name = '', 
                    last_name = '', 
                    email = '', 
                    external_id = '', ), 
                assessment_id = '', 
                send_email = True, 
                application_id = '', 
                requisition_id = '', 
                requisition_title = '', 
                metadata = {},
                candidate_redirect_url = '0'
            )
        else :
            return OrderRequest(
                candidate = openapi_client.models.mercury_candidate.MercuryCandidate(
                    first_name = '', 
                    last_name = '', 
                    email = '', 
                    external_id = '', ),
                assessment_id = '',
                application_id = '',
        )

    def testOrderRequest(self):
        """Test OrderRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
