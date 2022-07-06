# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class IscsiLunUpdationParamsDataAllOf(object):
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
        'assigned_size': 'int',
        'name': 'str'
    }

    attribute_map = {
        'assigned_size': 'assigned_size',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IscsiLunUpdationParamsDataAllOf - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._assigned_size = None
        self._name = None
        self.discriminator = None

        if "assigned_size" in kwargs:
            self.assigned_size = kwargs["assigned_size"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def assigned_size(self):
        """Gets the assigned_size of this IscsiLunUpdationParamsDataAllOf.  # noqa: E501


        :return: The assigned_size of this IscsiLunUpdationParamsDataAllOf.  # noqa: E501
        :rtype: int
        """
        return self._assigned_size

    @assigned_size.setter
    def assigned_size(self, assigned_size):
        """Sets the assigned_size of this IscsiLunUpdationParamsDataAllOf.


        :param assigned_size: The assigned_size of this IscsiLunUpdationParamsDataAllOf.  # noqa: E501
        :type assigned_size: int
        """

        self._assigned_size = assigned_size

    @property
    def name(self):
        """Gets the name of this IscsiLunUpdationParamsDataAllOf.  # noqa: E501


        :return: The name of this IscsiLunUpdationParamsDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IscsiLunUpdationParamsDataAllOf.


        :param name: The name of this IscsiLunUpdationParamsDataAllOf.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, IscsiLunUpdationParamsDataAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiLunUpdationParamsDataAllOf):
            return True

        return self.to_dict() != other.to_dict()
