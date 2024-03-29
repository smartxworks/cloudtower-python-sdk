# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ClusterImageOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    META_NAME_ASC = "meta_name_ASC"
    META_NAME_DESC = "meta_name_DESC"
    META_SIZE_ASC = "meta_size_ASC"
    META_SIZE_DESC = "meta_size_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    SIZE_ASC = "size_ASC"
    SIZE_DESC = "size_DESC"
    UPGRADE_TOOL_VERSION_ASC = "upgrade_tool_version_ASC"
    UPGRADE_TOOL_VERSION_DESC = "upgrade_tool_version_DESC"
    VERSION_ASC = "version_ASC"
    VERSION_DESC = "version_DESC"
    ZBS_VERSION_ASC = "zbs_version_ASC"
    ZBS_VERSION_DESC = "zbs_version_DESC"

    allowable_values = [ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, ID_ASC, ID_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, META_NAME_ASC, META_NAME_DESC, META_SIZE_ASC, META_SIZE_DESC, NAME_ASC, NAME_DESC, SIZE_ASC, SIZE_DESC, UPGRADE_TOOL_VERSION_ASC, UPGRADE_TOOL_VERSION_DESC, VERSION_ASC, VERSION_DESC, ZBS_VERSION_ASC, ZBS_VERSION_DESC]  # noqa: E501

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
        """ClusterImageOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, ClusterImageOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterImageOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
