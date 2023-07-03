# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmdkDiskModify(object):
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
        'bus': 'Bus',
        'volume_name': 'str',
        'boot': 'int',
        'vmdk_name': 'str'
    }

    attribute_map = {
        'elf_storage_policy': 'elf_storage_policy',
        'bus': 'bus',
        'volume_name': 'volume_name',
        'boot': 'boot',
        'vmdk_name': 'vmdk_name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmdkDiskModify - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._elf_storage_policy = None
        self._bus = None
        self._volume_name = None
        self._boot = None
        self._vmdk_name = None
        self.discriminator = None

        if "elf_storage_policy" in kwargs:
            self.elf_storage_policy = kwargs["elf_storage_policy"]
        if "bus" in kwargs:
            self.bus = kwargs["bus"]
        if "volume_name" in kwargs:
            self.volume_name = kwargs["volume_name"]
        if "boot" in kwargs:
            self.boot = kwargs["boot"]
        if "vmdk_name" in kwargs:
            self.vmdk_name = kwargs["vmdk_name"]

    @property
    def elf_storage_policy(self):
        """Gets the elf_storage_policy of this VmdkDiskModify.  # noqa: E501


        :return: The elf_storage_policy of this VmdkDiskModify.  # noqa: E501
        :rtype: VmVolumeElfStoragePolicyType
        """
        return self._elf_storage_policy

    @elf_storage_policy.setter
    def elf_storage_policy(self, elf_storage_policy):
        """Sets the elf_storage_policy of this VmdkDiskModify.


        :param elf_storage_policy: The elf_storage_policy of this VmdkDiskModify.  # noqa: E501
        :type elf_storage_policy: VmVolumeElfStoragePolicyType
        """

        self._elf_storage_policy = elf_storage_policy

    @property
    def bus(self):
        """Gets the bus of this VmdkDiskModify.  # noqa: E501


        :return: The bus of this VmdkDiskModify.  # noqa: E501
        :rtype: Bus
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """Sets the bus of this VmdkDiskModify.


        :param bus: The bus of this VmdkDiskModify.  # noqa: E501
        :type bus: Bus
        """

        self._bus = bus

    @property
    def volume_name(self):
        """Gets the volume_name of this VmdkDiskModify.  # noqa: E501


        :return: The volume_name of this VmdkDiskModify.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this VmdkDiskModify.


        :param volume_name: The volume_name of this VmdkDiskModify.  # noqa: E501
        :type volume_name: str
        """

        self._volume_name = volume_name

    @property
    def boot(self):
        """Gets the boot of this VmdkDiskModify.  # noqa: E501


        :return: The boot of this VmdkDiskModify.  # noqa: E501
        :rtype: int
        """
        return self._boot

    @boot.setter
    def boot(self, boot):
        """Sets the boot of this VmdkDiskModify.


        :param boot: The boot of this VmdkDiskModify.  # noqa: E501
        :type boot: int
        """

        self._boot = boot

    @property
    def vmdk_name(self):
        """Gets the vmdk_name of this VmdkDiskModify.  # noqa: E501


        :return: The vmdk_name of this VmdkDiskModify.  # noqa: E501
        :rtype: str
        """
        return self._vmdk_name

    @vmdk_name.setter
    def vmdk_name(self, vmdk_name):
        """Sets the vmdk_name of this VmdkDiskModify.


        :param vmdk_name: The vmdk_name of this VmdkDiskModify.  # noqa: E501
        :type vmdk_name: str
        """
        if self.local_vars_configuration.client_side_validation and vmdk_name is None:  # noqa: E501
            raise ValueError("Invalid value for `vmdk_name`, must not be `None`")  # noqa: E501

        self._vmdk_name = vmdk_name

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
        if not isinstance(other, VmdkDiskModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmdkDiskModify):
            return True

        return self.to_dict() != other.to_dict()
