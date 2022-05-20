# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.10.0
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


class PmemDimm(object):
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
        'capacity': 'int',
        'device_locator': 'str',
        'disk': 'NestedDisk',
        'health_status': 'DiskHealthStatus',
        'host': 'NestedHost',
        'id': 'str',
        'local_id': 'str',
        'name': 'str',
        'numa_node': 'int',
        'part_number': 'str',
        'remaining_life_percent': 'int',
        'version': 'str'
    }

    attribute_map = {
        'capacity': 'capacity',
        'device_locator': 'device_locator',
        'disk': 'disk',
        'health_status': 'health_status',
        'host': 'host',
        'id': 'id',
        'local_id': 'local_id',
        'name': 'name',
        'numa_node': 'numa_node',
        'part_number': 'part_number',
        'remaining_life_percent': 'remaining_life_percent',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """PmemDimm - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._capacity = None
        self._device_locator = None
        self._disk = None
        self._health_status = None
        self._host = None
        self._id = None
        self._local_id = None
        self._name = None
        self._numa_node = None
        self._part_number = None
        self._remaining_life_percent = None
        self._version = None
        self.discriminator = None

        if "capacity" in kwargs:
            self.capacity = kwargs["capacity"]
        if "device_locator" in kwargs:
            self.device_locator = kwargs["device_locator"]
        self.disk = kwargs.get("disk", None)
        self.health_status = kwargs.get("health_status", None)
        if "host" in kwargs:
            self.host = kwargs["host"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.local_id = kwargs.get("local_id", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "numa_node" in kwargs:
            self.numa_node = kwargs["numa_node"]
        if "part_number" in kwargs:
            self.part_number = kwargs["part_number"]
        self.remaining_life_percent = kwargs.get("remaining_life_percent", None)
        if "version" in kwargs:
            self.version = kwargs["version"]

    @property
    def capacity(self):
        """Gets the capacity of this PmemDimm.  # noqa: E501


        :return: The capacity of this PmemDimm.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this PmemDimm.


        :param capacity: The capacity of this PmemDimm.  # noqa: E501
        :type capacity: int
        """
        if self.local_vars_configuration.client_side_validation and capacity is None:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501

        self._capacity = capacity

    @property
    def device_locator(self):
        """Gets the device_locator of this PmemDimm.  # noqa: E501


        :return: The device_locator of this PmemDimm.  # noqa: E501
        :rtype: str
        """
        return self._device_locator

    @device_locator.setter
    def device_locator(self, device_locator):
        """Sets the device_locator of this PmemDimm.


        :param device_locator: The device_locator of this PmemDimm.  # noqa: E501
        :type device_locator: str
        """
        if self.local_vars_configuration.client_side_validation and device_locator is None:  # noqa: E501
            raise ValueError("Invalid value for `device_locator`, must not be `None`")  # noqa: E501

        self._device_locator = device_locator

    @property
    def disk(self):
        """Gets the disk of this PmemDimm.  # noqa: E501


        :return: The disk of this PmemDimm.  # noqa: E501
        :rtype: NestedDisk
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this PmemDimm.


        :param disk: The disk of this PmemDimm.  # noqa: E501
        :type disk: NestedDisk
        """

        self._disk = disk

    @property
    def health_status(self):
        """Gets the health_status of this PmemDimm.  # noqa: E501


        :return: The health_status of this PmemDimm.  # noqa: E501
        :rtype: DiskHealthStatus
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """Sets the health_status of this PmemDimm.


        :param health_status: The health_status of this PmemDimm.  # noqa: E501
        :type health_status: DiskHealthStatus
        """

        self._health_status = health_status

    @property
    def host(self):
        """Gets the host of this PmemDimm.  # noqa: E501


        :return: The host of this PmemDimm.  # noqa: E501
        :rtype: NestedHost
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this PmemDimm.


        :param host: The host of this PmemDimm.  # noqa: E501
        :type host: NestedHost
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def id(self):
        """Gets the id of this PmemDimm.  # noqa: E501


        :return: The id of this PmemDimm.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PmemDimm.


        :param id: The id of this PmemDimm.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this PmemDimm.  # noqa: E501


        :return: The local_id of this PmemDimm.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this PmemDimm.


        :param local_id: The local_id of this PmemDimm.  # noqa: E501
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this PmemDimm.  # noqa: E501


        :return: The name of this PmemDimm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PmemDimm.


        :param name: The name of this PmemDimm.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def numa_node(self):
        """Gets the numa_node of this PmemDimm.  # noqa: E501


        :return: The numa_node of this PmemDimm.  # noqa: E501
        :rtype: int
        """
        return self._numa_node

    @numa_node.setter
    def numa_node(self, numa_node):
        """Sets the numa_node of this PmemDimm.


        :param numa_node: The numa_node of this PmemDimm.  # noqa: E501
        :type numa_node: int
        """
        if self.local_vars_configuration.client_side_validation and numa_node is None:  # noqa: E501
            raise ValueError("Invalid value for `numa_node`, must not be `None`")  # noqa: E501

        self._numa_node = numa_node

    @property
    def part_number(self):
        """Gets the part_number of this PmemDimm.  # noqa: E501


        :return: The part_number of this PmemDimm.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this PmemDimm.


        :param part_number: The part_number of this PmemDimm.  # noqa: E501
        :type part_number: str
        """
        if self.local_vars_configuration.client_side_validation and part_number is None:  # noqa: E501
            raise ValueError("Invalid value for `part_number`, must not be `None`")  # noqa: E501

        self._part_number = part_number

    @property
    def remaining_life_percent(self):
        """Gets the remaining_life_percent of this PmemDimm.  # noqa: E501


        :return: The remaining_life_percent of this PmemDimm.  # noqa: E501
        :rtype: int
        """
        return self._remaining_life_percent

    @remaining_life_percent.setter
    def remaining_life_percent(self, remaining_life_percent):
        """Sets the remaining_life_percent of this PmemDimm.


        :param remaining_life_percent: The remaining_life_percent of this PmemDimm.  # noqa: E501
        :type remaining_life_percent: int
        """

        self._remaining_life_percent = remaining_life_percent

    @property
    def version(self):
        """Gets the version of this PmemDimm.  # noqa: E501


        :return: The version of this PmemDimm.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PmemDimm.


        :param version: The version of this PmemDimm.  # noqa: E501
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
        if not isinstance(other, PmemDimm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PmemDimm):
            return True

        return self.to_dict() != other.to_dict()
