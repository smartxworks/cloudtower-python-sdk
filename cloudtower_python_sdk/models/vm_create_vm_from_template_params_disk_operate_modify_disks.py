# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower_python_sdk.configuration import Configuration


class VmCreateVmFromTemplateParamsDiskOperateModifyDisks(object):
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
        'vm_volume_id': 'str',
        'bus': 'Bus',
        'disk_index': 'int'
    }

    attribute_map = {
        'vm_volume_id': 'vm_volume_id',
        'bus': 'bus',
        'disk_index': 'disk_index'
    }

    def __init__(self, vm_volume_id=None, bus=None, disk_index=None, local_vars_configuration=None):  # noqa: E501
        """VmCreateVmFromTemplateParamsDiskOperateModifyDisks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._vm_volume_id = None
        self._bus = None
        self._disk_index = None
        self.discriminator = None

        if vm_volume_id is not None:
            self.vm_volume_id = vm_volume_id
        if bus is not None:
            self.bus = bus
        self.disk_index = disk_index

    @property
    def vm_volume_id(self):
        """Gets the vm_volume_id of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501


        :return: The vm_volume_id of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501
        :rtype: str
        """
        return self._vm_volume_id

    @vm_volume_id.setter
    def vm_volume_id(self, vm_volume_id):
        """Sets the vm_volume_id of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.


        :param vm_volume_id: The vm_volume_id of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501
        :type vm_volume_id: str
        """

        self._vm_volume_id = vm_volume_id

    @property
    def bus(self):
        """Gets the bus of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501


        :return: The bus of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501
        :rtype: Bus
        """
        return self._bus

    @bus.setter
    def bus(self, bus):
        """Sets the bus of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.


        :param bus: The bus of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501
        :type bus: Bus
        """

        self._bus = bus

    @property
    def disk_index(self):
        """Gets the disk_index of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501


        :return: The disk_index of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501
        :rtype: int
        """
        return self._disk_index

    @disk_index.setter
    def disk_index(self, disk_index):
        """Sets the disk_index of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.


        :param disk_index: The disk_index of this VmCreateVmFromTemplateParamsDiskOperateModifyDisks.  # noqa: E501
        :type disk_index: int
        """
        if self.local_vars_configuration.client_side_validation and disk_index is None:  # noqa: E501
            raise ValueError("Invalid value for `disk_index`, must not be `None`")  # noqa: E501

        self._disk_index = disk_index

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
        if not isinstance(other, VmCreateVmFromTemplateParamsDiskOperateModifyDisks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmCreateVmFromTemplateParamsDiskOperateModifyDisks):
            return True

        return self.to_dict() != other.to_dict()
