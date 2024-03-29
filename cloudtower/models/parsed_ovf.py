# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ParsedOVF(object):
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
        'firmware': 'VmFirmware',
        'disks': 'list[OvfDisk]',
        'nics': 'list[OvfNic]',
        'memory': 'int',
        'cpu': 'OvfCpu',
        'vcpu': 'int',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'firmware': 'firmware',
        'disks': 'disks',
        'nics': 'nics',
        'memory': 'memory',
        'cpu': 'cpu',
        'vcpu': 'vcpu',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ParsedOVF - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._firmware = None
        self._disks = None
        self._nics = None
        self._memory = None
        self._cpu = None
        self._vcpu = None
        self._description = None
        self._name = None
        self.discriminator = None

        if "firmware" in kwargs:
            self.firmware = kwargs["firmware"]
        if "disks" in kwargs:
            self.disks = kwargs["disks"]
        if "nics" in kwargs:
            self.nics = kwargs["nics"]
        if "memory" in kwargs:
            self.memory = kwargs["memory"]
        if "cpu" in kwargs:
            self.cpu = kwargs["cpu"]
        if "vcpu" in kwargs:
            self.vcpu = kwargs["vcpu"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def firmware(self):
        """Gets the firmware of this ParsedOVF.  # noqa: E501


        :return: The firmware of this ParsedOVF.  # noqa: E501
        :rtype: VmFirmware
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this ParsedOVF.


        :param firmware: The firmware of this ParsedOVF.  # noqa: E501
        :type firmware: VmFirmware
        """
        if self.local_vars_configuration.client_side_validation and firmware is None:  # noqa: E501
            raise ValueError("Invalid value for `firmware`, must not be `None`")  # noqa: E501

        self._firmware = firmware

    @property
    def disks(self):
        """Gets the disks of this ParsedOVF.  # noqa: E501


        :return: The disks of this ParsedOVF.  # noqa: E501
        :rtype: list[OvfDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this ParsedOVF.


        :param disks: The disks of this ParsedOVF.  # noqa: E501
        :type disks: list[OvfDisk]
        """
        if self.local_vars_configuration.client_side_validation and disks is None:  # noqa: E501
            raise ValueError("Invalid value for `disks`, must not be `None`")  # noqa: E501

        self._disks = disks

    @property
    def nics(self):
        """Gets the nics of this ParsedOVF.  # noqa: E501


        :return: The nics of this ParsedOVF.  # noqa: E501
        :rtype: list[OvfNic]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this ParsedOVF.


        :param nics: The nics of this ParsedOVF.  # noqa: E501
        :type nics: list[OvfNic]
        """
        if self.local_vars_configuration.client_side_validation and nics is None:  # noqa: E501
            raise ValueError("Invalid value for `nics`, must not be `None`")  # noqa: E501

        self._nics = nics

    @property
    def memory(self):
        """Gets the memory of this ParsedOVF.  # noqa: E501


        :return: The memory of this ParsedOVF.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ParsedOVF.


        :param memory: The memory of this ParsedOVF.  # noqa: E501
        :type memory: int
        """
        if self.local_vars_configuration.client_side_validation and memory is None:  # noqa: E501
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this ParsedOVF.  # noqa: E501


        :return: The cpu of this ParsedOVF.  # noqa: E501
        :rtype: OvfCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ParsedOVF.


        :param cpu: The cpu of this ParsedOVF.  # noqa: E501
        :type cpu: OvfCpu
        """
        if self.local_vars_configuration.client_side_validation and cpu is None:  # noqa: E501
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def vcpu(self):
        """Gets the vcpu of this ParsedOVF.  # noqa: E501


        :return: The vcpu of this ParsedOVF.  # noqa: E501
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        """Sets the vcpu of this ParsedOVF.


        :param vcpu: The vcpu of this ParsedOVF.  # noqa: E501
        :type vcpu: int
        """
        if self.local_vars_configuration.client_side_validation and vcpu is None:  # noqa: E501
            raise ValueError("Invalid value for `vcpu`, must not be `None`")  # noqa: E501

        self._vcpu = vcpu

    @property
    def description(self):
        """Gets the description of this ParsedOVF.  # noqa: E501


        :return: The description of this ParsedOVF.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ParsedOVF.


        :param description: The description of this ParsedOVF.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ParsedOVF.  # noqa: E501


        :return: The name of this ParsedOVF.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParsedOVF.


        :param name: The name of this ParsedOVF.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, ParsedOVF):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParsedOVF):
            return True

        return self.to_dict() != other.to_dict()
