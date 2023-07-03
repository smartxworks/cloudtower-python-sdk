# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmExportFileOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DAMAGED_ASC = "damaged_ASC"
    DAMAGED_DESC = "damaged_DESC"
    DATA_PORT_ID_ASC = "data_port_id_ASC"
    DATA_PORT_ID_DESC = "data_port_id_DESC"
    ENTITYASYNCSTATUS_ASC = "entityAsyncStatus_ASC"
    ENTITYASYNCSTATUS_DESC = "entityAsyncStatus_DESC"
    FILES_ASC = "files_ASC"
    FILES_DESC = "files_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    STORAGE_CLUSTER_ID_ASC = "storage_cluster_id_ASC"
    STORAGE_CLUSTER_ID_DESC = "storage_cluster_id_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"

    allowable_values = [CREATEDAT_ASC, CREATEDAT_DESC, DAMAGED_ASC, DAMAGED_DESC, DATA_PORT_ID_ASC, DATA_PORT_ID_DESC, ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, FILES_ASC, FILES_DESC, ID_ASC, ID_DESC, STORAGE_CLUSTER_ID_ASC, STORAGE_CLUSTER_ID_DESC, TYPE_ASC, TYPE_DESC]  # noqa: E501

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
        """VmExportFileOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, VmExportFileOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmExportFileOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
