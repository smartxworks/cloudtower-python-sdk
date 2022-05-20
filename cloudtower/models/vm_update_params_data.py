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


class VmUpdateParamsData(object):
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
        'vcpu': 'int',
        'ha': 'bool',
        'memory': 'int',
        'cpu_cores': 'int',
        'cpu_sockets': 'int',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'vcpu': 'vcpu',
        'ha': 'ha',
        'memory': 'memory',
        'cpu_cores': 'cpu_cores',
        'cpu_sockets': 'cpu_sockets',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmUpdateParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._vcpu = None
        self._ha = None
        self._memory = None
        self._cpu_cores = None
        self._cpu_sockets = None
        self._description = None
        self._name = None
        self.discriminator = None

        if "vcpu" in kwargs:
            self.vcpu = kwargs["vcpu"]
        if "ha" in kwargs:
            self.ha = kwargs["ha"]
        if "memory" in kwargs:
            self.memory = kwargs["memory"]
        if "cpu_cores" in kwargs:
            self.cpu_cores = kwargs["cpu_cores"]
        if "cpu_sockets" in kwargs:
            self.cpu_sockets = kwargs["cpu_sockets"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def vcpu(self):
        """Gets the vcpu of this VmUpdateParamsData.  # noqa: E501


        :return: The vcpu of this VmUpdateParamsData.  # noqa: E501
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        """Sets the vcpu of this VmUpdateParamsData.


        :param vcpu: The vcpu of this VmUpdateParamsData.  # noqa: E501
        :type vcpu: int
        """

        self._vcpu = vcpu

    @property
    def ha(self):
        """Gets the ha of this VmUpdateParamsData.  # noqa: E501


        :return: The ha of this VmUpdateParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this VmUpdateParamsData.


        :param ha: The ha of this VmUpdateParamsData.  # noqa: E501
        :type ha: bool
        """

        self._ha = ha

    @property
    def memory(self):
        """Gets the memory of this VmUpdateParamsData.  # noqa: E501


        :return: The memory of this VmUpdateParamsData.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VmUpdateParamsData.


        :param memory: The memory of this VmUpdateParamsData.  # noqa: E501
        :type memory: int
        """

        self._memory = memory

    @property
    def cpu_cores(self):
        """Gets the cpu_cores of this VmUpdateParamsData.  # noqa: E501


        :return: The cpu_cores of this VmUpdateParamsData.  # noqa: E501
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """Sets the cpu_cores of this VmUpdateParamsData.


        :param cpu_cores: The cpu_cores of this VmUpdateParamsData.  # noqa: E501
        :type cpu_cores: int
        """

        self._cpu_cores = cpu_cores

    @property
    def cpu_sockets(self):
        """Gets the cpu_sockets of this VmUpdateParamsData.  # noqa: E501


        :return: The cpu_sockets of this VmUpdateParamsData.  # noqa: E501
        :rtype: int
        """
        return self._cpu_sockets

    @cpu_sockets.setter
    def cpu_sockets(self, cpu_sockets):
        """Sets the cpu_sockets of this VmUpdateParamsData.


        :param cpu_sockets: The cpu_sockets of this VmUpdateParamsData.  # noqa: E501
        :type cpu_sockets: int
        """

        self._cpu_sockets = cpu_sockets

    @property
    def description(self):
        """Gets the description of this VmUpdateParamsData.  # noqa: E501


        :return: The description of this VmUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VmUpdateParamsData.


        :param description: The description of this VmUpdateParamsData.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this VmUpdateParamsData.  # noqa: E501


        :return: The name of this VmUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmUpdateParamsData.


        :param name: The name of this VmUpdateParamsData.  # noqa: E501
        :type name: str
        """

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
        if not isinstance(other, VmUpdateParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmUpdateParamsData):
            return True

        return self.to_dict() != other.to_dict()
