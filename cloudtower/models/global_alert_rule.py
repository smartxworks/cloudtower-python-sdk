# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class GlobalAlertRule(object):
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
        'alert_rules': 'list[NestedAlertRule]',
        'boolean': 'bool',
        'cause': 'str',
        'default_thresholds': 'list[NestedThresholds]',
        'disabled': 'bool',
        'id': 'str',
        'impact': 'str',
        'message': 'str',
        'name': 'str',
        'object': 'AlertRuleObject',
        'operator': 'str',
        'solution': 'str',
        'thresholds': 'list[NestedThresholds]',
        'unit': 'AlertRuleUnit'
    }

    attribute_map = {
        'alert_rules': 'alert_rules',
        'boolean': 'boolean',
        'cause': 'cause',
        'default_thresholds': 'default_thresholds',
        'disabled': 'disabled',
        'id': 'id',
        'impact': 'impact',
        'message': 'message',
        'name': 'name',
        'object': 'object',
        'operator': 'operator',
        'solution': 'solution',
        'thresholds': 'thresholds',
        'unit': 'unit'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """GlobalAlertRule - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._alert_rules = None
        self._boolean = None
        self._cause = None
        self._default_thresholds = None
        self._disabled = None
        self._id = None
        self._impact = None
        self._message = None
        self._name = None
        self._object = None
        self._operator = None
        self._solution = None
        self._thresholds = None
        self._unit = None
        self.discriminator = None

        self.alert_rules = kwargs.get("alert_rules", None)
        if "boolean" in kwargs:
            self.boolean = kwargs["boolean"]
        if "cause" in kwargs:
            self.cause = kwargs["cause"]
        if "default_thresholds" in kwargs:
            self.default_thresholds = kwargs["default_thresholds"]
        if "disabled" in kwargs:
            self.disabled = kwargs["disabled"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "impact" in kwargs:
            self.impact = kwargs["impact"]
        if "message" in kwargs:
            self.message = kwargs["message"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.object = kwargs.get("object", None)
        if "operator" in kwargs:
            self.operator = kwargs["operator"]
        if "solution" in kwargs:
            self.solution = kwargs["solution"]
        if "thresholds" in kwargs:
            self.thresholds = kwargs["thresholds"]
        if "unit" in kwargs:
            self.unit = kwargs["unit"]

    @property
    def alert_rules(self):
        """Gets the alert_rules of this GlobalAlertRule.  # noqa: E501


        :return: The alert_rules of this GlobalAlertRule.  # noqa: E501
        :rtype: list[NestedAlertRule]
        """
        return self._alert_rules

    @alert_rules.setter
    def alert_rules(self, alert_rules):
        """Sets the alert_rules of this GlobalAlertRule.


        :param alert_rules: The alert_rules of this GlobalAlertRule.  # noqa: E501
        :type alert_rules: list[NestedAlertRule]
        """

        self._alert_rules = alert_rules

    @property
    def boolean(self):
        """Gets the boolean of this GlobalAlertRule.  # noqa: E501


        :return: The boolean of this GlobalAlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        """Sets the boolean of this GlobalAlertRule.


        :param boolean: The boolean of this GlobalAlertRule.  # noqa: E501
        :type boolean: bool
        """
        if self.local_vars_configuration.client_side_validation and boolean is None:  # noqa: E501
            raise ValueError("Invalid value for `boolean`, must not be `None`")  # noqa: E501

        self._boolean = boolean

    @property
    def cause(self):
        """Gets the cause of this GlobalAlertRule.  # noqa: E501


        :return: The cause of this GlobalAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this GlobalAlertRule.


        :param cause: The cause of this GlobalAlertRule.  # noqa: E501
        :type cause: str
        """
        if self.local_vars_configuration.client_side_validation and cause is None:  # noqa: E501
            raise ValueError("Invalid value for `cause`, must not be `None`")  # noqa: E501

        self._cause = cause

    @property
    def default_thresholds(self):
        """Gets the default_thresholds of this GlobalAlertRule.  # noqa: E501


        :return: The default_thresholds of this GlobalAlertRule.  # noqa: E501
        :rtype: list[NestedThresholds]
        """
        return self._default_thresholds

    @default_thresholds.setter
    def default_thresholds(self, default_thresholds):
        """Sets the default_thresholds of this GlobalAlertRule.


        :param default_thresholds: The default_thresholds of this GlobalAlertRule.  # noqa: E501
        :type default_thresholds: list[NestedThresholds]
        """
        if self.local_vars_configuration.client_side_validation and default_thresholds is None:  # noqa: E501
            raise ValueError("Invalid value for `default_thresholds`, must not be `None`")  # noqa: E501

        self._default_thresholds = default_thresholds

    @property
    def disabled(self):
        """Gets the disabled of this GlobalAlertRule.  # noqa: E501


        :return: The disabled of this GlobalAlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this GlobalAlertRule.


        :param disabled: The disabled of this GlobalAlertRule.  # noqa: E501
        :type disabled: bool
        """
        if self.local_vars_configuration.client_side_validation and disabled is None:  # noqa: E501
            raise ValueError("Invalid value for `disabled`, must not be `None`")  # noqa: E501

        self._disabled = disabled

    @property
    def id(self):
        """Gets the id of this GlobalAlertRule.  # noqa: E501


        :return: The id of this GlobalAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GlobalAlertRule.


        :param id: The id of this GlobalAlertRule.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def impact(self):
        """Gets the impact of this GlobalAlertRule.  # noqa: E501


        :return: The impact of this GlobalAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this GlobalAlertRule.


        :param impact: The impact of this GlobalAlertRule.  # noqa: E501
        :type impact: str
        """
        if self.local_vars_configuration.client_side_validation and impact is None:  # noqa: E501
            raise ValueError("Invalid value for `impact`, must not be `None`")  # noqa: E501

        self._impact = impact

    @property
    def message(self):
        """Gets the message of this GlobalAlertRule.  # noqa: E501


        :return: The message of this GlobalAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GlobalAlertRule.


        :param message: The message of this GlobalAlertRule.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def name(self):
        """Gets the name of this GlobalAlertRule.  # noqa: E501


        :return: The name of this GlobalAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalAlertRule.


        :param name: The name of this GlobalAlertRule.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def object(self):
        """Gets the object of this GlobalAlertRule.  # noqa: E501


        :return: The object of this GlobalAlertRule.  # noqa: E501
        :rtype: AlertRuleObject
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this GlobalAlertRule.


        :param object: The object of this GlobalAlertRule.  # noqa: E501
        :type object: AlertRuleObject
        """

        self._object = object

    @property
    def operator(self):
        """Gets the operator of this GlobalAlertRule.  # noqa: E501


        :return: The operator of this GlobalAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this GlobalAlertRule.


        :param operator: The operator of this GlobalAlertRule.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def solution(self):
        """Gets the solution of this GlobalAlertRule.  # noqa: E501


        :return: The solution of this GlobalAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """Sets the solution of this GlobalAlertRule.


        :param solution: The solution of this GlobalAlertRule.  # noqa: E501
        :type solution: str
        """
        if self.local_vars_configuration.client_side_validation and solution is None:  # noqa: E501
            raise ValueError("Invalid value for `solution`, must not be `None`")  # noqa: E501

        self._solution = solution

    @property
    def thresholds(self):
        """Gets the thresholds of this GlobalAlertRule.  # noqa: E501


        :return: The thresholds of this GlobalAlertRule.  # noqa: E501
        :rtype: list[NestedThresholds]
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this GlobalAlertRule.


        :param thresholds: The thresholds of this GlobalAlertRule.  # noqa: E501
        :type thresholds: list[NestedThresholds]
        """
        if self.local_vars_configuration.client_side_validation and thresholds is None:  # noqa: E501
            raise ValueError("Invalid value for `thresholds`, must not be `None`")  # noqa: E501

        self._thresholds = thresholds

    @property
    def unit(self):
        """Gets the unit of this GlobalAlertRule.  # noqa: E501


        :return: The unit of this GlobalAlertRule.  # noqa: E501
        :rtype: AlertRuleUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this GlobalAlertRule.


        :param unit: The unit of this GlobalAlertRule.  # noqa: E501
        :type unit: AlertRuleUnit
        """
        if self.local_vars_configuration.client_side_validation and unit is None:  # noqa: E501
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

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
        if not isinstance(other, GlobalAlertRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalAlertRule):
            return True

        return self.to_dict() != other.to_dict()
