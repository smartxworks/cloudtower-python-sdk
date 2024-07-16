# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloudExternalSubnet(object):
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
        'cidr': 'str',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'floating_ip_cidr': 'str',
        'floating_ips': 'list[NestedVirtualPrivateCloudFloatingIp]',
        'gateway': 'str',
        'id': 'str',
        'local_id': 'str',
        'name': 'str',
        'nat_gateway_cidr': 'str',
        'nat_gateways': 'list[NestedVirtualPrivateCloudNatGateway]',
        'router_gateway_cidr': 'str',
        'router_gateways': 'list[NestedVirtualPrivateCloudRouterGateway]',
        'vlan': 'NestedVlan',
        'vpc': 'NestedVirtualPrivateCloud'
    }

    attribute_map = {
        'cidr': 'cidr',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'floating_ip_cidr': 'floating_ip_cidr',
        'floating_ips': 'floating_ips',
        'gateway': 'gateway',
        'id': 'id',
        'local_id': 'local_id',
        'name': 'name',
        'nat_gateway_cidr': 'nat_gateway_cidr',
        'nat_gateways': 'nat_gateways',
        'router_gateway_cidr': 'router_gateway_cidr',
        'router_gateways': 'router_gateways',
        'vlan': 'vlan',
        'vpc': 'vpc'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloudExternalSubnet - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cidr = None
        self._description = None
        self._entity_async_status = None
        self._floating_ip_cidr = None
        self._floating_ips = None
        self._gateway = None
        self._id = None
        self._local_id = None
        self._name = None
        self._nat_gateway_cidr = None
        self._nat_gateways = None
        self._router_gateway_cidr = None
        self._router_gateways = None
        self._vlan = None
        self._vpc = None
        self.discriminator = None

        if "cidr" in kwargs:
            self.cidr = kwargs["cidr"]
        self.description = kwargs.get("description", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        self.floating_ip_cidr = kwargs.get("floating_ip_cidr", None)
        self.floating_ips = kwargs.get("floating_ips", None)
        if "gateway" in kwargs:
            self.gateway = kwargs["gateway"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.nat_gateway_cidr = kwargs.get("nat_gateway_cidr", None)
        self.nat_gateways = kwargs.get("nat_gateways", None)
        self.router_gateway_cidr = kwargs.get("router_gateway_cidr", None)
        self.router_gateways = kwargs.get("router_gateways", None)
        if "vlan" in kwargs:
            self.vlan = kwargs["vlan"]
        self.vpc = kwargs.get("vpc", None)

    @property
    def cidr(self):
        """Gets the cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this VirtualPrivateCloudExternalSubnet.


        :param cidr: The cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type cidr: str
        """
        if self.local_vars_configuration.client_side_validation and cidr is None:  # noqa: E501
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501

        self._cidr = cidr

    @property
    def description(self):
        """Gets the description of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The description of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualPrivateCloudExternalSubnet.


        :param description: The description of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The entity_async_status of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this VirtualPrivateCloudExternalSubnet.


        :param entity_async_status: The entity_async_status of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def floating_ip_cidr(self):
        """Gets the floating_ip_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The floating_ip_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._floating_ip_cidr

    @floating_ip_cidr.setter
    def floating_ip_cidr(self, floating_ip_cidr):
        """Sets the floating_ip_cidr of this VirtualPrivateCloudExternalSubnet.


        :param floating_ip_cidr: The floating_ip_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type floating_ip_cidr: str
        """

        self._floating_ip_cidr = floating_ip_cidr

    @property
    def floating_ips(self):
        """Gets the floating_ips of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The floating_ips of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudFloatingIp]
        """
        return self._floating_ips

    @floating_ips.setter
    def floating_ips(self, floating_ips):
        """Sets the floating_ips of this VirtualPrivateCloudExternalSubnet.


        :param floating_ips: The floating_ips of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type floating_ips: list[NestedVirtualPrivateCloudFloatingIp]
        """

        self._floating_ips = floating_ips

    @property
    def gateway(self):
        """Gets the gateway of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The gateway of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this VirtualPrivateCloudExternalSubnet.


        :param gateway: The gateway of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type gateway: str
        """
        if self.local_vars_configuration.client_side_validation and gateway is None:  # noqa: E501
            raise ValueError("Invalid value for `gateway`, must not be `None`")  # noqa: E501

        self._gateway = gateway

    @property
    def id(self):
        """Gets the id of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The id of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualPrivateCloudExternalSubnet.


        :param id: The id of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The local_id of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VirtualPrivateCloudExternalSubnet.


        :param local_id: The local_id of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The name of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualPrivateCloudExternalSubnet.


        :param name: The name of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nat_gateway_cidr(self):
        """Gets the nat_gateway_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The nat_gateway_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._nat_gateway_cidr

    @nat_gateway_cidr.setter
    def nat_gateway_cidr(self, nat_gateway_cidr):
        """Sets the nat_gateway_cidr of this VirtualPrivateCloudExternalSubnet.


        :param nat_gateway_cidr: The nat_gateway_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type nat_gateway_cidr: str
        """

        self._nat_gateway_cidr = nat_gateway_cidr

    @property
    def nat_gateways(self):
        """Gets the nat_gateways of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The nat_gateways of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudNatGateway]
        """
        return self._nat_gateways

    @nat_gateways.setter
    def nat_gateways(self, nat_gateways):
        """Sets the nat_gateways of this VirtualPrivateCloudExternalSubnet.


        :param nat_gateways: The nat_gateways of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type nat_gateways: list[NestedVirtualPrivateCloudNatGateway]
        """

        self._nat_gateways = nat_gateways

    @property
    def router_gateway_cidr(self):
        """Gets the router_gateway_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The router_gateway_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: str
        """
        return self._router_gateway_cidr

    @router_gateway_cidr.setter
    def router_gateway_cidr(self, router_gateway_cidr):
        """Sets the router_gateway_cidr of this VirtualPrivateCloudExternalSubnet.


        :param router_gateway_cidr: The router_gateway_cidr of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type router_gateway_cidr: str
        """

        self._router_gateway_cidr = router_gateway_cidr

    @property
    def router_gateways(self):
        """Gets the router_gateways of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The router_gateways of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudRouterGateway]
        """
        return self._router_gateways

    @router_gateways.setter
    def router_gateways(self, router_gateways):
        """Sets the router_gateways of this VirtualPrivateCloudExternalSubnet.


        :param router_gateways: The router_gateways of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type router_gateways: list[NestedVirtualPrivateCloudRouterGateway]
        """

        self._router_gateways = router_gateways

    @property
    def vlan(self):
        """Gets the vlan of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The vlan of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: NestedVlan
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this VirtualPrivateCloudExternalSubnet.


        :param vlan: The vlan of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type vlan: NestedVlan
        """
        if self.local_vars_configuration.client_side_validation and vlan is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan`, must not be `None`")  # noqa: E501

        self._vlan = vlan

    @property
    def vpc(self):
        """Gets the vpc of this VirtualPrivateCloudExternalSubnet.  # noqa: E501


        :return: The vpc of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :rtype: NestedVirtualPrivateCloud
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this VirtualPrivateCloudExternalSubnet.


        :param vpc: The vpc of this VirtualPrivateCloudExternalSubnet.  # noqa: E501
        :type vpc: NestedVirtualPrivateCloud
        """

        self._vpc = vpc

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
        if not isinstance(other, VirtualPrivateCloudExternalSubnet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloudExternalSubnet):
            return True

        return self.to_dict() != other.to_dict()