# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class BackupService(object):
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
        'application': 'NestedCloudTowerApplication',
        'backup_clusters': 'list[NestedCluster]',
        'backup_network_gateway': 'str',
        'backup_network_ip': 'str',
        'backup_network_subnet_mask': 'str',
        'backup_network_type': 'BackupServiceNetworkType',
        'backup_network_vlan': 'str',
        'backup_plans': 'list[NestedBackupPlan]',
        'backup_rd_iops_max': 'int',
        'backup_store_repositories': 'list[NestedBackupStoreRepository]',
        'backup_wr_iops_max': 'int',
        'description': 'str',
        'entity_async_status': 'EntityAsyncStatus',
        'id': 'str',
        'kube_config': 'str',
        'management_network_gateway': 'str',
        'management_network_ip': 'str',
        'management_network_subnet_mask': 'str',
        'management_network_vlan': 'str',
        'max_job_retry_times': 'int',
        'max_parallel_backup_jobs': 'int',
        'max_parallel_restore_jobs': 'int',
        'name': 'str',
        'network_status': 'list[NestedBackupServiceNetworkStatus]',
        'restore_rd_iops_max': 'int',
        'restore_wr_iops_max': 'int',
        'retry_interval': 'int',
        'running_vm': 'NestedVm',
        'status': 'BackupServiceStatus',
        'storage_network_gateway': 'str',
        'storage_network_ip': 'str',
        'storage_network_subnet_mask': 'str',
        'storage_network_type': 'BackupServiceNetworkType',
        'storage_network_vlan': 'str'
    }

    attribute_map = {
        'application': 'application',
        'backup_clusters': 'backup_clusters',
        'backup_network_gateway': 'backup_network_gateway',
        'backup_network_ip': 'backup_network_ip',
        'backup_network_subnet_mask': 'backup_network_subnet_mask',
        'backup_network_type': 'backup_network_type',
        'backup_network_vlan': 'backup_network_vlan',
        'backup_plans': 'backup_plans',
        'backup_rd_iops_max': 'backup_rd_iops_max',
        'backup_store_repositories': 'backup_store_repositories',
        'backup_wr_iops_max': 'backup_wr_iops_max',
        'description': 'description',
        'entity_async_status': 'entityAsyncStatus',
        'id': 'id',
        'kube_config': 'kube_config',
        'management_network_gateway': 'management_network_gateway',
        'management_network_ip': 'management_network_ip',
        'management_network_subnet_mask': 'management_network_subnet_mask',
        'management_network_vlan': 'management_network_vlan',
        'max_job_retry_times': 'max_job_retry_times',
        'max_parallel_backup_jobs': 'max_parallel_backup_jobs',
        'max_parallel_restore_jobs': 'max_parallel_restore_jobs',
        'name': 'name',
        'network_status': 'network_status',
        'restore_rd_iops_max': 'restore_rd_iops_max',
        'restore_wr_iops_max': 'restore_wr_iops_max',
        'retry_interval': 'retry_interval',
        'running_vm': 'running_vm',
        'status': 'status',
        'storage_network_gateway': 'storage_network_gateway',
        'storage_network_ip': 'storage_network_ip',
        'storage_network_subnet_mask': 'storage_network_subnet_mask',
        'storage_network_type': 'storage_network_type',
        'storage_network_vlan': 'storage_network_vlan'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """BackupService - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._application = None
        self._backup_clusters = None
        self._backup_network_gateway = None
        self._backup_network_ip = None
        self._backup_network_subnet_mask = None
        self._backup_network_type = None
        self._backup_network_vlan = None
        self._backup_plans = None
        self._backup_rd_iops_max = None
        self._backup_store_repositories = None
        self._backup_wr_iops_max = None
        self._description = None
        self._entity_async_status = None
        self._id = None
        self._kube_config = None
        self._management_network_gateway = None
        self._management_network_ip = None
        self._management_network_subnet_mask = None
        self._management_network_vlan = None
        self._max_job_retry_times = None
        self._max_parallel_backup_jobs = None
        self._max_parallel_restore_jobs = None
        self._name = None
        self._network_status = None
        self._restore_rd_iops_max = None
        self._restore_wr_iops_max = None
        self._retry_interval = None
        self._running_vm = None
        self._status = None
        self._storage_network_gateway = None
        self._storage_network_ip = None
        self._storage_network_subnet_mask = None
        self._storage_network_type = None
        self._storage_network_vlan = None
        self.discriminator = None

        self.application = kwargs.get("application", None)
        self.backup_clusters = kwargs.get("backup_clusters", None)
        self.backup_network_gateway = kwargs.get("backup_network_gateway", None)
        self.backup_network_ip = kwargs.get("backup_network_ip", None)
        self.backup_network_subnet_mask = kwargs.get("backup_network_subnet_mask", None)
        self.backup_network_type = kwargs.get("backup_network_type", None)
        self.backup_network_vlan = kwargs.get("backup_network_vlan", None)
        self.backup_plans = kwargs.get("backup_plans", None)
        self.backup_rd_iops_max = kwargs.get("backup_rd_iops_max", None)
        self.backup_store_repositories = kwargs.get("backup_store_repositories", None)
        self.backup_wr_iops_max = kwargs.get("backup_wr_iops_max", None)
        self.description = kwargs.get("description", None)
        self.entity_async_status = kwargs.get("entity_async_status", None)
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "kube_config" in kwargs:
            self.kube_config = kwargs["kube_config"]
        self.management_network_gateway = kwargs.get("management_network_gateway", None)
        self.management_network_ip = kwargs.get("management_network_ip", None)
        self.management_network_subnet_mask = kwargs.get("management_network_subnet_mask", None)
        self.management_network_vlan = kwargs.get("management_network_vlan", None)
        self.max_job_retry_times = kwargs.get("max_job_retry_times", None)
        self.max_parallel_backup_jobs = kwargs.get("max_parallel_backup_jobs", None)
        self.max_parallel_restore_jobs = kwargs.get("max_parallel_restore_jobs", None)
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.network_status = kwargs.get("network_status", None)
        self.restore_rd_iops_max = kwargs.get("restore_rd_iops_max", None)
        self.restore_wr_iops_max = kwargs.get("restore_wr_iops_max", None)
        self.retry_interval = kwargs.get("retry_interval", None)
        self.running_vm = kwargs.get("running_vm", None)
        self.status = kwargs.get("status", None)
        self.storage_network_gateway = kwargs.get("storage_network_gateway", None)
        self.storage_network_ip = kwargs.get("storage_network_ip", None)
        self.storage_network_subnet_mask = kwargs.get("storage_network_subnet_mask", None)
        self.storage_network_type = kwargs.get("storage_network_type", None)
        self.storage_network_vlan = kwargs.get("storage_network_vlan", None)

    @property
    def application(self):
        """Gets the application of this BackupService.  # noqa: E501


        :return: The application of this BackupService.  # noqa: E501
        :rtype: NestedCloudTowerApplication
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this BackupService.


        :param application: The application of this BackupService.  # noqa: E501
        :type application: NestedCloudTowerApplication
        """

        self._application = application

    @property
    def backup_clusters(self):
        """Gets the backup_clusters of this BackupService.  # noqa: E501


        :return: The backup_clusters of this BackupService.  # noqa: E501
        :rtype: list[NestedCluster]
        """
        return self._backup_clusters

    @backup_clusters.setter
    def backup_clusters(self, backup_clusters):
        """Sets the backup_clusters of this BackupService.


        :param backup_clusters: The backup_clusters of this BackupService.  # noqa: E501
        :type backup_clusters: list[NestedCluster]
        """

        self._backup_clusters = backup_clusters

    @property
    def backup_network_gateway(self):
        """Gets the backup_network_gateway of this BackupService.  # noqa: E501


        :return: The backup_network_gateway of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._backup_network_gateway

    @backup_network_gateway.setter
    def backup_network_gateway(self, backup_network_gateway):
        """Sets the backup_network_gateway of this BackupService.


        :param backup_network_gateway: The backup_network_gateway of this BackupService.  # noqa: E501
        :type backup_network_gateway: str
        """

        self._backup_network_gateway = backup_network_gateway

    @property
    def backup_network_ip(self):
        """Gets the backup_network_ip of this BackupService.  # noqa: E501


        :return: The backup_network_ip of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._backup_network_ip

    @backup_network_ip.setter
    def backup_network_ip(self, backup_network_ip):
        """Sets the backup_network_ip of this BackupService.


        :param backup_network_ip: The backup_network_ip of this BackupService.  # noqa: E501
        :type backup_network_ip: str
        """

        self._backup_network_ip = backup_network_ip

    @property
    def backup_network_subnet_mask(self):
        """Gets the backup_network_subnet_mask of this BackupService.  # noqa: E501


        :return: The backup_network_subnet_mask of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._backup_network_subnet_mask

    @backup_network_subnet_mask.setter
    def backup_network_subnet_mask(self, backup_network_subnet_mask):
        """Sets the backup_network_subnet_mask of this BackupService.


        :param backup_network_subnet_mask: The backup_network_subnet_mask of this BackupService.  # noqa: E501
        :type backup_network_subnet_mask: str
        """

        self._backup_network_subnet_mask = backup_network_subnet_mask

    @property
    def backup_network_type(self):
        """Gets the backup_network_type of this BackupService.  # noqa: E501


        :return: The backup_network_type of this BackupService.  # noqa: E501
        :rtype: BackupServiceNetworkType
        """
        return self._backup_network_type

    @backup_network_type.setter
    def backup_network_type(self, backup_network_type):
        """Sets the backup_network_type of this BackupService.


        :param backup_network_type: The backup_network_type of this BackupService.  # noqa: E501
        :type backup_network_type: BackupServiceNetworkType
        """

        self._backup_network_type = backup_network_type

    @property
    def backup_network_vlan(self):
        """Gets the backup_network_vlan of this BackupService.  # noqa: E501


        :return: The backup_network_vlan of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._backup_network_vlan

    @backup_network_vlan.setter
    def backup_network_vlan(self, backup_network_vlan):
        """Sets the backup_network_vlan of this BackupService.


        :param backup_network_vlan: The backup_network_vlan of this BackupService.  # noqa: E501
        :type backup_network_vlan: str
        """

        self._backup_network_vlan = backup_network_vlan

    @property
    def backup_plans(self):
        """Gets the backup_plans of this BackupService.  # noqa: E501


        :return: The backup_plans of this BackupService.  # noqa: E501
        :rtype: list[NestedBackupPlan]
        """
        return self._backup_plans

    @backup_plans.setter
    def backup_plans(self, backup_plans):
        """Sets the backup_plans of this BackupService.


        :param backup_plans: The backup_plans of this BackupService.  # noqa: E501
        :type backup_plans: list[NestedBackupPlan]
        """

        self._backup_plans = backup_plans

    @property
    def backup_rd_iops_max(self):
        """Gets the backup_rd_iops_max of this BackupService.  # noqa: E501


        :return: The backup_rd_iops_max of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._backup_rd_iops_max

    @backup_rd_iops_max.setter
    def backup_rd_iops_max(self, backup_rd_iops_max):
        """Sets the backup_rd_iops_max of this BackupService.


        :param backup_rd_iops_max: The backup_rd_iops_max of this BackupService.  # noqa: E501
        :type backup_rd_iops_max: int
        """

        self._backup_rd_iops_max = backup_rd_iops_max

    @property
    def backup_store_repositories(self):
        """Gets the backup_store_repositories of this BackupService.  # noqa: E501


        :return: The backup_store_repositories of this BackupService.  # noqa: E501
        :rtype: list[NestedBackupStoreRepository]
        """
        return self._backup_store_repositories

    @backup_store_repositories.setter
    def backup_store_repositories(self, backup_store_repositories):
        """Sets the backup_store_repositories of this BackupService.


        :param backup_store_repositories: The backup_store_repositories of this BackupService.  # noqa: E501
        :type backup_store_repositories: list[NestedBackupStoreRepository]
        """

        self._backup_store_repositories = backup_store_repositories

    @property
    def backup_wr_iops_max(self):
        """Gets the backup_wr_iops_max of this BackupService.  # noqa: E501


        :return: The backup_wr_iops_max of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._backup_wr_iops_max

    @backup_wr_iops_max.setter
    def backup_wr_iops_max(self, backup_wr_iops_max):
        """Sets the backup_wr_iops_max of this BackupService.


        :param backup_wr_iops_max: The backup_wr_iops_max of this BackupService.  # noqa: E501
        :type backup_wr_iops_max: int
        """

        self._backup_wr_iops_max = backup_wr_iops_max

    @property
    def description(self):
        """Gets the description of this BackupService.  # noqa: E501


        :return: The description of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackupService.


        :param description: The description of this BackupService.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def entity_async_status(self):
        """Gets the entity_async_status of this BackupService.  # noqa: E501


        :return: The entity_async_status of this BackupService.  # noqa: E501
        :rtype: EntityAsyncStatus
        """
        return self._entity_async_status

    @entity_async_status.setter
    def entity_async_status(self, entity_async_status):
        """Sets the entity_async_status of this BackupService.


        :param entity_async_status: The entity_async_status of this BackupService.  # noqa: E501
        :type entity_async_status: EntityAsyncStatus
        """

        self._entity_async_status = entity_async_status

    @property
    def id(self):
        """Gets the id of this BackupService.  # noqa: E501


        :return: The id of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupService.


        :param id: The id of this BackupService.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def kube_config(self):
        """Gets the kube_config of this BackupService.  # noqa: E501


        :return: The kube_config of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._kube_config

    @kube_config.setter
    def kube_config(self, kube_config):
        """Sets the kube_config of this BackupService.


        :param kube_config: The kube_config of this BackupService.  # noqa: E501
        :type kube_config: str
        """
        if self.local_vars_configuration.client_side_validation and kube_config is None:  # noqa: E501
            raise ValueError("Invalid value for `kube_config`, must not be `None`")  # noqa: E501

        self._kube_config = kube_config

    @property
    def management_network_gateway(self):
        """Gets the management_network_gateway of this BackupService.  # noqa: E501


        :return: The management_network_gateway of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._management_network_gateway

    @management_network_gateway.setter
    def management_network_gateway(self, management_network_gateway):
        """Sets the management_network_gateway of this BackupService.


        :param management_network_gateway: The management_network_gateway of this BackupService.  # noqa: E501
        :type management_network_gateway: str
        """

        self._management_network_gateway = management_network_gateway

    @property
    def management_network_ip(self):
        """Gets the management_network_ip of this BackupService.  # noqa: E501


        :return: The management_network_ip of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._management_network_ip

    @management_network_ip.setter
    def management_network_ip(self, management_network_ip):
        """Sets the management_network_ip of this BackupService.


        :param management_network_ip: The management_network_ip of this BackupService.  # noqa: E501
        :type management_network_ip: str
        """

        self._management_network_ip = management_network_ip

    @property
    def management_network_subnet_mask(self):
        """Gets the management_network_subnet_mask of this BackupService.  # noqa: E501


        :return: The management_network_subnet_mask of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._management_network_subnet_mask

    @management_network_subnet_mask.setter
    def management_network_subnet_mask(self, management_network_subnet_mask):
        """Sets the management_network_subnet_mask of this BackupService.


        :param management_network_subnet_mask: The management_network_subnet_mask of this BackupService.  # noqa: E501
        :type management_network_subnet_mask: str
        """

        self._management_network_subnet_mask = management_network_subnet_mask

    @property
    def management_network_vlan(self):
        """Gets the management_network_vlan of this BackupService.  # noqa: E501


        :return: The management_network_vlan of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._management_network_vlan

    @management_network_vlan.setter
    def management_network_vlan(self, management_network_vlan):
        """Sets the management_network_vlan of this BackupService.


        :param management_network_vlan: The management_network_vlan of this BackupService.  # noqa: E501
        :type management_network_vlan: str
        """

        self._management_network_vlan = management_network_vlan

    @property
    def max_job_retry_times(self):
        """Gets the max_job_retry_times of this BackupService.  # noqa: E501


        :return: The max_job_retry_times of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._max_job_retry_times

    @max_job_retry_times.setter
    def max_job_retry_times(self, max_job_retry_times):
        """Sets the max_job_retry_times of this BackupService.


        :param max_job_retry_times: The max_job_retry_times of this BackupService.  # noqa: E501
        :type max_job_retry_times: int
        """

        self._max_job_retry_times = max_job_retry_times

    @property
    def max_parallel_backup_jobs(self):
        """Gets the max_parallel_backup_jobs of this BackupService.  # noqa: E501


        :return: The max_parallel_backup_jobs of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._max_parallel_backup_jobs

    @max_parallel_backup_jobs.setter
    def max_parallel_backup_jobs(self, max_parallel_backup_jobs):
        """Sets the max_parallel_backup_jobs of this BackupService.


        :param max_parallel_backup_jobs: The max_parallel_backup_jobs of this BackupService.  # noqa: E501
        :type max_parallel_backup_jobs: int
        """

        self._max_parallel_backup_jobs = max_parallel_backup_jobs

    @property
    def max_parallel_restore_jobs(self):
        """Gets the max_parallel_restore_jobs of this BackupService.  # noqa: E501


        :return: The max_parallel_restore_jobs of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._max_parallel_restore_jobs

    @max_parallel_restore_jobs.setter
    def max_parallel_restore_jobs(self, max_parallel_restore_jobs):
        """Sets the max_parallel_restore_jobs of this BackupService.


        :param max_parallel_restore_jobs: The max_parallel_restore_jobs of this BackupService.  # noqa: E501
        :type max_parallel_restore_jobs: int
        """

        self._max_parallel_restore_jobs = max_parallel_restore_jobs

    @property
    def name(self):
        """Gets the name of this BackupService.  # noqa: E501


        :return: The name of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupService.


        :param name: The name of this BackupService.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def network_status(self):
        """Gets the network_status of this BackupService.  # noqa: E501


        :return: The network_status of this BackupService.  # noqa: E501
        :rtype: list[NestedBackupServiceNetworkStatus]
        """
        return self._network_status

    @network_status.setter
    def network_status(self, network_status):
        """Sets the network_status of this BackupService.


        :param network_status: The network_status of this BackupService.  # noqa: E501
        :type network_status: list[NestedBackupServiceNetworkStatus]
        """

        self._network_status = network_status

    @property
    def restore_rd_iops_max(self):
        """Gets the restore_rd_iops_max of this BackupService.  # noqa: E501


        :return: The restore_rd_iops_max of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._restore_rd_iops_max

    @restore_rd_iops_max.setter
    def restore_rd_iops_max(self, restore_rd_iops_max):
        """Sets the restore_rd_iops_max of this BackupService.


        :param restore_rd_iops_max: The restore_rd_iops_max of this BackupService.  # noqa: E501
        :type restore_rd_iops_max: int
        """

        self._restore_rd_iops_max = restore_rd_iops_max

    @property
    def restore_wr_iops_max(self):
        """Gets the restore_wr_iops_max of this BackupService.  # noqa: E501


        :return: The restore_wr_iops_max of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._restore_wr_iops_max

    @restore_wr_iops_max.setter
    def restore_wr_iops_max(self, restore_wr_iops_max):
        """Sets the restore_wr_iops_max of this BackupService.


        :param restore_wr_iops_max: The restore_wr_iops_max of this BackupService.  # noqa: E501
        :type restore_wr_iops_max: int
        """

        self._restore_wr_iops_max = restore_wr_iops_max

    @property
    def retry_interval(self):
        """Gets the retry_interval of this BackupService.  # noqa: E501


        :return: The retry_interval of this BackupService.  # noqa: E501
        :rtype: int
        """
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, retry_interval):
        """Sets the retry_interval of this BackupService.


        :param retry_interval: The retry_interval of this BackupService.  # noqa: E501
        :type retry_interval: int
        """

        self._retry_interval = retry_interval

    @property
    def running_vm(self):
        """Gets the running_vm of this BackupService.  # noqa: E501


        :return: The running_vm of this BackupService.  # noqa: E501
        :rtype: NestedVm
        """
        return self._running_vm

    @running_vm.setter
    def running_vm(self, running_vm):
        """Sets the running_vm of this BackupService.


        :param running_vm: The running_vm of this BackupService.  # noqa: E501
        :type running_vm: NestedVm
        """

        self._running_vm = running_vm

    @property
    def status(self):
        """Gets the status of this BackupService.  # noqa: E501


        :return: The status of this BackupService.  # noqa: E501
        :rtype: BackupServiceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupService.


        :param status: The status of this BackupService.  # noqa: E501
        :type status: BackupServiceStatus
        """

        self._status = status

    @property
    def storage_network_gateway(self):
        """Gets the storage_network_gateway of this BackupService.  # noqa: E501


        :return: The storage_network_gateway of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._storage_network_gateway

    @storage_network_gateway.setter
    def storage_network_gateway(self, storage_network_gateway):
        """Sets the storage_network_gateway of this BackupService.


        :param storage_network_gateway: The storage_network_gateway of this BackupService.  # noqa: E501
        :type storage_network_gateway: str
        """

        self._storage_network_gateway = storage_network_gateway

    @property
    def storage_network_ip(self):
        """Gets the storage_network_ip of this BackupService.  # noqa: E501


        :return: The storage_network_ip of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._storage_network_ip

    @storage_network_ip.setter
    def storage_network_ip(self, storage_network_ip):
        """Sets the storage_network_ip of this BackupService.


        :param storage_network_ip: The storage_network_ip of this BackupService.  # noqa: E501
        :type storage_network_ip: str
        """

        self._storage_network_ip = storage_network_ip

    @property
    def storage_network_subnet_mask(self):
        """Gets the storage_network_subnet_mask of this BackupService.  # noqa: E501


        :return: The storage_network_subnet_mask of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._storage_network_subnet_mask

    @storage_network_subnet_mask.setter
    def storage_network_subnet_mask(self, storage_network_subnet_mask):
        """Sets the storage_network_subnet_mask of this BackupService.


        :param storage_network_subnet_mask: The storage_network_subnet_mask of this BackupService.  # noqa: E501
        :type storage_network_subnet_mask: str
        """

        self._storage_network_subnet_mask = storage_network_subnet_mask

    @property
    def storage_network_type(self):
        """Gets the storage_network_type of this BackupService.  # noqa: E501


        :return: The storage_network_type of this BackupService.  # noqa: E501
        :rtype: BackupServiceNetworkType
        """
        return self._storage_network_type

    @storage_network_type.setter
    def storage_network_type(self, storage_network_type):
        """Sets the storage_network_type of this BackupService.


        :param storage_network_type: The storage_network_type of this BackupService.  # noqa: E501
        :type storage_network_type: BackupServiceNetworkType
        """

        self._storage_network_type = storage_network_type

    @property
    def storage_network_vlan(self):
        """Gets the storage_network_vlan of this BackupService.  # noqa: E501


        :return: The storage_network_vlan of this BackupService.  # noqa: E501
        :rtype: str
        """
        return self._storage_network_vlan

    @storage_network_vlan.setter
    def storage_network_vlan(self, storage_network_vlan):
        """Sets the storage_network_vlan of this BackupService.


        :param storage_network_vlan: The storage_network_vlan of this BackupService.  # noqa: E501
        :type storage_network_vlan: str
        """

        self._storage_network_vlan = storage_network_vlan

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
        if not isinstance(other, BackupService):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackupService):
            return True

        return self.to_dict() != other.to_dict()
