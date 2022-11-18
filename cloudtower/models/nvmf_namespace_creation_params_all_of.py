# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NvmfNamespaceCreationParamsAllOf(object):
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
        'namespace_id': 'int',
        'group_id': 'str',
        'is_shared': 'bool',
        'assigned_size_unit': 'ByteUnit',
        'assigned_size': 'int',
        'replica_num': 'int',
        'nvmf_subsystem_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'namespace_id': 'namespace_id',
        'group_id': 'group_id',
        'is_shared': 'is_shared',
        'assigned_size_unit': 'assigned_size_unit',
        'assigned_size': 'assigned_size',
        'replica_num': 'replica_num',
        'nvmf_subsystem_id': 'nvmf_subsystem_id',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NvmfNamespaceCreationParamsAllOf - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._namespace_id = None
        self._group_id = None
        self._is_shared = None
        self._assigned_size_unit = None
        self._assigned_size = None
        self._replica_num = None
        self._nvmf_subsystem_id = None
        self._name = None
        self.discriminator = None

        if "namespace_id" in kwargs:
            self.namespace_id = kwargs["namespace_id"]
        if "group_id" in kwargs:
            self.group_id = kwargs["group_id"]
        if "is_shared" in kwargs:
            self.is_shared = kwargs["is_shared"]
        if "assigned_size_unit" in kwargs:
            self.assigned_size_unit = kwargs["assigned_size_unit"]
        if "assigned_size" in kwargs:
            self.assigned_size = kwargs["assigned_size"]
        if "replica_num" in kwargs:
            self.replica_num = kwargs["replica_num"]
        if "nvmf_subsystem_id" in kwargs:
            self.nvmf_subsystem_id = kwargs["nvmf_subsystem_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def namespace_id(self):
        """Gets the namespace_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The namespace_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        """Sets the namespace_id of this NvmfNamespaceCreationParamsAllOf.


        :param namespace_id: The namespace_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :type namespace_id: int
        """

        self._namespace_id = namespace_id

    @property
    def group_id(self):
        """Gets the group_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The group_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this NvmfNamespaceCreationParamsAllOf.


        :param group_id: The group_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def is_shared(self):
        """Gets the is_shared of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The is_shared of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_shared

    @is_shared.setter
    def is_shared(self, is_shared):
        """Sets the is_shared of this NvmfNamespaceCreationParamsAllOf.


        :param is_shared: The is_shared of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :type is_shared: bool
        """

        self._is_shared = is_shared

    @property
    def assigned_size_unit(self):
        """Gets the assigned_size_unit of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The assigned_size_unit of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: ByteUnit
        """
        return self._assigned_size_unit

    @assigned_size_unit.setter
    def assigned_size_unit(self, assigned_size_unit):
        """Sets the assigned_size_unit of this NvmfNamespaceCreationParamsAllOf.


        :param assigned_size_unit: The assigned_size_unit of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :type assigned_size_unit: ByteUnit
        """

        self._assigned_size_unit = assigned_size_unit

    @property
    def assigned_size(self):
        """Gets the assigned_size of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The assigned_size of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._assigned_size

    @assigned_size.setter
    def assigned_size(self, assigned_size):
        """Sets the assigned_size of this NvmfNamespaceCreationParamsAllOf.


        :param assigned_size: The assigned_size of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :type assigned_size: int
        """
        if self.local_vars_configuration.client_side_validation and assigned_size is None:  # noqa: E501
            raise ValueError("Invalid value for `assigned_size`, must not be `None`")  # noqa: E501

        self._assigned_size = assigned_size

    @property
    def replica_num(self):
        """Gets the replica_num of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The replica_num of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this NvmfNamespaceCreationParamsAllOf.


        :param replica_num: The replica_num of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :type replica_num: int
        """
        if self.local_vars_configuration.client_side_validation and replica_num is None:  # noqa: E501
            raise ValueError("Invalid value for `replica_num`, must not be `None`")  # noqa: E501

        self._replica_num = replica_num

    @property
    def nvmf_subsystem_id(self):
        """Gets the nvmf_subsystem_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The nvmf_subsystem_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._nvmf_subsystem_id

    @nvmf_subsystem_id.setter
    def nvmf_subsystem_id(self, nvmf_subsystem_id):
        """Sets the nvmf_subsystem_id of this NvmfNamespaceCreationParamsAllOf.


        :param nvmf_subsystem_id: The nvmf_subsystem_id of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :type nvmf_subsystem_id: str
        """
        if self.local_vars_configuration.client_side_validation and nvmf_subsystem_id is None:  # noqa: E501
            raise ValueError("Invalid value for `nvmf_subsystem_id`, must not be `None`")  # noqa: E501

        self._nvmf_subsystem_id = nvmf_subsystem_id

    @property
    def name(self):
        """Gets the name of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501


        :return: The name of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NvmfNamespaceCreationParamsAllOf.


        :param name: The name of this NvmfNamespaceCreationParamsAllOf.  # noqa: E501
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
        if not isinstance(other, NvmfNamespaceCreationParamsAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NvmfNamespaceCreationParamsAllOf):
            return True

        return self.to_dict() != other.to_dict()
