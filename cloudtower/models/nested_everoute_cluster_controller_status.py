# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Contact: info@smartx.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedEverouteClusterControllerStatus(object):
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
        'current_number': 'int',
        'expect_number': 'int',
        'instances': 'list[NestedEverouteControllerStatus]',
        'number_health': 'int'
    }

    attribute_map = {
        'current_number': 'currentNumber',
        'expect_number': 'expectNumber',
        'instances': 'instances',
        'number_health': 'numberHealth'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedEverouteClusterControllerStatus - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._current_number = None
        self._expect_number = None
        self._instances = None
        self._number_health = None
        self.discriminator = None

        if "current_number" in kwargs:
            self.current_number = kwargs["current_number"]
        if "expect_number" in kwargs:
            self.expect_number = kwargs["expect_number"]
        self.instances = kwargs.get("instances", None)
        if "number_health" in kwargs:
            self.number_health = kwargs["number_health"]

    @property
    def current_number(self):
        """Gets the current_number of this NestedEverouteClusterControllerStatus.  # noqa: E501


        :return: The current_number of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_number

    @current_number.setter
    def current_number(self, current_number):
        """Sets the current_number of this NestedEverouteClusterControllerStatus.


        :param current_number: The current_number of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :type current_number: int
        """
        if self.local_vars_configuration.client_side_validation and current_number is None:  # noqa: E501
            raise ValueError("Invalid value for `current_number`, must not be `None`")  # noqa: E501

        self._current_number = current_number

    @property
    def expect_number(self):
        """Gets the expect_number of this NestedEverouteClusterControllerStatus.  # noqa: E501


        :return: The expect_number of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._expect_number

    @expect_number.setter
    def expect_number(self, expect_number):
        """Sets the expect_number of this NestedEverouteClusterControllerStatus.


        :param expect_number: The expect_number of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :type expect_number: int
        """
        if self.local_vars_configuration.client_side_validation and expect_number is None:  # noqa: E501
            raise ValueError("Invalid value for `expect_number`, must not be `None`")  # noqa: E501

        self._expect_number = expect_number

    @property
    def instances(self):
        """Gets the instances of this NestedEverouteClusterControllerStatus.  # noqa: E501


        :return: The instances of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :rtype: list[NestedEverouteControllerStatus]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this NestedEverouteClusterControllerStatus.


        :param instances: The instances of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :type instances: list[NestedEverouteControllerStatus]
        """

        self._instances = instances

    @property
    def number_health(self):
        """Gets the number_health of this NestedEverouteClusterControllerStatus.  # noqa: E501


        :return: The number_health of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :rtype: int
        """
        return self._number_health

    @number_health.setter
    def number_health(self, number_health):
        """Sets the number_health of this NestedEverouteClusterControllerStatus.


        :param number_health: The number_health of this NestedEverouteClusterControllerStatus.  # noqa: E501
        :type number_health: int
        """
        if self.local_vars_configuration.client_side_validation and number_health is None:  # noqa: E501
            raise ValueError("Invalid value for `number_health`, must not be `None`")  # noqa: E501

        self._number_health = number_health

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
        if not isinstance(other, NestedEverouteClusterControllerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedEverouteClusterControllerStatus):
            return True

        return self.to_dict() != other.to_dict()
