# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloudFloatingIp(object):
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
        'entity_async_status': 'EntityAsyncStatus',
        'external_ip': 'str',
        'external_subnet': 'NestedVirtualPrivateCloudExternalSubnet',
        'id': 'str',
        'local_id': 'str',
        'vpc': 'NestedVirtualPrivateCloud'
    }

    attribute_map = {
        'entity_async_status': 'entityAsyncStatus',
        'external_ip': 'external_ip',
        'external_subnet': 'external_subnet',
        'id': 'id',
        'local_id': 'local_id',
        'vpc': 'vpc'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloudFloatingIp - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._entity_async_status = None
        self._external_ip = None
        self._external_subnet = None
        self._id = None
        self._local_id = None
        self._vpc = None
        self.discriminator = None

        self.entity_async_status = kwargs.get("entity_async_status", None)
        self.external_ip = kwargs.get("external_ip", None)
        if "external_subnet" in kwargs:
            self.external_subnet = kwargs["external_subnet"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "vpc" in kwargs:
            self.vpc = kwargs["vpc"]

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this VirtualPrivateCloudFloatingIp.  # noqa: E501


        :return: The entity_async_status of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this VirtualPrivateCloudFloatingIp.


        :param entity_async_status: The entity_async_status of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def external_ip(self):
        """Gets the external_ip of this VirtualPrivateCloudFloatingIp.  # noqa: E501


        :return: The external_ip of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :rtype: str
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this VirtualPrivateCloudFloatingIp.


        :param external_ip: The external_ip of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :type external_ip: str
        """

        self._external_ip = external_ip

    @property
    def external_subnet(self):
        """Gets the external_subnet of this VirtualPrivateCloudFloatingIp.  # noqa: E501


        :return: The external_subnet of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :rtype: NestedVirtualPrivateCloudExternalSubnet
        """
        return self._external_subnet

    @external_subnet.setter
    def external_subnet(self, external_subnet):
        """Sets the external_subnet of this VirtualPrivateCloudFloatingIp.


        :param external_subnet: The external_subnet of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :type external_subnet: NestedVirtualPrivateCloudExternalSubnet
        """
        if self.local_vars_configuration.client_side_validation and external_subnet is None:  # noqa: E501
            raise ValueError("Invalid value for `external_subnet`, must not be `None`")  # noqa: E501

        self._external_subnet = external_subnet

    @property
    def id(self):
        """Gets the id of this VirtualPrivateCloudFloatingIp.  # noqa: E501


        :return: The id of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualPrivateCloudFloatingIp.


        :param id: The id of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this VirtualPrivateCloudFloatingIp.  # noqa: E501


        :return: The local_id of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VirtualPrivateCloudFloatingIp.


        :param local_id: The local_id of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def vpc(self):
        """Gets the vpc of this VirtualPrivateCloudFloatingIp.  # noqa: E501


        :return: The vpc of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :rtype: NestedVirtualPrivateCloud
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this VirtualPrivateCloudFloatingIp.


        :param vpc: The vpc of this VirtualPrivateCloudFloatingIp.  # noqa: E501
        :type vpc: NestedVirtualPrivateCloud
        """
        if self.local_vars_configuration.client_side_validation and vpc is None:  # noqa: E501
            raise ValueError("Invalid value for `vpc`, must not be `None`")  # noqa: E501

        self._vpc = vpc

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
        if not isinstance(other, VirtualPrivateCloudFloatingIp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloudFloatingIp):
            return True

        return self.to_dict() != other.to_dict()