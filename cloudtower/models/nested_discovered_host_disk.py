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


class NestedDiscoveredHostDisk(object):
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
        'dimm_ids': 'list[str]',
        'drive': 'str',
        'function': 'DiskFunction',
        'model': 'str',
        'numa_node': 'int',
        'persistent_memory_type': 'str',
        'serial': 'str',
        'size': 'int',
        'type': 'DiskType'
    }

    attribute_map = {
        'dimm_ids': 'dimm_ids',
        'drive': 'drive',
        'function': 'function',
        'model': 'model',
        'numa_node': 'numa_node',
        'persistent_memory_type': 'persistent_memory_type',
        'serial': 'serial',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedDiscoveredHostDisk - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._dimm_ids = None
        self._drive = None
        self._function = None
        self._model = None
        self._numa_node = None
        self._persistent_memory_type = None
        self._serial = None
        self._size = None
        self._type = None
        self.discriminator = None

        self.dimm_ids = kwargs.get("dimm_ids", None)
        if "drive" in kwargs:
            self.drive = kwargs["drive"]
        self.function = kwargs.get("function", None)
        if "model" in kwargs:
            self.model = kwargs["model"]
        self.numa_node = kwargs.get("numa_node", None)
        self.persistent_memory_type = kwargs.get("persistent_memory_type", None)
        if "serial" in kwargs:
            self.serial = kwargs["serial"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "type" in kwargs:
            self.type = kwargs["type"]

    @property
    def dimm_ids(self):
        """Gets the dimm_ids of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The dimm_ids of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: list[str]
        """
        return self._dimm_ids

    @dimm_ids.setter
    def dimm_ids(self, dimm_ids):
        """Sets the dimm_ids of this NestedDiscoveredHostDisk.


        :param dimm_ids: The dimm_ids of this NestedDiscoveredHostDisk.  # noqa: E501
        :type dimm_ids: list[str]
        """

        self._dimm_ids = dimm_ids

    @property
    def drive(self):
        """Gets the drive of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The drive of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: str
        """
        return self._drive

    @drive.setter
    def drive(self, drive):
        """Sets the drive of this NestedDiscoveredHostDisk.


        :param drive: The drive of this NestedDiscoveredHostDisk.  # noqa: E501
        :type drive: str
        """
        if self.local_vars_configuration.client_side_validation and drive is None:  # noqa: E501
            raise ValueError("Invalid value for `drive`, must not be `None`")  # noqa: E501

        self._drive = drive

    @property
    def function(self):
        """Gets the function of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The function of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: DiskFunction
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this NestedDiscoveredHostDisk.


        :param function: The function of this NestedDiscoveredHostDisk.  # noqa: E501
        :type function: DiskFunction
        """

        self._function = function

    @property
    def model(self):
        """Gets the model of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The model of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this NestedDiscoveredHostDisk.


        :param model: The model of this NestedDiscoveredHostDisk.  # noqa: E501
        :type model: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def numa_node(self):
        """Gets the numa_node of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The numa_node of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: int
        """
        return self._numa_node

    @numa_node.setter
    def numa_node(self, numa_node):
        """Sets the numa_node of this NestedDiscoveredHostDisk.


        :param numa_node: The numa_node of this NestedDiscoveredHostDisk.  # noqa: E501
        :type numa_node: int
        """

        self._numa_node = numa_node

    @property
    def persistent_memory_type(self):
        """Gets the persistent_memory_type of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The persistent_memory_type of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: str
        """
        return self._persistent_memory_type

    @persistent_memory_type.setter
    def persistent_memory_type(self, persistent_memory_type):
        """Sets the persistent_memory_type of this NestedDiscoveredHostDisk.


        :param persistent_memory_type: The persistent_memory_type of this NestedDiscoveredHostDisk.  # noqa: E501
        :type persistent_memory_type: str
        """

        self._persistent_memory_type = persistent_memory_type

    @property
    def serial(self):
        """Gets the serial of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The serial of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this NestedDiscoveredHostDisk.


        :param serial: The serial of this NestedDiscoveredHostDisk.  # noqa: E501
        :type serial: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def size(self):
        """Gets the size of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The size of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NestedDiscoveredHostDisk.


        :param size: The size of this NestedDiscoveredHostDisk.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def type(self):
        """Gets the type of this NestedDiscoveredHostDisk.  # noqa: E501


        :return: The type of this NestedDiscoveredHostDisk.  # noqa: E501
        :rtype: DiskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NestedDiscoveredHostDisk.


        :param type: The type of this NestedDiscoveredHostDisk.  # noqa: E501
        :type type: DiskType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, NestedDiscoveredHostDisk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedDiscoveredHostDisk):
            return True

        return self.to_dict() != other.to_dict()