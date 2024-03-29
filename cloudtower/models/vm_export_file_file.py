# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmExportFileFile(object):
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
        'md5': 'str',
        'file_size': 'int',
        'file_secret': 'str',
        'file_uuid': 'str',
        'type': 'VmExportFileType',
        'file_name': 'str'
    }

    attribute_map = {
        'md5': 'md5',
        'file_size': 'fileSize',
        'file_secret': 'fileSecret',
        'file_uuid': 'fileUUID',
        'type': 'type',
        'file_name': 'fileName'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmExportFileFile - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._md5 = None
        self._file_size = None
        self._file_secret = None
        self._file_uuid = None
        self._type = None
        self._file_name = None
        self.discriminator = None

        if "md5" in kwargs:
            self.md5 = kwargs["md5"]
        if "file_size" in kwargs:
            self.file_size = kwargs["file_size"]
        if "file_secret" in kwargs:
            self.file_secret = kwargs["file_secret"]
        if "file_uuid" in kwargs:
            self.file_uuid = kwargs["file_uuid"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "file_name" in kwargs:
            self.file_name = kwargs["file_name"]

    @property
    def md5(self):
        """Gets the md5 of this VmExportFileFile.  # noqa: E501


        :return: The md5 of this VmExportFileFile.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this VmExportFileFile.


        :param md5: The md5 of this VmExportFileFile.  # noqa: E501
        :type md5: str
        """
        if self.local_vars_configuration.client_side_validation and md5 is None:  # noqa: E501
            raise ValueError("Invalid value for `md5`, must not be `None`")  # noqa: E501

        self._md5 = md5

    @property
    def file_size(self):
        """Gets the file_size of this VmExportFileFile.  # noqa: E501


        :return: The file_size of this VmExportFileFile.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this VmExportFileFile.


        :param file_size: The file_size of this VmExportFileFile.  # noqa: E501
        :type file_size: int
        """
        if self.local_vars_configuration.client_side_validation and file_size is None:  # noqa: E501
            raise ValueError("Invalid value for `file_size`, must not be `None`")  # noqa: E501

        self._file_size = file_size

    @property
    def file_secret(self):
        """Gets the file_secret of this VmExportFileFile.  # noqa: E501


        :return: The file_secret of this VmExportFileFile.  # noqa: E501
        :rtype: str
        """
        return self._file_secret

    @file_secret.setter
    def file_secret(self, file_secret):
        """Sets the file_secret of this VmExportFileFile.


        :param file_secret: The file_secret of this VmExportFileFile.  # noqa: E501
        :type file_secret: str
        """
        if self.local_vars_configuration.client_side_validation and file_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `file_secret`, must not be `None`")  # noqa: E501

        self._file_secret = file_secret

    @property
    def file_uuid(self):
        """Gets the file_uuid of this VmExportFileFile.  # noqa: E501


        :return: The file_uuid of this VmExportFileFile.  # noqa: E501
        :rtype: str
        """
        return self._file_uuid

    @file_uuid.setter
    def file_uuid(self, file_uuid):
        """Sets the file_uuid of this VmExportFileFile.


        :param file_uuid: The file_uuid of this VmExportFileFile.  # noqa: E501
        :type file_uuid: str
        """
        if self.local_vars_configuration.client_side_validation and file_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `file_uuid`, must not be `None`")  # noqa: E501

        self._file_uuid = file_uuid

    @property
    def type(self):
        """Gets the type of this VmExportFileFile.  # noqa: E501


        :return: The type of this VmExportFileFile.  # noqa: E501
        :rtype: VmExportFileType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VmExportFileFile.


        :param type: The type of this VmExportFileFile.  # noqa: E501
        :type type: VmExportFileType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def file_name(self):
        """Gets the file_name of this VmExportFileFile.  # noqa: E501


        :return: The file_name of this VmExportFileFile.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this VmExportFileFile.


        :param file_name: The file_name of this VmExportFileFile.  # noqa: E501
        :type file_name: str
        """
        if self.local_vars_configuration.client_side_validation and file_name is None:  # noqa: E501
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

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
        if not isinstance(other, VmExportFileFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmExportFileFile):
            return True

        return self.to_dict() != other.to_dict()
