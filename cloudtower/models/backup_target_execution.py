# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class BackupTargetExecution(object):
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
        'backup_group': 'str',
        'backup_plan_execution': 'NestedBackupPlanExecution',
        'backup_restore_point': 'NestedBackupRestorePoint',
        'cluster_local_id': 'str',
        'duration': 'int',
        'entity_async_status': 'EntityAsyncStatus',
        'executed_at': 'str',
        'id': 'str',
        'local_id': 'str',
        'parent_backup': 'str',
        'read_bytes': 'int',
        'retry_times': 'int',
        'status': 'BackupExecutionStatus',
        'total_bytes': 'int',
        'type': 'BackupExecutionType',
        'vm': 'NestedVm',
        'vm_local_id': 'str',
        'vm_name': 'str'
    }

    attribute_map = {
        'backup_group': 'backup_group',
        'backup_plan_execution': 'backup_plan_execution',
        'backup_restore_point': 'backup_restore_point',
        'cluster_local_id': 'cluster_local_id',
        'duration': 'duration',
        'entity_async_status': 'entityAsyncStatus',
        'executed_at': 'executed_at',
        'id': 'id',
        'local_id': 'local_id',
        'parent_backup': 'parent_backup',
        'read_bytes': 'read_bytes',
        'retry_times': 'retry_times',
        'status': 'status',
        'total_bytes': 'total_bytes',
        'type': 'type',
        'vm': 'vm',
        'vm_local_id': 'vm_local_id',
        'vm_name': 'vm_name'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BackupTargetExecution - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._backup_group = None
        self._backup_plan_execution = None
        self._backup_restore_point = None
        self._cluster_local_id = None
        self._duration = None
        self._entity_async_status = None
        self._executed_at = None
        self._id = None
        self._local_id = None
        self._parent_backup = None
        self._read_bytes = None
        self._retry_times = None
        self._status = None
        self._total_bytes = None
        self._type = None
        self._vm = None
        self._vm_local_id = None
        self._vm_name = None
        self.discriminator = None

        if "backup_group" in kwargs:
            self.backup_group = kwargs["backup_group"]
        self.backup_plan_execution = kwargs.get("backup_plan_execution", None)
        self.backup_restore_point = kwargs.get("backup_restore_point", None)
        self.cluster_local_id = kwargs.get("cluster_local_id", None)
        self.duration = kwargs.get("duration", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "executed_at" in kwargs:
            self.executed_at = kwargs["executed_at"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "parent_backup" in kwargs:
            self.parent_backup = kwargs["parent_backup"]
        self.read_bytes = kwargs.get("read_bytes", None)
        self.retry_times = kwargs.get("retry_times", None)
        self.status = kwargs.get("status", None)
        self.total_bytes = kwargs.get("total_bytes", None)
        if "type" in kwargs:
            self.type = kwargs["type"]
        self.vm = kwargs.get("vm", None)
        self.vm_local_id = kwargs.get("vm_local_id", None)
        self.vm_name = kwargs.get("vm_name", None)

    @property
    def backup_group(self):
        """Gets the backup_group of this BackupTargetExecution.  # noqa: E501


        :return: The backup_group of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._backup_group

    @backup_group.setter
    def backup_group(self, backup_group):
        """Sets the backup_group of this BackupTargetExecution.


        :param backup_group: The backup_group of this BackupTargetExecution.  # noqa: E501
        :type backup_group: str
        """
        if self.local_vars_configuration.client_side_validation and backup_group is None:  # noqa: E501
            raise ValueError("Invalid value for `backup_group`, must not be `None`")  # noqa: E501

        self._backup_group = backup_group

    @property
    def backup_plan_execution(self):
        """Gets the backup_plan_execution of this BackupTargetExecution.  # noqa: E501


        :return: The backup_plan_execution of this BackupTargetExecution.  # noqa: E501
        :rtype: NestedBackupPlanExecution
        """
        return self._backup_plan_execution

    @backup_plan_execution.setter
    def backup_plan_execution(self, backup_plan_execution):
        """Sets the backup_plan_execution of this BackupTargetExecution.


        :param backup_plan_execution: The backup_plan_execution of this BackupTargetExecution.  # noqa: E501
        :type backup_plan_execution: NestedBackupPlanExecution
        """

        self._backup_plan_execution = backup_plan_execution

    @property
    def backup_restore_point(self):
        """Gets the backup_restore_point of this BackupTargetExecution.  # noqa: E501


        :return: The backup_restore_point of this BackupTargetExecution.  # noqa: E501
        :rtype: NestedBackupRestorePoint
        """
        return self._backup_restore_point

    @backup_restore_point.setter
    def backup_restore_point(self, backup_restore_point):
        """Sets the backup_restore_point of this BackupTargetExecution.


        :param backup_restore_point: The backup_restore_point of this BackupTargetExecution.  # noqa: E501
        :type backup_restore_point: NestedBackupRestorePoint
        """

        self._backup_restore_point = backup_restore_point

    @property
    def cluster_local_id(self):
        """Gets the cluster_local_id of this BackupTargetExecution.  # noqa: E501


        :return: The cluster_local_id of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._cluster_local_id

    @cluster_local_id.setter
    def cluster_local_id(self, cluster_local_id):
        """Sets the cluster_local_id of this BackupTargetExecution.


        :param cluster_local_id: The cluster_local_id of this BackupTargetExecution.  # noqa: E501
        :type cluster_local_id: str
        """

        self._cluster_local_id = cluster_local_id

    @property
    def duration(self):
        """Gets the duration of this BackupTargetExecution.  # noqa: E501


        :return: The duration of this BackupTargetExecution.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this BackupTargetExecution.


        :param duration: The duration of this BackupTargetExecution.  # noqa: E501
        :type duration: int
        """

        self._duration = duration

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this BackupTargetExecution.  # noqa: E501


        :return: The entity_async_status of this BackupTargetExecution.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this BackupTargetExecution.


        :param entity_async_status: The entity_async_status of this BackupTargetExecution.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def executed_at(self):
        """Gets the executed_at of this BackupTargetExecution.  # noqa: E501


        :return: The executed_at of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._executed_at

    @executed_at.setter
    def executed_at(self, executed_at):
        """Sets the executed_at of this BackupTargetExecution.


        :param executed_at: The executed_at of this BackupTargetExecution.  # noqa: E501
        :type executed_at: str
        """
        if self.local_vars_configuration.client_side_validation and executed_at is None:  # noqa: E501
            raise ValueError("Invalid value for `executed_at`, must not be `None`")  # noqa: E501

        self._executed_at = executed_at

    @property
    def id(self):
        """Gets the id of this BackupTargetExecution.  # noqa: E501


        :return: The id of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupTargetExecution.


        :param id: The id of this BackupTargetExecution.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def local_id(self):
        """Gets the local_id of this BackupTargetExecution.  # noqa: E501


        :return: The local_id of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this BackupTargetExecution.


        :param local_id: The local_id of this BackupTargetExecution.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def parent_backup(self):
        """Gets the parent_backup of this BackupTargetExecution.  # noqa: E501


        :return: The parent_backup of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._parent_backup

    @parent_backup.setter
    def parent_backup(self, parent_backup):
        """Sets the parent_backup of this BackupTargetExecution.


        :param parent_backup: The parent_backup of this BackupTargetExecution.  # noqa: E501
        :type parent_backup: str
        """
        if self.local_vars_configuration.client_side_validation and parent_backup is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_backup`, must not be `None`")  # noqa: E501

        self._parent_backup = parent_backup

    @property
    def read_bytes(self):
        """Gets the read_bytes of this BackupTargetExecution.  # noqa: E501


        :return: The read_bytes of this BackupTargetExecution.  # noqa: E501
        :rtype: int
        """
        return self._read_bytes

    @read_bytes.setter
    def read_bytes(self, read_bytes):
        """Sets the read_bytes of this BackupTargetExecution.


        :param read_bytes: The read_bytes of this BackupTargetExecution.  # noqa: E501
        :type read_bytes: int
        """

        self._read_bytes = read_bytes

    @property
    def retry_times(self):
        """Gets the retry_times of this BackupTargetExecution.  # noqa: E501


        :return: The retry_times of this BackupTargetExecution.  # noqa: E501
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        """Sets the retry_times of this BackupTargetExecution.


        :param retry_times: The retry_times of this BackupTargetExecution.  # noqa: E501
        :type retry_times: int
        """

        self._retry_times = retry_times

    @property
    def status(self):
        """Gets the status of this BackupTargetExecution.  # noqa: E501


        :return: The status of this BackupTargetExecution.  # noqa: E501
        :rtype: BackupExecutionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupTargetExecution.


        :param status: The status of this BackupTargetExecution.  # noqa: E501
        :type status: BackupExecutionStatus
        """

        self._status = status

    @property
    def total_bytes(self):
        """Gets the total_bytes of this BackupTargetExecution.  # noqa: E501


        :return: The total_bytes of this BackupTargetExecution.  # noqa: E501
        :rtype: int
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """Sets the total_bytes of this BackupTargetExecution.


        :param total_bytes: The total_bytes of this BackupTargetExecution.  # noqa: E501
        :type total_bytes: int
        """

        self._total_bytes = total_bytes

    @property
    def type(self):
        """Gets the type of this BackupTargetExecution.  # noqa: E501


        :return: The type of this BackupTargetExecution.  # noqa: E501
        :rtype: BackupExecutionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupTargetExecution.


        :param type: The type of this BackupTargetExecution.  # noqa: E501
        :type type: BackupExecutionType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def vm(self):
        """Gets the vm of this BackupTargetExecution.  # noqa: E501


        :return: The vm of this BackupTargetExecution.  # noqa: E501
        :rtype: NestedVm
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this BackupTargetExecution.


        :param vm: The vm of this BackupTargetExecution.  # noqa: E501
        :type vm: NestedVm
        """

        self._vm = vm

    @property
    def vm_local_id(self):
        """Gets the vm_local_id of this BackupTargetExecution.  # noqa: E501


        :return: The vm_local_id of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._vm_local_id

    @vm_local_id.setter
    def vm_local_id(self, vm_local_id):
        """Sets the vm_local_id of this BackupTargetExecution.


        :param vm_local_id: The vm_local_id of this BackupTargetExecution.  # noqa: E501
        :type vm_local_id: str
        """

        self._vm_local_id = vm_local_id

    @property
    def vm_name(self):
        """Gets the vm_name of this BackupTargetExecution.  # noqa: E501


        :return: The vm_name of this BackupTargetExecution.  # noqa: E501
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this BackupTargetExecution.


        :param vm_name: The vm_name of this BackupTargetExecution.  # noqa: E501
        :type vm_name: str
        """

        self._vm_name = vm_name

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
        if not isinstance(other, BackupTargetExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupTargetExecution):
            return True

        return self.to_dict() != other.to_dict()