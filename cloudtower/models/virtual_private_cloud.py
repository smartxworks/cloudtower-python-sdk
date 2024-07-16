# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloud(object):
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
        'associate_external_subnet_num': 'int',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'isolation_policies': 'list[NestedVirtualPrivateCloudIsolationPolicy]',
        'local_id': 'str',
        'mtu': 'int',
        'name': 'str',
        'route_tables': 'list[NestedVirtualPrivateCloudRouteTable]',
        'security_groups': 'list[NestedVirtualPrivateCloudSecurityGroup]',
        'security_policies': 'list[NestedVirtualPrivateCloudSecurityPolicy]',
        'subnets': 'list[NestedVirtualPrivateCloudSubnet]'
    }

    attribute_map = {
        'associate_external_subnet_num': 'associate_external_subnet_num',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'isolation_policies': 'isolation_policies',
        'local_id': 'local_id',
        'mtu': 'mtu',
        'name': 'name',
        'route_tables': 'route_tables',
        'security_groups': 'security_groups',
        'security_policies': 'security_policies',
        'subnets': 'subnets'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloud - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._associate_external_subnet_num = None
        self._description = None
        self._entity_async_status = None
        self._id = None
        self._isolation_policies = None
        self._local_id = None
        self._mtu = None
        self._name = None
        self._route_tables = None
        self._security_groups = None
        self._security_policies = None
        self._subnets = None
        self.discriminator = None

        self.associate_external_subnet_num = kwargs.get("associate_external_subnet_num", None)
        self.description = kwargs.get("description", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.isolation_policies = kwargs.get("isolation_policies", None)
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        self.mtu = kwargs.get("mtu", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.route_tables = kwargs.get("route_tables", None)
        self.security_groups = kwargs.get("security_groups", None)
        self.security_policies = kwargs.get("security_policies", None)
        self.subnets = kwargs.get("subnets", None)

    @property
    def associate_external_subnet_num(self):
        """Gets the associate_external_subnet_num of this VirtualPrivateCloud.  # noqa: E501


        :return: The associate_external_subnet_num of this VirtualPrivateCloud.  # noqa: E501
        :rtype: int
        """
        return self._associate_external_subnet_num

    @associate_external_subnet_num.setter
    def associate_external_subnet_num(self, associate_external_subnet_num):
        """Sets the associate_external_subnet_num of this VirtualPrivateCloud.


        :param associate_external_subnet_num: The associate_external_subnet_num of this VirtualPrivateCloud.  # noqa: E501
        :type associate_external_subnet_num: int
        """

        self._associate_external_subnet_num = associate_external_subnet_num

    @property
    def description(self):
        """Gets the description of this VirtualPrivateCloud.  # noqa: E501


        :return: The description of this VirtualPrivateCloud.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualPrivateCloud.


        :param description: The description of this VirtualPrivateCloud.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this VirtualPrivateCloud.  # noqa: E501


        :return: The entity_async_status of this VirtualPrivateCloud.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this VirtualPrivateCloud.


        :param entity_async_status: The entity_async_status of this VirtualPrivateCloud.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this VirtualPrivateCloud.  # noqa: E501


        :return: The id of this VirtualPrivateCloud.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualPrivateCloud.


        :param id: The id of this VirtualPrivateCloud.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def isolation_policies(self):
        """Gets the isolation_policies of this VirtualPrivateCloud.  # noqa: E501


        :return: The isolation_policies of this VirtualPrivateCloud.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudIsolationPolicy]
        """
        return self._isolation_policies

    @isolation_policies.setter
    def isolation_policies(self, isolation_policies):
        """Sets the isolation_policies of this VirtualPrivateCloud.


        :param isolation_policies: The isolation_policies of this VirtualPrivateCloud.  # noqa: E501
        :type isolation_policies: list[NestedVirtualPrivateCloudIsolationPolicy]
        """

        self._isolation_policies = isolation_policies

    @property
    def local_id(self):
        """Gets the local_id of this VirtualPrivateCloud.  # noqa: E501


        :return: The local_id of this VirtualPrivateCloud.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VirtualPrivateCloud.


        :param local_id: The local_id of this VirtualPrivateCloud.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def mtu(self):
        """Gets the mtu of this VirtualPrivateCloud.  # noqa: E501


        :return: The mtu of this VirtualPrivateCloud.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this VirtualPrivateCloud.


        :param mtu: The mtu of this VirtualPrivateCloud.  # noqa: E501
        :type mtu: int
        """

        self._mtu = mtu

    @property
    def name(self):
        """Gets the name of this VirtualPrivateCloud.  # noqa: E501


        :return: The name of this VirtualPrivateCloud.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualPrivateCloud.


        :param name: The name of this VirtualPrivateCloud.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def route_tables(self):
        """Gets the route_tables of this VirtualPrivateCloud.  # noqa: E501


        :return: The route_tables of this VirtualPrivateCloud.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudRouteTable]
        """
        return self._route_tables

    @route_tables.setter
    def route_tables(self, route_tables):
        """Sets the route_tables of this VirtualPrivateCloud.


        :param route_tables: The route_tables of this VirtualPrivateCloud.  # noqa: E501
        :type route_tables: list[NestedVirtualPrivateCloudRouteTable]
        """

        self._route_tables = route_tables

    @property
    def security_groups(self):
        """Gets the security_groups of this VirtualPrivateCloud.  # noqa: E501


        :return: The security_groups of this VirtualPrivateCloud.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudSecurityGroup]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this VirtualPrivateCloud.


        :param security_groups: The security_groups of this VirtualPrivateCloud.  # noqa: E501
        :type security_groups: list[NestedVirtualPrivateCloudSecurityGroup]
        """

        self._security_groups = security_groups

    @property
    def security_policies(self):
        """Gets the security_policies of this VirtualPrivateCloud.  # noqa: E501


        :return: The security_policies of this VirtualPrivateCloud.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudSecurityPolicy]
        """
        return self._security_policies

    @security_policies.setter
    def security_policies(self, security_policies):
        """Sets the security_policies of this VirtualPrivateCloud.


        :param security_policies: The security_policies of this VirtualPrivateCloud.  # noqa: E501
        :type security_policies: list[NestedVirtualPrivateCloudSecurityPolicy]
        """

        self._security_policies = security_policies

    @property
    def subnets(self):
        """Gets the subnets of this VirtualPrivateCloud.  # noqa: E501


        :return: The subnets of this VirtualPrivateCloud.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this VirtualPrivateCloud.


        :param subnets: The subnets of this VirtualPrivateCloud.  # noqa: E501
        :type subnets: list[NestedVirtualPrivateCloudSubnet]
        """

        self._subnets = subnets

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
        if not isinstance(other, VirtualPrivateCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloud):
            return True

        return self.to_dict() != other.to_dict()