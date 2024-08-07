# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloudRouteParams(object):
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
        'destination': 'str',
        'next_hop_local_id': 'str',
        'next_hop_type': 'VirtualPrivateCloudRouteNextHopType'
    }

    attribute_map = {
        'destination': 'destination',
        'next_hop_local_id': 'next_hop_local_id',
        'next_hop_type': 'next_hop_type'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloudRouteParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._destination = None
        self._next_hop_local_id = None
        self._next_hop_type = None
        self.discriminator = None

        if "destination" in kwargs:
            self.destination = kwargs["destination"]
        if "next_hop_local_id" in kwargs:
            self.next_hop_local_id = kwargs["next_hop_local_id"]
        if "next_hop_type" in kwargs:
            self.next_hop_type = kwargs["next_hop_type"]

    @property
    def destination(self):
        """Gets the destination of this VirtualPrivateCloudRouteParams.  # noqa: E501


        :return: The destination of this VirtualPrivateCloudRouteParams.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this VirtualPrivateCloudRouteParams.


        :param destination: The destination of this VirtualPrivateCloudRouteParams.  # noqa: E501
        :type destination: str
        """
        if self.local_vars_configuration.client_side_validation and destination is None:  # noqa: E501
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def next_hop_local_id(self):
        """Gets the next_hop_local_id of this VirtualPrivateCloudRouteParams.  # noqa: E501


        :return: The next_hop_local_id of this VirtualPrivateCloudRouteParams.  # noqa: E501
        :rtype: str
        """
        return self._next_hop_local_id

    @next_hop_local_id.setter
    def next_hop_local_id(self, next_hop_local_id):
        """Sets the next_hop_local_id of this VirtualPrivateCloudRouteParams.


        :param next_hop_local_id: The next_hop_local_id of this VirtualPrivateCloudRouteParams.  # noqa: E501
        :type next_hop_local_id: str
        """
        if self.local_vars_configuration.client_side_validation and next_hop_local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `next_hop_local_id`, must not be `None`")  # noqa: E501

        self._next_hop_local_id = next_hop_local_id

    @property
    def next_hop_type(self):
        """Gets the next_hop_type of this VirtualPrivateCloudRouteParams.  # noqa: E501


        :return: The next_hop_type of this VirtualPrivateCloudRouteParams.  # noqa: E501
        :rtype: VirtualPrivateCloudRouteNextHopType
        """
        return self._next_hop_type

    @next_hop_type.setter
    def next_hop_type(self, next_hop_type):
        """Sets the next_hop_type of this VirtualPrivateCloudRouteParams.


        :param next_hop_type: The next_hop_type of this VirtualPrivateCloudRouteParams.  # noqa: E501
        :type next_hop_type: VirtualPrivateCloudRouteNextHopType
        """
        if self.local_vars_configuration.client_side_validation and next_hop_type is None:  # noqa: E501
            raise ValueError("Invalid value for `next_hop_type`, must not be `None`")  # noqa: E501

        self._next_hop_type = next_hop_type

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
        if not isinstance(other, VirtualPrivateCloudRouteParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloudRouteParams):
            return True

        return self.to_dict() != other.to_dict()
