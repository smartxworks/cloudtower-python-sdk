# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.3.0
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


class GraphCreationParams(object):
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
        'network': 'NetworkType',
        'service': 'str',
        'metric_type': 'MetricType',
        'metric_count': 'int',
        'type': 'GraphType',
        'resource_type': 'str',
        'view_id': 'str',
        'title': 'str',
        'cluster_id': 'str',
        'connect_id': 'list[str]',
        'metric_name': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'network': 'network',
        'service': 'service',
        'metric_type': 'metric_type',
        'metric_count': 'metric_count',
        'type': 'type',
        'resource_type': 'resource_type',
        'view_id': 'view_id',
        'title': 'title',
        'cluster_id': 'cluster_id',
        'connect_id': 'connect_id',
        'metric_name': 'metric_name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GraphCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._instance_ids = None
        self._network = None
        self._service = None
        self._metric_type = None
        self._metric_count = None
        self._type = None
        self._resource_type = None
        self._view_id = None
        self._title = None
        self._cluster_id = None
        self._connect_id = None
        self._metric_name = None
        self.discriminator = None

        if "instance_ids" in kwargs:
            self.instance_ids = kwargs["instance_ids"]
        if "network" in kwargs:
            self.network = kwargs["network"]
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
        if "view_id" in kwargs:
            self.view_id = kwargs["view_id"]
        if "title" in kwargs:
            self.title = kwargs["title"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        if "connect_id" in kwargs:
            self.connect_id = kwargs["connect_id"]
        if "metric_name" in kwargs:
            self.metric_name = kwargs["metric_name"]

    @property
    def instance_ids(self):
        """Gets the instance_ids of this GraphCreationParams.  # noqa: E501


        :return: The instance_ids of this GraphCreationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this GraphCreationParams.


        :param instance_ids: The instance_ids of this GraphCreationParams.  # noqa: E501
        :type instance_ids: list[str]
        """

        self._instance_ids = instance_ids

    @property
    def network(self):
        """Gets the network of this GraphCreationParams.  # noqa: E501


        :return: The network of this GraphCreationParams.  # noqa: E501
        :rtype: NetworkType
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this GraphCreationParams.


        :param network: The network of this GraphCreationParams.  # noqa: E501
        :type network: NetworkType
        """

        self._network = network

    @property
    def service(self):
        """Gets the service of this GraphCreationParams.  # noqa: E501


        :return: The service of this GraphCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this GraphCreationParams.


        :param service: The service of this GraphCreationParams.  # noqa: E501
        :type service: str
        """

        self._service = service

    @property
    def metric_type(self):
        """Gets the metric_type of this GraphCreationParams.  # noqa: E501


        :return: The metric_type of this GraphCreationParams.  # noqa: E501
        :rtype: MetricType
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this GraphCreationParams.


        :param metric_type: The metric_type of this GraphCreationParams.  # noqa: E501
        :type metric_type: MetricType
        """

        self._metric_type = metric_type

    @property
    def metric_count(self):
        """Gets the metric_count of this GraphCreationParams.  # noqa: E501


        :return: The metric_count of this GraphCreationParams.  # noqa: E501
        :rtype: int
        """
        return self._metric_count

    @metric_count.setter
    def metric_count(self, metric_count):
        """Sets the metric_count of this GraphCreationParams.


        :param metric_count: The metric_count of this GraphCreationParams.  # noqa: E501
        :type metric_count: int
        """

        self._metric_count = metric_count

    @property
    def type(self):
        """Gets the type of this GraphCreationParams.  # noqa: E501


        :return: The type of this GraphCreationParams.  # noqa: E501
        :rtype: GraphType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GraphCreationParams.


        :param type: The type of this GraphCreationParams.  # noqa: E501
        :type type: GraphType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def resource_type(self):
        """Gets the resource_type of this GraphCreationParams.  # noqa: E501


        :return: The resource_type of this GraphCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this GraphCreationParams.


        :param resource_type: The resource_type of this GraphCreationParams.  # noqa: E501
        :type resource_type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def view_id(self):
        """Gets the view_id of this GraphCreationParams.  # noqa: E501


        :return: The view_id of this GraphCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """Sets the view_id of this GraphCreationParams.


        :param view_id: The view_id of this GraphCreationParams.  # noqa: E501
        :type view_id: str
        """
        if self.local_vars_configuration.client_side_validation and view_id is None:  # noqa: E501
            raise ValueError("Invalid value for `view_id`, must not be `None`")  # noqa: E501

        self._view_id = view_id

    @property
    def title(self):
        """Gets the title of this GraphCreationParams.  # noqa: E501


        :return: The title of this GraphCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GraphCreationParams.


        :param title: The title of this GraphCreationParams.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def cluster_id(self):
        """Gets the cluster_id of this GraphCreationParams.  # noqa: E501


        :return: The cluster_id of this GraphCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this GraphCreationParams.


        :param cluster_id: The cluster_id of this GraphCreationParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def connect_id(self):
        """Gets the connect_id of this GraphCreationParams.  # noqa: E501


        :return: The connect_id of this GraphCreationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._connect_id

    @connect_id.setter
    def connect_id(self, connect_id):
        """Sets the connect_id of this GraphCreationParams.


        :param connect_id: The connect_id of this GraphCreationParams.  # noqa: E501
        :type connect_id: list[str]
        """
        if self.local_vars_configuration.client_side_validation and connect_id is None:  # noqa: E501
            raise ValueError("Invalid value for `connect_id`, must not be `None`")  # noqa: E501

        self._connect_id = connect_id

    @property
    def metric_name(self):
        """Gets the metric_name of this GraphCreationParams.  # noqa: E501


        :return: The metric_name of this GraphCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this GraphCreationParams.


        :param metric_name: The metric_name of this GraphCreationParams.  # noqa: E501
        :type metric_name: str
        """
        if self.local_vars_configuration.client_side_validation and metric_name is None:  # noqa: E501
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

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
        if not isinstance(other, GraphCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GraphCreationParams):
            return True

        return self.to_dict() != other.to_dict()
