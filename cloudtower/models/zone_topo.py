# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ZoneTopo(object):
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
        'cluster_topo': 'NestedClusterTopo',
        'id': 'str',
        'local_id': 'str',
        'rack_topoes': 'list[NestedRackTopo]'
    }

    attribute_map = {
        'cluster': 'cluster',
        'cluster_topo': 'cluster_topo',
        'id': 'id',
        'local_id': 'local_id',
        'rack_topoes': 'rack_topoes'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ZoneTopo - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._cluster_topo = None
        self._id = None
        self._local_id = None
        self._rack_topoes = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "cluster_topo" in kwargs:
            self.cluster_topo = kwargs["cluster_topo"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        self.rack_topoes = kwargs.get("rack_topoes", None)

    @property
    def cluster(self):
        """Gets the cluster of this ZoneTopo.  # noqa: E501


        :return: The cluster of this ZoneTopo.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ZoneTopo.


        :param cluster: The cluster of this ZoneTopo.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def cluster_topo(self):
        """Gets the cluster_topo of this ZoneTopo.  # noqa: E501


        :return: The cluster_topo of this ZoneTopo.  # noqa: E501
        :rtype: NestedClusterTopo
        """
        return self._cluster_topo

    @cluster_topo.setter
    def cluster_topo(self, cluster_topo):
        """Sets the cluster_topo of this ZoneTopo.


        :param cluster_topo: The cluster_topo of this ZoneTopo.  # noqa: E501
        :type cluster_topo: NestedClusterTopo
        """
        if self.local_vars_configuration.client_side_validation and cluster_topo is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_topo`, must not be `None`")  # noqa: E501

        self._cluster_topo = cluster_topo

    @property
    def id(self):
        """Gets the id of this ZoneTopo.  # noqa: E501


        :return: The id of this ZoneTopo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ZoneTopo.


        :param id: The id of this ZoneTopo.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this ZoneTopo.  # noqa: E501


        :return: The local_id of this ZoneTopo.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this ZoneTopo.


        :param local_id: The local_id of this ZoneTopo.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def rack_topoes(self):
        """Gets the rack_topoes of this ZoneTopo.  # noqa: E501


        :return: The rack_topoes of this ZoneTopo.  # noqa: E501
        :rtype: list[NestedRackTopo]
        """
        return self._rack_topoes

    @rack_topoes.setter
    def rack_topoes(self, rack_topoes):
        """Sets the rack_topoes of this ZoneTopo.


        :param rack_topoes: The rack_topoes of this ZoneTopo.  # noqa: E501
        :type rack_topoes: list[NestedRackTopo]
        """

        self._rack_topoes = rack_topoes

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
        if not isinstance(other, ZoneTopo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ZoneTopo):
            return True

        return self.to_dict() != other.to_dict()
