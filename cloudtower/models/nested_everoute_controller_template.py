# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class NestedEverouteControllerTemplate(object):
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
        'cluster': 'str',
        'gateway': 'str',
        'memory': 'int',
        'netmask': 'str',
        'size': 'int',
        'vcpu': 'int'
    }

    attribute_map = {
        'cluster': 'cluster',
        'gateway': 'gateway',
        'memory': 'memory',
        'netmask': 'netmask',
        'size': 'size',
        'vcpu': 'vcpu'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedEverouteControllerTemplate - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._gateway = None
        self._memory = None
        self._netmask = None
        self._size = None
        self._vcpu = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "gateway" in kwargs:
            self.gateway = kwargs["gateway"]
        if "memory" in kwargs:
            self.memory = kwargs["memory"]
        if "netmask" in kwargs:
            self.netmask = kwargs["netmask"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "vcpu" in kwargs:
            self.vcpu = kwargs["vcpu"]

    @property
    def cluster(self):
        """Gets the cluster of this NestedEverouteControllerTemplate.  # noqa: E501


        :return: The cluster of this NestedEverouteControllerTemplate.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this NestedEverouteControllerTemplate.


        :param cluster: The cluster of this NestedEverouteControllerTemplate.  # noqa: E501
        :type cluster: str
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def gateway(self):
        """Gets the gateway of this NestedEverouteControllerTemplate.  # noqa: E501


        :return: The gateway of this NestedEverouteControllerTemplate.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this NestedEverouteControllerTemplate.


        :param gateway: The gateway of this NestedEverouteControllerTemplate.  # noqa: E501
        :type gateway: str
        """
        if self.local_vars_configuration.client_side_validation and gateway is None:  # noqa: E501
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def memory(self):
        """Gets the memory of this NestedEverouteControllerTemplate.  # noqa: E501


        :return: The memory of this NestedEverouteControllerTemplate.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this NestedEverouteControllerTemplate.


        :param memory: The memory of this NestedEverouteControllerTemplate.  # noqa: E501
        :type memory: int
        """
        if self.local_vars_configuration.client_side_validation and memory is None:  # noqa: E501
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def netmask(self):
        """Gets the netmask of this NestedEverouteControllerTemplate.  # noqa: E501


        :return: The netmask of this NestedEverouteControllerTemplate.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this NestedEverouteControllerTemplate.


        :param netmask: The netmask of this NestedEverouteControllerTemplate.  # noqa: E501
        :type netmask: str
        """
        if self.local_vars_configuration.client_side_validation and netmask is None:  # noqa: E501
            raise ValueError("Invalid value for `netmask`, must not be `None`")  # noqa: E501

        self._netmask = netmask

    @property
    def size(self):
        """Gets the size of this NestedEverouteControllerTemplate.  # noqa: E501


        :return: The size of this NestedEverouteControllerTemplate.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NestedEverouteControllerTemplate.


        :param size: The size of this NestedEverouteControllerTemplate.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def vcpu(self):
        """Gets the vcpu of this NestedEverouteControllerTemplate.  # noqa: E501


        :return: The vcpu of this NestedEverouteControllerTemplate.  # noqa: E501
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        """Sets the vcpu of this NestedEverouteControllerTemplate.


        :param vcpu: The vcpu of this NestedEverouteControllerTemplate.  # noqa: E501
        :type vcpu: int
        """
        if self.local_vars_configuration.client_side_validation and vcpu is None:  # noqa: E501
            raise ValueError("Invalid value for `vcpu`, must not be `None`")  # noqa: E501

        self._vcpu = vcpu

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
        if not isinstance(other, NestedEverouteControllerTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedEverouteControllerTemplate):
            return True

        return self.to_dict() != other.to_dict()
