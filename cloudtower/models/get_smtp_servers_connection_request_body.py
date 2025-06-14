# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class GetSmtpServersConnectionRequestBody(object):
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
        'after': 'str',
        'before': 'str',
        'first': 'int',
        'last': 'int',
        'order_by': 'SmtpServerOrderByInput',
        'skip': 'int',
        'where': 'SmtpServerWhereInput'
    }

    attribute_map = {
        'after': 'after',
        'before': 'before',
        'first': 'first',
        'last': 'last',
        'order_by': 'orderBy',
        'skip': 'skip',
        'where': 'where'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GetSmtpServersConnectionRequestBody - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._after = None
        self._before = None
        self._first = None
        self._last = None
        self._order_by = None
        self._skip = None
        self._where = None
        self.discriminator = None

        self.after = kwargs.get("after", None)
        self.before = kwargs.get("before", None)
        self.first = kwargs.get("first", None)
        self.last = kwargs.get("last", None)
        self.order_by = kwargs.get("order_by", None)
        self.skip = kwargs.get("skip", None)
        self.where = kwargs.get("where", None)

    @property
    def after(self):
        """Gets the after of this GetSmtpServersConnectionRequestBody.  # noqa: E501


        :return: The after of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this GetSmtpServersConnectionRequestBody.


        :param after: The after of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :type after: str
        """

        self._after = after

    @property
    def before(self):
        """Gets the before of this GetSmtpServersConnectionRequestBody.  # noqa: E501


        :return: The before of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this GetSmtpServersConnectionRequestBody.


        :param before: The before of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :type before: str
        """

        self._before = before

    @property
    def first(self):
        """Gets the first of this GetSmtpServersConnectionRequestBody.  # noqa: E501


        :return: The first of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this GetSmtpServersConnectionRequestBody.


        :param first: The first of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :type first: int
        """

        self._first = first

    @property
    def last(self):
        """Gets the last of this GetSmtpServersConnectionRequestBody.  # noqa: E501


        :return: The last of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this GetSmtpServersConnectionRequestBody.


        :param last: The last of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :type last: int
        """

        self._last = last

    @property
    def order_by(self):
        """Gets the order_by of this GetSmtpServersConnectionRequestBody.  # noqa: E501


        :return: The order_by of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :rtype: SmtpServerOrderByInput
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this GetSmtpServersConnectionRequestBody.


        :param order_by: The order_by of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :type order_by: SmtpServerOrderByInput
        """

        self._order_by = order_by

    @property
    def skip(self):
        """Gets the skip of this GetSmtpServersConnectionRequestBody.  # noqa: E501


        :return: The skip of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """Sets the skip of this GetSmtpServersConnectionRequestBody.


        :param skip: The skip of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :type skip: int
        """

        self._skip = skip

    @property
    def where(self):
        """Gets the where of this GetSmtpServersConnectionRequestBody.  # noqa: E501


        :return: The where of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :rtype: SmtpServerWhereInput
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this GetSmtpServersConnectionRequestBody.


        :param where: The where of this GetSmtpServersConnectionRequestBody.  # noqa: E501
        :type where: SmtpServerWhereInput
        """

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
        if not isinstance(other, GetSmtpServersConnectionRequestBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetSmtpServersConnectionRequestBody):
            return True

        return self.to_dict() != other.to_dict()
