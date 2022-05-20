# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class SnapshotGroupOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DELETED_ASC = "deleted_ASC"
    DELETED_DESC = "deleted_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    ESTIMATED_RECYCLING_TIME_ASC = "estimated_recycling_time_ASC"
    ESTIMATED_RECYCLING_TIME_DESC = "estimated_recycling_time_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    INTERNAL_ASC = "internal_ASC"
    INTERNAL_DESC = "internal_DESC"
    KEEP_ASC = "keep_ASC"
    KEEP_DESC = "keep_DESC"
    LOCAL_CREATED_AT_ASC = "local_created_at_ASC"
    LOCAL_CREATED_AT_DESC = "local_created_at_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    LOGICAL_SIZE_BYTES_ASC = "logical_size_bytes_ASC"
    LOGICAL_SIZE_BYTES_DESC = "logical_size_bytes_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    OBJECT_NUM_ASC = "object_num_ASC"
    OBJECT_NUM_DESC = "object_num_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"
    VM_INFO_ASC = "vm_info_ASC"
    VM_INFO_DESC = "vm_info_DESC"

    allowable_values = [CREATEDAT_ASC, CREATEDAT_DESC, DELETED_ASC, DELETED_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, ESTIMATED_RECYCLING_TIME_ASC, ESTIMATED_RECYCLING_TIME_DESC, ID_ASC, ID_DESC, INTERNAL_ASC, INTERNAL_DESC, KEEP_ASC, KEEP_DESC, LOCAL_CREATED_AT_ASC, LOCAL_CREATED_AT_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, LOGICAL_SIZE_BYTES_ASC, LOGICAL_SIZE_BYTES_DESC, NAME_ASC, NAME_DESC, OBJECT_NUM_ASC, OBJECT_NUM_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC, VM_INFO_ASC, VM_INFO_DESC]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SnapshotGroupOrderByInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())
        self.discriminator = None

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
        if not isinstance(other, SnapshotGroupOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotGroupOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
