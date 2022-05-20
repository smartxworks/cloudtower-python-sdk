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


class ElfDataStoreOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DESCRIPTION_ASC = "description_ASC"
    DESCRIPTION_DESC = "description_DESC"
    EXTERNAL_USE_ASC = "external_use_ASC"
    EXTERNAL_USE_DESC = "external_use_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    INTERNAL_ASC = "internal_ASC"
    INTERNAL_DESC = "internal_DESC"
    IP_WHITELIST_ASC = "ip_whitelist_ASC"
    IP_WHITELIST_DESC = "ip_whitelist_DESC"
    LOCAL_ID_ASC = "local_id_ASC"
    LOCAL_ID_DESC = "local_id_DESC"
    NAME_ASC = "name_ASC"
    NAME_DESC = "name_DESC"
    REPLICA_NUM_ASC = "replica_num_ASC"
    REPLICA_NUM_DESC = "replica_num_DESC"
    THIN_PROVISION_ASC = "thin_provision_ASC"
    THIN_PROVISION_DESC = "thin_provision_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"

    allowable_values = [CREATEDAT_ASC, CREATEDAT_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, EXTERNAL_USE_ASC, EXTERNAL_USE_DESC, ID_ASC, ID_DESC, INTERNAL_ASC, INTERNAL_DESC, IP_WHITELIST_ASC, IP_WHITELIST_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, NAME_ASC, NAME_DESC, REPLICA_NUM_ASC, REPLICA_NUM_DESC, THIN_PROVISION_ASC, THIN_PROVISION_DESC, TYPE_ASC, TYPE_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC]  # noqa: E501

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
        """ElfDataStoreOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, ElfDataStoreOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElfDataStoreOrderByInput):
            return True

        return self.to_dict() != other.to_dict()