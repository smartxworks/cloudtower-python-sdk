# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: info@smartx.com
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


class LogCollection(object):
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
        'groups': 'list[str]',
        'hosts': 'list[NestedHost]',
        'id': 'str',
        'local_id': 'str',
        'log_ended_at': 'str',
        'log_started_at': 'str',
        'owner': 'str',
        'path': 'str',
        'progress': 'float',
        'service_groups': 'object',
        'services': 'list[str]',
        'size': 'int',
        'started_at': 'str',
        'status': 'LogCollectionStatus',
        'witness': 'NestedWitness'
    }

    attribute_map = {
        'cluster': 'cluster',
        'groups': 'groups',
        'hosts': 'hosts',
        'id': 'id',
        'local_id': 'local_id',
        'log_ended_at': 'log_ended_at',
        'log_started_at': 'log_started_at',
        'owner': 'owner',
        'path': 'path',
        'progress': 'progress',
        'service_groups': 'service_groups',
        'services': 'services',
        'size': 'size',
        'started_at': 'started_at',
        'status': 'status',
        'witness': 'witness'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """LogCollection - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._groups = None
        self._hosts = None
        self._id = None
        self._local_id = None
        self._log_ended_at = None
        self._log_started_at = None
        self._owner = None
        self._path = None
        self._progress = None
        self._service_groups = None
        self._services = None
        self._size = None
        self._started_at = None
        self._status = None
        self._witness = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "groups" in kwargs:
            self.groups = kwargs["groups"]
        self.hosts = kwargs.get("hosts", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "log_ended_at" in kwargs:
            self.log_ended_at = kwargs["log_ended_at"]
        if "log_started_at" in kwargs:
            self.log_started_at = kwargs["log_started_at"]
        if "owner" in kwargs:
            self.owner = kwargs["owner"]
        if "path" in kwargs:
            self.path = kwargs["path"]
        if "progress" in kwargs:
            self.progress = kwargs["progress"]
        self.service_groups = kwargs.get("service_groups", None)
        if "services" in kwargs:
            self.services = kwargs["services"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "started_at" in kwargs:
            self.started_at = kwargs["started_at"]
        if "status" in kwargs:
            self.status = kwargs["status"]
        self.witness = kwargs.get("witness", None)

    @property
    def cluster(self):
        """Gets the cluster of this LogCollection.  # noqa: E501


        :return: The cluster of this LogCollection.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this LogCollection.


        :param cluster: The cluster of this LogCollection.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def groups(self):
        """Gets the groups of this LogCollection.  # noqa: E501


        :return: The groups of this LogCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this LogCollection.


        :param groups: The groups of this LogCollection.  # noqa: E501
        :type groups: list[str]
        """
        if self.local_vars_configuration.client_side_validation and groups is None:  # noqa: E501
            raise ValueError("Invalid value for `groups`, must not be `None`")  # noqa: E501

        self._groups = groups

    @property
    def hosts(self):
        """Gets the hosts of this LogCollection.  # noqa: E501


        :return: The hosts of this LogCollection.  # noqa: E501
        :rtype: list[NestedHost]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this LogCollection.


        :param hosts: The hosts of this LogCollection.  # noqa: E501
        :type hosts: list[NestedHost]
        """

        self._hosts = hosts

    @property
    def id(self):
        """Gets the id of this LogCollection.  # noqa: E501


        :return: The id of this LogCollection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogCollection.


        :param id: The id of this LogCollection.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this LogCollection.  # noqa: E501


        :return: The local_id of this LogCollection.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this LogCollection.


        :param local_id: The local_id of this LogCollection.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def log_ended_at(self):
        """Gets the log_ended_at of this LogCollection.  # noqa: E501


        :return: The log_ended_at of this LogCollection.  # noqa: E501
        :rtype: str
        """
        return self._log_ended_at

    @log_ended_at.setter
    def log_ended_at(self, log_ended_at):
        """Sets the log_ended_at of this LogCollection.


        :param log_ended_at: The log_ended_at of this LogCollection.  # noqa: E501
        :type log_ended_at: str
        """
        if self.local_vars_configuration.client_side_validation and log_ended_at is None:  # noqa: E501
            raise ValueError("Invalid value for `log_ended_at`, must not be `None`")  # noqa: E501

        self._log_ended_at = log_ended_at

    @property
    def log_started_at(self):
        """Gets the log_started_at of this LogCollection.  # noqa: E501


        :return: The log_started_at of this LogCollection.  # noqa: E501
        :rtype: str
        """
        return self._log_started_at

    @log_started_at.setter
    def log_started_at(self, log_started_at):
        """Sets the log_started_at of this LogCollection.


        :param log_started_at: The log_started_at of this LogCollection.  # noqa: E501
        :type log_started_at: str
        """
        if self.local_vars_configuration.client_side_validation and log_started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `log_started_at`, must not be `None`")  # noqa: E501

        self._log_started_at = log_started_at

    @property
    def owner(self):
        """Gets the owner of this LogCollection.  # noqa: E501


        :return: The owner of this LogCollection.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this LogCollection.


        :param owner: The owner of this LogCollection.  # noqa: E501
        :type owner: str
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def path(self):
        """Gets the path of this LogCollection.  # noqa: E501


        :return: The path of this LogCollection.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LogCollection.


        :param path: The path of this LogCollection.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def progress(self):
        """Gets the progress of this LogCollection.  # noqa: E501


        :return: The progress of this LogCollection.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this LogCollection.


        :param progress: The progress of this LogCollection.  # noqa: E501
        :type progress: float
        """
        if self.local_vars_configuration.client_side_validation and progress is None:  # noqa: E501
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def service_groups(self):
        """Gets the service_groups of this LogCollection.  # noqa: E501


        :return: The service_groups of this LogCollection.  # noqa: E501
        :rtype: object
        """
        return self._service_groups

    @service_groups.setter
    def service_groups(self, service_groups):
        """Sets the service_groups of this LogCollection.


        :param service_groups: The service_groups of this LogCollection.  # noqa: E501
        :type service_groups: object
        """

        self._service_groups = service_groups

    @property
    def services(self):
        """Gets the services of this LogCollection.  # noqa: E501


        :return: The services of this LogCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this LogCollection.


        :param services: The services of this LogCollection.  # noqa: E501
        :type services: list[str]
        """
        if self.local_vars_configuration.client_side_validation and services is None:  # noqa: E501
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501

        self._services = services

    @property
    def size(self):
        """Gets the size of this LogCollection.  # noqa: E501


        :return: The size of this LogCollection.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LogCollection.


        :param size: The size of this LogCollection.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def started_at(self):
        """Gets the started_at of this LogCollection.  # noqa: E501


        :return: The started_at of this LogCollection.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this LogCollection.


        :param started_at: The started_at of this LogCollection.  # noqa: E501
        :type started_at: str
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def status(self):
        """Gets the status of this LogCollection.  # noqa: E501


        :return: The status of this LogCollection.  # noqa: E501
        :rtype: LogCollectionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LogCollection.


        :param status: The status of this LogCollection.  # noqa: E501
        :type status: LogCollectionStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def witness(self):
        """Gets the witness of this LogCollection.  # noqa: E501


        :return: The witness of this LogCollection.  # noqa: E501
        :rtype: NestedWitness
        """
        return self._witness

    @witness.setter
    def witness(self, witness):
        """Sets the witness of this LogCollection.


        :param witness: The witness of this LogCollection.  # noqa: E501
        :type witness: NestedWitness
        """

        self._witness = witness

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
        if not isinstance(other, LogCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogCollection):
            return True

        return self.to_dict() != other.to_dict()
