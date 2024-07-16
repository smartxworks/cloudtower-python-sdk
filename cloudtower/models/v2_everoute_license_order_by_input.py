# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class V2EverouteLicenseOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CODE_ASC = "code_ASC"
    CODE_DESC = "code_DESC"
    EXPIRE_DATE_ASC = "expire_date_ASC"
    EXPIRE_DATE_DESC = "expire_date_DESC"
    FEATURE_TYPE_ASC = "feature_type_ASC"
    FEATURE_TYPE_DESC = "feature_type_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    MAX_SOCKET_NUM_ASC = "max_socket_num_ASC"
    MAX_SOCKET_NUM_DESC = "max_socket_num_DESC"
    MAX_VCPU_NUM_ASC = "max_vcpu_num_ASC"
    MAX_VCPU_NUM_DESC = "max_vcpu_num_DESC"
    MAX_VM_NUM_ASC = "max_vm_num_ASC"
    MAX_VM_NUM_DESC = "max_vm_num_DESC"
    MAX_VPC_SOCKET_NUM_ASC = "max_vpc_socket_num_ASC"
    MAX_VPC_SOCKET_NUM_DESC = "max_vpc_socket_num_DESC"
    PRICING_TYPE_ASC = "pricing_type_ASC"
    PRICING_TYPE_DESC = "pricing_type_DESC"
    SERIAL_ASC = "serial_ASC"
    SERIAL_DESC = "serial_DESC"
    SIGN_DATE_ASC = "sign_date_ASC"
    SIGN_DATE_DESC = "sign_date_DESC"
    SOFTWARE_EDITION_ASC = "software_edition_ASC"
    SOFTWARE_EDITION_DESC = "software_edition_DESC"
    TYPE_ASC = "type_ASC"
    TYPE_DESC = "type_DESC"
    UID_ASC = "uid_ASC"
    UID_DESC = "uid_DESC"
    VERSION_ASC = "version_ASC"
    VERSION_DESC = "version_DESC"

    allowable_values = [CODE_ASC, CODE_DESC, EXPIRE_DATE_ASC, EXPIRE_DATE_DESC, FEATURE_TYPE_ASC, FEATURE_TYPE_DESC, ID_ASC, ID_DESC, MAX_SOCKET_NUM_ASC, MAX_SOCKET_NUM_DESC, MAX_VCPU_NUM_ASC, MAX_VCPU_NUM_DESC, MAX_VM_NUM_ASC, MAX_VM_NUM_DESC, MAX_VPC_SOCKET_NUM_ASC, MAX_VPC_SOCKET_NUM_DESC, PRICING_TYPE_ASC, PRICING_TYPE_DESC, SERIAL_ASC, SERIAL_DESC, SIGN_DATE_ASC, SIGN_DATE_DESC, SOFTWARE_EDITION_ASC, SOFTWARE_EDITION_DESC, TYPE_ASC, TYPE_DESC, UID_ASC, UID_DESC, VERSION_ASC, VERSION_DESC]  # noqa: E501

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
        """V2EverouteLicenseOrderByInput - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, V2EverouteLicenseOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2EverouteLicenseOrderByInput):
            return True

        return self.to_dict() != other.to_dict()