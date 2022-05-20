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


class NestedTemplateNic(object):
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
        'enabled': 'bool',
        'index': 'int',
        'ip_address': 'str',
        'mac_address': 'str',
        'mirror': 'bool',
        'model': 'VmNicModel',
        'vlan': 'NestedFrozenVlan'
    }

    attribute_map = {
        'enabled': 'enabled',
        'index': 'index',
        'ip_address': 'ip_address',
        'mac_address': 'mac_address',
        'mirror': 'mirror',
        'model': 'model',
        'vlan': 'vlan'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedTemplateNic - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._enabled = None
        self._index = None
        self._ip_address = None
        self._mac_address = None
        self._mirror = None
        self._model = None
        self._vlan = None
        self.discriminator = None

        self.enabled = kwargs.get("enabled", None)
        if "index" in kwargs:
            self.index = kwargs["index"]
        self.ip_address = kwargs.get("ip_address", None)
        self.mac_address = kwargs.get("mac_address", None)
        self.mirror = kwargs.get("mirror", None)
        self.model = kwargs.get("model", None)
        if "vlan" in kwargs:
            self.vlan = kwargs["vlan"]

    @property
    def enabled(self):
        """Gets the enabled of this NestedTemplateNic.  # noqa: E501


        :return: The enabled of this NestedTemplateNic.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NestedTemplateNic.


        :param enabled: The enabled of this NestedTemplateNic.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def index(self):
        """Gets the index of this NestedTemplateNic.  # noqa: E501


        :return: The index of this NestedTemplateNic.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this NestedTemplateNic.


        :param index: The index of this NestedTemplateNic.  # noqa: E501
        :type index: int
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def ip_address(self):
        """Gets the ip_address of this NestedTemplateNic.  # noqa: E501


        :return: The ip_address of this NestedTemplateNic.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this NestedTemplateNic.


        :param ip_address: The ip_address of this NestedTemplateNic.  # noqa: E501
        :type ip_address: str
        """

        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this NestedTemplateNic.  # noqa: E501


        :return: The mac_address of this NestedTemplateNic.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NestedTemplateNic.


        :param mac_address: The mac_address of this NestedTemplateNic.  # noqa: E501
        :type mac_address: str
        """

        self._mac_address = mac_address

    @property
    def mirror(self):
        """Gets the mirror of this NestedTemplateNic.  # noqa: E501


        :return: The mirror of this NestedTemplateNic.  # noqa: E501
        :rtype: bool
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this NestedTemplateNic.


        :param mirror: The mirror of this NestedTemplateNic.  # noqa: E501
        :type mirror: bool
        """

        self._mirror = mirror

    @property
    def model(self):
        """Gets the model of this NestedTemplateNic.  # noqa: E501


        :return: The model of this NestedTemplateNic.  # noqa: E501
        :rtype: VmNicModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this NestedTemplateNic.


        :param model: The model of this NestedTemplateNic.  # noqa: E501
        :type model: VmNicModel
        """

        self._model = model

    @property
    def vlan(self):
        """Gets the vlan of this NestedTemplateNic.  # noqa: E501


        :return: The vlan of this NestedTemplateNic.  # noqa: E501
        :rtype: NestedFrozenVlan
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this NestedTemplateNic.


        :param vlan: The vlan of this NestedTemplateNic.  # noqa: E501
        :type vlan: NestedFrozenVlan
        """
        if self.local_vars_configuration.client_side_validation and vlan is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan`, must not be `None`")  # noqa: E501

        self._vlan = vlan

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
        if not isinstance(other, NestedTemplateNic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedTemplateNic):
            return True

        return self.to_dict() != other.to_dict()