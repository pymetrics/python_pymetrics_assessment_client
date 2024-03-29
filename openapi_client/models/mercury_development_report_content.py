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

from openapi_client.configuration import Configuration


class MercuryDevelopmentReportContent(object):
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
        'results': 'str',
        'strengths': 'str',
        'maximize_strengths': 'list[str]',
        'ways_to_develop': 'list[str]',
        'opportunities': 'str'
    }

    attribute_map = {
        'results': 'results',
        'strengths': 'strengths',
        'maximize_strengths': 'maximize_strengths',
        'ways_to_develop': 'ways_to_develop',
        'opportunities': 'opportunities'
    }

    def __init__(self, results=None, strengths=None, maximize_strengths=None, ways_to_develop=None, opportunities=None, local_vars_configuration=None):  # noqa: E501
        """MercuryDevelopmentReportContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._results = None
        self._strengths = None
        self._maximize_strengths = None
        self._ways_to_develop = None
        self._opportunities = None
        self.discriminator = None

        self.results = results
        self.strengths = strengths
        self.maximize_strengths = maximize_strengths
        self.ways_to_develop = ways_to_develop
        self.opportunities = opportunities

    @property
    def results(self):
        """Gets the results of this MercuryDevelopmentReportContent.  # noqa: E501


        :return: The results of this MercuryDevelopmentReportContent.  # noqa: E501
        :rtype: str
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this MercuryDevelopmentReportContent.


        :param results: The results of this MercuryDevelopmentReportContent.  # noqa: E501
        :type results: str
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def strengths(self):
        """Gets the strengths of this MercuryDevelopmentReportContent.  # noqa: E501


        :return: The strengths of this MercuryDevelopmentReportContent.  # noqa: E501
        :rtype: str
        """
        return self._strengths

    @strengths.setter
    def strengths(self, strengths):
        """Sets the strengths of this MercuryDevelopmentReportContent.


        :param strengths: The strengths of this MercuryDevelopmentReportContent.  # noqa: E501
        :type strengths: str
        """
        if self.local_vars_configuration.client_side_validation and strengths is None:  # noqa: E501
            raise ValueError("Invalid value for `strengths`, must not be `None`")  # noqa: E501

        self._strengths = strengths

    @property
    def maximize_strengths(self):
        """Gets the maximize_strengths of this MercuryDevelopmentReportContent.  # noqa: E501


        :return: The maximize_strengths of this MercuryDevelopmentReportContent.  # noqa: E501
        :rtype: list[str]
        """
        return self._maximize_strengths

    @maximize_strengths.setter
    def maximize_strengths(self, maximize_strengths):
        """Sets the maximize_strengths of this MercuryDevelopmentReportContent.


        :param maximize_strengths: The maximize_strengths of this MercuryDevelopmentReportContent.  # noqa: E501
        :type maximize_strengths: list[str]
        """
        if self.local_vars_configuration.client_side_validation and maximize_strengths is None:  # noqa: E501
            raise ValueError("Invalid value for `maximize_strengths`, must not be `None`")  # noqa: E501

        self._maximize_strengths = maximize_strengths

    @property
    def ways_to_develop(self):
        """Gets the ways_to_develop of this MercuryDevelopmentReportContent.  # noqa: E501


        :return: The ways_to_develop of this MercuryDevelopmentReportContent.  # noqa: E501
        :rtype: list[str]
        """
        return self._ways_to_develop

    @ways_to_develop.setter
    def ways_to_develop(self, ways_to_develop):
        """Sets the ways_to_develop of this MercuryDevelopmentReportContent.


        :param ways_to_develop: The ways_to_develop of this MercuryDevelopmentReportContent.  # noqa: E501
        :type ways_to_develop: list[str]
        """
        if self.local_vars_configuration.client_side_validation and ways_to_develop is None:  # noqa: E501
            raise ValueError("Invalid value for `ways_to_develop`, must not be `None`")  # noqa: E501

        self._ways_to_develop = ways_to_develop

    @property
    def opportunities(self):
        """Gets the opportunities of this MercuryDevelopmentReportContent.  # noqa: E501


        :return: The opportunities of this MercuryDevelopmentReportContent.  # noqa: E501
        :rtype: str
        """
        return self._opportunities

    @opportunities.setter
    def opportunities(self, opportunities):
        """Sets the opportunities of this MercuryDevelopmentReportContent.


        :param opportunities: The opportunities of this MercuryDevelopmentReportContent.  # noqa: E501
        :type opportunities: str
        """
        if self.local_vars_configuration.client_side_validation and opportunities is None:  # noqa: E501
            raise ValueError("Invalid value for `opportunities`, must not be `None`")  # noqa: E501

        self._opportunities = opportunities

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
        if not isinstance(other, MercuryDevelopmentReportContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MercuryDevelopmentReportContent):
            return True

        return self.to_dict() != other.to_dict()
