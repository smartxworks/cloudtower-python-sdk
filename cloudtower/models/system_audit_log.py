# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class SystemAuditLog(object):
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
        'finished_at': 'str',
        'id': 'str',
        'local_created_at': 'str',
        'local_id': 'str',
        'message': 'str',
        'resource_id': 'str',
        'status': 'UserAuditLogStatus'
    }

    attribute_map = {
        'action': 'action',
        'cluster': 'cluster',
        'finished_at': 'finished_at',
        'id': 'id',
        'local_created_at': 'local_created_at',
        'local_id': 'local_id',
        'message': 'message',
        'resource_id': 'resource_id',
        'status': 'status'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SystemAuditLog - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._action = None
        self._cluster = None
        self._finished_at = None
        self._id = None
        self._local_created_at = None
        self._local_id = None
        self._message = None
        self._resource_id = None
        self._status = None
        self.discriminator = None

        if "action" in kwargs:
            self.action = kwargs["action"]
        self.cluster = kwargs.get("cluster", None)
        self.finished_at = kwargs.get("finished_at", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        self.local_created_at = kwargs.get("local_created_at", None)
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "message" in kwargs:
            self.message = kwargs["message"]
        self.resource_id = kwargs.get("resource_id", None)
        self.status = kwargs.get("status", None)

    @property
    def action(self):
        """Gets the action of this SystemAuditLog.  # noqa: E501


        :return: The action of this SystemAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this SystemAuditLog.


        :param action: The action of this SystemAuditLog.  # noqa: E501
        :type action: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def cluster(self):
        """Gets the cluster of this SystemAuditLog.  # noqa: E501


        :return: The cluster of this SystemAuditLog.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this SystemAuditLog.


        :param cluster: The cluster of this SystemAuditLog.  # noqa: E501
        :type cluster: NestedCluster
        """

        self._cluster = cluster

    @property
    def finished_at(self):
        """Gets the finished_at of this SystemAuditLog.  # noqa: E501


        :return: The finished_at of this SystemAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this SystemAuditLog.


        :param finished_at: The finished_at of this SystemAuditLog.  # noqa: E501
        :type finished_at: str
        """

        self._finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this SystemAuditLog.  # noqa: E501


        :return: The id of this SystemAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SystemAuditLog.


        :param id: The id of this SystemAuditLog.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_created_at(self):
        """Gets the local_created_at of this SystemAuditLog.  # noqa: E501


        :return: The local_created_at of this SystemAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._local_created_at

    @local_created_at.setter
    def local_created_at(self, local_created_at):
        """Sets the local_created_at of this SystemAuditLog.


        :param local_created_at: The local_created_at of this SystemAuditLog.  # noqa: E501
        :type local_created_at: str
        """

        self._local_created_at = local_created_at

    @property
    def local_id(self):
        """Gets the local_id of this SystemAuditLog.  # noqa: E501


        :return: The local_id of this SystemAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this SystemAuditLog.


        :param local_id: The local_id of this SystemAuditLog.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def message(self):
        """Gets the message of this SystemAuditLog.  # noqa: E501


        :return: The message of this SystemAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SystemAuditLog.


        :param message: The message of this SystemAuditLog.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def resource_id(self):
        """Gets the resource_id of this SystemAuditLog.  # noqa: E501


        :return: The resource_id of this SystemAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this SystemAuditLog.


        :param resource_id: The resource_id of this SystemAuditLog.  # noqa: E501
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def status(self):
        """Gets the status of this SystemAuditLog.  # noqa: E501


        :return: The status of this SystemAuditLog.  # noqa: E501
        :rtype: UserAuditLogStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SystemAuditLog.


        :param status: The status of this SystemAuditLog.  # noqa: E501
        :type status: UserAuditLogStatus
        """

        self._status = status

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
        if not isinstance(other, SystemAuditLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemAuditLog):
            return True

        return self.to_dict() != other.to_dict()
