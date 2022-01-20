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


class VmNic(object):
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
        'enabled': 'bool',
        'gateway': 'str',
        'id': 'str',
        'interface_id': 'str',
        'ip_address': 'str',
        'local_id': 'str',
        'mac_address': 'str',
        'mirror': 'bool',
        'model': 'VmNicModel',
        'nic': 'NestedNic',
        'order': 'int',
        'subnet_mask': 'str',
        'vlan': 'NestedVlan',
        'vm': 'NestedVm'
    }

    attribute_map = {
        'enabled': 'enabled',
        'gateway': 'gateway',
        'id': 'id',
        'interface_id': 'interface_id',
        'ip_address': 'ip_address',
        'local_id': 'local_id',
        'mac_address': 'mac_address',
        'mirror': 'mirror',
        'model': 'model',
        'nic': 'nic',
        'order': 'order',
        'subnet_mask': 'subnet_mask',
        'vlan': 'vlan',
        'vm': 'vm'
    }

    def __init__(self, enabled=None, gateway=None, id=None, interface_id=None, ip_address=None, local_id=None, mac_address=None, mirror=None, model=None, nic=None, order=None, subnet_mask=None, vlan=None, vm=None, local_vars_configuration=None):  # noqa: E501
        """VmNic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._gateway = None
        self._id = None
        self._interface_id = None
        self._ip_address = None
        self._local_id = None
        self._mac_address = None
        self._mirror = None
        self._model = None
        self._nic = None
        self._order = None
        self._subnet_mask = None
        self._vlan = None
        self._vm = None
        self.discriminator = None

        self.enabled = enabled
        self.gateway = gateway
        self.id = id
        self.interface_id = interface_id
        self.ip_address = ip_address
        self.local_id = local_id
        self.mac_address = mac_address
        self.mirror = mirror
        self.model = model
        self.nic = nic
        self.order = order
        self.subnet_mask = subnet_mask
        self.vlan = vlan
        self.vm = vm

    @property
    def enabled(self):
        """Gets the enabled of this VmNic.  # noqa: E501


        :return: The enabled of this VmNic.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this VmNic.


        :param enabled: The enabled of this VmNic.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def gateway(self):
        """Gets the gateway of this VmNic.  # noqa: E501


        :return: The gateway of this VmNic.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this VmNic.


        :param gateway: The gateway of this VmNic.  # noqa: E501
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def id(self):
        """Gets the id of this VmNic.  # noqa: E501


        :return: The id of this VmNic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmNic.


        :param id: The id of this VmNic.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def interface_id(self):
        """Gets the interface_id of this VmNic.  # noqa: E501


        :return: The interface_id of this VmNic.  # noqa: E501
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """Sets the interface_id of this VmNic.


        :param interface_id: The interface_id of this VmNic.  # noqa: E501
        :type interface_id: str
        """

        self._interface_id = interface_id

    @property
    def ip_address(self):
        """Gets the ip_address of this VmNic.  # noqa: E501


        :return: The ip_address of this VmNic.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this VmNic.


        :param ip_address: The ip_address of this VmNic.  # noqa: E501
        :type ip_address: str
        """

        self._ip_address = ip_address

    @property
    def local_id(self):
        """Gets the local_id of this VmNic.  # noqa: E501


        :return: The local_id of this VmNic.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VmNic.


        :param local_id: The local_id of this VmNic.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def mac_address(self):
        """Gets the mac_address of this VmNic.  # noqa: E501


        :return: The mac_address of this VmNic.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this VmNic.


        :param mac_address: The mac_address of this VmNic.  # noqa: E501
        :type mac_address: str
        """

        self._mac_address = mac_address

    @property
    def mirror(self):
        """Gets the mirror of this VmNic.  # noqa: E501


        :return: The mirror of this VmNic.  # noqa: E501
        :rtype: bool
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this VmNic.


        :param mirror: The mirror of this VmNic.  # noqa: E501
        :type mirror: bool
        """

        self._mirror = mirror

    @property
    def model(self):
        """Gets the model of this VmNic.  # noqa: E501


        :return: The model of this VmNic.  # noqa: E501
        :rtype: VmNicModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this VmNic.


        :param model: The model of this VmNic.  # noqa: E501
        :type model: VmNicModel
        """

        self._model = model

    @property
    def nic(self):
        """Gets the nic of this VmNic.  # noqa: E501


        :return: The nic of this VmNic.  # noqa: E501
        :rtype: NestedNic
        """
        return self._nic

    @nic.setter
    def nic(self, nic):
        """Sets the nic of this VmNic.


        :param nic: The nic of this VmNic.  # noqa: E501
        :type nic: NestedNic
        """

        self._nic = nic

    @property
    def order(self):
        """Gets the order of this VmNic.  # noqa: E501


        :return: The order of this VmNic.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this VmNic.


        :param order: The order of this VmNic.  # noqa: E501
        :type order: int
        """

        self._order = order

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this VmNic.  # noqa: E501


        :return: The subnet_mask of this VmNic.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this VmNic.


        :param subnet_mask: The subnet_mask of this VmNic.  # noqa: E501
        :type subnet_mask: str
        """

        self._subnet_mask = subnet_mask

    @property
    def vlan(self):
        """Gets the vlan of this VmNic.  # noqa: E501


        :return: The vlan of this VmNic.  # noqa: E501
        :rtype: NestedVlan
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this VmNic.


        :param vlan: The vlan of this VmNic.  # noqa: E501
        :type vlan: NestedVlan
        """

        self._vlan = vlan

    @property
    def vm(self):
        """Gets the vm of this VmNic.  # noqa: E501


        :return: The vm of this VmNic.  # noqa: E501
        :rtype: NestedVm
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this VmNic.


        :param vm: The vm of this VmNic.  # noqa: E501
        :type vm: NestedVm
        """
        if self.local_vars_configuration.client_side_validation and vm is None:  # noqa: E501
            raise ValueError("Invalid value for `vm`, must not be `None`")  # noqa: E501

        self._vm = vm

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
        if not isinstance(other, VmNic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmNic):
            return True

        return self.to_dict() != other.to_dict()
