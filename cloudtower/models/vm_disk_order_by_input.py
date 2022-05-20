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


class VmDiskOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    BOOT_ASC = "boot_ASC"
    BOOT_DESC = "boot_DESC"
    BUS_ASC = "bus_ASC"
    BUS_DESC = "bus_DESC"
    CLOUD_INIT_IMAGE_NAME_ASC = "cloud_init_image_name_ASC"
    CLOUD_INIT_IMAGE_NAME_DESC = "cloud_init_image_name_DESC"
    CLOUD_INIT_IMAGE_PATH_ASC = "cloud_init_image_path_ASC"
    CLOUD_INIT_IMAGE_PATH_DESC = "cloud_init_image_path_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DEVICE_ASC = "device_ASC"
    DEVICE_DESC = "device_DESC"
    DISABLED_ASC = "disabled_ASC"
    DISABLED_DESC = "disabled_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    KEY_ASC = "key_ASC"
    KEY_DESC = "key_DESC"
    MAX_BANDWIDTH_ASC = "max_bandwidth_ASC"
    MAX_BANDWIDTH_DESC = "max_bandwidth_DESC"
    MAX_BANDWIDTH_POLICY_ASC = "max_bandwidth_policy_ASC"
    MAX_BANDWIDTH_POLICY_DESC = "max_bandwidth_policy_DESC"
    MAX_IOPS_ASC = "max_iops_ASC"
    MAX_IOPS_DESC = "max_iops_DESC"
    MAX_IOPS_POLICY_ASC = "max_iops_policy_ASC"
    MAX_IOPS_POLICY_DESC = "max_iops_policy_DESC"
    SERIAL_ASC = "serial_ASC"
    SERIAL_DESC = "serial_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"
    UNSAFE_IMAGE_PATH_ASC = "unsafe_image_path_ASC"
    UNSAFE_IMAGE_PATH_DESC = "unsafe_image_path_DESC"
    UNSAFE_IMAGE_UUID_ASC = "unsafe_image_uuid_ASC"
    UNSAFE_IMAGE_UUID_DESC = "unsafe_image_uuid_DESC"
    UNSAFE_PROVISION_ASC = "unsafe_provision_ASC"
    UNSAFE_PROVISION_DESC = "unsafe_provision_DESC"
    UPDATEDAT_ASC = "updatedAt_ASC"
    UPDATEDAT_DESC = "updatedAt_DESC"

    allowable_values = [BOOT_ASC, BOOT_DESC, BUS_ASC, BUS_DESC, CLOUD_INIT_IMAGE_NAME_ASC, CLOUD_INIT_IMAGE_NAME_DESC, CLOUD_INIT_IMAGE_PATH_ASC, CLOUD_INIT_IMAGE_PATH_DESC, CREATEDAT_ASC, CREATEDAT_DESC, DEVICE_ASC, DEVICE_DESC, DISABLED_ASC, DISABLED_DESC, ID_ASC, ID_DESC, KEY_ASC, KEY_DESC, MAX_BANDWIDTH_ASC, MAX_BANDWIDTH_DESC, MAX_BANDWIDTH_POLICY_ASC, MAX_BANDWIDTH_POLICY_DESC, MAX_IOPS_ASC, MAX_IOPS_DESC, MAX_IOPS_POLICY_ASC, MAX_IOPS_POLICY_DESC, SERIAL_ASC, SERIAL_DESC, TYPE_ASC, TYPE_DESC, UNSAFE_IMAGE_PATH_ASC, UNSAFE_IMAGE_PATH_DESC, UNSAFE_IMAGE_UUID_ASC, UNSAFE_IMAGE_UUID_DESC, UNSAFE_PROVISION_ASC, UNSAFE_PROVISION_DESC, UPDATEDAT_ASC, UPDATEDAT_DESC]  # noqa: E501

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
        """VmDiskOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, VmDiskOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmDiskOrderByInput):
            return True

        return self.to_dict() != other.to_dict()