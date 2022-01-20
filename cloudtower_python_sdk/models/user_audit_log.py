# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 1.9.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower_python_sdk.configuration import Configuration


class UserAuditLog(object):
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
        'action': 'str',
        'cluster': 'NestedCluster',
        'created_at': 'str',
        'finished_at': 'str',
        'id': 'str',
        'ip_address': 'str',
        'message': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'status': 'UserAuditLogStatus',
        'user': 'NestedUser'
    }

    attribute_map = {
        'action': 'action',
        'cluster': 'cluster',
        'created_at': 'createdAt',
        'finished_at': 'finished_at',
        'id': 'id',
        'ip_address': 'ip_address',
        'message': 'message',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'status': 'status',
        'user': 'user'
    }

    def __init__(self, action=None, cluster=None, created_at=None, finished_at=None, id=None, ip_address=None, message=None, resource_id=None, resource_type=None, status=None, user=None, local_vars_configuration=None):  # noqa: E501
        """UserAuditLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._cluster = None
        self._created_at = None
        self._finished_at = None
        self._id = None
        self._ip_address = None
        self._message = None
        self._resource_id = None
        self._resource_type = None
        self._status = None
        self._user = None
        self.discriminator = None

        self.action = action
        self.cluster = cluster
        self.created_at = created_at
        self.finished_at = finished_at
        self.id = id
        self.ip_address = ip_address
        self.message = message
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.status = status
        self.user = user

    @property
    def action(self):
        """Gets the action of this UserAuditLog.  # noqa: E501


        :return: The action of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UserAuditLog.


        :param action: The action of this UserAuditLog.  # noqa: E501
        :type action: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def cluster(self):
        """Gets the cluster of this UserAuditLog.  # noqa: E501


        :return: The cluster of this UserAuditLog.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this UserAuditLog.


        :param cluster: The cluster of this UserAuditLog.  # noqa: E501
        :type cluster: NestedCluster
        """

        self._cluster = cluster

    @property
    def created_at(self):
        """Gets the created_at of this UserAuditLog.  # noqa: E501


        :return: The created_at of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserAuditLog.


        :param created_at: The created_at of this UserAuditLog.  # noqa: E501
        :type created_at: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def finished_at(self):
        """Gets the finished_at of this UserAuditLog.  # noqa: E501


        :return: The finished_at of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this UserAuditLog.


        :param finished_at: The finished_at of this UserAuditLog.  # noqa: E501
        :type finished_at: str
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this UserAuditLog.  # noqa: E501


        :return: The id of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserAuditLog.


        :param id: The id of this UserAuditLog.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ip_address(self):
        """Gets the ip_address of this UserAuditLog.  # noqa: E501


        :return: The ip_address of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this UserAuditLog.


        :param ip_address: The ip_address of this UserAuditLog.  # noqa: E501
        :type ip_address: str
        """
        if self.local_vars_configuration.client_side_validation and ip_address is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def message(self):
        """Gets the message of this UserAuditLog.  # noqa: E501


        :return: The message of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UserAuditLog.


        :param message: The message of this UserAuditLog.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def resource_id(self):
        """Gets the resource_id of this UserAuditLog.  # noqa: E501


        :return: The resource_id of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this UserAuditLog.


        :param resource_id: The resource_id of this UserAuditLog.  # noqa: E501
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this UserAuditLog.  # noqa: E501


        :return: The resource_type of this UserAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this UserAuditLog.


        :param resource_type: The resource_type of this UserAuditLog.  # noqa: E501
        :type resource_type: str
        """

        self._resource_type = resource_type

    @property
    def status(self):
        """Gets the status of this UserAuditLog.  # noqa: E501


        :return: The status of this UserAuditLog.  # noqa: E501
        :rtype: UserAuditLogStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserAuditLog.


        :param status: The status of this UserAuditLog.  # noqa: E501
        :type status: UserAuditLogStatus
        """

        self._status = status

    @property
    def user(self):
        """Gets the user of this UserAuditLog.  # noqa: E501


        :return: The user of this UserAuditLog.  # noqa: E501
        :rtype: NestedUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserAuditLog.


        :param user: The user of this UserAuditLog.  # noqa: E501
        :type user: NestedUser
        """

        self._user = user

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
        if not isinstance(other, UserAuditLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAuditLog):
            return True

        return self.to_dict() != other.to_dict()
