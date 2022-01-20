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


class NestedPosition(object):
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
        'column': 'int',
        'row': 'int'
    }

    attribute_map = {
        'column': 'column',
        'row': 'row'
    }

    def __init__(self, column=None, row=None, local_vars_configuration=None):  # noqa: E501
        """NestedPosition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._column = None
        self._row = None
        self.discriminator = None

        self.column = column
        self.row = row

    @property
    def column(self):
        """Gets the column of this NestedPosition.  # noqa: E501


        :return: The column of this NestedPosition.  # noqa: E501
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this NestedPosition.


        :param column: The column of this NestedPosition.  # noqa: E501
        :type column: int
        """

        self._column = column

    @property
    def row(self):
        """Gets the row of this NestedPosition.  # noqa: E501


        :return: The row of this NestedPosition.  # noqa: E501
        :rtype: int
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this NestedPosition.


        :param row: The row of this NestedPosition.  # noqa: E501
        :type row: int
        """

        self._row = row

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
        if not isinstance(other, NestedPosition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedPosition):
            return True

        return self.to_dict() != other.to_dict()
