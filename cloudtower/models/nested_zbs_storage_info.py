# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedZbsStorageInfo(object):
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
        'cluster_id': 'str',
        'snapshot_info': 'list[NestedSnapshotInfo]'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'snapshot_info': 'snapshot_info'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedZbsStorageInfo - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster_id = None
        self._snapshot_info = None
        self.discriminator = None

        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        self.snapshot_info = kwargs.get("snapshot_info", None)

    @property
    def cluster_id(self):
        """Gets the cluster_id of this NestedZbsStorageInfo.  # noqa: E501


        :return: The cluster_id of this NestedZbsStorageInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this NestedZbsStorageInfo.


        :param cluster_id: The cluster_id of this NestedZbsStorageInfo.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def snapshot_info(self):
        """Gets the snapshot_info of this NestedZbsStorageInfo.  # noqa: E501


        :return: The snapshot_info of this NestedZbsStorageInfo.  # noqa: E501
        :rtype: list[NestedSnapshotInfo]
        """
        return self._snapshot_info

    @snapshot_info.setter
    def snapshot_info(self, snapshot_info):
        """Sets the snapshot_info of this NestedZbsStorageInfo.


        :param snapshot_info: The snapshot_info of this NestedZbsStorageInfo.  # noqa: E501
        :type snapshot_info: list[NestedSnapshotInfo]
        """

        self._snapshot_info = snapshot_info

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
        if not isinstance(other, NestedZbsStorageInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedZbsStorageInfo):
            return True

        return self.to_dict() != other.to_dict()
