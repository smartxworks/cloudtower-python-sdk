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


class NestedPartition(object):
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
        'path': 'str',
        'size': 'int',
        'usage': 'PartitionUsage',
        'used_size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'size': 'size',
        'usage': 'usage',
        'used_size': 'used_size'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedPartition - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._name = None
        self._path = None
        self._size = None
        self._usage = None
        self._used_size = None
        self.discriminator = None

        self.name = kwargs.get("name", None)
        self.path = kwargs.get("path", None)
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "usage" in kwargs:
            self.usage = kwargs["usage"]
        if "used_size" in kwargs:
            self.used_size = kwargs["used_size"]

    @property
    def name(self):
        """Gets the name of this NestedPartition.  # noqa: E501


        :return: The name of this NestedPartition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedPartition.


        :param name: The name of this NestedPartition.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this NestedPartition.  # noqa: E501


        :return: The path of this NestedPartition.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NestedPartition.


        :param path: The path of this NestedPartition.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def size(self):
        """Gets the size of this NestedPartition.  # noqa: E501


        :return: The size of this NestedPartition.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NestedPartition.


        :param size: The size of this NestedPartition.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def usage(self):
        """Gets the usage of this NestedPartition.  # noqa: E501


        :return: The usage of this NestedPartition.  # noqa: E501
        :rtype: PartitionUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this NestedPartition.


        :param usage: The usage of this NestedPartition.  # noqa: E501
        :type usage: PartitionUsage
        """
        if self.local_vars_configuration.client_side_validation and usage is None:  # noqa: E501
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

    @property
    def used_size(self):
        """Gets the used_size of this NestedPartition.  # noqa: E501


        :return: The used_size of this NestedPartition.  # noqa: E501
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this NestedPartition.


        :param used_size: The used_size of this NestedPartition.  # noqa: E501
        :type used_size: int
        """
        if self.local_vars_configuration.client_side_validation and used_size is None:  # noqa: E501
            raise ValueError("Invalid value for `used_size`, must not be `None`")  # noqa: E501

        self._used_size = used_size

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
        if not isinstance(other, NestedPartition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedPartition):
            return True

        return self.to_dict() != other.to_dict()
