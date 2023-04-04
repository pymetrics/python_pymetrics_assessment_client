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


class PontemOrderStatuses(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    REJECTED = "Rejected"
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FULFILLED = "Fulfilled"
    EXPIRED = "Expired"

    allowable_values = [REJECTED, PENDING, ACCEPTED, NOT_STARTED, IN_PROGRESS, COMPLETED, FULFILLED, EXPIRED]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """PontemOrderStatuses - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, PontemOrderStatuses):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PontemOrderStatuses):
            return True

        return self.to_dict() != other.to_dict()
