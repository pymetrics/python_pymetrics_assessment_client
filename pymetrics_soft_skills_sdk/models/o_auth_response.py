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


class OAuthResponse(object):
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
        'access_token': 'str',
        'token_type': 'str',
        'expires_in': 'int',
        'scope': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type',
        'expires_in': 'expires_in',
        'scope': 'scope'
    }

    def __init__(self, access_token=None, token_type=None, expires_in=None, scope=None, local_vars_configuration=None):  # noqa: E501
        """OAuthResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._token_type = None
        self._expires_in = None
        self._scope = None
        self.discriminator = None

        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.scope = scope

    @property
    def access_token(self):
        """Gets the access_token of this OAuthResponse.  # noqa: E501

        Bearer token to be placed in the `Authorization` header  # noqa: E501

        :return: The access_token of this OAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OAuthResponse.

        Bearer token to be placed in the `Authorization` header  # noqa: E501

        :param access_token: The access_token of this OAuthResponse.  # noqa: E501
        :type access_token: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def token_type(self):
        """Gets the token_type of this OAuthResponse.  # noqa: E501

        Usually set to `Bearer`  # noqa: E501

        :return: The token_type of this OAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this OAuthResponse.

        Usually set to `Bearer`  # noqa: E501

        :param token_type: The token_type of this OAuthResponse.  # noqa: E501
        :type token_type: str
        """
        if self.local_vars_configuration.client_side_validation and token_type is None:  # noqa: E501
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

    @property
    def expires_in(self):
        """Gets the expires_in of this OAuthResponse.  # noqa: E501

        Token expiration in seconds. Usually 3600  # noqa: E501

        :return: The expires_in of this OAuthResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this OAuthResponse.

        Token expiration in seconds. Usually 3600  # noqa: E501

        :param expires_in: The expires_in of this OAuthResponse.  # noqa: E501
        :type expires_in: int
        """
        if self.local_vars_configuration.client_side_validation and expires_in is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

    @property
    def scope(self):
        """Gets the scope of this OAuthResponse.  # noqa: E501

        A space-separated list of authorized scopes  # noqa: E501

        :return: The scope of this OAuthResponse.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OAuthResponse.

        A space-separated list of authorized scopes  # noqa: E501

        :param scope: The scope of this OAuthResponse.  # noqa: E501
        :type scope: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

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
        if not isinstance(other, OAuthResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuthResponse):
            return True

        return self.to_dict() != other.to_dict()
