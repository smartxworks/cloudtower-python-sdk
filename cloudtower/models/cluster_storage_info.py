# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ClusterStorageInfo(object):
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
        'allocable_storage_capacity': 'AllocatableStorageCapacity',
        'free_data_space': 'int',
        'failure_data_space': 'int',
        'used_data_space': 'int',
        'total_data_capacity': 'int',
        'storage_cluster': 'list[ClusterStorageInfo]',
        'stretch': 'bool',
        'type': 'ClusterType',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'allocable_storage_capacity': 'allocable_storage_capacity',
        'free_data_space': 'free_data_space',
        'failure_data_space': 'failure_data_space',
        'used_data_space': 'used_data_space',
        'total_data_capacity': 'total_data_capacity',
        'storage_cluster': 'storage_cluster',
        'stretch': 'stretch',
        'type': 'type',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ClusterStorageInfo - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._allocable_storage_capacity = None
        self._free_data_space = None
        self._failure_data_space = None
        self._used_data_space = None
        self._total_data_capacity = None
        self._storage_cluster = None
        self._stretch = None
        self._type = None
        self._name = None
        self._id = None
        self.discriminator = None

        if "allocable_storage_capacity" in kwargs:
            self.allocable_storage_capacity = kwargs["allocable_storage_capacity"]
        if "free_data_space" in kwargs:
            self.free_data_space = kwargs["free_data_space"]
        if "failure_data_space" in kwargs:
            self.failure_data_space = kwargs["failure_data_space"]
        if "used_data_space" in kwargs:
            self.used_data_space = kwargs["used_data_space"]
        if "total_data_capacity" in kwargs:
            self.total_data_capacity = kwargs["total_data_capacity"]
        if "storage_cluster" in kwargs:
            self.storage_cluster = kwargs["storage_cluster"]
        if "stretch" in kwargs:
            self.stretch = kwargs["stretch"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "id" in kwargs:
            self.id = kwargs["id"]

    @property
    def allocable_storage_capacity(self):
        """Gets the allocable_storage_capacity of this ClusterStorageInfo.  # noqa: E501


        :return: The allocable_storage_capacity of this ClusterStorageInfo.  # noqa: E501
        :rtype: AllocatableStorageCapacity
        """
        return self._allocable_storage_capacity

    @allocable_storage_capacity.setter
    def allocable_storage_capacity(self, allocable_storage_capacity):
        """Sets the allocable_storage_capacity of this ClusterStorageInfo.


        :param allocable_storage_capacity: The allocable_storage_capacity of this ClusterStorageInfo.  # noqa: E501
        :type allocable_storage_capacity: AllocatableStorageCapacity
        """

        self._allocable_storage_capacity = allocable_storage_capacity

    @property
    def free_data_space(self):
        """Gets the free_data_space of this ClusterStorageInfo.  # noqa: E501


        :return: The free_data_space of this ClusterStorageInfo.  # noqa: E501
        :rtype: int
        """
        return self._free_data_space

    @free_data_space.setter
    def free_data_space(self, free_data_space):
        """Sets the free_data_space of this ClusterStorageInfo.


        :param free_data_space: The free_data_space of this ClusterStorageInfo.  # noqa: E501
        :type free_data_space: int
        """

        self._free_data_space = free_data_space

    @property
    def failure_data_space(self):
        """Gets the failure_data_space of this ClusterStorageInfo.  # noqa: E501


        :return: The failure_data_space of this ClusterStorageInfo.  # noqa: E501
        :rtype: int
        """
        return self._failure_data_space

    @failure_data_space.setter
    def failure_data_space(self, failure_data_space):
        """Sets the failure_data_space of this ClusterStorageInfo.


        :param failure_data_space: The failure_data_space of this ClusterStorageInfo.  # noqa: E501
        :type failure_data_space: int
        """

        self._failure_data_space = failure_data_space

    @property
    def used_data_space(self):
        """Gets the used_data_space of this ClusterStorageInfo.  # noqa: E501


        :return: The used_data_space of this ClusterStorageInfo.  # noqa: E501
        :rtype: int
        """
        return self._used_data_space

    @used_data_space.setter
    def used_data_space(self, used_data_space):
        """Sets the used_data_space of this ClusterStorageInfo.


        :param used_data_space: The used_data_space of this ClusterStorageInfo.  # noqa: E501
        :type used_data_space: int
        """

        self._used_data_space = used_data_space

    @property
    def total_data_capacity(self):
        """Gets the total_data_capacity of this ClusterStorageInfo.  # noqa: E501


        :return: The total_data_capacity of this ClusterStorageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_data_capacity

    @total_data_capacity.setter
    def total_data_capacity(self, total_data_capacity):
        """Sets the total_data_capacity of this ClusterStorageInfo.


        :param total_data_capacity: The total_data_capacity of this ClusterStorageInfo.  # noqa: E501
        :type total_data_capacity: int
        """

        self._total_data_capacity = total_data_capacity

    @property
    def storage_cluster(self):
        """Gets the storage_cluster of this ClusterStorageInfo.  # noqa: E501


        :return: The storage_cluster of this ClusterStorageInfo.  # noqa: E501
        :rtype: list[ClusterStorageInfo]
        """
        return self._storage_cluster

    @storage_cluster.setter
    def storage_cluster(self, storage_cluster):
        """Sets the storage_cluster of this ClusterStorageInfo.


        :param storage_cluster: The storage_cluster of this ClusterStorageInfo.  # noqa: E501
        :type storage_cluster: list[ClusterStorageInfo]
        """

        self._storage_cluster = storage_cluster

    @property
    def stretch(self):
        """Gets the stretch of this ClusterStorageInfo.  # noqa: E501


        :return: The stretch of this ClusterStorageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._stretch

    @stretch.setter
    def stretch(self, stretch):
        """Sets the stretch of this ClusterStorageInfo.


        :param stretch: The stretch of this ClusterStorageInfo.  # noqa: E501
        :type stretch: bool
        """

        self._stretch = stretch

    @property
    def type(self):
        """Gets the type of this ClusterStorageInfo.  # noqa: E501


        :return: The type of this ClusterStorageInfo.  # noqa: E501
        :rtype: ClusterType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterStorageInfo.


        :param type: The type of this ClusterStorageInfo.  # noqa: E501
        :type type: ClusterType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this ClusterStorageInfo.  # noqa: E501


        :return: The name of this ClusterStorageInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterStorageInfo.


        :param name: The name of this ClusterStorageInfo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this ClusterStorageInfo.  # noqa: E501


        :return: The id of this ClusterStorageInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterStorageInfo.


        :param id: The id of this ClusterStorageInfo.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, ClusterStorageInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterStorageInfo):
            return True

        return self.to_dict() != other.to_dict()
