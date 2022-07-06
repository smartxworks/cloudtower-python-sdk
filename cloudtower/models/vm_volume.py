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


class VmVolume(object):
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
        'description': 'str',
        'elf_storage_policy': 'VmVolumeElfStoragePolicyType',
        'guest_size_usage': 'float',
        'guest_used_size': 'int',
        'id': 'str',
        'labels': 'list[NestedLabel]',
        'local_created_at': 'str',
        'local_id': 'str',
        'lun': 'NestedIscsiLun',
        'mounting': 'bool',
        'name': 'str',
        'path': 'str',
        'sharing': 'bool',
        'size': 'int',
        'unique_size': 'int',
        'vm_disks': 'list[NestedVmDisk]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'description': 'description',
        'elf_storage_policy': 'elf_storage_policy',
        'guest_size_usage': 'guest_size_usage',
        'guest_used_size': 'guest_used_size',
        'id': 'id',
        'labels': 'labels',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'lun': 'lun',
        'mounting': 'mounting',
        'name': 'name',
        'path': 'path',
        'sharing': 'sharing',
        'size': 'size',
        'unique_size': 'unique_size',
        'vm_disks': 'vm_disks'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmVolume - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._description = None
        self._elf_storage_policy = None
        self._guest_size_usage = None
        self._guest_used_size = None
        self._id = None
        self._labels = None
        self._local_created_at = None
        self._local_id = None
        self._lun = None
        self._mounting = None
        self._name = None
        self._path = None
        self._sharing = None
        self._size = None
        self._unique_size = None
        self._vm_disks = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        self.description = kwargs.get("description", None)
        if "elf_storage_policy" in kwargs:
            self.elf_storage_policy = kwargs["elf_storage_policy"]
        self.guest_size_usage = kwargs.get("guest_size_usage", None)
        self.guest_used_size = kwargs.get("guest_used_size", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.labels = kwargs.get("labels", None)
        if "local_created_at" in kwargs:
            self.local_created_at = kwargs["local_created_at"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        self.lun = kwargs.get("lun", None)
        if "mounting" in kwargs:
            self.mounting = kwargs["mounting"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "path" in kwargs:
            self.path = kwargs["path"]
        if "sharing" in kwargs:
            self.sharing = kwargs["sharing"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        self.unique_size = kwargs.get("unique_size", None)
        self.vm_disks = kwargs.get("vm_disks", None)

    @property
    def cluster(self):
        """Gets the cluster of this VmVolume.  # noqa: E501


        :return: The cluster of this VmVolume.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this VmVolume.


        :param cluster: The cluster of this VmVolume.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def description(self):
        """Gets the description of this VmVolume.  # noqa: E501


        :return: The description of this VmVolume.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VmVolume.


        :param description: The description of this VmVolume.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def elf_storage_policy(self):
        """Gets the elf_storage_policy of this VmVolume.  # noqa: E501


        :return: The elf_storage_policy of this VmVolume.  # noqa: E501
        :rtype: VmVolumeElfStoragePolicyType
        """
        return self._elf_storage_policy

    @elf_storage_policy.setter
    def elf_storage_policy(self, elf_storage_policy):
        """Sets the elf_storage_policy of this VmVolume.


        :param elf_storage_policy: The elf_storage_policy of this VmVolume.  # noqa: E501
        :type elf_storage_policy: VmVolumeElfStoragePolicyType
        """
        if self.local_vars_configuration.client_side_validation and elf_storage_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `elf_storage_policy`, must not be `None`")  # noqa: E501

        self._elf_storage_policy = elf_storage_policy

    @property
    def guest_size_usage(self):
        """Gets the guest_size_usage of this VmVolume.  # noqa: E501


        :return: The guest_size_usage of this VmVolume.  # noqa: E501
        :rtype: float
        """
        return self._guest_size_usage

    @guest_size_usage.setter
    def guest_size_usage(self, guest_size_usage):
        """Sets the guest_size_usage of this VmVolume.


        :param guest_size_usage: The guest_size_usage of this VmVolume.  # noqa: E501
        :type guest_size_usage: float
        """

        self._guest_size_usage = guest_size_usage

    @property
    def guest_used_size(self):
        """Gets the guest_used_size of this VmVolume.  # noqa: E501


        :return: The guest_used_size of this VmVolume.  # noqa: E501
        :rtype: int
        """
        return self._guest_used_size

    @guest_used_size.setter
    def guest_used_size(self, guest_used_size):
        """Sets the guest_used_size of this VmVolume.


        :param guest_used_size: The guest_used_size of this VmVolume.  # noqa: E501
        :type guest_used_size: int
        """

        self._guest_used_size = guest_used_size

    @property
    def id(self):
        """Gets the id of this VmVolume.  # noqa: E501


        :return: The id of this VmVolume.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmVolume.


        :param id: The id of this VmVolume.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this VmVolume.  # noqa: E501


        :return: The labels of this VmVolume.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this VmVolume.


        :param labels: The labels of this VmVolume.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def local_created_at(self):
        """Gets the local_created_at of this VmVolume.  # noqa: E501


        :return: The local_created_at of this VmVolume.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this VmVolume.


        :param local_created_at: The local_created_at of this VmVolume.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this VmVolume.  # noqa: E501


        :return: The local_id of this VmVolume.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VmVolume.


        :param local_id: The local_id of this VmVolume.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def lun(self):
        """Gets the lun of this VmVolume.  # noqa: E501


        :return: The lun of this VmVolume.  # noqa: E501
        :rtype: NestedIscsiLun
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """Sets the lun of this VmVolume.


        :param lun: The lun of this VmVolume.  # noqa: E501
        :type lun: NestedIscsiLun
        """

        self._lun = lun

    @property
    def mounting(self):
        """Gets the mounting of this VmVolume.  # noqa: E501


        :return: The mounting of this VmVolume.  # noqa: E501
        :rtype: bool
        """
        return self._mounting

    @mounting.setter
    def mounting(self, mounting):
        """Sets the mounting of this VmVolume.


        :param mounting: The mounting of this VmVolume.  # noqa: E501
        :type mounting: bool
        """
        if self.local_vars_configuration.client_side_validation and mounting is None:  # noqa: E501
            raise ValueError("Invalid value for `mounting`, must not be `None`")  # noqa: E501

        self._mounting = mounting

    @property
    def name(self):
        """Gets the name of this VmVolume.  # noqa: E501


        :return: The name of this VmVolume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmVolume.


        :param name: The name of this VmVolume.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this VmVolume.  # noqa: E501


        :return: The path of this VmVolume.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this VmVolume.


        :param path: The path of this VmVolume.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def sharing(self):
        """Gets the sharing of this VmVolume.  # noqa: E501


        :return: The sharing of this VmVolume.  # noqa: E501
        :rtype: bool
        """
        return self._sharing

    @sharing.setter
    def sharing(self, sharing):
        """Sets the sharing of this VmVolume.


        :param sharing: The sharing of this VmVolume.  # noqa: E501
        :type sharing: bool
        """
        if self.local_vars_configuration.client_side_validation and sharing is None:  # noqa: E501
            raise ValueError("Invalid value for `sharing`, must not be `None`")  # noqa: E501

        self._sharing = sharing

    @property
    def size(self):
        """Gets the size of this VmVolume.  # noqa: E501


        :return: The size of this VmVolume.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VmVolume.


        :param size: The size of this VmVolume.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def unique_size(self):
        """Gets the unique_size of this VmVolume.  # noqa: E501


        :return: The unique_size of this VmVolume.  # noqa: E501
        :rtype: int
        """
        return self._unique_size

    @unique_size.setter
    def unique_size(self, unique_size):
        """Sets the unique_size of this VmVolume.


        :param unique_size: The unique_size of this VmVolume.  # noqa: E501
        :type unique_size: int
        """

        self._unique_size = unique_size

    @property
    def vm_disks(self):
        """Gets the vm_disks of this VmVolume.  # noqa: E501


        :return: The vm_disks of this VmVolume.  # noqa: E501
        :rtype: list[NestedVmDisk]
        """
        return self._vm_disks

    @vm_disks.setter
    def vm_disks(self, vm_disks):
        """Sets the vm_disks of this VmVolume.


        :param vm_disks: The vm_disks of this VmVolume.  # noqa: E501
        :type vm_disks: list[NestedVmDisk]
        """

        self._vm_disks = vm_disks

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
        if not isinstance(other, VmVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmVolume):
            return True

        return self.to_dict() != other.to_dict()
