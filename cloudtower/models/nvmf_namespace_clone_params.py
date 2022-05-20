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


class NvmfNamespaceCloneParams(object):
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
        'namespace_group_id': 'str',
        'nvmf_subsystem_id': 'str',
        'name': 'str',
        'snapshot_id': 'str'
    }

    attribute_map = {
        'namespace_group_id': 'namespace_group_id',
        'nvmf_subsystem_id': 'nvmf_subsystem_id',
        'name': 'name',
        'snapshot_id': 'snapshot_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """NvmfNamespaceCloneParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._namespace_group_id = None
        self._nvmf_subsystem_id = None
        self._name = None
        self._snapshot_id = None
        self.discriminator = None

        if "namespace_group_id" in kwargs:
            self.namespace_group_id = kwargs["namespace_group_id"]
        if "nvmf_subsystem_id" in kwargs:
            self.nvmf_subsystem_id = kwargs["nvmf_subsystem_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "snapshot_id" in kwargs:
            self.snapshot_id = kwargs["snapshot_id"]

    @property
    def namespace_group_id(self):
        """Gets the namespace_group_id of this NvmfNamespaceCloneParams.  # noqa: E501


        :return: The namespace_group_id of this NvmfNamespaceCloneParams.  # noqa: E501
        :rtype: str
        """
        return self._namespace_group_id

    @namespace_group_id.setter
    def namespace_group_id(self, namespace_group_id):
        """Sets the namespace_group_id of this NvmfNamespaceCloneParams.


        :param namespace_group_id: The namespace_group_id of this NvmfNamespaceCloneParams.  # noqa: E501
        :type namespace_group_id: str
        """

        self._namespace_group_id = namespace_group_id

    @property
    def nvmf_subsystem_id(self):
        """Gets the nvmf_subsystem_id of this NvmfNamespaceCloneParams.  # noqa: E501


        :return: The nvmf_subsystem_id of this NvmfNamespaceCloneParams.  # noqa: E501
        :rtype: str
        """
        return self._nvmf_subsystem_id

    @nvmf_subsystem_id.setter
    def nvmf_subsystem_id(self, nvmf_subsystem_id):
        """Sets the nvmf_subsystem_id of this NvmfNamespaceCloneParams.


        :param nvmf_subsystem_id: The nvmf_subsystem_id of this NvmfNamespaceCloneParams.  # noqa: E501
        :type nvmf_subsystem_id: str
        """
        if self.local_vars_configuration.client_side_validation and nvmf_subsystem_id is None:  # noqa: E501
            raise ValueError("Invalid value for `nvmf_subsystem_id`, must not be `None`")  # noqa: E501

        self._nvmf_subsystem_id = nvmf_subsystem_id

    @property
    def name(self):
        """Gets the name of this NvmfNamespaceCloneParams.  # noqa: E501


        :return: The name of this NvmfNamespaceCloneParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NvmfNamespaceCloneParams.


        :param name: The name of this NvmfNamespaceCloneParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this NvmfNamespaceCloneParams.  # noqa: E501


        :return: The snapshot_id of this NvmfNamespaceCloneParams.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this NvmfNamespaceCloneParams.


        :param snapshot_id: The snapshot_id of this NvmfNamespaceCloneParams.  # noqa: E501
        :type snapshot_id: str
        """
        if self.local_vars_configuration.client_side_validation and snapshot_id is None:  # noqa: E501
            raise ValueError("Invalid value for `snapshot_id`, must not be `None`")  # noqa: E501

        self._snapshot_id = snapshot_id

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
        if not isinstance(other, NvmfNamespaceCloneParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NvmfNamespaceCloneParams):
            return True

        return self.to_dict() != other.to_dict()