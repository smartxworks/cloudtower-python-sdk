# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmDiskParams(object):
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
        'mount_cd_roms': 'list[VmCdRomParams]',
        'mount_disks': 'list[MountDisksParams]',
        'mount_new_create_disks': 'list[MountNewCreateDisksParams]'
    }

    attribute_map = {
        'mount_cd_roms': 'mount_cd_roms',
        'mount_disks': 'mount_disks',
        'mount_new_create_disks': 'mount_new_create_disks'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmDiskParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._mount_cd_roms = None
        self._mount_disks = None
        self._mount_new_create_disks = None
        self.discriminator = None

        if "mount_cd_roms" in kwargs:
            self.mount_cd_roms = kwargs["mount_cd_roms"]
        if "mount_disks" in kwargs:
            self.mount_disks = kwargs["mount_disks"]
        if "mount_new_create_disks" in kwargs:
            self.mount_new_create_disks = kwargs["mount_new_create_disks"]

    @property
    def mount_cd_roms(self):
        """Gets the mount_cd_roms of this VmDiskParams.  # noqa: E501


        :return: The mount_cd_roms of this VmDiskParams.  # noqa: E501
        :rtype: list[VmCdRomParams]
        """
        return self._mount_cd_roms

    @mount_cd_roms.setter
    def mount_cd_roms(self, mount_cd_roms):
        """Sets the mount_cd_roms of this VmDiskParams.


        :param mount_cd_roms: The mount_cd_roms of this VmDiskParams.  # noqa: E501
        :type mount_cd_roms: list[VmCdRomParams]
        """

        self._mount_cd_roms = mount_cd_roms

    @property
    def mount_disks(self):
        """Gets the mount_disks of this VmDiskParams.  # noqa: E501


        :return: The mount_disks of this VmDiskParams.  # noqa: E501
        :rtype: list[MountDisksParams]
        """
        return self._mount_disks

    @mount_disks.setter
    def mount_disks(self, mount_disks):
        """Sets the mount_disks of this VmDiskParams.


        :param mount_disks: The mount_disks of this VmDiskParams.  # noqa: E501
        :type mount_disks: list[MountDisksParams]
        """

        self._mount_disks = mount_disks

    @property
    def mount_new_create_disks(self):
        """Gets the mount_new_create_disks of this VmDiskParams.  # noqa: E501


        :return: The mount_new_create_disks of this VmDiskParams.  # noqa: E501
        :rtype: list[MountNewCreateDisksParams]
        """
        return self._mount_new_create_disks

    @mount_new_create_disks.setter
    def mount_new_create_disks(self, mount_new_create_disks):
        """Sets the mount_new_create_disks of this VmDiskParams.


        :param mount_new_create_disks: The mount_new_create_disks of this VmDiskParams.  # noqa: E501
        :type mount_new_create_disks: list[MountNewCreateDisksParams]
        """

        self._mount_new_create_disks = mount_new_create_disks

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
        if not isinstance(other, VmDiskParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmDiskParams):
            return True

        return self.to_dict() != other.to_dict()
