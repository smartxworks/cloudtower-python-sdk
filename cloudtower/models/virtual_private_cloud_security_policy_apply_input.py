# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloudSecurityPolicyApplyInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'security_group_id': 'str',
        'communicable': 'bool'
    }

    attribute_map = {
        'security_group_id': 'security_group_id',
        'communicable': 'communicable'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloudSecurityPolicyApplyInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._security_group_id = None
        self._communicable = None
        self.discriminator = None

        if "security_group_id" in kwargs:
            self.security_group_id = kwargs["security_group_id"]
        if "communicable" in kwargs:
            self.communicable = kwargs["communicable"]

    @property
    def security_group_id(self):
        """Gets the security_group_id of this VirtualPrivateCloudSecurityPolicyApplyInput.  # noqa: E501


        :return: The security_group_id of this VirtualPrivateCloudSecurityPolicyApplyInput.  # noqa: E501
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this VirtualPrivateCloudSecurityPolicyApplyInput.


        :param security_group_id: The security_group_id of this VirtualPrivateCloudSecurityPolicyApplyInput.  # noqa: E501
        :type security_group_id: str
        """
        if self.local_vars_configuration.client_side_validation and security_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `security_group_id`, must not be `None`")  # noqa: E501

        self._security_group_id = security_group_id

    @property
    def communicable(self):
        """Gets the communicable of this VirtualPrivateCloudSecurityPolicyApplyInput.  # noqa: E501


        :return: The communicable of this VirtualPrivateCloudSecurityPolicyApplyInput.  # noqa: E501
        :rtype: bool
        """
        return self._communicable

    @communicable.setter
    def communicable(self, communicable):
        """Sets the communicable of this VirtualPrivateCloudSecurityPolicyApplyInput.


        :param communicable: The communicable of this VirtualPrivateCloudSecurityPolicyApplyInput.  # noqa: E501
        :type communicable: bool
        """
        if self.local_vars_configuration.client_side_validation and communicable is None:  # noqa: E501
            raise ValueError("Invalid value for `communicable`, must not be `None`")  # noqa: E501

        self._communicable = communicable

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
        if not isinstance(other, VirtualPrivateCloudSecurityPolicyApplyInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloudSecurityPolicyApplyInput):
            return True

        return self.to_dict() != other.to_dict()
