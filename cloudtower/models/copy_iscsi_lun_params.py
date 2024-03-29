# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class CopyIscsiLunParams(object):
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
        'dest_iscsi_target_id': 'str',
        'name': 'str',
        'src_lun_id': 'str'
    }

    attribute_map = {
        'dest_iscsi_target_id': 'dest_iscsi_target_id',
        'name': 'name',
        'src_lun_id': 'src_lun_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CopyIscsiLunParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._dest_iscsi_target_id = None
        self._name = None
        self._src_lun_id = None
        self.discriminator = None

        if "dest_iscsi_target_id" in kwargs:
            self.dest_iscsi_target_id = kwargs["dest_iscsi_target_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "src_lun_id" in kwargs:
            self.src_lun_id = kwargs["src_lun_id"]

    @property
    def dest_iscsi_target_id(self):
        """Gets the dest_iscsi_target_id of this CopyIscsiLunParams.  # noqa: E501


        :return: The dest_iscsi_target_id of this CopyIscsiLunParams.  # noqa: E501
        :rtype: str
        """
        return self._dest_iscsi_target_id

    @dest_iscsi_target_id.setter
    def dest_iscsi_target_id(self, dest_iscsi_target_id):
        """Sets the dest_iscsi_target_id of this CopyIscsiLunParams.


        :param dest_iscsi_target_id: The dest_iscsi_target_id of this CopyIscsiLunParams.  # noqa: E501
        :type dest_iscsi_target_id: str
        """

        self._dest_iscsi_target_id = dest_iscsi_target_id

    @property
    def name(self):
        """Gets the name of this CopyIscsiLunParams.  # noqa: E501


        :return: The name of this CopyIscsiLunParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CopyIscsiLunParams.


        :param name: The name of this CopyIscsiLunParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def src_lun_id(self):
        """Gets the src_lun_id of this CopyIscsiLunParams.  # noqa: E501


        :return: The src_lun_id of this CopyIscsiLunParams.  # noqa: E501
        :rtype: str
        """
        return self._src_lun_id

    @src_lun_id.setter
    def src_lun_id(self, src_lun_id):
        """Sets the src_lun_id of this CopyIscsiLunParams.


        :param src_lun_id: The src_lun_id of this CopyIscsiLunParams.  # noqa: E501
        :type src_lun_id: str
        """
        if self.local_vars_configuration.client_side_validation and src_lun_id is None:  # noqa: E501
            raise ValueError("Invalid value for `src_lun_id`, must not be `None`")  # noqa: E501

        self._src_lun_id = src_lun_id

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
        if not isinstance(other, CopyIscsiLunParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CopyIscsiLunParams):
            return True

        return self.to_dict() != other.to_dict()
