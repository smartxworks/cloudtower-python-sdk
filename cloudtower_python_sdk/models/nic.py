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


class Nic(object):
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
        'driver': 'str',
        'driver_state': 'NicDriverState',
        'gateway_ip': 'str',
        'host': 'NestedHost',
        'ibdev': 'str',
        'id': 'str',
        'ip_address': 'str',
        'is_sriov': 'bool',
        'labels': 'list[NestedLabel]',
        'local_id': 'str',
        'mac_address': 'str',
        'max_vf_num': 'int',
        'model': 'str',
        'mtu': 'int',
        'name': 'str',
        'nic_uuid': 'str',
        'physical': 'bool',
        'rdma_enabled': 'bool',
        'running': 'bool',
        'speed': 'float',
        'subnet_mask': 'str',
        'total_vf_num': 'int',
        'type': 'NetworkType',
        'up': 'bool',
        'used_vf_num': 'int',
        'vds': 'NestedVds'
    }

    attribute_map = {
        'driver': 'driver',
        'driver_state': 'driver_state',
        'gateway_ip': 'gateway_ip',
        'host': 'host',
        'ibdev': 'ibdev',
        'id': 'id',
        'ip_address': 'ip_address',
        'is_sriov': 'is_sriov',
        'labels': 'labels',
        'local_id': 'local_id',
        'mac_address': 'mac_address',
        'max_vf_num': 'max_vf_num',
        'model': 'model',
        'mtu': 'mtu',
        'name': 'name',
        'nic_uuid': 'nic_uuid',
        'physical': 'physical',
        'rdma_enabled': 'rdma_enabled',
        'running': 'running',
        'speed': 'speed',
        'subnet_mask': 'subnet_mask',
        'total_vf_num': 'total_vf_num',
        'type': 'type',
        'up': 'up',
        'used_vf_num': 'used_vf_num',
        'vds': 'vds'
    }

    def __init__(self, driver=None, driver_state=None, gateway_ip=None, host=None, ibdev=None, id=None, ip_address=None, is_sriov=None, labels=None, local_id=None, mac_address=None, max_vf_num=None, model=None, mtu=None, name=None, nic_uuid=None, physical=None, rdma_enabled=None, running=None, speed=None, subnet_mask=None, total_vf_num=None, type=None, up=None, used_vf_num=None, vds=None, local_vars_configuration=None):  # noqa: E501
        """Nic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._driver = None
        self._driver_state = None
        self._gateway_ip = None
        self._host = None
        self._ibdev = None
        self._id = None
        self._ip_address = None
        self._is_sriov = None
        self._labels = None
        self._local_id = None
        self._mac_address = None
        self._max_vf_num = None
        self._model = None
        self._mtu = None
        self._name = None
        self._nic_uuid = None
        self._physical = None
        self._rdma_enabled = None
        self._running = None
        self._speed = None
        self._subnet_mask = None
        self._total_vf_num = None
        self._type = None
        self._up = None
        self._used_vf_num = None
        self._vds = None
        self.discriminator = None

        self.driver = driver
        self.driver_state = driver_state
        self.gateway_ip = gateway_ip
        self.host = host
        self.ibdev = ibdev
        self.id = id
        self.ip_address = ip_address
        self.is_sriov = is_sriov
        self.labels = labels
        self.local_id = local_id
        self.mac_address = mac_address
        self.max_vf_num = max_vf_num
        self.model = model
        self.mtu = mtu
        self.name = name
        self.nic_uuid = nic_uuid
        self.physical = physical
        self.rdma_enabled = rdma_enabled
        self.running = running
        self.speed = speed
        self.subnet_mask = subnet_mask
        self.total_vf_num = total_vf_num
        self.type = type
        self.up = up
        self.used_vf_num = used_vf_num
        self.vds = vds

    @property
    def driver(self):
        """Gets the driver of this Nic.  # noqa: E501


        :return: The driver of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this Nic.


        :param driver: The driver of this Nic.  # noqa: E501
        :type driver: str
        """

        self._driver = driver

    @property
    def driver_state(self):
        """Gets the driver_state of this Nic.  # noqa: E501


        :return: The driver_state of this Nic.  # noqa: E501
        :rtype: NicDriverState
        """
        return self._driver_state

    @driver_state.setter
    def driver_state(self, driver_state):
        """Sets the driver_state of this Nic.


        :param driver_state: The driver_state of this Nic.  # noqa: E501
        :type driver_state: NicDriverState
        """

        self._driver_state = driver_state

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this Nic.  # noqa: E501


        :return: The gateway_ip of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this Nic.


        :param gateway_ip: The gateway_ip of this Nic.  # noqa: E501
        :type gateway_ip: str
        """

        self._gateway_ip = gateway_ip

    @property
    def host(self):
        """Gets the host of this Nic.  # noqa: E501


        :return: The host of this Nic.  # noqa: E501
        :rtype: NestedHost
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Nic.


        :param host: The host of this Nic.  # noqa: E501
        :type host: NestedHost
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def ibdev(self):
        """Gets the ibdev of this Nic.  # noqa: E501


        :return: The ibdev of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._ibdev

    @ibdev.setter
    def ibdev(self, ibdev):
        """Sets the ibdev of this Nic.


        :param ibdev: The ibdev of this Nic.  # noqa: E501
        :type ibdev: str
        """

        self._ibdev = ibdev

    @property
    def id(self):
        """Gets the id of this Nic.  # noqa: E501


        :return: The id of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Nic.


        :param id: The id of this Nic.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip_address(self):
        """Gets the ip_address of this Nic.  # noqa: E501


        :return: The ip_address of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this Nic.


        :param ip_address: The ip_address of this Nic.  # noqa: E501
        :type ip_address: str
        """

        self._ip_address = ip_address

    @property
    def is_sriov(self):
        """Gets the is_sriov of this Nic.  # noqa: E501


        :return: The is_sriov of this Nic.  # noqa: E501
        :rtype: bool
        """
        return self._is_sriov

    @is_sriov.setter
    def is_sriov(self, is_sriov):
        """Sets the is_sriov of this Nic.


        :param is_sriov: The is_sriov of this Nic.  # noqa: E501
        :type is_sriov: bool
        """

        self._is_sriov = is_sriov

    @property
    def labels(self):
        """Gets the labels of this Nic.  # noqa: E501


        :return: The labels of this Nic.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Nic.


        :param labels: The labels of this Nic.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def local_id(self):
        """Gets the local_id of this Nic.  # noqa: E501


        :return: The local_id of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this Nic.


        :param local_id: The local_id of this Nic.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def mac_address(self):
        """Gets the mac_address of this Nic.  # noqa: E501


        :return: The mac_address of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Nic.


        :param mac_address: The mac_address of this Nic.  # noqa: E501
        :type mac_address: str
        """
        if self.local_vars_configuration.client_side_validation and mac_address is None:  # noqa: E501
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def max_vf_num(self):
        """Gets the max_vf_num of this Nic.  # noqa: E501


        :return: The max_vf_num of this Nic.  # noqa: E501
        :rtype: int
        """
        return self._max_vf_num

    @max_vf_num.setter
    def max_vf_num(self, max_vf_num):
        """Sets the max_vf_num of this Nic.


        :param max_vf_num: The max_vf_num of this Nic.  # noqa: E501
        :type max_vf_num: int
        """

        self._max_vf_num = max_vf_num

    @property
    def model(self):
        """Gets the model of this Nic.  # noqa: E501


        :return: The model of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Nic.


        :param model: The model of this Nic.  # noqa: E501
        :type model: str
        """

        self._model = model

    @property
    def mtu(self):
        """Gets the mtu of this Nic.  # noqa: E501


        :return: The mtu of this Nic.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this Nic.


        :param mtu: The mtu of this Nic.  # noqa: E501
        :type mtu: int
        """
        if self.local_vars_configuration.client_side_validation and mtu is None:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must not be `None`")  # noqa: E501

        self._mtu = mtu

    @property
    def name(self):
        """Gets the name of this Nic.  # noqa: E501


        :return: The name of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Nic.


        :param name: The name of this Nic.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nic_uuid(self):
        """Gets the nic_uuid of this Nic.  # noqa: E501


        :return: The nic_uuid of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._nic_uuid

    @nic_uuid.setter
    def nic_uuid(self, nic_uuid):
        """Sets the nic_uuid of this Nic.


        :param nic_uuid: The nic_uuid of this Nic.  # noqa: E501
        :type nic_uuid: str
        """

        self._nic_uuid = nic_uuid

    @property
    def physical(self):
        """Gets the physical of this Nic.  # noqa: E501


        :return: The physical of this Nic.  # noqa: E501
        :rtype: bool
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """Sets the physical of this Nic.


        :param physical: The physical of this Nic.  # noqa: E501
        :type physical: bool
        """
        if self.local_vars_configuration.client_side_validation and physical is None:  # noqa: E501
            raise ValueError("Invalid value for `physical`, must not be `None`")  # noqa: E501

        self._physical = physical

    @property
    def rdma_enabled(self):
        """Gets the rdma_enabled of this Nic.  # noqa: E501


        :return: The rdma_enabled of this Nic.  # noqa: E501
        :rtype: bool
        """
        return self._rdma_enabled

    @rdma_enabled.setter
    def rdma_enabled(self, rdma_enabled):
        """Sets the rdma_enabled of this Nic.


        :param rdma_enabled: The rdma_enabled of this Nic.  # noqa: E501
        :type rdma_enabled: bool
        """

        self._rdma_enabled = rdma_enabled

    @property
    def running(self):
        """Gets the running of this Nic.  # noqa: E501


        :return: The running of this Nic.  # noqa: E501
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this Nic.


        :param running: The running of this Nic.  # noqa: E501
        :type running: bool
        """
        if self.local_vars_configuration.client_side_validation and running is None:  # noqa: E501
            raise ValueError("Invalid value for `running`, must not be `None`")  # noqa: E501

        self._running = running

    @property
    def speed(self):
        """Gets the speed of this Nic.  # noqa: E501


        :return: The speed of this Nic.  # noqa: E501
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this Nic.


        :param speed: The speed of this Nic.  # noqa: E501
        :type speed: float
        """

        self._speed = speed

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this Nic.  # noqa: E501


        :return: The subnet_mask of this Nic.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this Nic.


        :param subnet_mask: The subnet_mask of this Nic.  # noqa: E501
        :type subnet_mask: str
        """

        self._subnet_mask = subnet_mask

    @property
    def total_vf_num(self):
        """Gets the total_vf_num of this Nic.  # noqa: E501


        :return: The total_vf_num of this Nic.  # noqa: E501
        :rtype: int
        """
        return self._total_vf_num

    @total_vf_num.setter
    def total_vf_num(self, total_vf_num):
        """Sets the total_vf_num of this Nic.


        :param total_vf_num: The total_vf_num of this Nic.  # noqa: E501
        :type total_vf_num: int
        """

        self._total_vf_num = total_vf_num

    @property
    def type(self):
        """Gets the type of this Nic.  # noqa: E501


        :return: The type of this Nic.  # noqa: E501
        :rtype: NetworkType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Nic.


        :param type: The type of this Nic.  # noqa: E501
        :type type: NetworkType
        """

        self._type = type

    @property
    def up(self):
        """Gets the up of this Nic.  # noqa: E501


        :return: The up of this Nic.  # noqa: E501
        :rtype: bool
        """
        return self._up

    @up.setter
    def up(self, up):
        """Sets the up of this Nic.


        :param up: The up of this Nic.  # noqa: E501
        :type up: bool
        """
        if self.local_vars_configuration.client_side_validation and up is None:  # noqa: E501
            raise ValueError("Invalid value for `up`, must not be `None`")  # noqa: E501

        self._up = up

    @property
    def used_vf_num(self):
        """Gets the used_vf_num of this Nic.  # noqa: E501


        :return: The used_vf_num of this Nic.  # noqa: E501
        :rtype: int
        """
        return self._used_vf_num

    @used_vf_num.setter
    def used_vf_num(self, used_vf_num):
        """Sets the used_vf_num of this Nic.


        :param used_vf_num: The used_vf_num of this Nic.  # noqa: E501
        :type used_vf_num: int
        """

        self._used_vf_num = used_vf_num

    @property
    def vds(self):
        """Gets the vds of this Nic.  # noqa: E501


        :return: The vds of this Nic.  # noqa: E501
        :rtype: NestedVds
        """
        return self._vds

    @vds.setter
    def vds(self, vds):
        """Sets the vds of this Nic.


        :param vds: The vds of this Nic.  # noqa: E501
        :type vds: NestedVds
        """

        self._vds = vds

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
        if not isinstance(other, Nic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Nic):
            return True

        return self.to_dict() != other.to_dict()
