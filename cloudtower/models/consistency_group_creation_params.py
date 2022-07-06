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


class ConsistencyGroupCreationParams(object):
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
        'namespaces_ids': 'list[str]',
        'iscsi_luns_ids': 'list[str]',
        'description': 'str',
        'cluster_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'namespaces_ids': 'namespaces_ids',
        'iscsi_luns_ids': 'iscsi_luns_ids',
        'description': 'description',
        'cluster_id': 'cluster_id',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ConsistencyGroupCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._namespaces_ids = None
        self._iscsi_luns_ids = None
        self._description = None
        self._cluster_id = None
        self._name = None
        self.discriminator = None

        if "namespaces_ids" in kwargs:
            self.namespaces_ids = kwargs["namespaces_ids"]
        if "iscsi_luns_ids" in kwargs:
            self.iscsi_luns_ids = kwargs["iscsi_luns_ids"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def namespaces_ids(self):
        """Gets the namespaces_ids of this ConsistencyGroupCreationParams.  # noqa: E501


        :return: The namespaces_ids of this ConsistencyGroupCreationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces_ids

    @namespaces_ids.setter
    def namespaces_ids(self, namespaces_ids):
        """Sets the namespaces_ids of this ConsistencyGroupCreationParams.


        :param namespaces_ids: The namespaces_ids of this ConsistencyGroupCreationParams.  # noqa: E501
        :type namespaces_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and namespaces_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `namespaces_ids`, must not be `None`")  # noqa: E501

        self._namespaces_ids = namespaces_ids

    @property
    def iscsi_luns_ids(self):
        """Gets the iscsi_luns_ids of this ConsistencyGroupCreationParams.  # noqa: E501


        :return: The iscsi_luns_ids of this ConsistencyGroupCreationParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._iscsi_luns_ids

    @iscsi_luns_ids.setter
    def iscsi_luns_ids(self, iscsi_luns_ids):
        """Sets the iscsi_luns_ids of this ConsistencyGroupCreationParams.


        :param iscsi_luns_ids: The iscsi_luns_ids of this ConsistencyGroupCreationParams.  # noqa: E501
        :type iscsi_luns_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and iscsi_luns_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `iscsi_luns_ids`, must not be `None`")  # noqa: E501

        self._iscsi_luns_ids = iscsi_luns_ids

    @property
    def description(self):
        """Gets the description of this ConsistencyGroupCreationParams.  # noqa: E501


        :return: The description of this ConsistencyGroupCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConsistencyGroupCreationParams.


        :param description: The description of this ConsistencyGroupCreationParams.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ConsistencyGroupCreationParams.  # noqa: E501


        :return: The cluster_id of this ConsistencyGroupCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ConsistencyGroupCreationParams.


        :param cluster_id: The cluster_id of this ConsistencyGroupCreationParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this ConsistencyGroupCreationParams.  # noqa: E501


        :return: The name of this ConsistencyGroupCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConsistencyGroupCreationParams.


        :param name: The name of this ConsistencyGroupCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, ConsistencyGroupCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsistencyGroupCreationParams):
            return True

        return self.to_dict() != other.to_dict()
