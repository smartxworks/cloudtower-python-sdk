# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class View(object):
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
        'graphs': 'list[NestedGraph]',
        'id': 'str',
        'local_id': 'str',
        'name': 'str',
        'time_span': 'int',
        'time_unit': 'TimeUnit'
    }

    attribute_map = {
        'cluster': 'cluster',
        'entity_async_status': 'entityAsyncStatus',
        'graphs': 'graphs',
        'id': 'id',
        'local_id': 'local_id',
        'name': 'name',
        'time_span': 'time_span',
        'time_unit': 'time_unit'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """View - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._entity_async_status = None
        self._graphs = None
        self._id = None
        self._local_id = None
        self._name = None
        self._time_span = None
        self._time_unit = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        self.entity_async_status = kwargs.get("entity_async_status", None)
        self.graphs = kwargs.get("graphs", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "time_span" in kwargs:
            self.time_span = kwargs["time_span"]
        if "time_unit" in kwargs:
            self.time_unit = kwargs["time_unit"]

    @property
    def cluster(self):
        """Gets the cluster of this View.  # noqa: E501


        :return: The cluster of this View.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this View.


        :param cluster: The cluster of this View.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this View.  # noqa: E501


        :return: The entity_async_status of this View.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this View.


        :param entity_async_status: The entity_async_status of this View.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def graphs(self):
        """Gets the graphs of this View.  # noqa: E501


        :return: The graphs of this View.  # noqa: E501
        :rtype: list[NestedGraph]
        """
        return self._graphs

    @graphs.setter
    def graphs(self, graphs):
        """Sets the graphs of this View.


        :param graphs: The graphs of this View.  # noqa: E501
        :type graphs: list[NestedGraph]
        """

        self._graphs = graphs

    @property
    def id(self):
        """Gets the id of this View.  # noqa: E501


        :return: The id of this View.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this View.


        :param id: The id of this View.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this View.  # noqa: E501


        :return: The local_id of this View.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this View.


        :param local_id: The local_id of this View.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this View.  # noqa: E501


        :return: The name of this View.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this View.


        :param name: The name of this View.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def time_span(self):
        """Gets the time_span of this View.  # noqa: E501


        :return: The time_span of this View.  # noqa: E501
        :rtype: int
        """
        return self._time_span

    @time_span.setter
    def time_span(self, time_span):
        """Sets the time_span of this View.


        :param time_span: The time_span of this View.  # noqa: E501
        :type time_span: int
        """
        if self.local_vars_configuration.client_side_validation and time_span is None:  # noqa: E501
            raise ValueError("Invalid value for `time_span`, must not be `None`")  # noqa: E501

        self._time_span = time_span

    @property
    def time_unit(self):
        """Gets the time_unit of this View.  # noqa: E501


        :return: The time_unit of this View.  # noqa: E501
        :rtype: TimeUnit
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this View.


        :param time_unit: The time_unit of this View.  # noqa: E501
        :type time_unit: TimeUnit
        """
        if self.local_vars_configuration.client_side_validation and time_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `time_unit`, must not be `None`")  # noqa: E501

        self._time_unit = time_unit

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
        if not isinstance(other, View):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, View):
            return True

        return self.to_dict() != other.to_dict()
