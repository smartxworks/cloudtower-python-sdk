# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedEverouteClusterStatus(object):
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
        'agents': 'NestedEverouteClusterAgentStatus',
        'conditions': 'list[NestedEverouteClusterCondition]',
        'controllers': 'NestedEverouteClusterControllerStatus',
        'message': 'str',
        'phase': 'EverouteClusterPhase',
        'reason': 'str',
        'retry_count': 'int',
        'version': 'str'
    }

    attribute_map = {
        'agents': 'agents',
        'conditions': 'conditions',
        'controllers': 'controllers',
        'message': 'message',
        'phase': 'phase',
        'reason': 'reason',
        'retry_count': 'retryCount',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedEverouteClusterStatus - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._agents = None
        self._conditions = None
        self._controllers = None
        self._message = None
        self._phase = None
        self._reason = None
        self._retry_count = None
        self._version = None
        self.discriminator = None

        self.agents = kwargs.get("agents", None)
        self.conditions = kwargs.get("conditions", None)
        self.controllers = kwargs.get("controllers", None)
        self.message = kwargs.get("message", None)
        self.phase = kwargs.get("phase", None)
        self.reason = kwargs.get("reason", None)
        self.retry_count = kwargs.get("retry_count", None)
        self.version = kwargs.get("version", None)

    @property
    def agents(self):
        """Gets the agents of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The agents of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: NestedEverouteClusterAgentStatus
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this NestedEverouteClusterStatus.


        :param agents: The agents of this NestedEverouteClusterStatus.  # noqa: E501
        :type agents: NestedEverouteClusterAgentStatus
        """

        self._agents = agents

    @property
    def conditions(self):
        """Gets the conditions of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The conditions of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: list[NestedEverouteClusterCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this NestedEverouteClusterStatus.


        :param conditions: The conditions of this NestedEverouteClusterStatus.  # noqa: E501
        :type conditions: list[NestedEverouteClusterCondition]
        """

        self._conditions = conditions

    @property
    def controllers(self):
        """Gets the controllers of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The controllers of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: NestedEverouteClusterControllerStatus
        """
        return self._controllers

    @controllers.setter
    def controllers(self, controllers):
        """Sets the controllers of this NestedEverouteClusterStatus.


        :param controllers: The controllers of this NestedEverouteClusterStatus.  # noqa: E501
        :type controllers: NestedEverouteClusterControllerStatus
        """

        self._controllers = controllers

    @property
    def message(self):
        """Gets the message of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The message of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NestedEverouteClusterStatus.


        :param message: The message of this NestedEverouteClusterStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def phase(self):
        """Gets the phase of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The phase of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: EverouteClusterPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this NestedEverouteClusterStatus.


        :param phase: The phase of this NestedEverouteClusterStatus.  # noqa: E501
        :type phase: EverouteClusterPhase
        """

        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The reason of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this NestedEverouteClusterStatus.


        :param reason: The reason of this NestedEverouteClusterStatus.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def retry_count(self):
        """Gets the retry_count of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The retry_count of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this NestedEverouteClusterStatus.


        :param retry_count: The retry_count of this NestedEverouteClusterStatus.  # noqa: E501
        :type retry_count: int
        """

        self._retry_count = retry_count

    @property
    def version(self):
        """Gets the version of this NestedEverouteClusterStatus.  # noqa: E501


        :return: The version of this NestedEverouteClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NestedEverouteClusterStatus.


        :param version: The version of this NestedEverouteClusterStatus.  # noqa: E501
        :type version: str
        """

        self._version = version

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
        if not isinstance(other, NestedEverouteClusterStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedEverouteClusterStatus):
            return True

        return self.to_dict() != other.to_dict()
