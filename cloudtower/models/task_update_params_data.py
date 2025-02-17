# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class TaskUpdateParamsData(object):
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
        'finished_at': 'str',
        'started_at': 'str',
        'resource_rollback_retry_count': 'int',
        'resource_rollback_error': 'str',
        'resource_rollbacked': 'bool',
        'steps': 'list[TaskStepCreationParams]',
        'error_message': 'str',
        'error_code': 'str',
        'progress': 'float',
        'status': 'TaskStatus',
        'snapshot': 'str',
        'args': 'object',
        'key': 'str',
        'type': 'TaskType',
        'resource_id': 'str',
        'cluster_id': 'str',
        'user_id': 'str',
        'resource_mutation': 'str',
        'resource_type': 'str',
        'description': 'TaskDescription'
    }

    attribute_map = {
        'finished_at': 'finished_at',
        'started_at': 'started_at',
        'resource_rollback_retry_count': 'resource_rollback_retry_count',
        'resource_rollback_error': 'resource_rollback_error',
        'resource_rollbacked': 'resource_rollbacked',
        'steps': 'steps',
        'error_message': 'error_message',
        'error_code': 'error_code',
        'progress': 'progress',
        'status': 'status',
        'snapshot': 'snapshot',
        'args': 'args',
        'key': 'key',
        'type': 'type',
        'resource_id': 'resource_id',
        'cluster_id': 'cluster_id',
        'user_id': 'user_id',
        'resource_mutation': 'resource_mutation',
        'resource_type': 'resource_type',
        'description': 'description'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """TaskUpdateParamsData - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._finished_at = None
        self._started_at = None
        self._resource_rollback_retry_count = None
        self._resource_rollback_error = None
        self._resource_rollbacked = None
        self._steps = None
        self._error_message = None
        self._error_code = None
        self._progress = None
        self._status = None
        self._snapshot = None
        self._args = None
        self._key = None
        self._type = None
        self._resource_id = None
        self._cluster_id = None
        self._user_id = None
        self._resource_mutation = None
        self._resource_type = None
        self._description = None
        self.discriminator = None

        if "finished_at" in kwargs:
            self.finished_at = kwargs["finished_at"]
        if "started_at" in kwargs:
            self.started_at = kwargs["started_at"]
        if "resource_rollback_retry_count" in kwargs:
            self.resource_rollback_retry_count = kwargs["resource_rollback_retry_count"]
        if "resource_rollback_error" in kwargs:
            self.resource_rollback_error = kwargs["resource_rollback_error"]
        if "resource_rollbacked" in kwargs:
            self.resource_rollbacked = kwargs["resource_rollbacked"]
        if "steps" in kwargs:
            self.steps = kwargs["steps"]
        if "error_message" in kwargs:
            self.error_message = kwargs["error_message"]
        if "error_code" in kwargs:
            self.error_code = kwargs["error_code"]
        if "progress" in kwargs:
            self.progress = kwargs["progress"]
        if "status" in kwargs:
            self.status = kwargs["status"]
        if "snapshot" in kwargs:
            self.snapshot = kwargs["snapshot"]
        if "args" in kwargs:
            self.args = kwargs["args"]
        if "key" in kwargs:
            self.key = kwargs["key"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        if "resource_id" in kwargs:
            self.resource_id = kwargs["resource_id"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]
        if "user_id" in kwargs:
            self.user_id = kwargs["user_id"]
        if "resource_mutation" in kwargs:
            self.resource_mutation = kwargs["resource_mutation"]
        if "resource_type" in kwargs:
            self.resource_type = kwargs["resource_type"]
        if "description" in kwargs:
            self.description = kwargs["description"]

    @property
    def finished_at(self):
        """Gets the finished_at of this TaskUpdateParamsData.  # noqa: E501


        :return: The finished_at of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this TaskUpdateParamsData.


        :param finished_at: The finished_at of this TaskUpdateParamsData.  # noqa: E501
        :type finished_at: str
        """

        self._finished_at = finished_at

    @property
    def started_at(self):
        """Gets the started_at of this TaskUpdateParamsData.  # noqa: E501


        :return: The started_at of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this TaskUpdateParamsData.


        :param started_at: The started_at of this TaskUpdateParamsData.  # noqa: E501
        :type started_at: str
        """

        self._started_at = started_at

    @property
    def resource_rollback_retry_count(self):
        """Gets the resource_rollback_retry_count of this TaskUpdateParamsData.  # noqa: E501


        :return: The resource_rollback_retry_count of this TaskUpdateParamsData.  # noqa: E501
        :rtype: int
        """
        return self._resource_rollback_retry_count

    @resource_rollback_retry_count.setter
    def resource_rollback_retry_count(self, resource_rollback_retry_count):
        """Sets the resource_rollback_retry_count of this TaskUpdateParamsData.


        :param resource_rollback_retry_count: The resource_rollback_retry_count of this TaskUpdateParamsData.  # noqa: E501
        :type resource_rollback_retry_count: int
        """

        self._resource_rollback_retry_count = resource_rollback_retry_count

    @property
    def resource_rollback_error(self):
        """Gets the resource_rollback_error of this TaskUpdateParamsData.  # noqa: E501


        :return: The resource_rollback_error of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_rollback_error

    @resource_rollback_error.setter
    def resource_rollback_error(self, resource_rollback_error):
        """Sets the resource_rollback_error of this TaskUpdateParamsData.


        :param resource_rollback_error: The resource_rollback_error of this TaskUpdateParamsData.  # noqa: E501
        :type resource_rollback_error: str
        """

        self._resource_rollback_error = resource_rollback_error

    @property
    def resource_rollbacked(self):
        """Gets the resource_rollbacked of this TaskUpdateParamsData.  # noqa: E501


        :return: The resource_rollbacked of this TaskUpdateParamsData.  # noqa: E501
        :rtype: bool
        """
        return self._resource_rollbacked

    @resource_rollbacked.setter
    def resource_rollbacked(self, resource_rollbacked):
        """Sets the resource_rollbacked of this TaskUpdateParamsData.


        :param resource_rollbacked: The resource_rollbacked of this TaskUpdateParamsData.  # noqa: E501
        :type resource_rollbacked: bool
        """

        self._resource_rollbacked = resource_rollbacked

    @property
    def steps(self):
        """Gets the steps of this TaskUpdateParamsData.  # noqa: E501


        :return: The steps of this TaskUpdateParamsData.  # noqa: E501
        :rtype: list[TaskStepCreationParams]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this TaskUpdateParamsData.


        :param steps: The steps of this TaskUpdateParamsData.  # noqa: E501
        :type steps: list[TaskStepCreationParams]
        """

        self._steps = steps

    @property
    def error_message(self):
        """Gets the error_message of this TaskUpdateParamsData.  # noqa: E501


        :return: The error_message of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this TaskUpdateParamsData.


        :param error_message: The error_message of this TaskUpdateParamsData.  # noqa: E501
        :type error_message: str
        """

        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this TaskUpdateParamsData.  # noqa: E501


        :return: The error_code of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this TaskUpdateParamsData.


        :param error_code: The error_code of this TaskUpdateParamsData.  # noqa: E501
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def progress(self):
        """Gets the progress of this TaskUpdateParamsData.  # noqa: E501


        :return: The progress of this TaskUpdateParamsData.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this TaskUpdateParamsData.


        :param progress: The progress of this TaskUpdateParamsData.  # noqa: E501
        :type progress: float
        """

        self._progress = progress

    @property
    def status(self):
        """Gets the status of this TaskUpdateParamsData.  # noqa: E501


        :return: The status of this TaskUpdateParamsData.  # noqa: E501
        :rtype: TaskStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskUpdateParamsData.


        :param status: The status of this TaskUpdateParamsData.  # noqa: E501
        :type status: TaskStatus
        """

        self._status = status

    @property
    def snapshot(self):
        """Gets the snapshot of this TaskUpdateParamsData.  # noqa: E501


        :return: The snapshot of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this TaskUpdateParamsData.


        :param snapshot: The snapshot of this TaskUpdateParamsData.  # noqa: E501
        :type snapshot: str
        """

        self._snapshot = snapshot

    @property
    def args(self):
        """Gets the args of this TaskUpdateParamsData.  # noqa: E501


        :return: The args of this TaskUpdateParamsData.  # noqa: E501
        :rtype: object
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this TaskUpdateParamsData.


        :param args: The args of this TaskUpdateParamsData.  # noqa: E501
        :type args: object
        """

        self._args = args

    @property
    def key(self):
        """Gets the key of this TaskUpdateParamsData.  # noqa: E501


        :return: The key of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TaskUpdateParamsData.


        :param key: The key of this TaskUpdateParamsData.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def type(self):
        """Gets the type of this TaskUpdateParamsData.  # noqa: E501


        :return: The type of this TaskUpdateParamsData.  # noqa: E501
        :rtype: TaskType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskUpdateParamsData.


        :param type: The type of this TaskUpdateParamsData.  # noqa: E501
        :type type: TaskType
        """

        self._type = type

    @property
    def resource_id(self):
        """Gets the resource_id of this TaskUpdateParamsData.  # noqa: E501


        :return: The resource_id of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this TaskUpdateParamsData.


        :param resource_id: The resource_id of this TaskUpdateParamsData.  # noqa: E501
        :type resource_id: str
        """

        self._resource_id = resource_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this TaskUpdateParamsData.  # noqa: E501


        :return: The cluster_id of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this TaskUpdateParamsData.


        :param cluster_id: The cluster_id of this TaskUpdateParamsData.  # noqa: E501
        :type cluster_id: str
        """

        self._cluster_id = cluster_id

    @property
    def user_id(self):
        """Gets the user_id of this TaskUpdateParamsData.  # noqa: E501


        :return: The user_id of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TaskUpdateParamsData.


        :param user_id: The user_id of this TaskUpdateParamsData.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def resource_mutation(self):
        """Gets the resource_mutation of this TaskUpdateParamsData.  # noqa: E501


        :return: The resource_mutation of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_mutation

    @resource_mutation.setter
    def resource_mutation(self, resource_mutation):
        """Sets the resource_mutation of this TaskUpdateParamsData.


        :param resource_mutation: The resource_mutation of this TaskUpdateParamsData.  # noqa: E501
        :type resource_mutation: str
        """

        self._resource_mutation = resource_mutation

    @property
    def resource_type(self):
        """Gets the resource_type of this TaskUpdateParamsData.  # noqa: E501


        :return: The resource_type of this TaskUpdateParamsData.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TaskUpdateParamsData.


        :param resource_type: The resource_type of this TaskUpdateParamsData.  # noqa: E501
        :type resource_type: str
        """

        self._resource_type = resource_type

    @property
    def description(self):
        """Gets the description of this TaskUpdateParamsData.  # noqa: E501


        :return: The description of this TaskUpdateParamsData.  # noqa: E501
        :rtype: TaskDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskUpdateParamsData.


        :param description: The description of this TaskUpdateParamsData.  # noqa: E501
        :type description: TaskDescription
        """

        self._description = description

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
        if not isinstance(other, TaskUpdateParamsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskUpdateParamsData):
            return True

        return self.to_dict() != other.to_dict()
