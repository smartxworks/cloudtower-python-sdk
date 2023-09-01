# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ContentLibraryVmdkCdromModify(object):
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
        'removed': 'bool',
        'boot': 'int',
        'index': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'removed': 'removed',
        'boot': 'boot',
        'index': 'index'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ContentLibraryVmdkCdromModify - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._enabled = None
        self._removed = None
        self._boot = None
        self._index = None
        self.discriminator = None

        if "enabled" in kwargs:
            self.enabled = kwargs["enabled"]
        if "removed" in kwargs:
            self.removed = kwargs["removed"]
        if "boot" in kwargs:
            self.boot = kwargs["boot"]
        if "index" in kwargs:
            self.index = kwargs["index"]

    @property
    def enabled(self):
        """Gets the enabled of this ContentLibraryVmdkCdromModify.  # noqa: E501


        :return: The enabled of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ContentLibraryVmdkCdromModify.


        :param enabled: The enabled of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def removed(self):
        """Gets the removed of this ContentLibraryVmdkCdromModify.  # noqa: E501


        :return: The removed of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :rtype: bool
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """Sets the removed of this ContentLibraryVmdkCdromModify.


        :param removed: The removed of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :type removed: bool
        """

        self._removed = removed

    @property
    def boot(self):
        """Gets the boot of this ContentLibraryVmdkCdromModify.  # noqa: E501


        :return: The boot of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :rtype: int
        """
        return self._boot

    @boot.setter
    def boot(self, boot):
        """Sets the boot of this ContentLibraryVmdkCdromModify.


        :param boot: The boot of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :type boot: int
        """

        self._boot = boot

    @property
    def index(self):
        """Gets the index of this ContentLibraryVmdkCdromModify.  # noqa: E501


        :return: The index of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ContentLibraryVmdkCdromModify.


        :param index: The index of this ContentLibraryVmdkCdromModify.  # noqa: E501
        :type index: int
        """
        if self.local_vars_configuration.client_side_validation and index is None:  # noqa: E501
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

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
        if not isinstance(other, ContentLibraryVmdkCdromModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentLibraryVmdkCdromModify):
            return True

        return self.to_dict() != other.to_dict()
