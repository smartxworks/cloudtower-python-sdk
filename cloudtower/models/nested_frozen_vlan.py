# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class NestedFrozenVlan(object):
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
        'name': 'str',
        'vds_ovs': 'str',
        'vlan_id': 'int',
        'vlan_local_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'vds_ovs': 'vds_ovs',
        'vlan_id': 'vlan_id',
        'vlan_local_id': 'vlan_local_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedFrozenVlan - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._name = None
        self._vds_ovs = None
        self._vlan_id = None
        self._vlan_local_id = None
        self.discriminator = None

        if "name" in kwargs:
            self.name = kwargs["name"]
        if "vds_ovs" in kwargs:
            self.vds_ovs = kwargs["vds_ovs"]
        if "vlan_id" in kwargs:
            self.vlan_id = kwargs["vlan_id"]
        if "vlan_local_id" in kwargs:
            self.vlan_local_id = kwargs["vlan_local_id"]

    @property
    def name(self):
        """Gets the name of this NestedFrozenVlan.  # noqa: E501


        :return: The name of this NestedFrozenVlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedFrozenVlan.


        :param name: The name of this NestedFrozenVlan.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def vds_ovs(self):
        """Gets the vds_ovs of this NestedFrozenVlan.  # noqa: E501


        :return: The vds_ovs of this NestedFrozenVlan.  # noqa: E501
        :rtype: str
        """
        return self._vds_ovs

    @vds_ovs.setter
    def vds_ovs(self, vds_ovs):
        """Sets the vds_ovs of this NestedFrozenVlan.


        :param vds_ovs: The vds_ovs of this NestedFrozenVlan.  # noqa: E501
        :type vds_ovs: str
        """
        if self.local_vars_configuration.client_side_validation and vds_ovs is None:  # noqa: E501
            raise ValueError("Invalid value for `vds_ovs`, must not be `None`")  # noqa: E501

        self._vds_ovs = vds_ovs

    @property
    def vlan_id(self):
        """Gets the vlan_id of this NestedFrozenVlan.  # noqa: E501


        :return: The vlan_id of this NestedFrozenVlan.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this NestedFrozenVlan.


        :param vlan_id: The vlan_id of this NestedFrozenVlan.  # noqa: E501
        :type vlan_id: int
        """
        if self.local_vars_configuration.client_side_validation and vlan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must not be `None`")  # noqa: E501

        self._vlan_id = vlan_id

    @property
    def vlan_local_id(self):
        """Gets the vlan_local_id of this NestedFrozenVlan.  # noqa: E501


        :return: The vlan_local_id of this NestedFrozenVlan.  # noqa: E501
        :rtype: str
        """
        return self._vlan_local_id

    @vlan_local_id.setter
    def vlan_local_id(self, vlan_local_id):
        """Sets the vlan_local_id of this NestedFrozenVlan.


        :param vlan_local_id: The vlan_local_id of this NestedFrozenVlan.  # noqa: E501
        :type vlan_local_id: str
        """
        if self.local_vars_configuration.client_side_validation and vlan_local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan_local_id`, must not be `None`")  # noqa: E501

        self._vlan_local_id = vlan_local_id

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
        if not isinstance(other, NestedFrozenVlan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedFrozenVlan):
            return True

        return self.to_dict() != other.to_dict()
