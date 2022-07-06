# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class UpdateAccessRestrictionParams(object):
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
        'access_list': 'list[str]',
        'access_mode': 'AccessMode'
    }

    attribute_map = {
        'access_list': 'access_list',
        'access_mode': 'access_mode'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """UpdateAccessRestrictionParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._access_list = None
        self._access_mode = None
        self.discriminator = None

        if "access_list" in kwargs:
            self.access_list = kwargs["access_list"]
        if "access_mode" in kwargs:
            self.access_mode = kwargs["access_mode"]

    @property
    def access_list(self):
        """Gets the access_list of this UpdateAccessRestrictionParams.  # noqa: E501


        :return: The access_list of this UpdateAccessRestrictionParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._access_list

    @access_list.setter
    def access_list(self, access_list):
        """Sets the access_list of this UpdateAccessRestrictionParams.


        :param access_list: The access_list of this UpdateAccessRestrictionParams.  # noqa: E501
        :type access_list: list[str]
        """
        if self.local_vars_configuration.client_side_validation and access_list is None:  # noqa: E501
            raise ValueError("Invalid value for `access_list`, must not be `None`")  # noqa: E501

        self._access_list = access_list

    @property
    def access_mode(self):
        """Gets the access_mode of this UpdateAccessRestrictionParams.  # noqa: E501


        :return: The access_mode of this UpdateAccessRestrictionParams.  # noqa: E501
        :rtype: AccessMode
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this UpdateAccessRestrictionParams.


        :param access_mode: The access_mode of this UpdateAccessRestrictionParams.  # noqa: E501
        :type access_mode: AccessMode
        """
        if self.local_vars_configuration.client_side_validation and access_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `access_mode`, must not be `None`")  # noqa: E501

        self._access_mode = access_mode

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
        if not isinstance(other, UpdateAccessRestrictionParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAccessRestrictionParams):
            return True

        return self.to_dict() != other.to_dict()