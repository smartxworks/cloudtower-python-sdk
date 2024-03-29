# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ExportFileDownloadLinks(object):
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
        'link': 'str',
        'filename': 'str'
    }

    attribute_map = {
        'link': 'link',
        'filename': 'filename'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ExportFileDownloadLinks - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._link = None
        self._filename = None
        self.discriminator = None

        if "link" in kwargs:
            self.link = kwargs["link"]
        if "filename" in kwargs:
            self.filename = kwargs["filename"]

    @property
    def link(self):
        """Gets the link of this ExportFileDownloadLinks.  # noqa: E501


        :return: The link of this ExportFileDownloadLinks.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ExportFileDownloadLinks.


        :param link: The link of this ExportFileDownloadLinks.  # noqa: E501
        :type link: str
        """
        if self.local_vars_configuration.client_side_validation and link is None:  # noqa: E501
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def filename(self):
        """Gets the filename of this ExportFileDownloadLinks.  # noqa: E501


        :return: The filename of this ExportFileDownloadLinks.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ExportFileDownloadLinks.


        :param filename: The filename of this ExportFileDownloadLinks.  # noqa: E501
        :type filename: str
        """
        if self.local_vars_configuration.client_side_validation and filename is None:  # noqa: E501
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

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
        if not isinstance(other, ExportFileDownloadLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportFileDownloadLinks):
            return True

        return self.to_dict() != other.to_dict()
