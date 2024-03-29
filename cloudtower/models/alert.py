# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class Alert(object):
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
        'alert_rule': 'NestedAlertRule',
        'cause': 'str',
        'cluster': 'NestedCluster',
        'create_time': 'str',
        'disk': 'NestedDisk',
        'ended': 'bool',
        'host': 'NestedHost',
        'id': 'str',
        'impact': 'str',
        'labels': 'object',
        'local_create_time': 'str',
        'local_end_time': 'str',
        'local_id': 'str',
        'local_start_time': 'str',
        'local_update_time': 'str',
        'message': 'str',
        'severity': 'str',
        'solution': 'str',
        'threshold': 'float',
        'value': 'float',
        'vms': 'list[NestedVm]'
    }

    attribute_map = {
        'alert_rule': 'alert_rule',
        'cause': 'cause',
        'cluster': 'cluster',
        'create_time': 'create_time',
        'disk': 'disk',
        'ended': 'ended',
        'host': 'host',
        'id': 'id',
        'impact': 'impact',
        'labels': 'labels',
        'local_create_time': 'local_create_time',
        'local_end_time': 'local_end_time',
        'local_id': 'local_id',
        'local_start_time': 'local_start_time',
        'local_update_time': 'local_update_time',
        'message': 'message',
        'severity': 'severity',
        'solution': 'solution',
        'threshold': 'threshold',
        'value': 'value',
        'vms': 'vms'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Alert - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._alert_rule = None
        self._cause = None
        self._cluster = None
        self._create_time = None
        self._disk = None
        self._ended = None
        self._host = None
        self._id = None
        self._impact = None
        self._labels = None
        self._local_create_time = None
        self._local_end_time = None
        self._local_id = None
        self._local_start_time = None
        self._local_update_time = None
        self._message = None
        self._severity = None
        self._solution = None
        self._threshold = None
        self._value = None
        self._vms = None
        self.discriminator = None

        self.alert_rule = kwargs.get("alert_rule", None)
        if "cause" in kwargs:
            self.cause = kwargs["cause"]
        self.cluster = kwargs.get("cluster", None)
        self.create_time = kwargs.get("create_time", None)
        self.disk = kwargs.get("disk", None)
        if "ended" in kwargs:
            self.ended = kwargs["ended"]
        self.host = kwargs.get("host", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "impact" in kwargs:
            self.impact = kwargs["impact"]
        if "labels" in kwargs:
            self.labels = kwargs["labels"]
        if "local_create_time" in kwargs:
            self.local_create_time = kwargs["local_create_time"]
        if "local_end_time" in kwargs:
            self.local_end_time = kwargs["local_end_time"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "local_start_time" in kwargs:
            self.local_start_time = kwargs["local_start_time"]
        if "local_update_time" in kwargs:
            self.local_update_time = kwargs["local_update_time"]
        if "message" in kwargs:
            self.message = kwargs["message"]
        if "severity" in kwargs:
            self.severity = kwargs["severity"]
        if "solution" in kwargs:
            self.solution = kwargs["solution"]
        if "threshold" in kwargs:
            self.threshold = kwargs["threshold"]
        if "value" in kwargs:
            self.value = kwargs["value"]
        self.vms = kwargs.get("vms", None)

    @property
    def alert_rule(self):
        """Gets the alert_rule of this Alert.  # noqa: E501


        :return: The alert_rule of this Alert.  # noqa: E501
        :rtype: NestedAlertRule
        """
        return self._alert_rule

    @alert_rule.setter
    def alert_rule(self, alert_rule):
        """Sets the alert_rule of this Alert.


        :param alert_rule: The alert_rule of this Alert.  # noqa: E501
        :type alert_rule: NestedAlertRule
        """

        self._alert_rule = alert_rule

    @property
    def cause(self):
        """Gets the cause of this Alert.  # noqa: E501


        :return: The cause of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this Alert.


        :param cause: The cause of this Alert.  # noqa: E501
        :type cause: str
        """
        if self.local_vars_configuration.client_side_validation and cause is None:  # noqa: E501
            raise ValueError("Invalid value for `cause`, must not be `None`")  # noqa: E501

        self._cause = cause

    @property
    def cluster(self):
        """Gets the cluster of this Alert.  # noqa: E501


        :return: The cluster of this Alert.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Alert.


        :param cluster: The cluster of this Alert.  # noqa: E501
        :type cluster: NestedCluster
        """

        self._cluster = cluster

    @property
    def create_time(self):
        """Gets the create_time of this Alert.  # noqa: E501


        :return: The create_time of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Alert.


        :param create_time: The create_time of this Alert.  # noqa: E501
        :type create_time: str
        """

        self._create_time = create_time

    @property
    def disk(self):
        """Gets the disk of this Alert.  # noqa: E501


        :return: The disk of this Alert.  # noqa: E501
        :rtype: NestedDisk
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this Alert.


        :param disk: The disk of this Alert.  # noqa: E501
        :type disk: NestedDisk
        """

        self._disk = disk

    @property
    def ended(self):
        """Gets the ended of this Alert.  # noqa: E501


        :return: The ended of this Alert.  # noqa: E501
        :rtype: bool
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this Alert.


        :param ended: The ended of this Alert.  # noqa: E501
        :type ended: bool
        """
        if self.local_vars_configuration.client_side_validation and ended is None:  # noqa: E501
            raise ValueError("Invalid value for `ended`, must not be `None`")  # noqa: E501

        self._ended = ended

    @property
    def host(self):
        """Gets the host of this Alert.  # noqa: E501


        :return: The host of this Alert.  # noqa: E501
        :rtype: NestedHost
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Alert.


        :param host: The host of this Alert.  # noqa: E501
        :type host: NestedHost
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this Alert.  # noqa: E501


        :return: The id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alert.


        :param id: The id of this Alert.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact(self):
        """Gets the impact of this Alert.  # noqa: E501


        :return: The impact of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this Alert.


        :param impact: The impact of this Alert.  # noqa: E501
        :type impact: str
        """
        if self.local_vars_configuration.client_side_validation and impact is None:  # noqa: E501
            raise ValueError("Invalid value for `impact`, must not be `None`")  # noqa: E501

        self._impact = impact

    @property
    def labels(self):
        """Gets the labels of this Alert.  # noqa: E501


        :return: The labels of this Alert.  # noqa: E501
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Alert.


        :param labels: The labels of this Alert.  # noqa: E501
        :type labels: object
        """
        if self.local_vars_configuration.client_side_validation and labels is None:  # noqa: E501
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def local_create_time(self):
        """Gets the local_create_time of this Alert.  # noqa: E501


        :return: The local_create_time of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._local_create_time

    @local_create_time.setter
    def local_create_time(self, local_create_time):
        """Sets the local_create_time of this Alert.


        :param local_create_time: The local_create_time of this Alert.  # noqa: E501
        :type local_create_time: str
        """
        if self.local_vars_configuration.client_side_validation and local_create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `local_create_time`, must not be `None`")  # noqa: E501

        self._local_create_time = local_create_time

    @property
    def local_end_time(self):
        """Gets the local_end_time of this Alert.  # noqa: E501


        :return: The local_end_time of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._local_end_time

    @local_end_time.setter
    def local_end_time(self, local_end_time):
        """Sets the local_end_time of this Alert.


        :param local_end_time: The local_end_time of this Alert.  # noqa: E501
        :type local_end_time: str
        """
        if self.local_vars_configuration.client_side_validation and local_end_time is None:  # noqa: E501
            raise ValueError("Invalid value for `local_end_time`, must not be `None`")  # noqa: E501

        self._local_end_time = local_end_time

    @property
    def local_id(self):
        """Gets the local_id of this Alert.  # noqa: E501


        :return: The local_id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this Alert.


        :param local_id: The local_id of this Alert.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def local_start_time(self):
        """Gets the local_start_time of this Alert.  # noqa: E501


        :return: The local_start_time of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._local_start_time

    @local_start_time.setter
    def local_start_time(self, local_start_time):
        """Sets the local_start_time of this Alert.


        :param local_start_time: The local_start_time of this Alert.  # noqa: E501
        :type local_start_time: str
        """
        if self.local_vars_configuration.client_side_validation and local_start_time is None:  # noqa: E501
            raise ValueError("Invalid value for `local_start_time`, must not be `None`")  # noqa: E501

        self._local_start_time = local_start_time

    @property
    def local_update_time(self):
        """Gets the local_update_time of this Alert.  # noqa: E501


        :return: The local_update_time of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._local_update_time

    @local_update_time.setter
    def local_update_time(self, local_update_time):
        """Sets the local_update_time of this Alert.


        :param local_update_time: The local_update_time of this Alert.  # noqa: E501
        :type local_update_time: str
        """
        if self.local_vars_configuration.client_side_validation and local_update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `local_update_time`, must not be `None`")  # noqa: E501

        self._local_update_time = local_update_time

    @property
    def message(self):
        """Gets the message of this Alert.  # noqa: E501


        :return: The message of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Alert.


        :param message: The message of this Alert.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def severity(self):
        """Gets the severity of this Alert.  # noqa: E501


        :return: The severity of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Alert.


        :param severity: The severity of this Alert.  # noqa: E501
        :type severity: str
        """
        if self.local_vars_configuration.client_side_validation and severity is None:  # noqa: E501
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def solution(self):
        """Gets the solution of this Alert.  # noqa: E501


        :return: The solution of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """Sets the solution of this Alert.


        :param solution: The solution of this Alert.  # noqa: E501
        :type solution: str
        """
        if self.local_vars_configuration.client_side_validation and solution is None:  # noqa: E501
            raise ValueError("Invalid value for `solution`, must not be `None`")  # noqa: E501

        self._solution = solution

    @property
    def threshold(self):
        """Gets the threshold of this Alert.  # noqa: E501


        :return: The threshold of this Alert.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this Alert.


        :param threshold: The threshold of this Alert.  # noqa: E501
        :type threshold: float
        """
        if self.local_vars_configuration.client_side_validation and threshold is None:  # noqa: E501
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501

        self._threshold = threshold

    @property
    def value(self):
        """Gets the value of this Alert.  # noqa: E501


        :return: The value of this Alert.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Alert.


        :param value: The value of this Alert.  # noqa: E501
        :type value: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def vms(self):
        """Gets the vms of this Alert.  # noqa: E501


        :return: The vms of this Alert.  # noqa: E501
        :rtype: list[NestedVm]
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this Alert.


        :param vms: The vms of this Alert.  # noqa: E501
        :type vms: list[NestedVm]
        """

        self._vms = vms

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
        if not isinstance(other, Alert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Alert):
            return True

        return self.to_dict() != other.to_dict()
