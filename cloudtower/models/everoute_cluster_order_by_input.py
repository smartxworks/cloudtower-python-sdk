# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.10.0
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


class EverouteClusterOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CONTROLLER_INSTANCES_ASC = "controller_instances_ASC"
    CONTROLLER_INSTANCES_DESC = "controller_instances_DESC"
    CONTROLLER_TEMPLATE_ASC = "controller_template_ASC"
    CONTROLLER_TEMPLATE_DESC = "controller_template_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    GLOBAL_DEFAULT_ACTION_ASC = "global_default_action_ASC"
    GLOBAL_DEFAULT_ACTION_DESC = "global_default_action_DESC"
    GLOBAL_WHITELIST_ASC = "global_whitelist_ASC"
    GLOBAL_WHITELIST_DESC = "global_whitelist_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    INSTALLED_ASC = "installed_ASC"
    INSTALLED_DESC = "installed_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    PHASE_ASC = "phase_ASC"
    PHASE_DESC = "phase_DESC"
    STATUS_ASC = "status_ASC"
    STATUS_DESC = "status_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"
    VERSION_ASC = "version_ASC"
    VERSION_DESC = "version_DESC"

    allowable_values = [CONTROLLER_INSTANCES_ASC, CONTROLLER_INSTANCES_DESC, CONTROLLER_TEMPLATE_ASC, CONTROLLER_TEMPLATE_DESC, CREATEDAT_ASC, CREATEDAT_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, GLOBAL_DEFAULT_ACTION_ASC, GLOBAL_DEFAULT_ACTION_DESC, GLOBAL_WHITELIST_ASC, GLOBAL_WHITELIST_DESC, ID_ASC, ID_DESC, INSTALLED_ASC, INSTALLED_DESC, NAME_ASC, NAME_DESC, PHASE_ASC, PHASE_DESC, STATUS_ASC, STATUS_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC, VERSION_ASC, VERSION_DESC]  # noqa: E501

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
        """EverouteClusterOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, EverouteClusterOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EverouteClusterOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
