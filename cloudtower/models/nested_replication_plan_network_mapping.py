# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedReplicationPlanNetworkMapping(object):
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
        'source': 'NestedReplicationNetworkInformation',
        'target': 'NestedReplicationNetworkInformation'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedReplicationPlanNetworkMapping - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._source = None
        self._target = None
        self.discriminator = None

        if "source" in kwargs:
            self.source = kwargs["source"]
        if "target" in kwargs:
            self.target = kwargs["target"]

    @property
    def source(self):
        """Gets the source of this NestedReplicationPlanNetworkMapping.  # noqa: E501


        :return: The source of this NestedReplicationPlanNetworkMapping.  # noqa: E501
        :rtype: NestedReplicationNetworkInformation
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this NestedReplicationPlanNetworkMapping.


        :param source: The source of this NestedReplicationPlanNetworkMapping.  # noqa: E501
        :type source: NestedReplicationNetworkInformation
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def target(self):
        """Gets the target of this NestedReplicationPlanNetworkMapping.  # noqa: E501


        :return: The target of this NestedReplicationPlanNetworkMapping.  # noqa: E501
        :rtype: NestedReplicationNetworkInformation
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this NestedReplicationPlanNetworkMapping.


        :param target: The target of this NestedReplicationPlanNetworkMapping.  # noqa: E501
        :type target: NestedReplicationNetworkInformation
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, NestedReplicationPlanNetworkMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedReplicationPlanNetworkMapping):
            return True

        return self.to_dict() != other.to_dict()
