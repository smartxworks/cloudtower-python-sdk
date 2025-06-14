# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class IsolationPolicyUpdateParams(object):
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
        'ingress': 'list[SecurityPolicyIngressEgressInput]',
        'egress': 'list[SecurityPolicyIngressEgressInput]',
        'mode': 'IsolationMode'
    }

    attribute_map = {
        'ingress': 'ingress',
        'egress': 'egress',
        'mode': 'mode'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """IsolationPolicyUpdateParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._ingress = None
        self._egress = None
        self._mode = None
        self.discriminator = None

        if "ingress" in kwargs:
            self.ingress = kwargs["ingress"]
        if "egress" in kwargs:
            self.egress = kwargs["egress"]
        if "mode" in kwargs:
            self.mode = kwargs["mode"]

    @property
    def ingress(self):
        """Gets the ingress of this IsolationPolicyUpdateParams.  # noqa: E501


        :return: The ingress of this IsolationPolicyUpdateParams.  # noqa: E501
        :rtype: list[SecurityPolicyIngressEgressInput]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """Sets the ingress of this IsolationPolicyUpdateParams.


        :param ingress: The ingress of this IsolationPolicyUpdateParams.  # noqa: E501
        :type ingress: list[SecurityPolicyIngressEgressInput]
        """

        self._ingress = ingress

    @property
    def egress(self):
        """Gets the egress of this IsolationPolicyUpdateParams.  # noqa: E501


        :return: The egress of this IsolationPolicyUpdateParams.  # noqa: E501
        :rtype: list[SecurityPolicyIngressEgressInput]
        """
        return self._egress

    @egress.setter
    def egress(self, egress):
        """Sets the egress of this IsolationPolicyUpdateParams.


        :param egress: The egress of this IsolationPolicyUpdateParams.  # noqa: E501
        :type egress: list[SecurityPolicyIngressEgressInput]
        """

        self._egress = egress

    @property
    def mode(self):
        """Gets the mode of this IsolationPolicyUpdateParams.  # noqa: E501


        :return: The mode of this IsolationPolicyUpdateParams.  # noqa: E501
        :rtype: IsolationMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this IsolationPolicyUpdateParams.


        :param mode: The mode of this IsolationPolicyUpdateParams.  # noqa: E501
        :type mode: IsolationMode
        """

        self._mode = mode

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
        if not isinstance(other, IsolationPolicyUpdateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IsolationPolicyUpdateParams):
            return True

        return self.to_dict() != other.to_dict()
