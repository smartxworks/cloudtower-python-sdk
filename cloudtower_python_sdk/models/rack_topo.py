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


class RackTopo(object):
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
        'brick_topoes': 'list[NestedBrickTopo]',
        'cluster': 'NestedCluster',
        'height': 'int',
        'id': 'str',
        'local_id': 'str',
        'name': 'str',
        'zone_topo': 'NestedZoneTopo'
    }

    attribute_map = {
        'brick_topoes': 'brick_topoes',
        'cluster': 'cluster',
        'height': 'height',
        'id': 'id',
        'local_id': 'local_id',
        'name': 'name',
        'zone_topo': 'zone_topo'
    }

    def __init__(self, brick_topoes=None, cluster=None, height=None, id=None, local_id=None, name=None, zone_topo=None, local_vars_configuration=None):  # noqa: E501
        """RackTopo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._brick_topoes = None
        self._cluster = None
        self._height = None
        self._id = None
        self._local_id = None
        self._name = None
        self._zone_topo = None
        self.discriminator = None

        self.brick_topoes = brick_topoes
        self.cluster = cluster
        self.height = height
        self.id = id
        self.local_id = local_id
        self.name = name
        self.zone_topo = zone_topo

    @property
    def brick_topoes(self):
        """Gets the brick_topoes of this RackTopo.  # noqa: E501


        :return: The brick_topoes of this RackTopo.  # noqa: E501
        :rtype: list[NestedBrickTopo]
        """
        return self._brick_topoes

    @brick_topoes.setter
    def brick_topoes(self, brick_topoes):
        """Sets the brick_topoes of this RackTopo.


        :param brick_topoes: The brick_topoes of this RackTopo.  # noqa: E501
        :type brick_topoes: list[NestedBrickTopo]
        """

        self._brick_topoes = brick_topoes

    @property
    def cluster(self):
        """Gets the cluster of this RackTopo.  # noqa: E501


        :return: The cluster of this RackTopo.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this RackTopo.


        :param cluster: The cluster of this RackTopo.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def height(self):
        """Gets the height of this RackTopo.  # noqa: E501


        :return: The height of this RackTopo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this RackTopo.


        :param height: The height of this RackTopo.  # noqa: E501
        :type height: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def id(self):
        """Gets the id of this RackTopo.  # noqa: E501


        :return: The id of this RackTopo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RackTopo.


        :param id: The id of this RackTopo.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this RackTopo.  # noqa: E501


        :return: The local_id of this RackTopo.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this RackTopo.


        :param local_id: The local_id of this RackTopo.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this RackTopo.  # noqa: E501


        :return: The name of this RackTopo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RackTopo.


        :param name: The name of this RackTopo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def zone_topo(self):
        """Gets the zone_topo of this RackTopo.  # noqa: E501


        :return: The zone_topo of this RackTopo.  # noqa: E501
        :rtype: NestedZoneTopo
        """
        return self._zone_topo

    @zone_topo.setter
    def zone_topo(self, zone_topo):
        """Sets the zone_topo of this RackTopo.


        :param zone_topo: The zone_topo of this RackTopo.  # noqa: E501
        :type zone_topo: NestedZoneTopo
        """
        if self.local_vars_configuration.client_side_validation and zone_topo is None:  # noqa: E501
            raise ValueError("Invalid value for `zone_topo`, must not be `None`")  # noqa: E501

        self._zone_topo = zone_topo

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
        if not isinstance(other, RackTopo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RackTopo):
            return True

        return self.to_dict() != other.to_dict()
