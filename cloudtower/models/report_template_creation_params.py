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


class ReportTemplateCreationParams(object):
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
        'resource_meta': 'list[ResourceMeta]',
        'execute_plan': 'list[ExecutePlan]',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'resource_meta': 'resource_meta',
        'execute_plan': 'execute_plan',
        'description': 'description',
        'name': 'name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ReportTemplateCreationParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._resource_meta = None
        self._execute_plan = None
        self._description = None
        self._name = None
        self.discriminator = None

        if "resource_meta" in kwargs:
            self.resource_meta = kwargs["resource_meta"]
        if "execute_plan" in kwargs:
            self.execute_plan = kwargs["execute_plan"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "name" in kwargs:
            self.name = kwargs["name"]

    @property
    def resource_meta(self):
        """Gets the resource_meta of this ReportTemplateCreationParams.  # noqa: E501


        :return: The resource_meta of this ReportTemplateCreationParams.  # noqa: E501
        :rtype: list[ResourceMeta]
        """
        return self._resource_meta

    @resource_meta.setter
    def resource_meta(self, resource_meta):
        """Sets the resource_meta of this ReportTemplateCreationParams.


        :param resource_meta: The resource_meta of this ReportTemplateCreationParams.  # noqa: E501
        :type resource_meta: list[ResourceMeta]
        """
        if self.local_vars_configuration.client_side_validation and resource_meta is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_meta`, must not be `None`")  # noqa: E501

        self._resource_meta = resource_meta

    @property
    def execute_plan(self):
        """Gets the execute_plan of this ReportTemplateCreationParams.  # noqa: E501


        :return: The execute_plan of this ReportTemplateCreationParams.  # noqa: E501
        :rtype: list[ExecutePlan]
        """
        return self._execute_plan

    @execute_plan.setter
    def execute_plan(self, execute_plan):
        """Sets the execute_plan of this ReportTemplateCreationParams.


        :param execute_plan: The execute_plan of this ReportTemplateCreationParams.  # noqa: E501
        :type execute_plan: list[ExecutePlan]
        """
        if self.local_vars_configuration.client_side_validation and execute_plan is None:  # noqa: E501
            raise ValueError("Invalid value for `execute_plan`, must not be `None`")  # noqa: E501

        self._execute_plan = execute_plan

    @property
    def description(self):
        """Gets the description of this ReportTemplateCreationParams.  # noqa: E501


        :return: The description of this ReportTemplateCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportTemplateCreationParams.


        :param description: The description of this ReportTemplateCreationParams.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this ReportTemplateCreationParams.  # noqa: E501


        :return: The name of this ReportTemplateCreationParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportTemplateCreationParams.


        :param name: The name of this ReportTemplateCreationParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, ReportTemplateCreationParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportTemplateCreationParams):
            return True

        return self.to_dict() != other.to_dict()