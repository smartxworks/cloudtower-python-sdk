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


class HostCreationParamsData(object):
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
        'ifaces': 'list[HostBatchCreateIfaceInput]',
        'disks': 'list[HostBatchCreateDiskInput]',
        'platform_password': 'str',
        'platform_username': 'str',
        'platform_ip': 'str',
        'ipmi': 'HostBatchCreateIpmiInput',
        'hostname': 'str',
        'host_uuid': 'str',
        'host_ip': 'str'
    }

    attribute_map = {
        'ifaces': 'ifaces',
        'disks': 'disks',
        'platform_password': 'platform_password',
        'platform_username': 'platform_username',
        'platform_ip': 'platform_ip',
        'ipmi': 'ipmi',
        'hostname': 'hostname',
        'host_uuid': 'host_uuid',
        'host_ip': 'host_ip'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """HostCreationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._ifaces = None
        self._disks = None
        self._platform_password = None
        self._platform_username = None
        self._platform_ip = None
        self._ipmi = None
        self._hostname = None
        self._host_uuid = None
        self._host_ip = None
        self.discriminator = None

        if "ifaces" in kwargs:
            self.ifaces = kwargs["ifaces"]
        if "disks" in kwargs:
            self.disks = kwargs["disks"]
        if "platform_password" in kwargs:
            self.platform_password = kwargs["platform_password"]
        if "platform_username" in kwargs:
            self.platform_username = kwargs["platform_username"]
        if "platform_ip" in kwargs:
            self.platform_ip = kwargs["platform_ip"]
        if "ipmi" in kwargs:
            self.ipmi = kwargs["ipmi"]
        if "hostname" in kwargs:
            self.hostname = kwargs["hostname"]
        if "host_uuid" in kwargs:
            self.host_uuid = kwargs["host_uuid"]
        if "host_ip" in kwargs:
            self.host_ip = kwargs["host_ip"]

    @property
    def ifaces(self):
        """Gets the ifaces of this HostCreationParamsData.  # noqa: E501


        :return: The ifaces of this HostCreationParamsData.  # noqa: E501
        :rtype: list[HostBatchCreateIfaceInput]
        """
        return self._ifaces

    @ifaces.setter
    def ifaces(self, ifaces):
        """Sets the ifaces of this HostCreationParamsData.


        :param ifaces: The ifaces of this HostCreationParamsData.  # noqa: E501
        :type ifaces: list[HostBatchCreateIfaceInput]
        """
        if self.local_vars_configuration.client_side_validation and ifaces is None:  # noqa: E501
            raise ValueError("Invalid value for `ifaces`, must not be `None`")  # noqa: E501

        self._ifaces = ifaces

    @property
    def disks(self):
        """Gets the disks of this HostCreationParamsData.  # noqa: E501


        :return: The disks of this HostCreationParamsData.  # noqa: E501
        :rtype: list[HostBatchCreateDiskInput]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this HostCreationParamsData.


        :param disks: The disks of this HostCreationParamsData.  # noqa: E501
        :type disks: list[HostBatchCreateDiskInput]
        """
        if self.local_vars_configuration.client_side_validation and disks is None:  # noqa: E501
            raise ValueError("Invalid value for `disks`, must not be `None`")  # noqa: E501

        self._disks = disks

    @property
    def platform_password(self):
        """Gets the platform_password of this HostCreationParamsData.  # noqa: E501


        :return: The platform_password of this HostCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._platform_password

    @platform_password.setter
    def platform_password(self, platform_password):
        """Sets the platform_password of this HostCreationParamsData.


        :param platform_password: The platform_password of this HostCreationParamsData.  # noqa: E501
        :type platform_password: str
        """

        self._platform_password = platform_password

    @property
    def platform_username(self):
        """Gets the platform_username of this HostCreationParamsData.  # noqa: E501


        :return: The platform_username of this HostCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._platform_username

    @platform_username.setter
    def platform_username(self, platform_username):
        """Sets the platform_username of this HostCreationParamsData.


        :param platform_username: The platform_username of this HostCreationParamsData.  # noqa: E501
        :type platform_username: str
        """

        self._platform_username = platform_username

    @property
    def platform_ip(self):
        """Gets the platform_ip of this HostCreationParamsData.  # noqa: E501


        :return: The platform_ip of this HostCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._platform_ip

    @platform_ip.setter
    def platform_ip(self, platform_ip):
        """Sets the platform_ip of this HostCreationParamsData.


        :param platform_ip: The platform_ip of this HostCreationParamsData.  # noqa: E501
        :type platform_ip: str
        """

        self._platform_ip = platform_ip

    @property
    def ipmi(self):
        """Gets the ipmi of this HostCreationParamsData.  # noqa: E501


        :return: The ipmi of this HostCreationParamsData.  # noqa: E501
        :rtype: HostBatchCreateIpmiInput
        """
        return self._ipmi

    @ipmi.setter
    def ipmi(self, ipmi):
        """Sets the ipmi of this HostCreationParamsData.


        :param ipmi: The ipmi of this HostCreationParamsData.  # noqa: E501
        :type ipmi: HostBatchCreateIpmiInput
        """

        self._ipmi = ipmi

    @property
    def hostname(self):
        """Gets the hostname of this HostCreationParamsData.  # noqa: E501


        :return: The hostname of this HostCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this HostCreationParamsData.


        :param hostname: The hostname of this HostCreationParamsData.  # noqa: E501
        :type hostname: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def host_uuid(self):
        """Gets the host_uuid of this HostCreationParamsData.  # noqa: E501


        :return: The host_uuid of this HostCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._host_uuid

    @host_uuid.setter
    def host_uuid(self, host_uuid):
        """Sets the host_uuid of this HostCreationParamsData.


        :param host_uuid: The host_uuid of this HostCreationParamsData.  # noqa: E501
        :type host_uuid: str
        """
        if self.local_vars_configuration.client_side_validation and host_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `host_uuid`, must not be `None`")  # noqa: E501

        self._host_uuid = host_uuid

    @property
    def host_ip(self):
        """Gets the host_ip of this HostCreationParamsData.  # noqa: E501


        :return: The host_ip of this HostCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this HostCreationParamsData.


        :param host_ip: The host_ip of this HostCreationParamsData.  # noqa: E501
        :type host_ip: str
        """
        if self.local_vars_configuration.client_side_validation and host_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `host_ip`, must not be `None`")  # noqa: E501

        self._host_ip = host_ip

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
        if not isinstance(other, HostCreationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostCreationParamsData):
            return True

        return self.to_dict() != other.to_dict()
