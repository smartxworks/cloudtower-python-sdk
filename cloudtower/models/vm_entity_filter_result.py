# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.1.0
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


class VmEntityFilterResult(object):
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
        'entity_filter': 'NestedEntityFilter',
        'id': 'str',
        'result': 'list[float]',
        'vm': 'NestedVm'
    }

    attribute_map = {
        'entity_filter': 'entityFilter',
        'id': 'id',
        'result': 'result',
        'vm': 'vm'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmEntityFilterResult - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._entity_filter = None
        self._id = None
        self._result = None
        self._vm = None
        self.discriminator = None

        if "entity_filter" in kwargs:
            self.entity_filter = kwargs["entity_filter"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "result" in kwargs:
            self.result = kwargs["result"]
        if "vm" in kwargs:
            self.vm = kwargs["vm"]

    @property
    def entity_filter(self):
        """Gets the entity_filter of this VmEntityFilterResult.  # noqa: E501


        :return: The entity_filter of this VmEntityFilterResult.  # noqa: E501
        :rtype: NestedEntityFilter
        """
        return self._entity_filter

    @entity_filter.setter
    def entity_filter(self, entity_filter):
        """Sets the entity_filter of this VmEntityFilterResult.


        :param entity_filter: The entity_filter of this VmEntityFilterResult.  # noqa: E501
        :type entity_filter: NestedEntityFilter
        """
        if self.local_vars_configuration.client_side_validation and entity_filter is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_filter`, must not be `None`")  # noqa: E501

        self._entity_filter = entity_filter

    @property
    def id(self):
        """Gets the id of this VmEntityFilterResult.  # noqa: E501


        :return: The id of this VmEntityFilterResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmEntityFilterResult.


        :param id: The id of this VmEntityFilterResult.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def result(self):
        """Gets the result of this VmEntityFilterResult.  # noqa: E501


        :return: The result of this VmEntityFilterResult.  # noqa: E501
        :rtype: list[float]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this VmEntityFilterResult.


        :param result: The result of this VmEntityFilterResult.  # noqa: E501
        :type result: list[float]
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def vm(self):
        """Gets the vm of this VmEntityFilterResult.  # noqa: E501


        :return: The vm of this VmEntityFilterResult.  # noqa: E501
        :rtype: NestedVm
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this VmEntityFilterResult.


        :param vm: The vm of this VmEntityFilterResult.  # noqa: E501
        :type vm: NestedVm
        """
        if self.local_vars_configuration.client_side_validation and vm is None:  # noqa: E501
            raise ValueError("Invalid value for `vm`, must not be `None`")  # noqa: E501

        self._vm = vm

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
        if not isinstance(other, VmEntityFilterResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmEntityFilterResult):
            return True

        return self.to_dict() != other.to_dict()
