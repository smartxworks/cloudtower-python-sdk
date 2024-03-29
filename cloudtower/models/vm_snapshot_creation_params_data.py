# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VmSnapshotCreationParamsData(object):
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
        'consistent_type': 'ConsistentType',
        'name': 'str',
        'vm_id': 'str'
    }

    attribute_map = {
        'consistent_type': 'consistent_type',
        'name': 'name',
        'vm_id': 'vm_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmSnapshotCreationParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._consistent_type = None
        self._name = None
        self._vm_id = None
        self.discriminator = None

        if "consistent_type" in kwargs:
            self.consistent_type = kwargs["consistent_type"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "vm_id" in kwargs:
            self.vm_id = kwargs["vm_id"]

    @property
    def consistent_type(self):
        """Gets the consistent_type of this VmSnapshotCreationParamsData.  # noqa: E501


        :return: The consistent_type of this VmSnapshotCreationParamsData.  # noqa: E501
        :rtype: ConsistentType
        """
        return self._consistent_type

    @consistent_type.setter
    def consistent_type(self, consistent_type):
        """Sets the consistent_type of this VmSnapshotCreationParamsData.


        :param consistent_type: The consistent_type of this VmSnapshotCreationParamsData.  # noqa: E501
        :type consistent_type: ConsistentType
        """

        self._consistent_type = consistent_type

    @property
    def name(self):
        """Gets the name of this VmSnapshotCreationParamsData.  # noqa: E501


        :return: The name of this VmSnapshotCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmSnapshotCreationParamsData.


        :param name: The name of this VmSnapshotCreationParamsData.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def vm_id(self):
        """Gets the vm_id of this VmSnapshotCreationParamsData.  # noqa: E501


        :return: The vm_id of this VmSnapshotCreationParamsData.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this VmSnapshotCreationParamsData.


        :param vm_id: The vm_id of this VmSnapshotCreationParamsData.  # noqa: E501
        :type vm_id: str
        """
        if self.local_vars_configuration.client_side_validation and vm_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_id`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, VmSnapshotCreationParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmSnapshotCreationParamsData):
            return True

        return self.to_dict() != other.to_dict()
