# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Contact: info@smartx.com
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


class StopVmInCutoverMigrationParams(object):
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
        'force': 'bool',
        'tasks': 'TaskWhereInput'
    }

    attribute_map = {
        'force': 'force',
        'tasks': 'tasks'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """StopVmInCutoverMigrationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._force = None
        self._tasks = None
        self.discriminator = None

        if "force" in kwargs:
            self.force = kwargs["force"]
        if "tasks" in kwargs:
            self.tasks = kwargs["tasks"]

    @property
    def force(self):
        """Gets the force of this StopVmInCutoverMigrationParams.  # noqa: E501


        :return: The force of this StopVmInCutoverMigrationParams.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this StopVmInCutoverMigrationParams.


        :param force: The force of this StopVmInCutoverMigrationParams.  # noqa: E501
        :type force: bool
        """

        self._force = force

    @property
    def tasks(self):
        """Gets the tasks of this StopVmInCutoverMigrationParams.  # noqa: E501


        :return: The tasks of this StopVmInCutoverMigrationParams.  # noqa: E501
        :rtype: TaskWhereInput
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this StopVmInCutoverMigrationParams.


        :param tasks: The tasks of this StopVmInCutoverMigrationParams.  # noqa: E501
        :type tasks: TaskWhereInput
        """
        if self.local_vars_configuration.client_side_validation and tasks is None:  # noqa: E501
            raise ValueError("Invalid value for `tasks`, must not be `None`")  # noqa: E501

        self._tasks = tasks

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
        if not isinstance(other, StopVmInCutoverMigrationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopVmInCutoverMigrationParams):
            return True

        return self.to_dict() != other.to_dict()
