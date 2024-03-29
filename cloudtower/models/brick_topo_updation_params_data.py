# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class BrickTopoUpdationParamsData(object):
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
        'tag_position_in_brick': 'list[NestedTagPosition]',
        'node_topoes': 'NodeTopoWhereInput',
        'capacity': 'NestedCapacity',
        'height': 'int',
        'name': 'str',
        'position': 'int'
    }

    attribute_map = {
        'tag_position_in_brick': 'tag_position_in_brick',
        'node_topoes': 'node_topoes',
        'capacity': 'capacity',
        'height': 'height',
        'name': 'name',
        'position': 'position'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BrickTopoUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._tag_position_in_brick = None
        self._node_topoes = None
        self._capacity = None
        self._height = None
        self._name = None
        self._position = None
        self.discriminator = None

        self.tag_position_in_brick = kwargs.get("tag_position_in_brick", None)
        if "node_topoes" in kwargs:
            self.node_topoes = kwargs["node_topoes"]
        if "capacity" in kwargs:
            self.capacity = kwargs["capacity"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "position" in kwargs:
            self.position = kwargs["position"]

    @property
    def tag_position_in_brick(self):
        """Gets the tag_position_in_brick of this BrickTopoUpdationParamsData.  # noqa: E501


        :return: The tag_position_in_brick of this BrickTopoUpdationParamsData.  # noqa: E501
        :rtype: list[NestedTagPosition]
        """
        return self._tag_position_in_brick

    @tag_position_in_brick.setter
    def tag_position_in_brick(self, tag_position_in_brick):
        """Sets the tag_position_in_brick of this BrickTopoUpdationParamsData.


        :param tag_position_in_brick: The tag_position_in_brick of this BrickTopoUpdationParamsData.  # noqa: E501
        :type tag_position_in_brick: list[NestedTagPosition]
        """

        self._tag_position_in_brick = tag_position_in_brick

    @property
    def node_topoes(self):
        """Gets the node_topoes of this BrickTopoUpdationParamsData.  # noqa: E501


        :return: The node_topoes of this BrickTopoUpdationParamsData.  # noqa: E501
        :rtype: NodeTopoWhereInput
        """
        return self._node_topoes

    @node_topoes.setter
    def node_topoes(self, node_topoes):
        """Sets the node_topoes of this BrickTopoUpdationParamsData.


        :param node_topoes: The node_topoes of this BrickTopoUpdationParamsData.  # noqa: E501
        :type node_topoes: NodeTopoWhereInput
        """

        self._node_topoes = node_topoes

    @property
    def capacity(self):
        """Gets the capacity of this BrickTopoUpdationParamsData.  # noqa: E501


        :return: The capacity of this BrickTopoUpdationParamsData.  # noqa: E501
        :rtype: NestedCapacity
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this BrickTopoUpdationParamsData.


        :param capacity: The capacity of this BrickTopoUpdationParamsData.  # noqa: E501
        :type capacity: NestedCapacity
        """

        self._capacity = capacity

    @property
    def height(self):
        """Gets the height of this BrickTopoUpdationParamsData.  # noqa: E501


        :return: The height of this BrickTopoUpdationParamsData.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BrickTopoUpdationParamsData.


        :param height: The height of this BrickTopoUpdationParamsData.  # noqa: E501
        :type height: int
        """

        self._height = height

    @property
    def name(self):
        """Gets the name of this BrickTopoUpdationParamsData.  # noqa: E501


        :return: The name of this BrickTopoUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrickTopoUpdationParamsData.


        :param name: The name of this BrickTopoUpdationParamsData.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def position(self):
        """Gets the position of this BrickTopoUpdationParamsData.  # noqa: E501


        :return: The position of this BrickTopoUpdationParamsData.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this BrickTopoUpdationParamsData.


        :param position: The position of this BrickTopoUpdationParamsData.  # noqa: E501
        :type position: int
        """

        self._position = position

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
        if not isinstance(other, BrickTopoUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BrickTopoUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
