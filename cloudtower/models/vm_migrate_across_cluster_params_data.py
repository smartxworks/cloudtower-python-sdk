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


class VmMigrateAcrossClusterParamsData(object):
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
        'vm_config': 'MigrateVmConfig',
        'cluster_id': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'vm_config': 'vm_config',
        'cluster_id': 'cluster_id',
        'host_id': 'host_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmMigrateAcrossClusterParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._vm_config = None
        self._cluster_id = None
        self._host_id = None
        self.discriminator = None

        if "vm_config" in kwargs:
            self.vm_config = kwargs["vm_config"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        if "host_id" in kwargs:
            self.host_id = kwargs["host_id"]

    @property
    def vm_config(self):
        """Gets the vm_config of this VmMigrateAcrossClusterParamsData.  # noqa: E501


        :return: The vm_config of this VmMigrateAcrossClusterParamsData.  # noqa: E501
        :rtype: MigrateVmConfig
        """
        return self._vm_config

    @vm_config.setter
    def vm_config(self, vm_config):
        """Sets the vm_config of this VmMigrateAcrossClusterParamsData.


        :param vm_config: The vm_config of this VmMigrateAcrossClusterParamsData.  # noqa: E501
        :type vm_config: MigrateVmConfig
        """
        if self.local_vars_configuration.client_side_validation and vm_config is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_config`, must not be `None`")  # noqa: E501

        self._vm_config = vm_config

    @property
    def cluster_id(self):
        """Gets the cluster_id of this VmMigrateAcrossClusterParamsData.  # noqa: E501


        :return: The cluster_id of this VmMigrateAcrossClusterParamsData.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this VmMigrateAcrossClusterParamsData.


        :param cluster_id: The cluster_id of this VmMigrateAcrossClusterParamsData.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def host_id(self):
        """Gets the host_id of this VmMigrateAcrossClusterParamsData.  # noqa: E501


        :return: The host_id of this VmMigrateAcrossClusterParamsData.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this VmMigrateAcrossClusterParamsData.


        :param host_id: The host_id of this VmMigrateAcrossClusterParamsData.  # noqa: E501
        :type host_id: str
        """

        self._host_id = host_id

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
        if not isinstance(other, VmMigrateAcrossClusterParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmMigrateAcrossClusterParamsData):
            return True

        return self.to_dict() != other.to_dict()
