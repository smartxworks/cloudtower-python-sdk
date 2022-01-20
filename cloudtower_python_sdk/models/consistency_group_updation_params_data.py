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


class ConsistencyGroupUpdationParamsData(object):
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
        'remain_volume_snapshot': 'bool',
        'namespaces_ids': 'list[str]',
        'iscsi_luns_ids': 'list[str]',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'remain_volume_snapshot': 'remain_volume_snapshot',
        'namespaces_ids': 'namespaces_ids',
        'iscsi_luns_ids': 'iscsi_luns_ids',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, remain_volume_snapshot=None, namespaces_ids=None, iscsi_luns_ids=None, description=None, name=None, local_vars_configuration=None):  # noqa: E501
        """ConsistencyGroupUpdationParamsData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._remain_volume_snapshot = None
        self._namespaces_ids = None
        self._iscsi_luns_ids = None
        self._description = None
        self._name = None
        self.discriminator = None

        if remain_volume_snapshot is not None:
            self.remain_volume_snapshot = remain_volume_snapshot
        if namespaces_ids is not None:
            self.namespaces_ids = namespaces_ids
        if iscsi_luns_ids is not None:
            self.iscsi_luns_ids = iscsi_luns_ids
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name

    @property
    def remain_volume_snapshot(self):
        """Gets the remain_volume_snapshot of this ConsistencyGroupUpdationParamsData.  # noqa: E501


        :return: The remain_volume_snapshot of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._remain_volume_snapshot

    @remain_volume_snapshot.setter
    def remain_volume_snapshot(self, remain_volume_snapshot):
        """Sets the remain_volume_snapshot of this ConsistencyGroupUpdationParamsData.


        :param remain_volume_snapshot: The remain_volume_snapshot of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :type remain_volume_snapshot: bool
        """

        self._remain_volume_snapshot = remain_volume_snapshot

    @property
    def namespaces_ids(self):
        """Gets the namespaces_ids of this ConsistencyGroupUpdationParamsData.  # noqa: E501


        :return: The namespaces_ids of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces_ids

    @namespaces_ids.setter
    def namespaces_ids(self, namespaces_ids):
        """Sets the namespaces_ids of this ConsistencyGroupUpdationParamsData.


        :param namespaces_ids: The namespaces_ids of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :type namespaces_ids: list[str]
        """

        self._namespaces_ids = namespaces_ids

    @property
    def iscsi_luns_ids(self):
        """Gets the iscsi_luns_ids of this ConsistencyGroupUpdationParamsData.  # noqa: E501


        :return: The iscsi_luns_ids of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._iscsi_luns_ids

    @iscsi_luns_ids.setter
    def iscsi_luns_ids(self, iscsi_luns_ids):
        """Sets the iscsi_luns_ids of this ConsistencyGroupUpdationParamsData.


        :param iscsi_luns_ids: The iscsi_luns_ids of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :type iscsi_luns_ids: list[str]
        """

        self._iscsi_luns_ids = iscsi_luns_ids

    @property
    def description(self):
        """Gets the description of this ConsistencyGroupUpdationParamsData.  # noqa: E501


        :return: The description of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConsistencyGroupUpdationParamsData.


        :param description: The description of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ConsistencyGroupUpdationParamsData.  # noqa: E501


        :return: The name of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConsistencyGroupUpdationParamsData.


        :param name: The name of this ConsistencyGroupUpdationParamsData.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, ConsistencyGroupUpdationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsistencyGroupUpdationParamsData):
            return True

        return self.to_dict() != other.to_dict()
