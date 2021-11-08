# coding: utf-8

"""
    pymetrics Assessment API

    ### This is pymetrics's public API for assessments, usually as part of a job application workflow. The typical use case for this is to support an externally initiated assessment for a candidate job application. This is often done \"inline\" with the candidate's application, or asynchronously after the candidate submits their application.  The expected sequence of API calls is: * `Generate OAuth Token` with the OAuth Client ID and Secret you've been provided * `Get Assessment Configurations` to determine which configured assessment templates are available * `Create Assessment Order` for a selected Assessment and candidate job application * `Get Assessment Order` to receive the recommendation results, once they are available  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class MercuryAssessmentOrder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'invite_link': 'str',
        'status': 'PontemOrderStatuses',
        'create_date': 'datetime',
        'candidate': 'MercuryCandidate',
        'assessment_id': 'str',
        'assessment': 'MercuryAssessment',
        'application_id': 'str',
        'ats_type': 'AtsType',
        'requisition_id': 'str',
        'requisition_title': 'str',
        'metadata': 'object',
        'recruiter_report': 'str',
        'results': 'list[MercuryResult]',
        'reports': 'list[MercuryReport]',
        'candidate_redirect_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'invite_link': 'invite_link',
        'status': 'status',
        'create_date': 'create_date',
        'candidate': 'candidate',
        'assessment_id': 'assessment_id',
        'assessment': 'assessment',
        'application_id': 'application_id',
        'ats_type': 'ats_type',
        'requisition_id': 'requisition_id',
        'requisition_title': 'requisition_title',
        'metadata': 'metadata',
        'recruiter_report': 'recruiter_report',
        'results': 'results',
        'reports': 'reports',
        'candidate_redirect_url': 'candidate_redirect_url'
    }

    def __init__(self, id=None, invite_link=None, status=None, create_date=None, candidate=None, assessment_id=None, assessment=None, application_id=None, ats_type=None, requisition_id=None, requisition_title=None, metadata=None, recruiter_report=None, results=None, reports=None, candidate_redirect_url=None, local_vars_configuration=None):  # noqa: E501
        """MercuryAssessmentOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._invite_link = None
        self._status = None
        self._create_date = None
        self._candidate = None
        self._assessment_id = None
        self._assessment = None
        self._application_id = None
        self._ats_type = None
        self._requisition_id = None
        self._requisition_title = None
        self._metadata = None
        self._recruiter_report = None
        self._results = None
        self._reports = None
        self._candidate_redirect_url = None
        self.discriminator = None

        self.id = id
        self.invite_link = invite_link
        self.status = status
        self.create_date = create_date
        self.candidate = candidate
        self.assessment_id = assessment_id
        self.assessment = assessment
        self.application_id = application_id
        self.ats_type = ats_type
        if requisition_id is not None:
            self.requisition_id = requisition_id
        if requisition_title is not None:
            self.requisition_title = requisition_title
        if metadata is not None:
            self.metadata = metadata
        if recruiter_report is not None:
            self.recruiter_report = recruiter_report
        if results is not None:
            self.results = results
        if reports is not None:
            self.reports = reports
        if candidate_redirect_url is not None:
            self.candidate_redirect_url = candidate_redirect_url

    @property
    def id(self):
        """Gets the id of this MercuryAssessmentOrder.  # noqa: E501


        :return: The id of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MercuryAssessmentOrder.


        :param id: The id of this MercuryAssessmentOrder.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def invite_link(self):
        """Gets the invite_link of this MercuryAssessmentOrder.  # noqa: E501


        :return: The invite_link of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._invite_link

    @invite_link.setter
    def invite_link(self, invite_link):
        """Sets the invite_link of this MercuryAssessmentOrder.


        :param invite_link: The invite_link of this MercuryAssessmentOrder.  # noqa: E501
        :type invite_link: str
        """
        if self.local_vars_configuration.client_side_validation and invite_link is None:  # noqa: E501
            raise ValueError("Invalid value for `invite_link`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                invite_link is not None and len(invite_link) > 65536):
            raise ValueError("Invalid value for `invite_link`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                invite_link is not None and len(invite_link) < 1):
            raise ValueError("Invalid value for `invite_link`, length must be greater than or equal to `1`")  # noqa: E501

        self._invite_link = invite_link

    @property
    def status(self):
        """Gets the status of this MercuryAssessmentOrder.  # noqa: E501


        :return: The status of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: PontemOrderStatuses
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MercuryAssessmentOrder.


        :param status: The status of this MercuryAssessmentOrder.  # noqa: E501
        :type status: PontemOrderStatuses
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def create_date(self):
        """Gets the create_date of this MercuryAssessmentOrder.  # noqa: E501


        :return: The create_date of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this MercuryAssessmentOrder.


        :param create_date: The create_date of this MercuryAssessmentOrder.  # noqa: E501
        :type create_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_date is None:  # noqa: E501
            raise ValueError("Invalid value for `create_date`, must not be `None`")  # noqa: E501

        self._create_date = create_date

    @property
    def candidate(self):
        """Gets the candidate of this MercuryAssessmentOrder.  # noqa: E501


        :return: The candidate of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: MercuryCandidate
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """Sets the candidate of this MercuryAssessmentOrder.


        :param candidate: The candidate of this MercuryAssessmentOrder.  # noqa: E501
        :type candidate: MercuryCandidate
        """
        if self.local_vars_configuration.client_side_validation and candidate is None:  # noqa: E501
            raise ValueError("Invalid value for `candidate`, must not be `None`")  # noqa: E501

        self._candidate = candidate

    @property
    def assessment_id(self):
        """Gets the assessment_id of this MercuryAssessmentOrder.  # noqa: E501

        Deprecated. Will be removed in a future version. Use assessment object instead  # noqa: E501

        :return: The assessment_id of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._assessment_id

    @assessment_id.setter
    def assessment_id(self, assessment_id):
        """Sets the assessment_id of this MercuryAssessmentOrder.

        Deprecated. Will be removed in a future version. Use assessment object instead  # noqa: E501

        :param assessment_id: The assessment_id of this MercuryAssessmentOrder.  # noqa: E501
        :type assessment_id: str
        """
        if self.local_vars_configuration.client_side_validation and assessment_id is None:  # noqa: E501
            raise ValueError("Invalid value for `assessment_id`, must not be `None`")  # noqa: E501

        self._assessment_id = assessment_id

    @property
    def assessment(self):
        """Gets the assessment of this MercuryAssessmentOrder.  # noqa: E501


        :return: The assessment of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: MercuryAssessment
        """
        return self._assessment

    @assessment.setter
    def assessment(self, assessment):
        """Sets the assessment of this MercuryAssessmentOrder.


        :param assessment: The assessment of this MercuryAssessmentOrder.  # noqa: E501
        :type assessment: MercuryAssessment
        """
        if self.local_vars_configuration.client_side_validation and assessment is None:  # noqa: E501
            raise ValueError("Invalid value for `assessment`, must not be `None`")  # noqa: E501

        self._assessment = assessment

    @property
    def application_id(self):
        """Gets the application_id of this MercuryAssessmentOrder.  # noqa: E501


        :return: The application_id of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this MercuryAssessmentOrder.


        :param application_id: The application_id of this MercuryAssessmentOrder.  # noqa: E501
        :type application_id: str
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def ats_type(self):
        """Gets the ats_type of this MercuryAssessmentOrder.  # noqa: E501


        :return: The ats_type of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: AtsType
        """
        return self._ats_type

    @ats_type.setter
    def ats_type(self, ats_type):
        """Sets the ats_type of this MercuryAssessmentOrder.


        :param ats_type: The ats_type of this MercuryAssessmentOrder.  # noqa: E501
        :type ats_type: AtsType
        """
        if self.local_vars_configuration.client_side_validation and ats_type is None:  # noqa: E501
            raise ValueError("Invalid value for `ats_type`, must not be `None`")  # noqa: E501

        self._ats_type = ats_type

    @property
    def requisition_id(self):
        """Gets the requisition_id of this MercuryAssessmentOrder.  # noqa: E501


        :return: The requisition_id of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._requisition_id

    @requisition_id.setter
    def requisition_id(self, requisition_id):
        """Sets the requisition_id of this MercuryAssessmentOrder.


        :param requisition_id: The requisition_id of this MercuryAssessmentOrder.  # noqa: E501
        :type requisition_id: str
        """

        self._requisition_id = requisition_id

    @property
    def requisition_title(self):
        """Gets the requisition_title of this MercuryAssessmentOrder.  # noqa: E501


        :return: The requisition_title of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._requisition_title

    @requisition_title.setter
    def requisition_title(self, requisition_title):
        """Sets the requisition_title of this MercuryAssessmentOrder.


        :param requisition_title: The requisition_title of this MercuryAssessmentOrder.  # noqa: E501
        :type requisition_title: str
        """

        self._requisition_title = requisition_title

    @property
    def metadata(self):
        """Gets the metadata of this MercuryAssessmentOrder.  # noqa: E501


        :return: The metadata of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MercuryAssessmentOrder.


        :param metadata: The metadata of this MercuryAssessmentOrder.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def recruiter_report(self):
        """Gets the recruiter_report of this MercuryAssessmentOrder.  # noqa: E501


        :return: The recruiter_report of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._recruiter_report

    @recruiter_report.setter
    def recruiter_report(self, recruiter_report):
        """Sets the recruiter_report of this MercuryAssessmentOrder.


        :param recruiter_report: The recruiter_report of this MercuryAssessmentOrder.  # noqa: E501
        :type recruiter_report: str
        """
        if (self.local_vars_configuration.client_side_validation and
                recruiter_report is not None and len(recruiter_report) > 65536):
            raise ValueError("Invalid value for `recruiter_report`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                recruiter_report is not None and len(recruiter_report) < 1):
            raise ValueError("Invalid value for `recruiter_report`, length must be greater than or equal to `1`")  # noqa: E501

        self._recruiter_report = recruiter_report

    @property
    def results(self):
        """Gets the results of this MercuryAssessmentOrder.  # noqa: E501


        :return: The results of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: list[MercuryResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this MercuryAssessmentOrder.


        :param results: The results of this MercuryAssessmentOrder.  # noqa: E501
        :type results: list[MercuryResult]
        """

        self._results = results

    @property
    def reports(self):
        """Gets the reports of this MercuryAssessmentOrder.  # noqa: E501


        :return: The reports of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: list[MercuryReport]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this MercuryAssessmentOrder.


        :param reports: The reports of this MercuryAssessmentOrder.  # noqa: E501
        :type reports: list[MercuryReport]
        """

        self._reports = reports

    @property
    def candidate_redirect_url(self):
        """Gets the candidate_redirect_url of this MercuryAssessmentOrder.  # noqa: E501


        :return: The candidate_redirect_url of this MercuryAssessmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._candidate_redirect_url

    @candidate_redirect_url.setter
    def candidate_redirect_url(self, candidate_redirect_url):
        """Sets the candidate_redirect_url of this MercuryAssessmentOrder.


        :param candidate_redirect_url: The candidate_redirect_url of this MercuryAssessmentOrder.  # noqa: E501
        :type candidate_redirect_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                candidate_redirect_url is not None and len(candidate_redirect_url) > 65536):
            raise ValueError("Invalid value for `candidate_redirect_url`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                candidate_redirect_url is not None and len(candidate_redirect_url) < 1):
            raise ValueError("Invalid value for `candidate_redirect_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._candidate_redirect_url = candidate_redirect_url

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MercuryAssessmentOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MercuryAssessmentOrder):
            return True

        return self.to_dict() != other.to_dict()
