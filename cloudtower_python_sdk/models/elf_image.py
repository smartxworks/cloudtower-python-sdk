# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower_python_sdk.configuration import Configuration


class ElfImage(object):
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
        'content_library_image': 'NestedContentLibraryImage',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'labels': 'list[NestedLabel]',
        'local_created_at': 'str',
        'local_id': 'str',
        'name': 'str',
        'path': 'str',
        'size': 'float',
        'upload_task': 'NestedUploadTask',
        'vm_disks': 'list[NestedVmDisk]',
        'vm_snapshots': 'list[NestedVmSnapshot]',
        'vm_templates': 'list[NestedVmTemplate]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'content_library_image': 'content_library_image',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'labels': 'labels',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'name': 'name',
        'path': 'path',
        'size': 'size',
        'upload_task': 'upload_task',
        'vm_disks': 'vm_disks',
        'vm_snapshots': 'vm_snapshots',
        'vm_templates': 'vm_templates'
    }

    def __init__(self, cluster=None, content_library_image=None, description=None, entity_async_status=None, id=None, labels=None, local_created_at=None, local_id=None, name=None, path=None, size=None, upload_task=None, vm_disks=None, vm_snapshots=None, vm_templates=None, local_vars_configuration=None):  # noqa: E501
        """ElfImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cluster = None
        self._content_library_image = None
        self._description = None
        self._entity_async_status = None
        self._id = None
        self._labels = None
        self._local_created_at = None
        self._local_id = None
        self._name = None
        self._path = None
        self._size = None
        self._upload_task = None
        self._vm_disks = None
        self._vm_snapshots = None
        self._vm_templates = None
        self.discriminator = None

        self.cluster = cluster
        self.content_library_image = content_library_image
        self.description = description
        self.entity_async_status = entity_async_status
        self.id = id
        self.labels = labels
        self.local_created_at = local_created_at
        self.local_id = local_id
        self.name = name
        self.path = path
        self.size = size
        self.upload_task = upload_task
        self.vm_disks = vm_disks
        self.vm_snapshots = vm_snapshots
        self.vm_templates = vm_templates

    @property
    def cluster(self):
        """Gets the cluster of this ElfImage.  # noqa: E501


        :return: The cluster of this ElfImage.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ElfImage.


        :param cluster: The cluster of this ElfImage.  # noqa: E501
        :type cluster: NestedCluster
        """

        self._cluster = cluster

    @property
    def content_library_image(self):
        """Gets the content_library_image of this ElfImage.  # noqa: E501


        :return: The content_library_image of this ElfImage.  # noqa: E501
        :rtype: NestedContentLibraryImage
        """
        return self._content_library_image

    @content_library_image.setter
    def content_library_image(self, content_library_image):
        """Sets the content_library_image of this ElfImage.


        :param content_library_image: The content_library_image of this ElfImage.  # noqa: E501
        :type content_library_image: NestedContentLibraryImage
        """

        self._content_library_image = content_library_image

    @property
    def description(self):
        """Gets the description of this ElfImage.  # noqa: E501


        :return: The description of this ElfImage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ElfImage.


        :param description: The description of this ElfImage.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this ElfImage.  # noqa: E501


        :return: The entity_async_status of this ElfImage.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this ElfImage.


        :param entity_async_status: The entity_async_status of this ElfImage.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this ElfImage.  # noqa: E501


        :return: The id of this ElfImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElfImage.


        :param id: The id of this ElfImage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this ElfImage.  # noqa: E501


        :return: The labels of this ElfImage.  # noqa: E501
        :rtype: list[NestedLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ElfImage.


        :param labels: The labels of this ElfImage.  # noqa: E501
        :type labels: list[NestedLabel]
        """

        self._labels = labels

    @property
    def local_created_at(self):
        """Gets the local_created_at of this ElfImage.  # noqa: E501


        :return: The local_created_at of this ElfImage.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this ElfImage.


        :param local_created_at: The local_created_at of this ElfImage.  # noqa: E501
        :type local_created_at: str
        """
        if self.local_vars_configuration.client_side_validation and local_created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `local_created_at`, must not be `None`")  # noqa: E501

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this ElfImage.  # noqa: E501


        :return: The local_id of this ElfImage.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this ElfImage.


        :param local_id: The local_id of this ElfImage.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this ElfImage.  # noqa: E501


        :return: The name of this ElfImage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElfImage.


        :param name: The name of this ElfImage.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this ElfImage.  # noqa: E501


        :return: The path of this ElfImage.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ElfImage.


        :param path: The path of this ElfImage.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def size(self):
        """Gets the size of this ElfImage.  # noqa: E501


        :return: The size of this ElfImage.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ElfImage.


        :param size: The size of this ElfImage.  # noqa: E501
        :type size: float
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def upload_task(self):
        """Gets the upload_task of this ElfImage.  # noqa: E501


        :return: The upload_task of this ElfImage.  # noqa: E501
        :rtype: NestedUploadTask
        """
        return self._upload_task

    @upload_task.setter
    def upload_task(self, upload_task):
        """Sets the upload_task of this ElfImage.


        :param upload_task: The upload_task of this ElfImage.  # noqa: E501
        :type upload_task: NestedUploadTask
        """

        self._upload_task = upload_task

    @property
    def vm_disks(self):
        """Gets the vm_disks of this ElfImage.  # noqa: E501


        :return: The vm_disks of this ElfImage.  # noqa: E501
        :rtype: list[NestedVmDisk]
        """
        return self._vm_disks

    @vm_disks.setter
    def vm_disks(self, vm_disks):
        """Sets the vm_disks of this ElfImage.


        :param vm_disks: The vm_disks of this ElfImage.  # noqa: E501
        :type vm_disks: list[NestedVmDisk]
        """

        self._vm_disks = vm_disks

    @property
    def vm_snapshots(self):
        """Gets the vm_snapshots of this ElfImage.  # noqa: E501


        :return: The vm_snapshots of this ElfImage.  # noqa: E501
        :rtype: list[NestedVmSnapshot]
        """
        return self._vm_snapshots

    @vm_snapshots.setter
    def vm_snapshots(self, vm_snapshots):
        """Sets the vm_snapshots of this ElfImage.


        :param vm_snapshots: The vm_snapshots of this ElfImage.  # noqa: E501
        :type vm_snapshots: list[NestedVmSnapshot]
        """

        self._vm_snapshots = vm_snapshots

    @property
    def vm_templates(self):
        """Gets the vm_templates of this ElfImage.  # noqa: E501


        :return: The vm_templates of this ElfImage.  # noqa: E501
        :rtype: list[NestedVmTemplate]
        """
        return self._vm_templates

    @vm_templates.setter
    def vm_templates(self, vm_templates):
        """Sets the vm_templates of this ElfImage.


        :param vm_templates: The vm_templates of this ElfImage.  # noqa: E501
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
        if not isinstance(other, ElfImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElfImage):
            return True

        return self.to_dict() != other.to_dict()
