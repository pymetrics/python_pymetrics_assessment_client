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


class MercuryCandidate(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'external_id': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'external_id': 'external_id'
    }

    def __init__(self, first_name=None, last_name=None, email=None, external_id=None, local_vars_configuration=None):  # noqa: E501
        """MercuryCandidate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._first_name = None
        self._last_name = None
        self._email = None
        self._external_id = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.email = email
        if external_id is not None:
            self.external_id = external_id

    @property
    def first_name(self):
        """Gets the first_name of this MercuryCandidate.  # noqa: E501


        :return: The first_name of this MercuryCandidate.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MercuryCandidate.


        :param first_name: The first_name of this MercuryCandidate.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MercuryCandidate.  # noqa: E501


        :return: The last_name of this MercuryCandidate.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MercuryCandidate.


        :param last_name: The last_name of this MercuryCandidate.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this MercuryCandidate.  # noqa: E501

        One component of the uniqueness and idempotency criteria. This should be your candidate's email address, and will be used as their pymetrics username.  # noqa: E501

        :return: The email of this MercuryCandidate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MercuryCandidate.

        One component of the uniqueness and idempotency criteria. This should be your candidate's email address, and will be used as their pymetrics username.  # noqa: E501

        :param email: The email of this MercuryCandidate.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def external_id(self):
        """Gets the external_id of this MercuryCandidate.  # noqa: E501


        :return: The external_id of this MercuryCandidate.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this MercuryCandidate.


        :param external_id: The external_id of this MercuryCandidate.  # noqa: E501
        :type external_id: str
        """

        self._external_id = external_id

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
        if not isinstance(other, MercuryCandidate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MercuryCandidate):
            return True

        return self.to_dict() != other.to_dict()
