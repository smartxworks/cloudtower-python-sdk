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


class WithTaskDeleteEntityFilter(object):
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
        'task_id': 'str',
        'data': 'DeleteEntityFilter'
    }

    attribute_map = {
        'task_id': 'task_id',
        'data': 'data'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """WithTaskDeleteEntityFilter - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._task_id = None
        self._data = None
        self.discriminator = None

        self.task_id = kwargs.get("task_id", None)
        if "data" in kwargs:
            self.data = kwargs["data"]

    @property
    def task_id(self):
        """Gets the task_id of this WithTaskDeleteEntityFilter.  # noqa: E501


        :return: The task_id of this WithTaskDeleteEntityFilter.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this WithTaskDeleteEntityFilter.


        :param task_id: The task_id of this WithTaskDeleteEntityFilter.  # noqa: E501
        :type task_id: str
        """

        self._task_id = task_id

    @property
    def data(self):
        """Gets the data of this WithTaskDeleteEntityFilter.  # noqa: E501


        :return: The data of this WithTaskDeleteEntityFilter.  # noqa: E501
        :rtype: DeleteEntityFilter
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WithTaskDeleteEntityFilter.


        :param data: The data of this WithTaskDeleteEntityFilter.  # noqa: E501
        :type data: DeleteEntityFilter
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, WithTaskDeleteEntityFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WithTaskDeleteEntityFilter):
            return True

        return self.to_dict() != other.to_dict()
