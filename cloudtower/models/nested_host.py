# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedHost(object):
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
        'id': 'str',
        'management_ip': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'management_ip': 'management_ip',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedHost - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._id = None
        self._management_ip = None
        self._name = None
        self.discriminator = None

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "management_ip" in kwargs:
            self.management_ip = kwargs["management_ip"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def id(self):
        """Gets the id of this NestedHost.  # noqa: E501


        :return: The id of this NestedHost.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedHost.


        :param id: The id of this NestedHost.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def management_ip(self):
        """Gets the management_ip of this NestedHost.  # noqa: E501


        :return: The management_ip of this NestedHost.  # noqa: E501
        :rtype: str
        """
        return self._management_ip

    @management_ip.setter
    def management_ip(self, management_ip):
        """Sets the management_ip of this NestedHost.


        :param management_ip: The management_ip of this NestedHost.  # noqa: E501
        :type management_ip: str
        """
        if self.local_vars_configuration.client_side_validation and management_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `management_ip`, must not be `None`")  # noqa: E501

        self._management_ip = management_ip

    @property
    def name(self):
        """Gets the name of this NestedHost.  # noqa: E501


        :return: The name of this NestedHost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedHost.


        :param name: The name of this NestedHost.  # noqa: E501
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
        if not isinstance(other, NestedHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedHost):
            return True

        return self.to_dict() != other.to_dict()
