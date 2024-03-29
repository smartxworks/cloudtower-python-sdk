# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmDiskOperate(object):
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
        'remove_disks': 'VmDiskOperateRemoveDisks',
        'modify_disks': 'list[DiskOperateModifyDisk]',
        'new_disks': 'VmDiskParams'
    }

    attribute_map = {
        'remove_disks': 'remove_disks',
        'modify_disks': 'modify_disks',
        'new_disks': 'new_disks'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmDiskOperate - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._remove_disks = None
        self._modify_disks = None
        self._new_disks = None
        self.discriminator = None

        if "remove_disks" in kwargs:
            self.remove_disks = kwargs["remove_disks"]
        if "modify_disks" in kwargs:
            self.modify_disks = kwargs["modify_disks"]
        if "new_disks" in kwargs:
            self.new_disks = kwargs["new_disks"]

    @property
    def remove_disks(self):
        """Gets the remove_disks of this VmDiskOperate.  # noqa: E501


        :return: The remove_disks of this VmDiskOperate.  # noqa: E501
        :rtype: VmDiskOperateRemoveDisks
        """
        return self._remove_disks

    @remove_disks.setter
    def remove_disks(self, remove_disks):
        """Sets the remove_disks of this VmDiskOperate.


        :param remove_disks: The remove_disks of this VmDiskOperate.  # noqa: E501
        :type remove_disks: VmDiskOperateRemoveDisks
        """

        self._remove_disks = remove_disks

    @property
    def modify_disks(self):
        """Gets the modify_disks of this VmDiskOperate.  # noqa: E501


        :return: The modify_disks of this VmDiskOperate.  # noqa: E501
        :rtype: list[DiskOperateModifyDisk]
        """
        return self._modify_disks

    @modify_disks.setter
    def modify_disks(self, modify_disks):
        """Sets the modify_disks of this VmDiskOperate.


        :param modify_disks: The modify_disks of this VmDiskOperate.  # noqa: E501
        :type modify_disks: list[DiskOperateModifyDisk]
        """

        self._modify_disks = modify_disks

    @property
    def new_disks(self):
        """Gets the new_disks of this VmDiskOperate.  # noqa: E501


        :return: The new_disks of this VmDiskOperate.  # noqa: E501
        :rtype: VmDiskParams
        """
        return self._new_disks

    @new_disks.setter
    def new_disks(self, new_disks):
        """Sets the new_disks of this VmDiskOperate.


        :param new_disks: The new_disks of this VmDiskOperate.  # noqa: E501
        :type new_disks: VmDiskParams
        """

        self._new_disks = new_disks

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
        if not isinstance(other, VmDiskOperate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmDiskOperate):
            return True

        return self.to_dict() != other.to_dict()
