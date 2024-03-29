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


class MercuryFactorContent(object):
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
        'name': 'str',
        'definition': 'str',
        'quadrant': 'str',
        'model_directions': 'list[MercuryModelDirection]',
        'high_label': 'str',
        'low_label': 'str',
        'development_report_factor_content': 'MercuryDevelopmentReportContent'
    }

    attribute_map = {
        'name': 'name',
        'definition': 'definition',
        'quadrant': 'quadrant',
        'model_directions': 'model_directions',
        'high_label': 'high_label',
        'low_label': 'low_label',
        'development_report_factor_content': 'development_report_factor_content'
    }

    def __init__(self, name=None, definition=None, quadrant=None, model_directions=None, high_label=None, low_label=None, development_report_factor_content=None, local_vars_configuration=None):  # noqa: E501
        """MercuryFactorContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._definition = None
        self._quadrant = None
        self._model_directions = None
        self._high_label = None
        self._low_label = None
        self._development_report_factor_content = None
        self.discriminator = None

        self.name = name
        self.definition = definition
        self.quadrant = quadrant
        self.model_directions = model_directions
        self.high_label = high_label
        self.low_label = low_label
        if development_report_factor_content is not None:
            self.development_report_factor_content = development_report_factor_content

    @property
    def name(self):
        """Gets the name of this MercuryFactorContent.  # noqa: E501


        :return: The name of this MercuryFactorContent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MercuryFactorContent.


        :param name: The name of this MercuryFactorContent.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def definition(self):
        """Gets the definition of this MercuryFactorContent.  # noqa: E501


        :return: The definition of this MercuryFactorContent.  # noqa: E501
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this MercuryFactorContent.


        :param definition: The definition of this MercuryFactorContent.  # noqa: E501
        :type definition: str
        """
        if self.local_vars_configuration.client_side_validation and definition is None:  # noqa: E501
            raise ValueError("Invalid value for `definition`, must not be `None`")  # noqa: E501

        self._definition = definition

    @property
    def quadrant(self):
        """Gets the quadrant of this MercuryFactorContent.  # noqa: E501


        :return: The quadrant of this MercuryFactorContent.  # noqa: E501
        :rtype: str
        """
        return self._quadrant

    @quadrant.setter
    def quadrant(self, quadrant):
        """Sets the quadrant of this MercuryFactorContent.


        :param quadrant: The quadrant of this MercuryFactorContent.  # noqa: E501
        :type quadrant: str
        """
        if self.local_vars_configuration.client_side_validation and quadrant is None:  # noqa: E501
            raise ValueError("Invalid value for `quadrant`, must not be `None`")  # noqa: E501

        self._quadrant = quadrant

    @property
    def model_directions(self):
        """Gets the model_directions of this MercuryFactorContent.  # noqa: E501


        :return: The model_directions of this MercuryFactorContent.  # noqa: E501
        :rtype: list[MercuryModelDirection]
        """
        return self._model_directions

    @model_directions.setter
    def model_directions(self, model_directions):
        """Sets the model_directions of this MercuryFactorContent.


        :param model_directions: The model_directions of this MercuryFactorContent.  # noqa: E501
        :type model_directions: list[MercuryModelDirection]
        """
        if self.local_vars_configuration.client_side_validation and model_directions is None:  # noqa: E501
            raise ValueError("Invalid value for `model_directions`, must not be `None`")  # noqa: E501

        self._model_directions = model_directions

    @property
    def high_label(self):
        """Gets the high_label of this MercuryFactorContent.  # noqa: E501


        :return: The high_label of this MercuryFactorContent.  # noqa: E501
        :rtype: str
        """
        return self._high_label

    @high_label.setter
    def high_label(self, high_label):
        """Sets the high_label of this MercuryFactorContent.


        :param high_label: The high_label of this MercuryFactorContent.  # noqa: E501
        :type high_label: str
        """
        if self.local_vars_configuration.client_side_validation and high_label is None:  # noqa: E501
            raise ValueError("Invalid value for `high_label`, must not be `None`")  # noqa: E501

        self._high_label = high_label

    @property
    def low_label(self):
        """Gets the low_label of this MercuryFactorContent.  # noqa: E501


        :return: The low_label of this MercuryFactorContent.  # noqa: E501
        :rtype: str
        """
        return self._low_label

    @low_label.setter
    def low_label(self, low_label):
        """Sets the low_label of this MercuryFactorContent.


        :param low_label: The low_label of this MercuryFactorContent.  # noqa: E501
        :type low_label: str
        """
        if self.local_vars_configuration.client_side_validation and low_label is None:  # noqa: E501
            raise ValueError("Invalid value for `low_label`, must not be `None`")  # noqa: E501

        self._low_label = low_label

    @property
    def development_report_factor_content(self):
        """Gets the development_report_factor_content of this MercuryFactorContent.  # noqa: E501


        :return: The development_report_factor_content of this MercuryFactorContent.  # noqa: E501
        :rtype: MercuryDevelopmentReportContent
        """
        return self._development_report_factor_content

    @development_report_factor_content.setter
    def development_report_factor_content(self, development_report_factor_content):
        """Sets the development_report_factor_content of this MercuryFactorContent.


        :param development_report_factor_content: The development_report_factor_content of this MercuryFactorContent.  # noqa: E501
        :type development_report_factor_content: MercuryDevelopmentReportContent
        """

        self._development_report_factor_content = development_report_factor_content

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
        if not isinstance(other, MercuryFactorContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MercuryFactorContent):
            return True

        return self.to_dict() != other.to_dict()
