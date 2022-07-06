# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class ClusterImage(object):
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
        'cluster': 'NestedCluster',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'local_id': 'str',
        'meta_name': 'str',
        'meta_size': 'int',
        'name': 'str',
        'size': 'int',
        'upgrade_from': 'list[str]',
        'upgrade_tool_version': 'str',
        'version': 'str',
        'zbs_version': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'local_id': 'local_id',
        'meta_name': 'meta_name',
        'meta_size': 'meta_size',
        'name': 'name',
        'size': 'size',
        'upgrade_from': 'upgrade_from',
        'upgrade_tool_version': 'upgrade_tool_version',
        'version': 'version',
        'zbs_version': 'zbs_version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ClusterImage - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._entity_async_status = None
        self._id = None
        self._local_id = None
        self._meta_name = None
        self._meta_size = None
        self._name = None
        self._size = None
        self._upgrade_from = None
        self._upgrade_tool_version = None
        self._version = None
        self._zbs_version = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.local_id = kwargs.get("local_id", None)
        if "meta_name" in kwargs:
            self.meta_name = kwargs["meta_name"]
        if "meta_size" in kwargs:
            self.meta_size = kwargs["meta_size"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "upgrade_from" in kwargs:
            self.upgrade_from = kwargs["upgrade_from"]
        self.upgrade_tool_version = kwargs.get("upgrade_tool_version", None)
        if "version" in kwargs:
            self.version = kwargs["version"]
        self.zbs_version = kwargs.get("zbs_version", None)

    @property
    def cluster(self):
        """Gets the cluster of this ClusterImage.  # noqa: E501


        :return: The cluster of this ClusterImage.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ClusterImage.


        :param cluster: The cluster of this ClusterImage.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this ClusterImage.  # noqa: E501


        :return: The entity_async_status of this ClusterImage.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this ClusterImage.


        :param entity_async_status: The entity_async_status of this ClusterImage.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this ClusterImage.  # noqa: E501


        :return: The id of this ClusterImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterImage.


        :param id: The id of this ClusterImage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this ClusterImage.  # noqa: E501


        :return: The local_id of this ClusterImage.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this ClusterImage.


        :param local_id: The local_id of this ClusterImage.  # noqa: E501
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def meta_name(self):
        """Gets the meta_name of this ClusterImage.  # noqa: E501


        :return: The meta_name of this ClusterImage.  # noqa: E501
        :rtype: str
        """
        return self._meta_name

    @meta_name.setter
    def meta_name(self, meta_name):
        """Sets the meta_name of this ClusterImage.


        :param meta_name: The meta_name of this ClusterImage.  # noqa: E501
        :type meta_name: str
        """
        if self.local_vars_configuration.client_side_validation and meta_name is None:  # noqa: E501
            raise ValueError("Invalid value for `meta_name`, must not be `None`")  # noqa: E501

        self._meta_name = meta_name

    @property
    def meta_size(self):
        """Gets the meta_size of this ClusterImage.  # noqa: E501


        :return: The meta_size of this ClusterImage.  # noqa: E501
        :rtype: int
        """
        return self._meta_size

    @meta_size.setter
    def meta_size(self, meta_size):
        """Sets the meta_size of this ClusterImage.


        :param meta_size: The meta_size of this ClusterImage.  # noqa: E501
        :type meta_size: int
        """
        if self.local_vars_configuration.client_side_validation and meta_size is None:  # noqa: E501
            raise ValueError("Invalid value for `meta_size`, must not be `None`")  # noqa: E501

        self._meta_size = meta_size

    @property
    def name(self):
        """Gets the name of this ClusterImage.  # noqa: E501


        :return: The name of this ClusterImage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterImage.


        :param name: The name of this ClusterImage.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this ClusterImage.  # noqa: E501


        :return: The size of this ClusterImage.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ClusterImage.


        :param size: The size of this ClusterImage.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def upgrade_from(self):
        """Gets the upgrade_from of this ClusterImage.  # noqa: E501


        :return: The upgrade_from of this ClusterImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._upgrade_from

    @upgrade_from.setter
    def upgrade_from(self, upgrade_from):
        """Sets the upgrade_from of this ClusterImage.


        :param upgrade_from: The upgrade_from of this ClusterImage.  # noqa: E501
        :type upgrade_from: list[str]
        """
        if self.local_vars_configuration.client_side_validation and upgrade_from is None:  # noqa: E501
            raise ValueError("Invalid value for `upgrade_from`, must not be `None`")  # noqa: E501

        self._upgrade_from = upgrade_from

    @property
    def upgrade_tool_version(self):
        """Gets the upgrade_tool_version of this ClusterImage.  # noqa: E501


        :return: The upgrade_tool_version of this ClusterImage.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_tool_version

    @upgrade_tool_version.setter
    def upgrade_tool_version(self, upgrade_tool_version):
        """Sets the upgrade_tool_version of this ClusterImage.


        :param upgrade_tool_version: The upgrade_tool_version of this ClusterImage.  # noqa: E501
        :type upgrade_tool_version: str
        """

        self._upgrade_tool_version = upgrade_tool_version

    @property
    def version(self):
        """Gets the version of this ClusterImage.  # noqa: E501


        :return: The version of this ClusterImage.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterImage.


        :param version: The version of this ClusterImage.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def zbs_version(self):
        """Gets the zbs_version of this ClusterImage.  # noqa: E501


        :return: The zbs_version of this ClusterImage.  # noqa: E501
        :rtype: str
        """
        return self._zbs_version

    @zbs_version.setter
    def zbs_version(self, zbs_version):
        """Sets the zbs_version of this ClusterImage.


        :param zbs_version: The zbs_version of this ClusterImage.  # noqa: E501
        :type zbs_version: str
        """

        self._zbs_version = zbs_version

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
        if not isinstance(other, ClusterImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterImage):
            return True

        return self.to_dict() != other.to_dict()
