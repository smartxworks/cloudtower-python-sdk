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


class BrickTopo(object):
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
        'capacity': 'NestedCapacity',
        'cluster': 'NestedCluster',
        'cluster_topo': 'NestedClusterTopo',
        'disk_layout': 'NestedBrickDiskLayout',
        'height': 'int',
        'id': 'str',
        'local_id': 'str',
        'model': 'str',
        'name': 'str',
        'node_topoes': 'list[NestedNodeTopo]',
        'position': 'int',
        'power_layout': 'Direction',
        'power_position': 'PowerPosition',
        'powers': 'list[NestedBrickPower]',
        'rack_topo': 'NestedRackTopo',
        'tag_position_in_brick': 'list[NestedTagPosition]'
    }

    attribute_map = {
        'capacity': 'capacity',
        'cluster': 'cluster',
        'cluster_topo': 'cluster_topo',
        'disk_layout': 'disk_layout',
        'height': 'height',
        'id': 'id',
        'local_id': 'local_id',
        'model': 'model',
        'name': 'name',
        'node_topoes': 'node_topoes',
        'position': 'position',
        'power_layout': 'power_layout',
        'power_position': 'power_position',
        'powers': 'powers',
        'rack_topo': 'rack_topo',
        'tag_position_in_brick': 'tag_position_in_brick'
    }

    def __init__(self, capacity=None, cluster=None, cluster_topo=None, disk_layout=None, height=None, id=None, local_id=None, model=None, name=None, node_topoes=None, position=None, power_layout=None, power_position=None, powers=None, rack_topo=None, tag_position_in_brick=None, local_vars_configuration=None):  # noqa: E501
        """BrickTopo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._capacity = None
        self._cluster = None
        self._cluster_topo = None
        self._disk_layout = None
        self._height = None
        self._id = None
        self._local_id = None
        self._model = None
        self._name = None
        self._node_topoes = None
        self._position = None
        self._power_layout = None
        self._power_position = None
        self._powers = None
        self._rack_topo = None
        self._tag_position_in_brick = None
        self.discriminator = None

        self.capacity = capacity
        self.cluster = cluster
        self.cluster_topo = cluster_topo
        self.disk_layout = disk_layout
        self.height = height
        self.id = id
        self.local_id = local_id
        self.model = model
        self.name = name
        self.node_topoes = node_topoes
        self.position = position
        self.power_layout = power_layout
        self.power_position = power_position
        self.powers = powers
        self.rack_topo = rack_topo
        self.tag_position_in_brick = tag_position_in_brick

    @property
    def capacity(self):
        """Gets the capacity of this BrickTopo.  # noqa: E501


        :return: The capacity of this BrickTopo.  # noqa: E501
        :rtype: NestedCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this BrickTopo.


        :param capacity: The capacity of this BrickTopo.  # noqa: E501
        :type capacity: NestedCapacity
        """
        if self.local_vars_configuration.client_side_validation and capacity is None:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501

        self._capacity = capacity

    @property
    def cluster(self):
        """Gets the cluster of this BrickTopo.  # noqa: E501


        :return: The cluster of this BrickTopo.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this BrickTopo.


        :param cluster: The cluster of this BrickTopo.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def cluster_topo(self):
        """Gets the cluster_topo of this BrickTopo.  # noqa: E501


        :return: The cluster_topo of this BrickTopo.  # noqa: E501
        :rtype: NestedClusterTopo
        """
        return self._cluster_topo

    @cluster_topo.setter
    def cluster_topo(self, cluster_topo):
        """Sets the cluster_topo of this BrickTopo.


        :param cluster_topo: The cluster_topo of this BrickTopo.  # noqa: E501
        :type cluster_topo: NestedClusterTopo
        """

        self._cluster_topo = cluster_topo

    @property
    def disk_layout(self):
        """Gets the disk_layout of this BrickTopo.  # noqa: E501


        :return: The disk_layout of this BrickTopo.  # noqa: E501
        :rtype: NestedBrickDiskLayout
        """
        return self._disk_layout

    @disk_layout.setter
    def disk_layout(self, disk_layout):
        """Sets the disk_layout of this BrickTopo.


        :param disk_layout: The disk_layout of this BrickTopo.  # noqa: E501
        :type disk_layout: NestedBrickDiskLayout
        """

        self._disk_layout = disk_layout

    @property
    def height(self):
        """Gets the height of this BrickTopo.  # noqa: E501


        :return: The height of this BrickTopo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BrickTopo.


        :param height: The height of this BrickTopo.  # noqa: E501
        :type height: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def id(self):
        """Gets the id of this BrickTopo.  # noqa: E501


        :return: The id of this BrickTopo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BrickTopo.


        :param id: The id of this BrickTopo.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this BrickTopo.  # noqa: E501


        :return: The local_id of this BrickTopo.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this BrickTopo.


        :param local_id: The local_id of this BrickTopo.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def model(self):
        """Gets the model of this BrickTopo.  # noqa: E501


        :return: The model of this BrickTopo.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this BrickTopo.


        :param model: The model of this BrickTopo.  # noqa: E501
        :type model: str
        """

        self._model = model

    @property
    def name(self):
        """Gets the name of this BrickTopo.  # noqa: E501


        :return: The name of this BrickTopo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrickTopo.


        :param name: The name of this BrickTopo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_topoes(self):
        """Gets the node_topoes of this BrickTopo.  # noqa: E501


        :return: The node_topoes of this BrickTopo.  # noqa: E501
        :rtype: list[NestedNodeTopo]
        """
        return self._node_topoes

    @node_topoes.setter
    def node_topoes(self, node_topoes):
        """Sets the node_topoes of this BrickTopo.


        :param node_topoes: The node_topoes of this BrickTopo.  # noqa: E501
        :type node_topoes: list[NestedNodeTopo]
        """

        self._node_topoes = node_topoes

    @property
    def position(self):
        """Gets the position of this BrickTopo.  # noqa: E501


        :return: The position of this BrickTopo.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this BrickTopo.


        :param position: The position of this BrickTopo.  # noqa: E501
        :type position: int
        """
        if self.local_vars_configuration.client_side_validation and position is None:  # noqa: E501
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def power_layout(self):
        """Gets the power_layout of this BrickTopo.  # noqa: E501


        :return: The power_layout of this BrickTopo.  # noqa: E501
        :rtype: Direction
        """
        return self._power_layout

    @power_layout.setter
    def power_layout(self, power_layout):
        """Sets the power_layout of this BrickTopo.


        :param power_layout: The power_layout of this BrickTopo.  # noqa: E501
        :type power_layout: Direction
        """

        self._power_layout = power_layout

    @property
    def power_position(self):
        """Gets the power_position of this BrickTopo.  # noqa: E501


        :return: The power_position of this BrickTopo.  # noqa: E501
        :rtype: PowerPosition
        """
        return self._power_position

    @power_position.setter
    def power_position(self, power_position):
        """Sets the power_position of this BrickTopo.


        :param power_position: The power_position of this BrickTopo.  # noqa: E501
        :type power_position: PowerPosition
        """

        self._power_position = power_position

    @property
    def powers(self):
        """Gets the powers of this BrickTopo.  # noqa: E501


        :return: The powers of this BrickTopo.  # noqa: E501
        :rtype: list[NestedBrickPower]
        """
        return self._powers

    @powers.setter
    def powers(self, powers):
        """Sets the powers of this BrickTopo.


        :param powers: The powers of this BrickTopo.  # noqa: E501
        :type powers: list[NestedBrickPower]
        """

        self._powers = powers

    @property
    def rack_topo(self):
        """Gets the rack_topo of this BrickTopo.  # noqa: E501


        :return: The rack_topo of this BrickTopo.  # noqa: E501
        :rtype: NestedRackTopo
        """
        return self._rack_topo

    @rack_topo.setter
    def rack_topo(self, rack_topo):
        """Sets the rack_topo of this BrickTopo.


        :param rack_topo: The rack_topo of this BrickTopo.  # noqa: E501
        :type rack_topo: NestedRackTopo
        """

        self._rack_topo = rack_topo

    @property
    def tag_position_in_brick(self):
        """Gets the tag_position_in_brick of this BrickTopo.  # noqa: E501


        :return: The tag_position_in_brick of this BrickTopo.  # noqa: E501
        :rtype: list[NestedTagPosition]
        """
        return self._tag_position_in_brick

    @tag_position_in_brick.setter
    def tag_position_in_brick(self, tag_position_in_brick):
        """Sets the tag_position_in_brick of this BrickTopo.


        :param tag_position_in_brick: The tag_position_in_brick of this BrickTopo.  # noqa: E501
        :type tag_position_in_brick: list[NestedTagPosition]
        """

        self._tag_position_in_brick = tag_position_in_brick

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
        if not isinstance(other, BrickTopo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrickTopo):
            return True

        return self.to_dict() != other.to_dict()
