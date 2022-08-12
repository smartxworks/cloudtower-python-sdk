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


class NestedDiscoveredHostIface(object):
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
        'ipv4': 'str',
        'ipv6': 'str',
        'mac_address': 'str',
        'mtu': 'int',
        'name': 'str',
        'pci_slot_name': 'str',
        'rdma_enabled': 'bool',
        'speed': 'float',
        'up': 'bool'
    }

    attribute_map = {
        'ipv4': 'ipv4',
        'ipv6': 'ipv6',
        'mac_address': 'mac_address',
        'mtu': 'mtu',
        'name': 'name',
        'pci_slot_name': 'pci_slot_name',
        'rdma_enabled': 'rdma_enabled',
        'speed': 'speed',
        'up': 'up'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedDiscoveredHostIface - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._ipv4 = None
        self._ipv6 = None
        self._mac_address = None
        self._mtu = None
        self._name = None
        self._pci_slot_name = None
        self._rdma_enabled = None
        self._speed = None
        self._up = None
        self.discriminator = None

        self.ipv4 = kwargs.get("ipv4", None)
        self.ipv6 = kwargs.get("ipv6", None)
        if "mac_address" in kwargs:
            self.mac_address = kwargs["mac_address"]
        if "mtu" in kwargs:
            self.mtu = kwargs["mtu"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.pci_slot_name = kwargs.get("pci_slot_name", None)
        self.rdma_enabled = kwargs.get("rdma_enabled", None)
        self.speed = kwargs.get("speed", None)
        if "up" in kwargs:
            self.up = kwargs["up"]

    @property
    def ipv4(self):
        """Gets the ipv4 of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The ipv4 of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this NestedDiscoveredHostIface.


        :param ipv4: The ipv4 of this NestedDiscoveredHostIface.  # noqa: E501
        :type ipv4: str
        """

        self._ipv4 = ipv4

    @property
    def ipv6(self):
        """Gets the ipv6 of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The ipv6 of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this NestedDiscoveredHostIface.


        :param ipv6: The ipv6 of this NestedDiscoveredHostIface.  # noqa: E501
        :type ipv6: str
        """

        self._ipv6 = ipv6

    @property
    def mac_address(self):
        """Gets the mac_address of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The mac_address of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NestedDiscoveredHostIface.


        :param mac_address: The mac_address of this NestedDiscoveredHostIface.  # noqa: E501
        :type mac_address: str
        """
        if self.local_vars_configuration.client_side_validation and mac_address is None:  # noqa: E501
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def mtu(self):
        """Gets the mtu of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The mtu of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this NestedDiscoveredHostIface.


        :param mtu: The mtu of this NestedDiscoveredHostIface.  # noqa: E501
        :type mtu: int
        """
        if self.local_vars_configuration.client_side_validation and mtu is None:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must not be `None`")  # noqa: E501

        self._mtu = mtu

    @property
    def name(self):
        """Gets the name of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The name of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedDiscoveredHostIface.


        :param name: The name of this NestedDiscoveredHostIface.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def pci_slot_name(self):
        """Gets the pci_slot_name of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The pci_slot_name of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: str
        """
        return self._pci_slot_name

    @pci_slot_name.setter
    def pci_slot_name(self, pci_slot_name):
        """Sets the pci_slot_name of this NestedDiscoveredHostIface.


        :param pci_slot_name: The pci_slot_name of this NestedDiscoveredHostIface.  # noqa: E501
        :type pci_slot_name: str
        """

        self._pci_slot_name = pci_slot_name

    @property
    def rdma_enabled(self):
        """Gets the rdma_enabled of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The rdma_enabled of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: bool
        """
        return self._rdma_enabled

    @rdma_enabled.setter
    def rdma_enabled(self, rdma_enabled):
        """Sets the rdma_enabled of this NestedDiscoveredHostIface.


        :param rdma_enabled: The rdma_enabled of this NestedDiscoveredHostIface.  # noqa: E501
        :type rdma_enabled: bool
        """

        self._rdma_enabled = rdma_enabled

    @property
    def speed(self):
        """Gets the speed of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The speed of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this NestedDiscoveredHostIface.


        :param speed: The speed of this NestedDiscoveredHostIface.  # noqa: E501
        :type speed: float
        """

        self._speed = speed

    @property
    def up(self):
        """Gets the up of this NestedDiscoveredHostIface.  # noqa: E501


        :return: The up of this NestedDiscoveredHostIface.  # noqa: E501
        :rtype: bool
        """
        return self._up

    @up.setter
    def up(self, up):
        """Sets the up of this NestedDiscoveredHostIface.


        :param up: The up of this NestedDiscoveredHostIface.  # noqa: E501
        :type up: bool
        """
        if self.local_vars_configuration.client_side_validation and up is None:  # noqa: E501
            raise ValueError("Invalid value for `up`, must not be `None`")  # noqa: E501

        self._up = up

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
        if not isinstance(other, NestedDiscoveredHostIface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedDiscoveredHostIface):
            return True

        return self.to_dict() != other.to_dict()
