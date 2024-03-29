# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class OvfCpu(object):
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
        'sockets': 'int',
        'cores': 'int'
    }

    attribute_map = {
        'sockets': 'sockets',
        'cores': 'cores'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """OvfCpu - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._sockets = None
        self._cores = None
        self.discriminator = None

        if "sockets" in kwargs:
            self.sockets = kwargs["sockets"]
        if "cores" in kwargs:
            self.cores = kwargs["cores"]

    @property
    def sockets(self):
        """Gets the sockets of this OvfCpu.  # noqa: E501


        :return: The sockets of this OvfCpu.  # noqa: E501
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets):
        """Sets the sockets of this OvfCpu.


        :param sockets: The sockets of this OvfCpu.  # noqa: E501
        :type sockets: int
        """
        if self.local_vars_configuration.client_side_validation and sockets is None:  # noqa: E501
            raise ValueError("Invalid value for `sockets`, must not be `None`")  # noqa: E501

        self._sockets = sockets

    @property
    def cores(self):
        """Gets the cores of this OvfCpu.  # noqa: E501


        :return: The cores of this OvfCpu.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this OvfCpu.


        :param cores: The cores of this OvfCpu.  # noqa: E501
        :type cores: int
        """
        if self.local_vars_configuration.client_side_validation and cores is None:  # noqa: E501
            raise ValueError("Invalid value for `cores`, must not be `None`")  # noqa: E501

        self._cores = cores

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
        if not isinstance(other, OvfCpu):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OvfCpu):
            return True

        return self.to_dict() != other.to_dict()
