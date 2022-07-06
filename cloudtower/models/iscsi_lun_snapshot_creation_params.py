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


class IscsiLunSnapshotCreationParams(object):
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
        'iscsi_target_id': 'str',
        'name': 'str',
        'iscsi_lun_id': 'str'
    }

    attribute_map = {
        'iscsi_target_id': 'iscsi_target_id',
        'name': 'name',
        'iscsi_lun_id': 'iscsi_lun_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IscsiLunSnapshotCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._iscsi_target_id = None
        self._name = None
        self._iscsi_lun_id = None
        self.discriminator = None

        if "iscsi_target_id" in kwargs:
            self.iscsi_target_id = kwargs["iscsi_target_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "iscsi_lun_id" in kwargs:
            self.iscsi_lun_id = kwargs["iscsi_lun_id"]

    @property
    def iscsi_target_id(self):
        """Gets the iscsi_target_id of this IscsiLunSnapshotCreationParams.  # noqa: E501


        :return: The iscsi_target_id of this IscsiLunSnapshotCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_target_id

    @iscsi_target_id.setter
    def iscsi_target_id(self, iscsi_target_id):
        """Sets the iscsi_target_id of this IscsiLunSnapshotCreationParams.


        :param iscsi_target_id: The iscsi_target_id of this IscsiLunSnapshotCreationParams.  # noqa: E501
        :type iscsi_target_id: str
        """
        if self.local_vars_configuration.client_side_validation and iscsi_target_id is None:  # noqa: E501
            raise ValueError("Invalid value for `iscsi_target_id`, must not be `None`")  # noqa: E501

        self._iscsi_target_id = iscsi_target_id

    @property
    def name(self):
        """Gets the name of this IscsiLunSnapshotCreationParams.  # noqa: E501


        :return: The name of this IscsiLunSnapshotCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IscsiLunSnapshotCreationParams.


        :param name: The name of this IscsiLunSnapshotCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def iscsi_lun_id(self):
        """Gets the iscsi_lun_id of this IscsiLunSnapshotCreationParams.  # noqa: E501


        :return: The iscsi_lun_id of this IscsiLunSnapshotCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._iscsi_lun_id

    @iscsi_lun_id.setter
    def iscsi_lun_id(self, iscsi_lun_id):
        """Sets the iscsi_lun_id of this IscsiLunSnapshotCreationParams.


        :param iscsi_lun_id: The iscsi_lun_id of this IscsiLunSnapshotCreationParams.  # noqa: E501
        :type iscsi_lun_id: str
        """
        if self.local_vars_configuration.client_side_validation and iscsi_lun_id is None:  # noqa: E501
            raise ValueError("Invalid value for `iscsi_lun_id`, must not be `None`")  # noqa: E501

        self._iscsi_lun_id = iscsi_lun_id

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
        if not isinstance(other, IscsiLunSnapshotCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IscsiLunSnapshotCreationParams):
            return True

        return self.to_dict() != other.to_dict()
