# coding: utf-8

"""
    pymetrics API

    ### This is pymetrics's public API. The API can be used to get information on candidates as part of a job application workflow, or for employee career pathing and development. The typical use case for this is to support an externally initiated assessment for a candidate job application. This is often done \"inline\" with the candidate's application, or asynchronously after the candidate submits their application. This data can then be used for career pathing and employee development in subsequent stages.  The expected sequence of API calls is: * `Generate OAuth Token` with the OAuth Client ID and Secret you've been provided * `Get Assessment Configurations` to determine which configured assessment templates are available * `Create Assessment Order` for a selected Assessment and candidate job application * `Get Assessment Order` to receive the recommendation results and reports, once they are available  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from pymetrics_soft_skills_sdk.configuration import Configuration


class MercuryReport(object):
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
        'report_type': 'PontemReportTypes',
        'download_url': 'str',
        'create_date': 'datetime',
        'modify_date': 'datetime'
    }

    attribute_map = {
        'report_type': 'report_type',
        'download_url': 'download_url',
        'create_date': 'create_date',
        'modify_date': 'modify_date'
    }

    def __init__(self, report_type=None, download_url=None, create_date=None, modify_date=None, local_vars_configuration=None):  # noqa: E501
        """MercuryReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._report_type = None
        self._download_url = None
        self._create_date = None
        self._modify_date = None
        self.discriminator = None

        self.report_type = report_type
        self.download_url = download_url
        self.create_date = create_date
        self.modify_date = modify_date

    @property
    def report_type(self):
        """Gets the report_type of this MercuryReport.  # noqa: E501


        :return: The report_type of this MercuryReport.  # noqa: E501
        :rtype: PontemReportTypes
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this MercuryReport.


        :param report_type: The report_type of this MercuryReport.  # noqa: E501
        :type report_type: PontemReportTypes
        """
        if self.local_vars_configuration.client_side_validation and report_type is None:  # noqa: E501
            raise ValueError("Invalid value for `report_type`, must not be `None`")  # noqa: E501

        self._report_type = report_type

    @property
    def download_url(self):
        """Gets the download_url of this MercuryReport.  # noqa: E501

        This is a presigned URL to download a report from.  # noqa: E501

        :return: The download_url of this MercuryReport.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this MercuryReport.

        This is a presigned URL to download a report from.  # noqa: E501

        :param download_url: The download_url of this MercuryReport.  # noqa: E501
        :type download_url: str
        """
        if self.local_vars_configuration.client_side_validation and download_url is None:  # noqa: E501
            raise ValueError("Invalid value for `download_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                download_url is not None and len(download_url) > 65536):
            raise ValueError("Invalid value for `download_url`, length must be less than or equal to `65536`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                download_url is not None and len(download_url) < 1):
            raise ValueError("Invalid value for `download_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._download_url = download_url

    @property
    def create_date(self):
        """Gets the create_date of this MercuryReport.  # noqa: E501


        :return: The create_date of this MercuryReport.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this MercuryReport.


        :param create_date: The create_date of this MercuryReport.  # noqa: E501
        :type create_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_date is None:  # noqa: E501
            raise ValueError("Invalid value for `create_date`, must not be `None`")  # noqa: E501

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this MercuryReport.  # noqa: E501


        :return: The modify_date of this MercuryReport.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this MercuryReport.


        :param modify_date: The modify_date of this MercuryReport.  # noqa: E501
        :type modify_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and modify_date is None:  # noqa: E501
            raise ValueError("Invalid value for `modify_date`, must not be `None`")  # noqa: E501

        self._modify_date = modify_date

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
        if not isinstance(other, MercuryReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MercuryReport):
            return True

        return self.to_dict() != other.to_dict()
