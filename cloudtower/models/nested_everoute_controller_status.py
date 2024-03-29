# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class NestedEverouteControllerStatus(object):
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
        'ip_addr': 'str',
        'is_health': 'bool',
        'message': 'str',
        'metrics': 'NestedEverouteClusterVMMetrics',
        'phase': 'EverouteClusterPhase',
        'reason': 'str',
        'vm': 'NestedVm',
        'vm_id': 'str'
    }

    attribute_map = {
        'ip_addr': 'ipAddr',
        'is_health': 'isHealth',
        'message': 'message',
        'metrics': 'metrics',
        'phase': 'phase',
        'reason': 'reason',
        'vm': 'vm',
        'vm_id': 'vmID'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NestedEverouteControllerStatus - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._ip_addr = None
        self._is_health = None
        self._message = None
        self._metrics = None
        self._phase = None
        self._reason = None
        self._vm = None
        self._vm_id = None
        self.discriminator = None

        self.ip_addr = kwargs.get("ip_addr", None)
        if "is_health" in kwargs:
            self.is_health = kwargs["is_health"]
        self.message = kwargs.get("message", None)
        self.metrics = kwargs.get("metrics", None)
        self.phase = kwargs.get("phase", None)
        self.reason = kwargs.get("reason", None)
        self.vm = kwargs.get("vm", None)
        self.vm_id = kwargs.get("vm_id", None)

    @property
    def ip_addr(self):
        """Gets the ip_addr of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The ip_addr of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this NestedEverouteControllerStatus.


        :param ip_addr: The ip_addr of this NestedEverouteControllerStatus.  # noqa: E501
        :type ip_addr: str
        """

        self._ip_addr = ip_addr

    @property
    def is_health(self):
        """Gets the is_health of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The is_health of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_health

    @is_health.setter
    def is_health(self, is_health):
        """Sets the is_health of this NestedEverouteControllerStatus.


        :param is_health: The is_health of this NestedEverouteControllerStatus.  # noqa: E501
        :type is_health: bool
        """
        if self.local_vars_configuration.client_side_validation and is_health is None:  # noqa: E501
            raise ValueError("Invalid value for `is_health`, must not be `None`")  # noqa: E501

        self._is_health = is_health

    @property
    def message(self):
        """Gets the message of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The message of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NestedEverouteControllerStatus.


        :param message: The message of this NestedEverouteControllerStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def metrics(self):
        """Gets the metrics of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The metrics of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: NestedEverouteClusterVMMetrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this NestedEverouteControllerStatus.


        :param metrics: The metrics of this NestedEverouteControllerStatus.  # noqa: E501
        :type metrics: NestedEverouteClusterVMMetrics
        """

        self._metrics = metrics

    @property
    def phase(self):
        """Gets the phase of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The phase of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: EverouteClusterPhase
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this NestedEverouteControllerStatus.


        :param phase: The phase of this NestedEverouteControllerStatus.  # noqa: E501
        :type phase: EverouteClusterPhase
        """

        self._phase = phase

    @property
    def reason(self):
        """Gets the reason of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The reason of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this NestedEverouteControllerStatus.


        :param reason: The reason of this NestedEverouteControllerStatus.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def vm(self):
        """Gets the vm of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The vm of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: NestedVm
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this NestedEverouteControllerStatus.


        :param vm: The vm of this NestedEverouteControllerStatus.  # noqa: E501
        :type vm: NestedVm
        """

        self._vm = vm

    @property
    def vm_id(self):
        """Gets the vm_id of this NestedEverouteControllerStatus.  # noqa: E501


        :return: The vm_id of this NestedEverouteControllerStatus.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this NestedEverouteControllerStatus.


        :param vm_id: The vm_id of this NestedEverouteControllerStatus.  # noqa: E501
        :type vm_id: str
        """

        self._vm_id = vm_id

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
        if not isinstance(other, NestedEverouteControllerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NestedEverouteControllerStatus):
            return True

        return self.to_dict() != other.to_dict()
