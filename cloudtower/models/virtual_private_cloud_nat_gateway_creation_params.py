# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloudNatGatewayCreationParams(object):
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
        'external_ips': 'list[VirtualPrivateCloudExternalIpsParams]',
        'external_ip': 'str',
        'external_subnet_group_id': 'str',
        'external_subnet_id': 'str',
        'dnat_rules': 'list[VirtualPrivateCloudDnatRuleParams]',
        'enable_dnat': 'bool',
        'enable_snat': 'bool',
        'vpc_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'external_ips': 'external_ips',
        'external_ip': 'external_ip',
        'external_subnet_group_id': 'external_subnet_group_id',
        'external_subnet_id': 'external_subnet_id',
        'dnat_rules': 'dnat_rules',
        'enable_dnat': 'enable_dnat',
        'enable_snat': 'enable_snat',
        'vpc_id': 'vpc_id',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloudNatGatewayCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._external_ips = None
        self._external_ip = None
        self._external_subnet_group_id = None
        self._external_subnet_id = None
        self._dnat_rules = None
        self._enable_dnat = None
        self._enable_snat = None
        self._vpc_id = None
        self._name = None
        self.discriminator = None

        if "external_ips" in kwargs:
            self.external_ips = kwargs["external_ips"]
        if "external_ip" in kwargs:
            self.external_ip = kwargs["external_ip"]
        if "external_subnet_group_id" in kwargs:
            self.external_subnet_group_id = kwargs["external_subnet_group_id"]
        if "external_subnet_id" in kwargs:
            self.external_subnet_id = kwargs["external_subnet_id"]
        if "dnat_rules" in kwargs:
            self.dnat_rules = kwargs["dnat_rules"]
        if "enable_dnat" in kwargs:
            self.enable_dnat = kwargs["enable_dnat"]
        if "enable_snat" in kwargs:
            self.enable_snat = kwargs["enable_snat"]
        if "vpc_id" in kwargs:
            self.vpc_id = kwargs["vpc_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def external_ips(self):
        """Gets the external_ips of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The external_ips of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: list[VirtualPrivateCloudExternalIpsParams]
        """
        return self._external_ips

    @external_ips.setter
    def external_ips(self, external_ips):
        """Sets the external_ips of this VirtualPrivateCloudNatGatewayCreationParams.


        :param external_ips: The external_ips of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type external_ips: list[VirtualPrivateCloudExternalIpsParams]
        """

        self._external_ips = external_ips

    @property
    def external_ip(self):
        """Gets the external_ip of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The external_ip of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this VirtualPrivateCloudNatGatewayCreationParams.


        :param external_ip: The external_ip of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type external_ip: str
        """

        self._external_ip = external_ip

    @property
    def external_subnet_group_id(self):
        """Gets the external_subnet_group_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The external_subnet_group_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._external_subnet_group_id

    @external_subnet_group_id.setter
    def external_subnet_group_id(self, external_subnet_group_id):
        """Sets the external_subnet_group_id of this VirtualPrivateCloudNatGatewayCreationParams.


        :param external_subnet_group_id: The external_subnet_group_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type external_subnet_group_id: str
        """

        self._external_subnet_group_id = external_subnet_group_id

    @property
    def external_subnet_id(self):
        """Gets the external_subnet_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The external_subnet_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._external_subnet_id

    @external_subnet_id.setter
    def external_subnet_id(self, external_subnet_id):
        """Sets the external_subnet_id of this VirtualPrivateCloudNatGatewayCreationParams.


        :param external_subnet_id: The external_subnet_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type external_subnet_id: str
        """

        self._external_subnet_id = external_subnet_id

    @property
    def dnat_rules(self):
        """Gets the dnat_rules of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The dnat_rules of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: list[VirtualPrivateCloudDnatRuleParams]
        """
        return self._dnat_rules

    @dnat_rules.setter
    def dnat_rules(self, dnat_rules):
        """Sets the dnat_rules of this VirtualPrivateCloudNatGatewayCreationParams.


        :param dnat_rules: The dnat_rules of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type dnat_rules: list[VirtualPrivateCloudDnatRuleParams]
        """

        self._dnat_rules = dnat_rules

    @property
    def enable_dnat(self):
        """Gets the enable_dnat of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The enable_dnat of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dnat

    @enable_dnat.setter
    def enable_dnat(self, enable_dnat):
        """Sets the enable_dnat of this VirtualPrivateCloudNatGatewayCreationParams.


        :param enable_dnat: The enable_dnat of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type enable_dnat: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_dnat is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_dnat`, must not be `None`")  # noqa: E501

        self._enable_dnat = enable_dnat

    @property
    def enable_snat(self):
        """Gets the enable_snat of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The enable_snat of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: bool
        """
        return self._enable_snat

    @enable_snat.setter
    def enable_snat(self, enable_snat):
        """Sets the enable_snat of this VirtualPrivateCloudNatGatewayCreationParams.


        :param enable_snat: The enable_snat of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type enable_snat: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_snat is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_snat`, must not be `None`")  # noqa: E501

        self._enable_snat = enable_snat

    @property
    def vpc_id(self):
        """Gets the vpc_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The vpc_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this VirtualPrivateCloudNatGatewayCreationParams.


        :param vpc_id: The vpc_id of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type vpc_id: str
        """
        if self.local_vars_configuration.client_side_validation and vpc_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def name(self):
        """Gets the name of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501


        :return: The name of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualPrivateCloudNatGatewayCreationParams.


        :param name: The name of this VirtualPrivateCloudNatGatewayCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, VirtualPrivateCloudNatGatewayCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloudNatGatewayCreationParams):
            return True

        return self.to_dict() != other.to_dict()
