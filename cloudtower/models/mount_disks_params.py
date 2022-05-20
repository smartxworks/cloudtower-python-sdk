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


class MountDisksParams(object):
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
        'max_bandwidth_policy': 'VmDiskIoRestrictType',
        'max_bandwidth': 'int',
        'max_iops_policy': 'VmDiskIoRestrictType',
        'max_iops': 'int',
        'vm_volume_id': 'str',
        'index': 'int',
        'key': 'int',
        'bus': 'Bus',
        'boot': 'int'
    }

    attribute_map = {
        'max_bandwidth_policy': 'max_bandwidth_policy',
        'max_bandwidth': 'max_bandwidth',
        'max_iops_policy': 'max_iops_policy',
        'max_iops': 'max_iops',
        'vm_volume_id': 'vm_volume_id',
        'index': 'index',
        'key': 'key',
        'bus': 'bus',
        'boot': 'boot'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """MountDisksParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._max_bandwidth_policy = None
        self._max_bandwidth = None
        self._max_iops_policy = None
        self._max_iops = None
        self._vm_volume_id = None
        self._index = None
        self._key = None
        self._bus = None
        self._boot = None
        self.discriminator = None

        if "max_bandwidth_policy" in kwargs:
            self.max_bandwidth_policy = kwargs["max_bandwidth_policy"]
        if "max_bandwidth" in kwargs:
            self.max_bandwidth = kwargs["max_bandwidth"]
        if "max_iops_policy" in kwargs:
            self.max_iops_policy = kwargs["max_iops_policy"]
        if "max_iops" in kwargs:
            self.max_iops = kwargs["max_iops"]
        if "vm_volume_id" in kwargs:
            self.vm_volume_id = kwargs["vm_volume_id"]
        if "index" in kwargs:
            self.index = kwargs["index"]
        if "key" in kwargs:
            self.key = kwargs["key"]
        if "bus" in kwargs:
            self.bus = kwargs["bus"]
        if "boot" in kwargs:
            self.boot = kwargs["boot"]

    @property
    def max_bandwidth_policy(self):
        """Gets the max_bandwidth_policy of this MountDisksParams.  # noqa: E501


        :return: The max_bandwidth_policy of this MountDisksParams.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_bandwidth_policy

    @max_bandwidth_policy.setter
    def max_bandwidth_policy(self, max_bandwidth_policy):
        """Sets the max_bandwidth_policy of this MountDisksParams.


        :param max_bandwidth_policy: The max_bandwidth_policy of this MountDisksParams.  # noqa: E501
        :type max_bandwidth_policy: VmDiskIoRestrictType
        """

        self._max_bandwidth_policy = max_bandwidth_policy

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this MountDisksParams.  # noqa: E501


        :return: The max_bandwidth of this MountDisksParams.  # noqa: E501
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this MountDisksParams.


        :param max_bandwidth: The max_bandwidth of this MountDisksParams.  # noqa: E501
        :type max_bandwidth: int
        """

        self._max_bandwidth = max_bandwidth

    @property
    def max_iops_policy(self):
        """Gets the max_iops_policy of this MountDisksParams.  # noqa: E501


        :return: The max_iops_policy of this MountDisksParams.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_iops_policy

    @max_iops_policy.setter
    def max_iops_policy(self, max_iops_policy):
        """Sets the max_iops_policy of this MountDisksParams.


        :param max_iops_policy: The max_iops_policy of this MountDisksParams.  # noqa: E501
        :type max_iops_policy: VmDiskIoRestrictType
        """

        self._max_iops_policy = max_iops_policy

    @property
    def max_iops(self):
        """Gets the max_iops of this MountDisksParams.  # noqa: E501


        :return: The max_iops of this MountDisksParams.  # noqa: E501
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this MountDisksParams.


        :param max_iops: The max_iops of this MountDisksParams.  # noqa: E501
        :type max_iops: int
        """

        self._max_iops = max_iops

    @property
    def vm_volume_id(self):
        """Gets the vm_volume_id of this MountDisksParams.  # noqa: E501


        :return: The vm_volume_id of this MountDisksParams.  # noqa: E501
        :rtype: str
        """
        return self._vm_volume_id

    @vm_volume_id.setter
    def vm_volume_id(self, vm_volume_id):
        """Sets the vm_volume_id of this MountDisksParams.


        :param vm_volume_id: The vm_volume_id of this MountDisksParams.  # noqa: E501
        :type vm_volume_id: str
        """
        if self.local_vars_configuration.client_side_validation and vm_volume_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_volume_id`, must not be `None`")  # noqa: E501

        self._vm_volume_id = vm_volume_id

    @property
    def index(self):
        """Gets the index of this MountDisksParams.  # noqa: E501


        :return: The index of this MountDisksParams.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this MountDisksParams.


        :param index: The index of this MountDisksParams.  # noqa: E501
        :type index: int
        """

        self._index = index

    @property
    def key(self):
        """Gets the key of this MountDisksParams.  # noqa: E501


        :return: The key of this MountDisksParams.  # noqa: E501
        :rtype: int
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MountDisksParams.


        :param key: The key of this MountDisksParams.  # noqa: E501
        :type key: int
        """

        self._key = key

    @property
    def bus(self):
        """Gets the bus of this MountDisksParams.  # noqa: E501


        :return: The bus of this MountDisksParams.  # noqa: E501
        :rtype: Bus
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """Sets the bus of this MountDisksParams.


        :param bus: The bus of this MountDisksParams.  # noqa: E501
        :type bus: Bus
        """
        if self.local_vars_configuration.client_side_validation and bus is None:  # noqa: E501
            raise ValueError("Invalid value for `bus`, must not be `None`")  # noqa: E501

        self._bus = bus

    @property
    def boot(self):
        """Gets the boot of this MountDisksParams.  # noqa: E501


        :return: The boot of this MountDisksParams.  # noqa: E501
        :rtype: int
        """
        return self._boot

    @boot.setter
    def boot(self, boot):
        """Sets the boot of this MountDisksParams.


        :param boot: The boot of this MountDisksParams.  # noqa: E501
        :type boot: int
        """
        if self.local_vars_configuration.client_side_validation and boot is None:  # noqa: E501
            raise ValueError("Invalid value for `boot`, must not be `None`")  # noqa: E501

        self._boot = boot

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
        if not isinstance(other, MountDisksParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MountDisksParams):
            return True

        return self.to_dict() != other.to_dict()