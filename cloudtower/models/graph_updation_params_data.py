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


class GraphUpdationParamsData(object):
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
        'instance_ids': 'list[str]',
        'luns': 'IscsiLunWhereInput',
        'vm_nics': 'VmNicWhereInput',
        'nics': 'NicWhereInput',
        'disks': 'DiskWhereInput',
        'vm_volumes': 'VmVolumeWhereInput',
        'vms': 'VmWhereInput',
        'hosts': 'HostWhereInput',
        'network': 'NetworkType',
        'cluster': 'ClusterWhereInput',
        'service': 'str',
        'metric_type': 'MetricType',
        'metric_count': 'int',
        'type': 'GraphType',
        'resource_type': 'str',
        'title': 'str',
        'metric_name': 'str',
        'connect_id': 'list[str]'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'luns': 'luns',
        'vm_nics': 'vmNics',
        'nics': 'nics',
        'disks': 'disks',
        'vm_volumes': 'vmVolumes',
        'vms': 'vms',
        'hosts': 'hosts',
        'network': 'network',
        'cluster': 'cluster',
        'service': 'service',
        'metric_type': 'metric_type',
        'metric_count': 'metric_count',
        'type': 'type',
        'resource_type': 'resource_type',
        'title': 'title',
        'metric_name': 'metric_name',
        'connect_id': 'connect_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GraphUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._instance_ids = None
        self._luns = None
        self._vm_nics = None
        self._nics = None
        self._disks = None
        self._vm_volumes = None
        self._vms = None
        self._hosts = None
        self._network = None
        self._cluster = None
        self._service = None
        self._metric_type = None
        self._metric_count = None
        self._type = None
        self._resource_type = None
        self._title = None
        self._metric_name = None
        self._connect_id = None
        self.discriminator = None

        if "instance_ids" in kwargs:
            self.instance_ids = kwargs["instance_ids"]
        if "luns" in kwargs:
            self.luns = kwargs["luns"]
        if "vm_nics" in kwargs:
            self.vm_nics = kwargs["vm_nics"]
        if "nics" in kwargs:
            self.nics = kwargs["nics"]
        if "disks" in kwargs:
            self.disks = kwargs["disks"]
        if "vm_volumes" in kwargs:
            self.vm_volumes = kwargs["vm_volumes"]
        if "vms" in kwargs:
            self.vms = kwargs["vms"]
        if "hosts" in kwargs:
            self.hosts = kwargs["hosts"]
        if "network" in kwargs:
            self.network = kwargs["network"]
        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "service" in kwargs:
            self.service = kwargs["service"]
        if "metric_type" in kwargs:
            self.metric_type = kwargs["metric_type"]
        if "metric_count" in kwargs:
            self.metric_count = kwargs["metric_count"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "resource_type" in kwargs:
            self.resource_type = kwargs["resource_type"]
        if "title" in kwargs:
            self.title = kwargs["title"]
        if "metric_name" in kwargs:
            self.metric_name = kwargs["metric_name"]
        if "connect_id" in kwargs:
            self.connect_id = kwargs["connect_id"]

    @property
    def instance_ids(self):
        """Gets the instance_ids of this GraphUpdationParamsData.  # noqa: E501


        :return: The instance_ids of this GraphUpdationParamsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this GraphUpdationParamsData.


        :param instance_ids: The instance_ids of this GraphUpdationParamsData.  # noqa: E501
        :type instance_ids: list[str]
        """

        self._instance_ids = instance_ids

    @property
    def luns(self):
        """Gets the luns of this GraphUpdationParamsData.  # noqa: E501


        :return: The luns of this GraphUpdationParamsData.  # noqa: E501
        :rtype: IscsiLunWhereInput
        """
        return self._luns

    @luns.setter
    def luns(self, luns):
        """Sets the luns of this GraphUpdationParamsData.


        :param luns: The luns of this GraphUpdationParamsData.  # noqa: E501
        :type luns: IscsiLunWhereInput
        """

        self._luns = luns

    @property
    def vm_nics(self):
        """Gets the vm_nics of this GraphUpdationParamsData.  # noqa: E501


        :return: The vm_nics of this GraphUpdationParamsData.  # noqa: E501
        :rtype: VmNicWhereInput
        """
        return self._vm_nics

    @vm_nics.setter
    def vm_nics(self, vm_nics):
        """Sets the vm_nics of this GraphUpdationParamsData.


        :param vm_nics: The vm_nics of this GraphUpdationParamsData.  # noqa: E501
        :type vm_nics: VmNicWhereInput
        """

        self._vm_nics = vm_nics

    @property
    def nics(self):
        """Gets the nics of this GraphUpdationParamsData.  # noqa: E501


        :return: The nics of this GraphUpdationParamsData.  # noqa: E501
        :rtype: NicWhereInput
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this GraphUpdationParamsData.


        :param nics: The nics of this GraphUpdationParamsData.  # noqa: E501
        :type nics: NicWhereInput
        """

        self._nics = nics

    @property
    def disks(self):
        """Gets the disks of this GraphUpdationParamsData.  # noqa: E501


        :return: The disks of this GraphUpdationParamsData.  # noqa: E501
        :rtype: DiskWhereInput
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this GraphUpdationParamsData.


        :param disks: The disks of this GraphUpdationParamsData.  # noqa: E501
        :type disks: DiskWhereInput
        """

        self._disks = disks

    @property
    def vm_volumes(self):
        """Gets the vm_volumes of this GraphUpdationParamsData.  # noqa: E501


        :return: The vm_volumes of this GraphUpdationParamsData.  # noqa: E501
        :rtype: VmVolumeWhereInput
        """
        return self._vm_volumes

    @vm_volumes.setter
    def vm_volumes(self, vm_volumes):
        """Sets the vm_volumes of this GraphUpdationParamsData.


        :param vm_volumes: The vm_volumes of this GraphUpdationParamsData.  # noqa: E501
        :type vm_volumes: VmVolumeWhereInput
        """

        self._vm_volumes = vm_volumes

    @property
    def vms(self):
        """Gets the vms of this GraphUpdationParamsData.  # noqa: E501


        :return: The vms of this GraphUpdationParamsData.  # noqa: E501
        :rtype: VmWhereInput
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this GraphUpdationParamsData.


        :param vms: The vms of this GraphUpdationParamsData.  # noqa: E501
        :type vms: VmWhereInput
        """

        self._vms = vms

    @property
    def hosts(self):
        """Gets the hosts of this GraphUpdationParamsData.  # noqa: E501


        :return: The hosts of this GraphUpdationParamsData.  # noqa: E501
        :rtype: HostWhereInput
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this GraphUpdationParamsData.


        :param hosts: The hosts of this GraphUpdationParamsData.  # noqa: E501
        :type hosts: HostWhereInput
        """

        self._hosts = hosts

    @property
    def network(self):
        """Gets the network of this GraphUpdationParamsData.  # noqa: E501


        :return: The network of this GraphUpdationParamsData.  # noqa: E501
        :rtype: NetworkType
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this GraphUpdationParamsData.


        :param network: The network of this GraphUpdationParamsData.  # noqa: E501
        :type network: NetworkType
        """

        self._network = network

    @property
    def cluster(self):
        """Gets the cluster of this GraphUpdationParamsData.  # noqa: E501


        :return: The cluster of this GraphUpdationParamsData.  # noqa: E501
        :rtype: ClusterWhereInput
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this GraphUpdationParamsData.


        :param cluster: The cluster of this GraphUpdationParamsData.  # noqa: E501
        :type cluster: ClusterWhereInput
        """

        self._cluster = cluster

    @property
    def service(self):
        """Gets the service of this GraphUpdationParamsData.  # noqa: E501


        :return: The service of this GraphUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this GraphUpdationParamsData.


        :param service: The service of this GraphUpdationParamsData.  # noqa: E501
        :type service: str
        """

        self._service = service

    @property
    def metric_type(self):
        """Gets the metric_type of this GraphUpdationParamsData.  # noqa: E501


        :return: The metric_type of this GraphUpdationParamsData.  # noqa: E501
        :rtype: MetricType
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this GraphUpdationParamsData.


        :param metric_type: The metric_type of this GraphUpdationParamsData.  # noqa: E501
        :type metric_type: MetricType
        """

        self._metric_type = metric_type

    @property
    def metric_count(self):
        """Gets the metric_count of this GraphUpdationParamsData.  # noqa: E501


        :return: The metric_count of this GraphUpdationParamsData.  # noqa: E501
        :rtype: int
        """
        return self._metric_count

    @metric_count.setter
    def metric_count(self, metric_count):
        """Sets the metric_count of this GraphUpdationParamsData.


        :param metric_count: The metric_count of this GraphUpdationParamsData.  # noqa: E501
        :type metric_count: int
        """

        self._metric_count = metric_count

    @property
    def type(self):
        """Gets the type of this GraphUpdationParamsData.  # noqa: E501


        :return: The type of this GraphUpdationParamsData.  # noqa: E501
        :rtype: GraphType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GraphUpdationParamsData.


        :param type: The type of this GraphUpdationParamsData.  # noqa: E501
        :type type: GraphType
        """

        self._type = type

    @property
    def resource_type(self):
        """Gets the resource_type of this GraphUpdationParamsData.  # noqa: E501


        :return: The resource_type of this GraphUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this GraphUpdationParamsData.


        :param resource_type: The resource_type of this GraphUpdationParamsData.  # noqa: E501
        :type resource_type: str
        """

        self._resource_type = resource_type

    @property
    def title(self):
        """Gets the title of this GraphUpdationParamsData.  # noqa: E501


        :return: The title of this GraphUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GraphUpdationParamsData.


        :param title: The title of this GraphUpdationParamsData.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def metric_name(self):
        """Gets the metric_name of this GraphUpdationParamsData.  # noqa: E501


        :return: The metric_name of this GraphUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this GraphUpdationParamsData.


        :param metric_name: The metric_name of this GraphUpdationParamsData.  # noqa: E501
        :type metric_name: str
        """

        self._metric_name = metric_name

    @property
    def connect_id(self):
        """Gets the connect_id of this GraphUpdationParamsData.  # noqa: E501


        :return: The connect_id of this GraphUpdationParamsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._connect_id

    @connect_id.setter
    def connect_id(self, connect_id):
        """Sets the connect_id of this GraphUpdationParamsData.


        :param connect_id: The connect_id of this GraphUpdationParamsData.  # noqa: E501
        :type connect_id: list[str]
        """

        self._connect_id = connect_id

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
        if not isinstance(other, GraphUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GraphUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
