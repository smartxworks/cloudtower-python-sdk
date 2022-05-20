# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class MountNewCreateDisksParamsVmVolume(object):
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
        'elf_storage_policy': 'VmVolumeElfStoragePolicyType',
        'path': 'str',
        'size': 'int',
        'name': 'str'
    }

    attribute_map = {
        'elf_storage_policy': 'elf_storage_policy',
        'path': 'path',
        'size': 'size',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """MountNewCreateDisksParamsVmVolume - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._elf_storage_policy = None
        self._path = None
        self._size = None
        self._name = None
        self.discriminator = None

        if "elf_storage_policy" in kwargs:
            self.elf_storage_policy = kwargs["elf_storage_policy"]
        if "path" in kwargs:
            self.path = kwargs["path"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def elf_storage_policy(self):
        """Gets the elf_storage_policy of this MountNewCreateDisksParamsVmVolume.  # noqa: E501


        :return: The elf_storage_policy of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :rtype: VmVolumeElfStoragePolicyType
        """
        return self._elf_storage_policy

    @elf_storage_policy.setter
    def elf_storage_policy(self, elf_storage_policy):
        """Sets the elf_storage_policy of this MountNewCreateDisksParamsVmVolume.


        :param elf_storage_policy: The elf_storage_policy of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :type elf_storage_policy: VmVolumeElfStoragePolicyType
        """
        if self.local_vars_configuration.client_side_validation and elf_storage_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `elf_storage_policy`, must not be `None`")  # noqa: E501

        self._elf_storage_policy = elf_storage_policy

    @property
    def path(self):
        """Gets the path of this MountNewCreateDisksParamsVmVolume.  # noqa: E501


        :return: The path of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MountNewCreateDisksParamsVmVolume.


        :param path: The path of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def size(self):
        """Gets the size of this MountNewCreateDisksParamsVmVolume.  # noqa: E501


        :return: The size of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MountNewCreateDisksParamsVmVolume.


        :param size: The size of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def name(self):
        """Gets the name of this MountNewCreateDisksParamsVmVolume.  # noqa: E501


        :return: The name of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MountNewCreateDisksParamsVmVolume.


        :param name: The name of this MountNewCreateDisksParamsVmVolume.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, MountNewCreateDisksParamsVmVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MountNewCreateDisksParamsVmVolume):
            return True

        return self.to_dict() != other.to_dict()