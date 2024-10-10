# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class Graph(object):
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
        'disks': 'list[NestedDisk]',
        'entity_async_status': 'EntityAsyncStatus',
        'hosts': 'list[NestedHost]',
        'id': 'str',
        'instance_ids': 'list[str]',
        'local_id': 'str',
        'luns': 'list[NestedIscsiLun]',
        'metric_count': 'int',
        'metric_name': 'str',
        'metric_type': 'MetricType',
        'namespaces': 'list[NestedNvmfNamespace]',
        'network': 'NetworkType',
        'nics': 'list[NestedNic]',
        'resource_type': 'str',
        'service': 'str',
        'targets': 'object',
        'title': 'str',
        'type': 'GraphType',
        'view': 'NestedView',
        'vm_nics': 'list[NestedVmNic]',
        'vm_volumes': 'list[NestedVmVolume]',
        'vms': 'list[NestedVm]',
        'witnesses': 'list[NestedWitness]',
        'zones': 'list[NestedZone]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'disks': 'disks',
        'entity_async_status': 'entityAsyncStatus',
        'hosts': 'hosts',
        'id': 'id',
        'instance_ids': 'instance_ids',
        'local_id': 'local_id',
        'luns': 'luns',
        'metric_count': 'metric_count',
        'metric_name': 'metric_name',
        'metric_type': 'metric_type',
        'namespaces': 'namespaces',
        'network': 'network',
        'nics': 'nics',
        'resource_type': 'resource_type',
        'service': 'service',
        'targets': 'targets',
        'title': 'title',
        'type': 'type',
        'view': 'view',
        'vm_nics': 'vmNics',
        'vm_volumes': 'vmVolumes',
        'vms': 'vms',
        'witnesses': 'witnesses',
        'zones': 'zones'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Graph - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._disks = None
        self._entity_async_status = None
        self._hosts = None
        self._id = None
        self._instance_ids = None
        self._local_id = None
        self._luns = None
        self._metric_count = None
        self._metric_name = None
        self._metric_type = None
        self._namespaces = None
        self._network = None
        self._nics = None
        self._resource_type = None
        self._service = None
        self._targets = None
        self._title = None
        self._type = None
        self._view = None
        self._vm_nics = None
        self._vm_volumes = None
        self._vms = None
        self._witnesses = None
        self._zones = None
        self.discriminator = None

        self.cluster = kwargs.get("cluster", None)
        self.disks = kwargs.get("disks", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        self.hosts = kwargs.get("hosts", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "instance_ids" in kwargs:
            self.instance_ids = kwargs["instance_ids"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        self.luns = kwargs.get("luns", None)
        if "metric_count" in kwargs:
            self.metric_count = kwargs["metric_count"]
        if "metric_name" in kwargs:
            self.metric_name = kwargs["metric_name"]
        if "metric_type" in kwargs:
            self.metric_type = kwargs["metric_type"]
        self.namespaces = kwargs.get("namespaces", None)
        self.network = kwargs.get("network", None)
        self.nics = kwargs.get("nics", None)
        if "resource_type" in kwargs:
            self.resource_type = kwargs["resource_type"]
        self.service = kwargs.get("service", None)
        if "targets" in kwargs:
            self.targets = kwargs["targets"]
        if "title" in kwargs:
            self.title = kwargs["title"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "view" in kwargs:
            self.view = kwargs["view"]
        self.vm_nics = kwargs.get("vm_nics", None)
        self.vm_volumes = kwargs.get("vm_volumes", None)
        self.vms = kwargs.get("vms", None)
        self.witnesses = kwargs.get("witnesses", None)
        self.zones = kwargs.get("zones", None)

    @property
    def cluster(self):
        """Gets the cluster of this Graph.  # noqa: E501


        :return: The cluster of this Graph.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Graph.


        :param cluster: The cluster of this Graph.  # noqa: E501
        :type cluster: NestedCluster
        """

        self._cluster = cluster

    @property
    def disks(self):
        """Gets the disks of this Graph.  # noqa: E501


        :return: The disks of this Graph.  # noqa: E501
        :rtype: list[NestedDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this Graph.


        :param disks: The disks of this Graph.  # noqa: E501
        :type disks: list[NestedDisk]
        """

        self._disks = disks

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this Graph.  # noqa: E501


        :return: The entity_async_status of this Graph.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this Graph.


        :param entity_async_status: The entity_async_status of this Graph.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def hosts(self):
        """Gets the hosts of this Graph.  # noqa: E501


        :return: The hosts of this Graph.  # noqa: E501
        :rtype: list[NestedHost]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this Graph.


        :param hosts: The hosts of this Graph.  # noqa: E501
        :type hosts: list[NestedHost]
        """

        self._hosts = hosts

    @property
    def id(self):
        """Gets the id of this Graph.  # noqa: E501


        :return: The id of this Graph.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Graph.


        :param id: The id of this Graph.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def instance_ids(self):
        """Gets the instance_ids of this Graph.  # noqa: E501


        :return: The instance_ids of this Graph.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this Graph.


        :param instance_ids: The instance_ids of this Graph.  # noqa: E501
        :type instance_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and instance_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_ids`, must not be `None`")  # noqa: E501

        self._instance_ids = instance_ids

    @property
    def local_id(self):
        """Gets the local_id of this Graph.  # noqa: E501


        :return: The local_id of this Graph.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this Graph.


        :param local_id: The local_id of this Graph.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def luns(self):
        """Gets the luns of this Graph.  # noqa: E501


        :return: The luns of this Graph.  # noqa: E501
        :rtype: list[NestedIscsiLun]
        """
        return self._luns

    @luns.setter
    def luns(self, luns):
        """Sets the luns of this Graph.


        :param luns: The luns of this Graph.  # noqa: E501
        :type luns: list[NestedIscsiLun]
        """

        self._luns = luns

    @property
    def metric_count(self):
        """Gets the metric_count of this Graph.  # noqa: E501


        :return: The metric_count of this Graph.  # noqa: E501
        :rtype: int
        """
        return self._metric_count

    @metric_count.setter
    def metric_count(self, metric_count):
        """Sets the metric_count of this Graph.


        :param metric_count: The metric_count of this Graph.  # noqa: E501
        :type metric_count: int
        """
        if self.local_vars_configuration.client_side_validation and metric_count is None:  # noqa: E501
            raise ValueError("Invalid value for `metric_count`, must not be `None`")  # noqa: E501

        self._metric_count = metric_count

    @property
    def metric_name(self):
        """Gets the metric_name of this Graph.  # noqa: E501


        :return: The metric_name of this Graph.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this Graph.


        :param metric_name: The metric_name of this Graph.  # noqa: E501
        :type metric_name: str
        """
        if self.local_vars_configuration.client_side_validation and metric_name is None:  # noqa: E501
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def metric_type(self):
        """Gets the metric_type of this Graph.  # noqa: E501


        :return: The metric_type of this Graph.  # noqa: E501
        :rtype: MetricType
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this Graph.


        :param metric_type: The metric_type of this Graph.  # noqa: E501
        :type metric_type: MetricType
        """
        if self.local_vars_configuration.client_side_validation and metric_type is None:  # noqa: E501
            raise ValueError("Invalid value for `metric_type`, must not be `None`")  # noqa: E501

        self._metric_type = metric_type

    @property
    def namespaces(self):
        """Gets the namespaces of this Graph.  # noqa: E501


        :return: The namespaces of this Graph.  # noqa: E501
        :rtype: list[NestedNvmfNamespace]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this Graph.


        :param namespaces: The namespaces of this Graph.  # noqa: E501
        :type namespaces: list[NestedNvmfNamespace]
        """

        self._namespaces = namespaces

    @property
    def network(self):
        """Gets the network of this Graph.  # noqa: E501


        :return: The network of this Graph.  # noqa: E501
        :rtype: NetworkType
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this Graph.


        :param network: The network of this Graph.  # noqa: E501
        :type network: NetworkType
        """

        self._network = network

    @property
    def nics(self):
        """Gets the nics of this Graph.  # noqa: E501


        :return: The nics of this Graph.  # noqa: E501
        :rtype: list[NestedNic]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this Graph.


        :param nics: The nics of this Graph.  # noqa: E501
        :type nics: list[NestedNic]
        """

        self._nics = nics

    @property
    def resource_type(self):
        """Gets the resource_type of this Graph.  # noqa: E501


        :return: The resource_type of this Graph.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Graph.


        :param resource_type: The resource_type of this Graph.  # noqa: E501
        :type resource_type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def service(self):
        """Gets the service of this Graph.  # noqa: E501


        :return: The service of this Graph.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Graph.


        :param service: The service of this Graph.  # noqa: E501
        :type service: str
        """

        self._service = service

    @property
    def targets(self):
        """Gets the targets of this Graph.  # noqa: E501


        :return: The targets of this Graph.  # noqa: E501
        :rtype: object
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this Graph.


        :param targets: The targets of this Graph.  # noqa: E501
        :type targets: object
        """
        if self.local_vars_configuration.client_side_validation and targets is None:  # noqa: E501
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

    @property
    def title(self):
        """Gets the title of this Graph.  # noqa: E501


        :return: The title of this Graph.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Graph.


        :param title: The title of this Graph.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def type(self):
        """Gets the type of this Graph.  # noqa: E501


        :return: The type of this Graph.  # noqa: E501
        :rtype: GraphType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Graph.


        :param type: The type of this Graph.  # noqa: E501
        :type type: GraphType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def view(self):
        """Gets the view of this Graph.  # noqa: E501


        :return: The view of this Graph.  # noqa: E501
        :rtype: NestedView
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this Graph.


        :param view: The view of this Graph.  # noqa: E501
        :type view: NestedView
        """
        if self.local_vars_configuration.client_side_validation and view is None:  # noqa: E501
            raise ValueError("Invalid value for `view`, must not be `None`")  # noqa: E501

        self._view = view

    @property
    def vm_nics(self):
        """Gets the vm_nics of this Graph.  # noqa: E501


        :return: The vm_nics of this Graph.  # noqa: E501
        :rtype: list[NestedVmNic]
        """
        return self._vm_nics

    @vm_nics.setter
    def vm_nics(self, vm_nics):
        """Sets the vm_nics of this Graph.


        :param vm_nics: The vm_nics of this Graph.  # noqa: E501
        :type vm_nics: list[NestedVmNic]
        """

        self._vm_nics = vm_nics

    @property
    def vm_volumes(self):
        """Gets the vm_volumes of this Graph.  # noqa: E501


        :return: The vm_volumes of this Graph.  # noqa: E501
        :rtype: list[NestedVmVolume]
        """
        return self._vm_volumes

    @vm_volumes.setter
    def vm_volumes(self, vm_volumes):
        """Sets the vm_volumes of this Graph.


        :param vm_volumes: The vm_volumes of this Graph.  # noqa: E501
        :type vm_volumes: list[NestedVmVolume]
        """

        self._vm_volumes = vm_volumes

    @property
    def vms(self):
        """Gets the vms of this Graph.  # noqa: E501


        :return: The vms of this Graph.  # noqa: E501
        :rtype: list[NestedVm]
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this Graph.


        :param vms: The vms of this Graph.  # noqa: E501
        :type vms: list[NestedVm]
        """

        self._vms = vms

    @property
    def witnesses(self):
        """Gets the witnesses of this Graph.  # noqa: E501


        :return: The witnesses of this Graph.  # noqa: E501
        :rtype: list[NestedWitness]
        """
        return self._witnesses

    @witnesses.setter
    def witnesses(self, witnesses):
        """Sets the witnesses of this Graph.


        :param witnesses: The witnesses of this Graph.  # noqa: E501
        :type witnesses: list[NestedWitness]
        """

        self._witnesses = witnesses

    @property
    def zones(self):
        """Gets the zones of this Graph.  # noqa: E501


        :return: The zones of this Graph.  # noqa: E501
        :rtype: list[NestedZone]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this Graph.


        :param zones: The zones of this Graph.  # noqa: E501
        :type zones: list[NestedZone]
        """

        self._zones = zones

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
        if not isinstance(other, Graph):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Graph):
            return True

        return self.to_dict() != other.to_dict()
