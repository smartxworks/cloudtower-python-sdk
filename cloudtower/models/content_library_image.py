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


class ContentLibraryImage(object):
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
        'clusters': 'list[NestedCluster]',
        'created_at': 'str',
        'description': 'str',
        'elf_image_uuids': 'list[str]',
        'elf_images': 'list[NestedElfImage]',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'labels': 'list[NestedLabel]',
        'name': 'str',
        'path': 'str',
        'size': 'int',
        'vm_disks': 'list[NestedVmDisk]',
        'vm_snapshots': 'list[NestedVmSnapshot]',
        'vm_templates': 'list[NestedVmTemplate]'
    }

    attribute_map = {
        'clusters': 'clusters',
        'created_at': 'createdAt',
        'description': 'description',
        'elf_image_uuids': 'elf_image_uuids',
        'elf_images': 'elf_images',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'labels': 'labels',
        'name': 'name',
        'path': 'path',
        'size': 'size',
        'vm_disks': 'vm_disks',
        'vm_snapshots': 'vm_snapshots',
        'vm_templates': 'vm_templates'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ContentLibraryImage - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._clusters = None
        self._created_at = None
        self._description = None
        self._elf_image_uuids = None
        self._elf_images = None
        self._entity_async_status = None
        self._id = None
        self._labels = None
        self._name = None
        self._path = None
        self._size = None
        self._vm_disks = None
        self._vm_snapshots = None
        self._vm_templates = None
        self.discriminator = None

        self.clusters = kwargs.get("clusters", None)
        if "created_at" in kwargs:
            self.created_at = kwargs["created_at"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "elf_image_uuids" in kwargs:
            self.elf_image_uuids = kwargs["elf_image_uuids"]
        self.elf_images = kwargs.get("elf_images", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.labels = kwargs.get("labels", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "path" in kwargs:
            self.path = kwargs["path"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        self.vm_disks = kwargs.get("vm_disks", None)
        self.vm_snapshots = kwargs.get("vm_snapshots", None)
        self.vm_templates = kwargs.get("vm_templates", None)

    @property
    def clusters(self):
        """Gets the clusters of this ContentLibraryImage.  # noqa: E501


        :return: The clusters of this ContentLibraryImage.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this ContentLibraryImage.


        :param clusters: The clusters of this ContentLibraryImage.  # noqa: E501
        :type clusters: list[NestedCluster]
        """

        self._clusters = clusters

    @property
    def created_at(self):
        """Gets the created_at of this ContentLibraryImage.  # noqa: E501


        :return: The created_at of this ContentLibraryImage.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ContentLibraryImage.


        :param created_at: The created_at of this ContentLibraryImage.  # noqa: E501
        :type created_at: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ContentLibraryImage.  # noqa: E501


        :return: The description of this ContentLibraryImage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContentLibraryImage.


        :param description: The description of this ContentLibraryImage.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def elf_image_uuids(self):
        """Gets the elf_image_uuids of this ContentLibraryImage.  # noqa: E501


        :return: The elf_image_uuids of this ContentLibraryImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._elf_image_uuids

    @elf_image_uuids.setter
    def elf_image_uuids(self, elf_image_uuids):
        """Sets the elf_image_uuids of this ContentLibraryImage.


        :param elf_image_uuids: The elf_image_uuids of this ContentLibraryImage.  # noqa: E501
        :type elf_image_uuids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and elf_image_uuids is None:  # noqa: E501
            raise ValueError("Invalid value for `elf_image_uuids`, must not be `None`")  # noqa: E501

        self._elf_image_uuids = elf_image_uuids

    @property
    def elf_images(self):
        """Gets the elf_images of this ContentLibraryImage.  # noqa: E501


        :return: The elf_images of this ContentLibraryImage.  # noqa: E501
        :rtype: list[NestedElfImage]
        """
        return self._elf_images

    @elf_images.setter
    def elf_images(self, elf_images):
        """Sets the elf_images of this ContentLibraryImage.


        :param elf_images: The elf_images of this ContentLibraryImage.  # noqa: E501
        :type elf_images: list[NestedElfImage]
        """

        self._elf_images = elf_images

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this ContentLibraryImage.  # noqa: E501


        :return: The entity_async_status of this ContentLibraryImage.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this ContentLibraryImage.


        :param entity_async_status: The entity_async_status of this ContentLibraryImage.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this ContentLibraryImage.  # noqa: E501


        :return: The id of this ContentLibraryImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContentLibraryImage.


        :param id: The id of this ContentLibraryImage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this ContentLibraryImage.  # noqa: E501


        :return: The labels of this ContentLibraryImage.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ContentLibraryImage.


        :param labels: The labels of this ContentLibraryImage.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this ContentLibraryImage.  # noqa: E501


        :return: The name of this ContentLibraryImage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentLibraryImage.


        :param name: The name of this ContentLibraryImage.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this ContentLibraryImage.  # noqa: E501


        :return: The path of this ContentLibraryImage.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ContentLibraryImage.


        :param path: The path of this ContentLibraryImage.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def size(self):
        """Gets the size of this ContentLibraryImage.  # noqa: E501


        :return: The size of this ContentLibraryImage.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ContentLibraryImage.


        :param size: The size of this ContentLibraryImage.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def vm_disks(self):
        """Gets the vm_disks of this ContentLibraryImage.  # noqa: E501


        :return: The vm_disks of this ContentLibraryImage.  # noqa: E501
        :rtype: list[NestedVmDisk]
        """
        return self._vm_disks

    @vm_disks.setter
    def vm_disks(self, vm_disks):
        """Sets the vm_disks of this ContentLibraryImage.


        :param vm_disks: The vm_disks of this ContentLibraryImage.  # noqa: E501
        :type vm_disks: list[NestedVmDisk]
        """

        self._vm_disks = vm_disks

    @property
    def vm_snapshots(self):
        """Gets the vm_snapshots of this ContentLibraryImage.  # noqa: E501


        :return: The vm_snapshots of this ContentLibraryImage.  # noqa: E501
        :rtype: list[NestedVmSnapshot]
        """
        return self._vm_snapshots

    @vm_snapshots.setter
    def vm_snapshots(self, vm_snapshots):
        """Sets the vm_snapshots of this ContentLibraryImage.


        :param vm_snapshots: The vm_snapshots of this ContentLibraryImage.  # noqa: E501
        :type vm_snapshots: list[NestedVmSnapshot]
        """

        self._vm_snapshots = vm_snapshots

    @property
    def vm_templates(self):
        """Gets the vm_templates of this ContentLibraryImage.  # noqa: E501


        :return: The vm_templates of this ContentLibraryImage.  # noqa: E501
        :rtype: list[NestedVmTemplate]
        """
        return self._vm_templates

    @vm_templates.setter
    def vm_templates(self, vm_templates):
        """Sets the vm_templates of this ContentLibraryImage.


        :param vm_templates: The vm_templates of this ContentLibraryImage.  # noqa: E501
        :type vm_templates: list[NestedVmTemplate]
        """

        self._vm_templates = vm_templates

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
        if not isinstance(other, ContentLibraryImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentLibraryImage):
            return True

        return self.to_dict() != other.to_dict()