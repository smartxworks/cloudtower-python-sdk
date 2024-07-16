# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class VirtualPrivateCloudSecurityPolicy(object):
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
        'apply_to': 'list[NestedVirtualPrivateCloudSecurityPolicyApply]',
        'description': 'str',
        'egress': 'list[NestedVirtualPrivateCloudNetworkPolicyRule]',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'ingress': 'list[NestedVirtualPrivateCloudNetworkPolicyRule]',
        'local_id': 'str',
        'name': 'str',
        'policy_mode': 'VirtualPrivateCloudSecurityPolicyMode',
        'vpc': 'NestedVirtualPrivateCloud'
    }

    attribute_map = {
        'apply_to': 'apply_to',
        'description': 'description',
        'egress': 'egress',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'ingress': 'ingress',
        'local_id': 'local_id',
        'name': 'name',
        'policy_mode': 'policy_mode',
        'vpc': 'vpc'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VirtualPrivateCloudSecurityPolicy - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._apply_to = None
        self._description = None
        self._egress = None
        self._entity_async_status = None
        self._id = None
        self._ingress = None
        self._local_id = None
        self._name = None
        self._policy_mode = None
        self._vpc = None
        self.discriminator = None

        if "apply_to" in kwargs:
            self.apply_to = kwargs["apply_to"]
        self.description = kwargs.get("description", None)
        self.egress = kwargs.get("egress", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.ingress = kwargs.get("ingress", None)
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.policy_mode = kwargs.get("policy_mode", None)
        if "vpc" in kwargs:
            self.vpc = kwargs["vpc"]

    @property
    def apply_to(self):
        """Gets the apply_to of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The apply_to of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudSecurityPolicyApply]
        """
        return self._apply_to

    @apply_to.setter
    def apply_to(self, apply_to):
        """Sets the apply_to of this VirtualPrivateCloudSecurityPolicy.


        :param apply_to: The apply_to of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type apply_to: list[NestedVirtualPrivateCloudSecurityPolicyApply]
        """
        if self.local_vars_configuration.client_side_validation and apply_to is None:  # noqa: E501
            raise ValueError("Invalid value for `apply_to`, must not be `None`")  # noqa: E501

        self._apply_to = apply_to

    @property
    def description(self):
        """Gets the description of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The description of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualPrivateCloudSecurityPolicy.


        :param description: The description of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def egress(self):
        """Gets the egress of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The egress of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudNetworkPolicyRule]
        """
        return self._egress

    @egress.setter
    def egress(self, egress):
        """Sets the egress of this VirtualPrivateCloudSecurityPolicy.


        :param egress: The egress of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type egress: list[NestedVirtualPrivateCloudNetworkPolicyRule]
        """

        self._egress = egress

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The entity_async_status of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this VirtualPrivateCloudSecurityPolicy.


        :param entity_async_status: The entity_async_status of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The id of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualPrivateCloudSecurityPolicy.


        :param id: The id of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ingress(self):
        """Gets the ingress of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The ingress of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: list[NestedVirtualPrivateCloudNetworkPolicyRule]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """Sets the ingress of this VirtualPrivateCloudSecurityPolicy.


        :param ingress: The ingress of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type ingress: list[NestedVirtualPrivateCloudNetworkPolicyRule]
        """

        self._ingress = ingress

    @property
    def local_id(self):
        """Gets the local_id of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The local_id of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this VirtualPrivateCloudSecurityPolicy.


        :param local_id: The local_id of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The name of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualPrivateCloudSecurityPolicy.


        :param name: The name of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def policy_mode(self):
        """Gets the policy_mode of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The policy_mode of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: VirtualPrivateCloudSecurityPolicyMode
        """
        return self._policy_mode

    @policy_mode.setter
    def policy_mode(self, policy_mode):
        """Sets the policy_mode of this VirtualPrivateCloudSecurityPolicy.


        :param policy_mode: The policy_mode of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :type policy_mode: VirtualPrivateCloudSecurityPolicyMode
        """

        self._policy_mode = policy_mode

    @property
    def vpc(self):
        """Gets the vpc of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501


        :return: The vpc of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
        :rtype: NestedVirtualPrivateCloud
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this VirtualPrivateCloudSecurityPolicy.


        :param vpc: The vpc of this VirtualPrivateCloudSecurityPolicy.  # noqa: E501
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
        if not isinstance(other, VirtualPrivateCloudSecurityPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualPrivateCloudSecurityPolicy):
            return True

        return self.to_dict() != other.to_dict()
