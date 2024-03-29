# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class GraphOrderByInput(object):
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
    METRIC_COUNT_ASC = "metric_count_ASC"
    METRIC_COUNT_DESC = "metric_count_DESC"
    METRIC_NAME_ASC = "metric_name_ASC"
    METRIC_NAME_DESC = "metric_name_DESC"
    METRIC_TYPE_ASC = "metric_type_ASC"
    METRIC_TYPE_DESC = "metric_type_DESC"
    NETWORK_ASC = "network_ASC"
    NETWORK_DESC = "network_DESC"
    RESOURCE_TYPE_ASC = "resource_type_ASC"
    RESOURCE_TYPE_DESC = "resource_type_DESC"
    SERVICE_ASC = "service_ASC"
    SERVICE_DESC = "service_DESC"
    TARGETS_ASC = "targets_ASC"
    TARGETS_DESC = "targets_DESC"
    TITLE_ASC = "title_ASC"
    TITLE_DESC = "title_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"

    allowable_values = [ENTITYASYNCSTATUS_ASC, ENTITYASYNCSTATUS_DESC, ID_ASC, ID_DESC, LOCAL_ID_ASC, LOCAL_ID_DESC, METRIC_COUNT_ASC, METRIC_COUNT_DESC, METRIC_NAME_ASC, METRIC_NAME_DESC, METRIC_TYPE_ASC, METRIC_TYPE_DESC, NETWORK_ASC, NETWORK_DESC, RESOURCE_TYPE_ASC, RESOURCE_TYPE_DESC, SERVICE_ASC, SERVICE_DESC, TARGETS_ASC, TARGETS_DESC, TITLE_ASC, TITLE_DESC, TYPE_ASC, TYPE_DESC]  # noqa: E501

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
        """GraphOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, GraphOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GraphOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
