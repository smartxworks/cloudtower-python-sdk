# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower_python_sdk.configuration import Configuration


class VmAddFolderParams(object):
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
        'data': 'VmAddFolderParamsData',
        'where': 'VmWhereInput'
    }

    attribute_map = {
        'data': 'data',
        'where': 'where'
    }

    def __init__(self, data=None, where=None, local_vars_configuration=None):  # noqa: E501
        """VmAddFolderParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._where = None
        self.discriminator = None

        self.data = data
        self.where = where

    @property
    def data(self):
        """Gets the data of this VmAddFolderParams.  # noqa: E501


        :return: The data of this VmAddFolderParams.  # noqa: E501
        :rtype: VmAddFolderParamsData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VmAddFolderParams.


        :param data: The data of this VmAddFolderParams.  # noqa: E501
        :type data: VmAddFolderParamsData
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def where(self):
        """Gets the where of this VmAddFolderParams.  # noqa: E501


        :return: The where of this VmAddFolderParams.  # noqa: E501
        :rtype: VmWhereInput
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this VmAddFolderParams.


        :param where: The where of this VmAddFolderParams.  # noqa: E501
        :type where: VmWhereInput
        """
        if self.local_vars_configuration.client_side_validation and where is None:  # noqa: E501
            raise ValueError("Invalid value for `where`, must not be `None`")  # noqa: E501

        self._where = where

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
        if not isinstance(other, VmAddFolderParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmAddFolderParams):
            return True

        return self.to_dict() != other.to_dict()
