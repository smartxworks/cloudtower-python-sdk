# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloudSecurityPolicyUpdateParams(object):
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
        'ingress': 'list[VirtualPrivateCloudNetworkPolicyRuleInput]',
        'egress': 'list[VirtualPrivateCloudNetworkPolicyRuleInput]',
        'apply_to': 'list[VirtualPrivateCloudSecurityPolicyApplyInput]',
        'policy_mode': 'VirtualPrivateCloudSecurityPolicyMode',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'ingress': 'ingress',
        'egress': 'egress',
        'apply_to': 'apply_to',
        'policy_mode': 'policy_mode',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloudSecurityPolicyUpdateParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._ingress = None
        self._egress = None
        self._apply_to = None
        self._policy_mode = None
        self._description = None
        self._name = None
        self.discriminator = None

        if "ingress" in kwargs:
            self.ingress = kwargs["ingress"]
        if "egress" in kwargs:
            self.egress = kwargs["egress"]
        if "apply_to" in kwargs:
            self.apply_to = kwargs["apply_to"]
        if "policy_mode" in kwargs:
            self.policy_mode = kwargs["policy_mode"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def ingress(self):
        """Gets the ingress of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501


        :return: The ingress of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :rtype: list[VirtualPrivateCloudNetworkPolicyRuleInput]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """Sets the ingress of this VirtualPrivateCloudSecurityPolicyUpdateParams.


        :param ingress: The ingress of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :type ingress: list[VirtualPrivateCloudNetworkPolicyRuleInput]
        """

        self._ingress = ingress

    @property
    def egress(self):
        """Gets the egress of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501


        :return: The egress of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :rtype: list[VirtualPrivateCloudNetworkPolicyRuleInput]
        """
        return self._egress

    @egress.setter
    def egress(self, egress):
        """Sets the egress of this VirtualPrivateCloudSecurityPolicyUpdateParams.


        :param egress: The egress of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :type egress: list[VirtualPrivateCloudNetworkPolicyRuleInput]
        """

        self._egress = egress

    @property
    def apply_to(self):
        """Gets the apply_to of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501


        :return: The apply_to of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :rtype: list[VirtualPrivateCloudSecurityPolicyApplyInput]
        """
        return self._apply_to

    @apply_to.setter
    def apply_to(self, apply_to):
        """Sets the apply_to of this VirtualPrivateCloudSecurityPolicyUpdateParams.


        :param apply_to: The apply_to of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :type apply_to: list[VirtualPrivateCloudSecurityPolicyApplyInput]
        """

        self._apply_to = apply_to

    @property
    def policy_mode(self):
        """Gets the policy_mode of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501


        :return: The policy_mode of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :rtype: VirtualPrivateCloudSecurityPolicyMode
        """
        return self._policy_mode

    @policy_mode.setter
    def policy_mode(self, policy_mode):
        """Sets the policy_mode of this VirtualPrivateCloudSecurityPolicyUpdateParams.


        :param policy_mode: The policy_mode of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :type policy_mode: VirtualPrivateCloudSecurityPolicyMode
        """

        self._policy_mode = policy_mode

    @property
    def description(self):
        """Gets the description of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501


        :return: The description of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualPrivateCloudSecurityPolicyUpdateParams.


        :param description: The description of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501


        :return: The name of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualPrivateCloudSecurityPolicyUpdateParams.


        :param name: The name of this VirtualPrivateCloudSecurityPolicyUpdateParams.  # noqa: E501
        :type name: str
        """

        self._name = name

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
        if not isinstance(other, VirtualPrivateCloudSecurityPolicyUpdateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloudSecurityPolicyUpdateParams):
            return True

        return self.to_dict() != other.to_dict()
