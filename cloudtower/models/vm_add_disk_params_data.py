# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmAddDiskParamsData(object):
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
        'max_bandwidth_unit': 'BPSUnit',
        'max_bandwidth': 'int',
        'max_iops_policy': 'VmDiskIoRestrictType',
        'max_iops': 'int',
        'io_policy': 'VmDiskIoPolicy',
        'vm_disks': 'VmAddDiskParamsDataVmDisks'
    }

    attribute_map = {
        'max_bandwidth_policy': 'max_bandwidth_policy',
        'max_bandwidth_unit': 'max_bandwidth_unit',
        'max_bandwidth': 'max_bandwidth',
        'max_iops_policy': 'max_iops_policy',
        'max_iops': 'max_iops',
        'io_policy': 'io_policy',
        'vm_disks': 'vm_disks'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmAddDiskParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._max_bandwidth_policy = None
        self._max_bandwidth_unit = None
        self._max_bandwidth = None
        self._max_iops_policy = None
        self._max_iops = None
        self._io_policy = None
        self._vm_disks = None
        self.discriminator = None

        if "max_bandwidth_policy" in kwargs:
            self.max_bandwidth_policy = kwargs["max_bandwidth_policy"]
        if "max_bandwidth_unit" in kwargs:
            self.max_bandwidth_unit = kwargs["max_bandwidth_unit"]
        if "max_bandwidth" in kwargs:
            self.max_bandwidth = kwargs["max_bandwidth"]
        if "max_iops_policy" in kwargs:
            self.max_iops_policy = kwargs["max_iops_policy"]
        if "max_iops" in kwargs:
            self.max_iops = kwargs["max_iops"]
        if "io_policy" in kwargs:
            self.io_policy = kwargs["io_policy"]
        if "vm_disks" in kwargs:
            self.vm_disks = kwargs["vm_disks"]

    @property
    def max_bandwidth_policy(self):
        """Gets the max_bandwidth_policy of this VmAddDiskParamsData.  # noqa: E501


        :return: The max_bandwidth_policy of this VmAddDiskParamsData.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_bandwidth_policy

    @max_bandwidth_policy.setter
    def max_bandwidth_policy(self, max_bandwidth_policy):
        """Sets the max_bandwidth_policy of this VmAddDiskParamsData.


        :param max_bandwidth_policy: The max_bandwidth_policy of this VmAddDiskParamsData.  # noqa: E501
        :type max_bandwidth_policy: VmDiskIoRestrictType
        """

        self._max_bandwidth_policy = max_bandwidth_policy

    @property
    def max_bandwidth_unit(self):
        """Gets the max_bandwidth_unit of this VmAddDiskParamsData.  # noqa: E501


        :return: The max_bandwidth_unit of this VmAddDiskParamsData.  # noqa: E501
        :rtype: BPSUnit
        """
        return self._max_bandwidth_unit

    @max_bandwidth_unit.setter
    def max_bandwidth_unit(self, max_bandwidth_unit):
        """Sets the max_bandwidth_unit of this VmAddDiskParamsData.


        :param max_bandwidth_unit: The max_bandwidth_unit of this VmAddDiskParamsData.  # noqa: E501
        :type max_bandwidth_unit: BPSUnit
        """

        self._max_bandwidth_unit = max_bandwidth_unit

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this VmAddDiskParamsData.  # noqa: E501


        :return: The max_bandwidth of this VmAddDiskParamsData.  # noqa: E501
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this VmAddDiskParamsData.


        :param max_bandwidth: The max_bandwidth of this VmAddDiskParamsData.  # noqa: E501
        :type max_bandwidth: int
        """

        self._max_bandwidth = max_bandwidth

    @property
    def max_iops_policy(self):
        """Gets the max_iops_policy of this VmAddDiskParamsData.  # noqa: E501


        :return: The max_iops_policy of this VmAddDiskParamsData.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_iops_policy

    @max_iops_policy.setter
    def max_iops_policy(self, max_iops_policy):
        """Sets the max_iops_policy of this VmAddDiskParamsData.


        :param max_iops_policy: The max_iops_policy of this VmAddDiskParamsData.  # noqa: E501
        :type max_iops_policy: VmDiskIoRestrictType
        """

        self._max_iops_policy = max_iops_policy

    @property
    def max_iops(self):
        """Gets the max_iops of this VmAddDiskParamsData.  # noqa: E501


        :return: The max_iops of this VmAddDiskParamsData.  # noqa: E501
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this VmAddDiskParamsData.


        :param max_iops: The max_iops of this VmAddDiskParamsData.  # noqa: E501
        :type max_iops: int
        """

        self._max_iops = max_iops

    @property
    def io_policy(self):
        """Gets the io_policy of this VmAddDiskParamsData.  # noqa: E501


        :return: The io_policy of this VmAddDiskParamsData.  # noqa: E501
        :rtype: VmDiskIoPolicy
        """
        return self._io_policy

    @io_policy.setter
    def io_policy(self, io_policy):
        """Sets the io_policy of this VmAddDiskParamsData.


        :param io_policy: The io_policy of this VmAddDiskParamsData.  # noqa: E501
        :type io_policy: VmDiskIoPolicy
        """

        self._io_policy = io_policy

    @property
    def vm_disks(self):
        """Gets the vm_disks of this VmAddDiskParamsData.  # noqa: E501


        :return: The vm_disks of this VmAddDiskParamsData.  # noqa: E501
        :rtype: VmAddDiskParamsDataVmDisks
        """
        return self._vm_disks

    @vm_disks.setter
    def vm_disks(self, vm_disks):
        """Sets the vm_disks of this VmAddDiskParamsData.


        :param vm_disks: The vm_disks of this VmAddDiskParamsData.  # noqa: E501
        :type vm_disks: VmAddDiskParamsDataVmDisks
        """
        if self.local_vars_configuration.client_side_validation and vm_disks is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_disks`, must not be `None`")  # noqa: E501

        self._vm_disks = vm_disks

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
        if not isinstance(other, VmAddDiskParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmAddDiskParamsData):
            return True

        return self.to_dict() != other.to_dict()
