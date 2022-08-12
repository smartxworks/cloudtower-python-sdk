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


class NfsInodeOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ASSIGNED_SIZE_ASC = "assigned_size_ASC"
    ASSIGNED_SIZE_DESC = "assigned_size_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    FILE_ASC = "file_ASC"
    FILE_DESC = "file_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    LOCAL_UPDATED_AT_ASC = "local_updated_at_ASC"
    LOCAL_UPDATED_AT_DESC = "local_updated_at_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    PARENT_ID_ASC = "parent_id_ASC"
    PARENT_ID_DESC = "parent_id_DESC"
    SHARED_SIZE_ASC = "shared_size_ASC"
    SHARED_SIZE_DESC = "shared_size_DESC"
    SNAPSHOT_NUM_ASC = "snapshot_num_ASC"
    SNAPSHOT_NUM_DESC = "snapshot_num_DESC"
    UNIQUE_SIZE_ASC = "unique_size_ASC"
    UNIQUE_SIZE_DESC = "unique_size_DESC"

    allowable_values = [ASSIGNED_SIZE_ASC, ASSIGNED_SIZE_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, FILE_ASC, FILE_DESC, ID_ASC, ID_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, LOCAL_UPDATED_AT_ASC, LOCAL_UPDATED_AT_DESC, NAME_ASC, NAME_DESC, PARENT_ID_ASC, PARENT_ID_DESC, SHARED_SIZE_ASC, SHARED_SIZE_DESC, SNAPSHOT_NUM_ASC, SNAPSHOT_NUM_DESC, UNIQUE_SIZE_ASC, UNIQUE_SIZE_DESC]  # noqa: E501

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
        """NfsInodeOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, NfsInodeOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NfsInodeOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
