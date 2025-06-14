# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedVirtualPrivateCloudExternalSubnet(object):
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
        'edge_gateway': 'NestedVirtualPrivateCloudEdgeGateway',
        'floating_ip_cidr': 'str',
        'id': 'str',
        'name': 'str',
        'nat_gateway_cidr': 'str',
        'router_gateway_cidr': 'str'
    }

    attribute_map = {
        'edge_gateway': 'edge_gateway',
        'floating_ip_cidr': 'floating_ip_cidr',
        'id': 'id',
        'name': 'name',
        'nat_gateway_cidr': 'nat_gateway_cidr',
        'router_gateway_cidr': 'router_gateway_cidr'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedVirtualPrivateCloudExternalSubnet - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._edge_gateway = None
        self._floating_ip_cidr = None
        self._id = None
        self._name = None
        self._nat_gateway_cidr = None
        self._router_gateway_cidr = None
        self.discriminator = None

        self.edge_gateway = kwargs.get("edge_gateway", None)
        self.floating_ip_cidr = kwargs.get("floating_ip_cidr", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.nat_gateway_cidr = kwargs.get("nat_gateway_cidr", None)
        self.router_gateway_cidr = kwargs.get("router_gateway_cidr", None)

    @property
    def edge_gateway(self):
        """Gets the edge_gateway of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The edge_gateway of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: NestedVirtualPrivateCloudEdgeGateway
        """
        return self._edge_gateway

    @edge_gateway.setter
    def edge_gateway(self, edge_gateway):
        """Sets the edge_gateway of this NestedVirtualPrivateCloudExternalSubnet.


        :param edge_gateway: The edge_gateway of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type edge_gateway: NestedVirtualPrivateCloudEdgeGateway
        """

        self._edge_gateway = edge_gateway

    @property
    def floating_ip_cidr(self):
        """Gets the floating_ip_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The floating_ip_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._floating_ip_cidr

    @floating_ip_cidr.setter
    def floating_ip_cidr(self, floating_ip_cidr):
        """Sets the floating_ip_cidr of this NestedVirtualPrivateCloudExternalSubnet.


        :param floating_ip_cidr: The floating_ip_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type floating_ip_cidr: str
        """

        self._floating_ip_cidr = floating_ip_cidr

    @property
    def id(self):
        """Gets the id of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The id of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedVirtualPrivateCloudExternalSubnet.


        :param id: The id of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The name of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedVirtualPrivateCloudExternalSubnet.


        :param name: The name of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nat_gateway_cidr(self):
        """Gets the nat_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The nat_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_cidr

    @nat_gateway_cidr.setter
    def nat_gateway_cidr(self, nat_gateway_cidr):
        """Sets the nat_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.


        :param nat_gateway_cidr: The nat_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type nat_gateway_cidr: str
        """

        self._nat_gateway_cidr = nat_gateway_cidr

    @property
    def router_gateway_cidr(self):
        """Gets the router_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The router_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._router_gateway_cidr

    @router_gateway_cidr.setter
    def router_gateway_cidr(self, router_gateway_cidr):
        """Sets the router_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.


        :param router_gateway_cidr: The router_gateway_cidr of this NestedVirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type router_gateway_cidr: str
        """

        self._router_gateway_cidr = router_gateway_cidr

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
        if not isinstance(other, NestedVirtualPrivateCloudExternalSubnet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedVirtualPrivateCloudExternalSubnet):
            return True

        return self.to_dict() != other.to_dict()
