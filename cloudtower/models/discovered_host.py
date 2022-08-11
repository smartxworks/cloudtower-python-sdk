# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.2.0
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


class DiscoveredHost(object):
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
        'all_flash': 'bool',
        'deployed': 'bool',
        'dimms': 'list[NestedDiscoveredHostDimms]',
        'disks': 'list[NestedDiscoveredHostDisk]',
        'host_ip': 'str',
        'host_uuid': 'str',
        'hostname': 'str',
        'ifaces': 'list[NestedDiscoveredHostIface]',
        'ipmi_ip': 'str',
        'is_os_in_raid1': 'bool',
        'product': 'str',
        'serial': 'str',
        'sockets': 'int',
        'version': 'str'
    }

    attribute_map = {
        'all_flash': 'all_flash',
        'deployed': 'deployed',
        'dimms': 'dimms',
        'disks': 'disks',
        'host_ip': 'host_ip',
        'host_uuid': 'host_uuid',
        'hostname': 'hostname',
        'ifaces': 'ifaces',
        'ipmi_ip': 'ipmi_ip',
        'is_os_in_raid1': 'is_os_in_raid1',
        'product': 'product',
        'serial': 'serial',
        'sockets': 'sockets',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DiscoveredHost - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._all_flash = None
        self._deployed = None
        self._dimms = None
        self._disks = None
        self._host_ip = None
        self._host_uuid = None
        self._hostname = None
        self._ifaces = None
        self._ipmi_ip = None
        self._is_os_in_raid1 = None
        self._product = None
        self._serial = None
        self._sockets = None
        self._version = None
        self.discriminator = None

        if "all_flash" in kwargs:
            self.all_flash = kwargs["all_flash"]
        self.deployed = kwargs.get("deployed", None)
        self.dimms = kwargs.get("dimms", None)
        if "disks" in kwargs:
            self.disks = kwargs["disks"]
        if "host_ip" in kwargs:
            self.host_ip = kwargs["host_ip"]
        if "host_uuid" in kwargs:
            self.host_uuid = kwargs["host_uuid"]
        if "hostname" in kwargs:
            self.hostname = kwargs["hostname"]
        if "ifaces" in kwargs:
            self.ifaces = kwargs["ifaces"]
        self.ipmi_ip = kwargs.get("ipmi_ip", None)
        self.is_os_in_raid1 = kwargs.get("is_os_in_raid1", None)
        self.product = kwargs.get("product", None)
        if "serial" in kwargs:
            self.serial = kwargs["serial"]
        if "sockets" in kwargs:
            self.sockets = kwargs["sockets"]
        if "version" in kwargs:
            self.version = kwargs["version"]

    @property
    def all_flash(self):
        """Gets the all_flash of this DiscoveredHost.  # noqa: E501


        :return: The all_flash of this DiscoveredHost.  # noqa: E501
        :rtype: bool
        """
        return self._all_flash

    @all_flash.setter
    def all_flash(self, all_flash):
        """Sets the all_flash of this DiscoveredHost.


        :param all_flash: The all_flash of this DiscoveredHost.  # noqa: E501
        :type all_flash: bool
        """
        if self.local_vars_configuration.client_side_validation and all_flash is None:  # noqa: E501
            raise ValueError("Invalid value for `all_flash`, must not be `None`")  # noqa: E501

        self._all_flash = all_flash

    @property
    def deployed(self):
        """Gets the deployed of this DiscoveredHost.  # noqa: E501


        :return: The deployed of this DiscoveredHost.  # noqa: E501
        :rtype: bool
        """
        return self._deployed

    @deployed.setter
    def deployed(self, deployed):
        """Sets the deployed of this DiscoveredHost.


        :param deployed: The deployed of this DiscoveredHost.  # noqa: E501
        :type deployed: bool
        """

        self._deployed = deployed

    @property
    def dimms(self):
        """Gets the dimms of this DiscoveredHost.  # noqa: E501


        :return: The dimms of this DiscoveredHost.  # noqa: E501
        :rtype: list[NestedDiscoveredHostDimms]
        """
        return self._dimms

    @dimms.setter
    def dimms(self, dimms):
        """Sets the dimms of this DiscoveredHost.


        :param dimms: The dimms of this DiscoveredHost.  # noqa: E501
        :type dimms: list[NestedDiscoveredHostDimms]
        """

        self._dimms = dimms

    @property
    def disks(self):
        """Gets the disks of this DiscoveredHost.  # noqa: E501


        :return: The disks of this DiscoveredHost.  # noqa: E501
        :rtype: list[NestedDiscoveredHostDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this DiscoveredHost.


        :param disks: The disks of this DiscoveredHost.  # noqa: E501
        :type disks: list[NestedDiscoveredHostDisk]
        """
        if self.local_vars_configuration.client_side_validation and disks is None:  # noqa: E501
            raise ValueError("Invalid value for `disks`, must not be `None`")  # noqa: E501

        self._disks = disks

    @property
    def host_ip(self):
        """Gets the host_ip of this DiscoveredHost.  # noqa: E501


        :return: The host_ip of this DiscoveredHost.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this DiscoveredHost.


        :param host_ip: The host_ip of this DiscoveredHost.  # noqa: E501
        :type host_ip: str
        """
        if self.local_vars_configuration.client_side_validation and host_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `host_ip`, must not be `None`")  # noqa: E501

        self._host_ip = host_ip

    @property
    def host_uuid(self):
        """Gets the host_uuid of this DiscoveredHost.  # noqa: E501


        :return: The host_uuid of this DiscoveredHost.  # noqa: E501
        :rtype: str
        """
        return self._host_uuid

    @host_uuid.setter
    def host_uuid(self, host_uuid):
        """Sets the host_uuid of this DiscoveredHost.


        :param host_uuid: The host_uuid of this DiscoveredHost.  # noqa: E501
        :type host_uuid: str
        """
        if self.local_vars_configuration.client_side_validation and host_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `host_uuid`, must not be `None`")  # noqa: E501

        self._host_uuid = host_uuid

    @property
    def hostname(self):
        """Gets the hostname of this DiscoveredHost.  # noqa: E501


        :return: The hostname of this DiscoveredHost.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DiscoveredHost.


        :param hostname: The hostname of this DiscoveredHost.  # noqa: E501
        :type hostname: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def ifaces(self):
        """Gets the ifaces of this DiscoveredHost.  # noqa: E501


        :return: The ifaces of this DiscoveredHost.  # noqa: E501
        :rtype: list[NestedDiscoveredHostIface]
        """
        return self._ifaces

    @ifaces.setter
    def ifaces(self, ifaces):
        """Sets the ifaces of this DiscoveredHost.


        :param ifaces: The ifaces of this DiscoveredHost.  # noqa: E501
        :type ifaces: list[NestedDiscoveredHostIface]
        """
        if self.local_vars_configuration.client_side_validation and ifaces is None:  # noqa: E501
            raise ValueError("Invalid value for `ifaces`, must not be `None`")  # noqa: E501

        self._ifaces = ifaces

    @property
    def ipmi_ip(self):
        """Gets the ipmi_ip of this DiscoveredHost.  # noqa: E501


        :return: The ipmi_ip of this DiscoveredHost.  # noqa: E501
        :rtype: str
        """
        return self._ipmi_ip

    @ipmi_ip.setter
    def ipmi_ip(self, ipmi_ip):
        """Sets the ipmi_ip of this DiscoveredHost.


        :param ipmi_ip: The ipmi_ip of this DiscoveredHost.  # noqa: E501
        :type ipmi_ip: str
        """

        self._ipmi_ip = ipmi_ip

    @property
    def is_os_in_raid1(self):
        """Gets the is_os_in_raid1 of this DiscoveredHost.  # noqa: E501


        :return: The is_os_in_raid1 of this DiscoveredHost.  # noqa: E501
        :rtype: bool
        """
        return self._is_os_in_raid1

    @is_os_in_raid1.setter
    def is_os_in_raid1(self, is_os_in_raid1):
        """Sets the is_os_in_raid1 of this DiscoveredHost.


        :param is_os_in_raid1: The is_os_in_raid1 of this DiscoveredHost.  # noqa: E501
        :type is_os_in_raid1: bool
        """

        self._is_os_in_raid1 = is_os_in_raid1

    @property
    def product(self):
        """Gets the product of this DiscoveredHost.  # noqa: E501


        :return: The product of this DiscoveredHost.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this DiscoveredHost.


        :param product: The product of this DiscoveredHost.  # noqa: E501
        :type product: str
        """

        self._product = product

    @property
    def serial(self):
        """Gets the serial of this DiscoveredHost.  # noqa: E501


        :return: The serial of this DiscoveredHost.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DiscoveredHost.


        :param serial: The serial of this DiscoveredHost.  # noqa: E501
        :type serial: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def sockets(self):
        """Gets the sockets of this DiscoveredHost.  # noqa: E501


        :return: The sockets of this DiscoveredHost.  # noqa: E501
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """Sets the sockets of this DiscoveredHost.


        :param sockets: The sockets of this DiscoveredHost.  # noqa: E501
        :type sockets: int
        """
        if self.local_vars_configuration.client_side_validation and sockets is None:  # noqa: E501
            raise ValueError("Invalid value for `sockets`, must not be `None`")  # noqa: E501

        self._sockets = sockets

    @property
    def version(self):
        """Gets the version of this DiscoveredHost.  # noqa: E501


        :return: The version of this DiscoveredHost.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DiscoveredHost.


        :param version: The version of this DiscoveredHost.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, DiscoveredHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiscoveredHost):
            return True

        return self.to_dict() != other.to_dict()
