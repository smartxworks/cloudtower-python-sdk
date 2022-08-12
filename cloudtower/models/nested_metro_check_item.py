# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Contact: info@smartx.com
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


class NestedMetroCheckItem(object):
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
        'critical': 'list[str]',
        'info': 'list[str]',
        'key': 'str',
        'labels': 'object',
        'notice': 'list[str]',
        'status': 'MetroCheckStatusEnum'
    }

    attribute_map = {
        'critical': 'critical',
        'info': 'info',
        'key': 'key',
        'labels': 'labels',
        'notice': 'notice',
        'status': 'status'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedMetroCheckItem - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._critical = None
        self._info = None
        self._key = None
        self._labels = None
        self._notice = None
        self._status = None
        self.discriminator = None

        if "critical" in kwargs:
            self.critical = kwargs["critical"]
        if "info" in kwargs:
            self.info = kwargs["info"]
        if "key" in kwargs:
            self.key = kwargs["key"]
        if "labels" in kwargs:
            self.labels = kwargs["labels"]
        if "notice" in kwargs:
            self.notice = kwargs["notice"]
        if "status" in kwargs:
            self.status = kwargs["status"]

    @property
    def critical(self):
        """Gets the critical of this NestedMetroCheckItem.  # noqa: E501


        :return: The critical of this NestedMetroCheckItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this NestedMetroCheckItem.


        :param critical: The critical of this NestedMetroCheckItem.  # noqa: E501
        :type critical: list[str]
        """
        if self.local_vars_configuration.client_side_validation and critical is None:  # noqa: E501
            raise ValueError("Invalid value for `critical`, must not be `None`")  # noqa: E501

        self._critical = critical

    @property
    def info(self):
        """Gets the info of this NestedMetroCheckItem.  # noqa: E501


        :return: The info of this NestedMetroCheckItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this NestedMetroCheckItem.


        :param info: The info of this NestedMetroCheckItem.  # noqa: E501
        :type info: list[str]
        """
        if self.local_vars_configuration.client_side_validation and info is None:  # noqa: E501
            raise ValueError("Invalid value for `info`, must not be `None`")  # noqa: E501

        self._info = info

    @property
    def key(self):
        """Gets the key of this NestedMetroCheckItem.  # noqa: E501


        :return: The key of this NestedMetroCheckItem.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NestedMetroCheckItem.


        :param key: The key of this NestedMetroCheckItem.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def labels(self):
        """Gets the labels of this NestedMetroCheckItem.  # noqa: E501


        :return: The labels of this NestedMetroCheckItem.  # noqa: E501
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NestedMetroCheckItem.


        :param labels: The labels of this NestedMetroCheckItem.  # noqa: E501
        :type labels: object
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def notice(self):
        """Gets the notice of this NestedMetroCheckItem.  # noqa: E501


        :return: The notice of this NestedMetroCheckItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._notice

    @notice.setter
    def notice(self, notice):
        """Sets the notice of this NestedMetroCheckItem.


        :param notice: The notice of this NestedMetroCheckItem.  # noqa: E501
        :type notice: list[str]
        """
        if self.local_vars_configuration.client_side_validation and notice is None:  # noqa: E501
            raise ValueError("Invalid value for `notice`, must not be `None`")  # noqa: E501

        self._notice = notice

    @property
    def status(self):
        """Gets the status of this NestedMetroCheckItem.  # noqa: E501


        :return: The status of this NestedMetroCheckItem.  # noqa: E501
        :rtype: MetroCheckStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NestedMetroCheckItem.


        :param status: The status of this NestedMetroCheckItem.  # noqa: E501
        :type status: MetroCheckStatusEnum
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, NestedMetroCheckItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedMetroCheckItem):
            return True

        return self.to_dict() != other.to_dict()
