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


class EntityFilterOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    APPLY_TO_ALL_CLUSTERS_ASC = "apply_to_all_clusters_ASC"
    APPLY_TO_ALL_CLUSTERS_DESC = "apply_to_all_clusters_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    ENTITY_TYPE_ASC = "entity_type_ASC"
    ENTITY_TYPE_DESC = "entity_type_DESC"
    FILTER_STATUS_ASC = "filter_status_ASC"
    FILTER_STATUS_DESC = "filter_status_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    LAST_EXECUTED_AT_ASC = "last_executed_at_ASC"
    LAST_EXECUTED_AT_DESC = "last_executed_at_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    PRESET_ASC = "preset_ASC"
    PRESET_DESC = "preset_DESC"
    RULES_ASC = "rules_ASC"
    RULES_DESC = "rules_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"

    allowable_values = [APPLY_TO_ALL_CLUSTERS_ASC, APPLY_TO_ALL_CLUSTERS_DESC, CREATEDAT_ASC, CREATEDAT_DESC, ENTITY_TYPE_ASC, ENTITY_TYPE_DESC, FILTER_STATUS_ASC, FILTER_STATUS_DESC, ID_ASC, ID_DESC, LAST_EXECUTED_AT_ASC, LAST_EXECUTED_AT_DESC, NAME_ASC, NAME_DESC, PRESET_ASC, PRESET_DESC, RULES_ASC, RULES_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC]  # noqa: E501

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

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """EntityFilterOrderByInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
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
        if not isinstance(other, EntityFilterOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityFilterOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
