# coding: utf-8

"""
    CloudTower APIs

    cloudtower operation API and SDK  # noqa: E501

    The version of the OpenAPI document: 2.2.0
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


class TableReporterParamsFilter(object):
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
        'nvmf_subsystems': 'GetNvmfSubsystemsRequestBody',
        'content_library_vm_templates': 'GetContentLibraryVmTemplatesRequestBody',
        'nvmf_namespace_snapshots': 'GetNvmfNamespaceSnapshotsRequestBody',
        'content_library_images': 'GetContentLibraryImagesRequestBody',
        'nvmf_namespaces': 'GetNvmfNamespacesRequestBody',
        'namespace_groups': 'GetNamespaceGroupsRequestBody',
        'iscsi_luns': 'GetIscsiLunsRequestBody',
        'tasks': 'GetTasksRequestBody',
        'user_audit_logs': 'GetUserAuditLogsRequestBody',
        'system_audit_logs': 'GetSystemAuditLogsRequestBody',
        'iscsi_lun_snapshots': 'GetIscsiLunSnapshotsRequestBody',
        'iscsi_connections': 'GetIscsiConnectionsRequestBody',
        'consistency_groups': 'GetConsistencyGroupsRequestBody',
        'users': 'GetUsersRequestBody',
        'vm_entity_filters': 'GetEntityFiltersRequestBody',
        'snapshot_plans': 'GetSnapshotPlansRequestBody',
        'global_alert_rules': 'GetGlobalAlertRulesRequestBody',
        'alerts': 'GetAlertsRequestBody',
        'vm_placement_groups': 'GetVmPlacementGroupsRequestBody',
        'vm_templates': 'GetVmTemplatesRequestBody',
        'elf_images': 'GetElfImagesRequestBody',
        'vm_volumes': 'GetVmVolumesRequestBody',
        'vlans': 'GetVlansRequestBody',
        'disks': 'GetDisksRequestBody',
        'vdses': 'GetVdsesRequestBody',
        'elf_data_stores': 'GetElfDataStoresRequestBody',
        'vms': 'GetVmsRequestBody',
        'nfs_exports': 'GetNfsExportsRequestBody',
        'iscsi_targets': 'GetIscsiTargetsRequestBody',
        'usb_devices': 'GetUsbDevicesRequestBody',
        'nics': 'GetNicsRequestBody',
        'clusters': 'GetClustersRequestBody',
        'datacenters': 'GetDatacentersRequestBody',
        'hosts': 'GetHostsRequestBody'
    }

    attribute_map = {
        'nvmf_subsystems': 'nvmfSubsystems',
        'content_library_vm_templates': 'contentLibraryVmTemplates',
        'nvmf_namespace_snapshots': 'nvmfNamespaceSnapshots',
        'content_library_images': 'contentLibraryImages',
        'nvmf_namespaces': 'nvmfNamespaces',
        'namespace_groups': 'namespaceGroups',
        'iscsi_luns': 'iscsiLuns',
        'tasks': 'tasks',
        'user_audit_logs': 'userAuditLogs',
        'system_audit_logs': 'systemAuditLogs',
        'iscsi_lun_snapshots': 'iscsiLunSnapshots',
        'iscsi_connections': 'iscsiConnections',
        'consistency_groups': 'consistencyGroups',
        'users': 'users',
        'vm_entity_filters': 'vmEntityFilters',
        'snapshot_plans': 'snapshotPlans',
        'global_alert_rules': 'globalAlertRules',
        'alerts': 'alerts',
        'vm_placement_groups': 'vmPlacementGroups',
        'vm_templates': 'vmTemplates',
        'elf_images': 'elfImages',
        'vm_volumes': 'vmVolumes',
        'vlans': 'vlans',
        'disks': 'disks',
        'vdses': 'vdses',
        'elf_data_stores': 'elfDataStores',
        'vms': 'vms',
        'nfs_exports': 'nfsExports',
        'iscsi_targets': 'iscsiTargets',
        'usb_devices': 'usbDevices',
        'nics': 'nics',
        'clusters': 'clusters',
        'datacenters': 'datacenters',
        'hosts': 'hosts'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """TableReporterParamsFilter - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._nvmf_subsystems = None
        self._content_library_vm_templates = None
        self._nvmf_namespace_snapshots = None
        self._content_library_images = None
        self._nvmf_namespaces = None
        self._namespace_groups = None
        self._iscsi_luns = None
        self._tasks = None
        self._user_audit_logs = None
        self._system_audit_logs = None
        self._iscsi_lun_snapshots = None
        self._iscsi_connections = None
        self._consistency_groups = None
        self._users = None
        self._vm_entity_filters = None
        self._snapshot_plans = None
        self._global_alert_rules = None
        self._alerts = None
        self._vm_placement_groups = None
        self._vm_templates = None
        self._elf_images = None
        self._vm_volumes = None
        self._vlans = None
        self._disks = None
        self._vdses = None
        self._elf_data_stores = None
        self._vms = None
        self._nfs_exports = None
        self._iscsi_targets = None
        self._usb_devices = None
        self._nics = None
        self._clusters = None
        self._datacenters = None
        self._hosts = None
        self.discriminator = None

        if "nvmf_subsystems" in kwargs:
            self.nvmf_subsystems = kwargs["nvmf_subsystems"]
        if "content_library_vm_templates" in kwargs:
            self.content_library_vm_templates = kwargs["content_library_vm_templates"]
        if "nvmf_namespace_snapshots" in kwargs:
            self.nvmf_namespace_snapshots = kwargs["nvmf_namespace_snapshots"]
        if "content_library_images" in kwargs:
            self.content_library_images = kwargs["content_library_images"]
        if "nvmf_namespaces" in kwargs:
            self.nvmf_namespaces = kwargs["nvmf_namespaces"]
        if "namespace_groups" in kwargs:
            self.namespace_groups = kwargs["namespace_groups"]
        if "iscsi_luns" in kwargs:
            self.iscsi_luns = kwargs["iscsi_luns"]
        if "tasks" in kwargs:
            self.tasks = kwargs["tasks"]
        if "user_audit_logs" in kwargs:
            self.user_audit_logs = kwargs["user_audit_logs"]
        if "system_audit_logs" in kwargs:
            self.system_audit_logs = kwargs["system_audit_logs"]
        if "iscsi_lun_snapshots" in kwargs:
            self.iscsi_lun_snapshots = kwargs["iscsi_lun_snapshots"]
        if "iscsi_connections" in kwargs:
            self.iscsi_connections = kwargs["iscsi_connections"]
        if "consistency_groups" in kwargs:
            self.consistency_groups = kwargs["consistency_groups"]
        if "users" in kwargs:
            self.users = kwargs["users"]
        if "vm_entity_filters" in kwargs:
            self.vm_entity_filters = kwargs["vm_entity_filters"]
        if "snapshot_plans" in kwargs:
            self.snapshot_plans = kwargs["snapshot_plans"]
        if "global_alert_rules" in kwargs:
            self.global_alert_rules = kwargs["global_alert_rules"]
        if "alerts" in kwargs:
            self.alerts = kwargs["alerts"]
        if "vm_placement_groups" in kwargs:
            self.vm_placement_groups = kwargs["vm_placement_groups"]
        if "vm_templates" in kwargs:
            self.vm_templates = kwargs["vm_templates"]
        if "elf_images" in kwargs:
            self.elf_images = kwargs["elf_images"]
        if "vm_volumes" in kwargs:
            self.vm_volumes = kwargs["vm_volumes"]
        if "vlans" in kwargs:
            self.vlans = kwargs["vlans"]
        if "disks" in kwargs:
            self.disks = kwargs["disks"]
        if "vdses" in kwargs:
            self.vdses = kwargs["vdses"]
        if "elf_data_stores" in kwargs:
            self.elf_data_stores = kwargs["elf_data_stores"]
        if "vms" in kwargs:
            self.vms = kwargs["vms"]
        if "nfs_exports" in kwargs:
            self.nfs_exports = kwargs["nfs_exports"]
        if "iscsi_targets" in kwargs:
            self.iscsi_targets = kwargs["iscsi_targets"]
        if "usb_devices" in kwargs:
            self.usb_devices = kwargs["usb_devices"]
        if "nics" in kwargs:
            self.nics = kwargs["nics"]
        if "clusters" in kwargs:
            self.clusters = kwargs["clusters"]
        if "datacenters" in kwargs:
            self.datacenters = kwargs["datacenters"]
        if "hosts" in kwargs:
            self.hosts = kwargs["hosts"]

    @property
    def nvmf_subsystems(self):
        """Gets the nvmf_subsystems of this TableReporterParamsFilter.  # noqa: E501


        :return: The nvmf_subsystems of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetNvmfSubsystemsRequestBody
        """
        return self._nvmf_subsystems

    @nvmf_subsystems.setter
    def nvmf_subsystems(self, nvmf_subsystems):
        """Sets the nvmf_subsystems of this TableReporterParamsFilter.


        :param nvmf_subsystems: The nvmf_subsystems of this TableReporterParamsFilter.  # noqa: E501
        :type nvmf_subsystems: GetNvmfSubsystemsRequestBody
        """

        self._nvmf_subsystems = nvmf_subsystems

    @property
    def content_library_vm_templates(self):
        """Gets the content_library_vm_templates of this TableReporterParamsFilter.  # noqa: E501


        :return: The content_library_vm_templates of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetContentLibraryVmTemplatesRequestBody
        """
        return self._content_library_vm_templates

    @content_library_vm_templates.setter
    def content_library_vm_templates(self, content_library_vm_templates):
        """Sets the content_library_vm_templates of this TableReporterParamsFilter.


        :param content_library_vm_templates: The content_library_vm_templates of this TableReporterParamsFilter.  # noqa: E501
        :type content_library_vm_templates: GetContentLibraryVmTemplatesRequestBody
        """

        self._content_library_vm_templates = content_library_vm_templates

    @property
    def nvmf_namespace_snapshots(self):
        """Gets the nvmf_namespace_snapshots of this TableReporterParamsFilter.  # noqa: E501


        :return: The nvmf_namespace_snapshots of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetNvmfNamespaceSnapshotsRequestBody
        """
        return self._nvmf_namespace_snapshots

    @nvmf_namespace_snapshots.setter
    def nvmf_namespace_snapshots(self, nvmf_namespace_snapshots):
        """Sets the nvmf_namespace_snapshots of this TableReporterParamsFilter.


        :param nvmf_namespace_snapshots: The nvmf_namespace_snapshots of this TableReporterParamsFilter.  # noqa: E501
        :type nvmf_namespace_snapshots: GetNvmfNamespaceSnapshotsRequestBody
        """

        self._nvmf_namespace_snapshots = nvmf_namespace_snapshots

    @property
    def content_library_images(self):
        """Gets the content_library_images of this TableReporterParamsFilter.  # noqa: E501


        :return: The content_library_images of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetContentLibraryImagesRequestBody
        """
        return self._content_library_images

    @content_library_images.setter
    def content_library_images(self, content_library_images):
        """Sets the content_library_images of this TableReporterParamsFilter.


        :param content_library_images: The content_library_images of this TableReporterParamsFilter.  # noqa: E501
        :type content_library_images: GetContentLibraryImagesRequestBody
        """

        self._content_library_images = content_library_images

    @property
    def nvmf_namespaces(self):
        """Gets the nvmf_namespaces of this TableReporterParamsFilter.  # noqa: E501


        :return: The nvmf_namespaces of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetNvmfNamespacesRequestBody
        """
        return self._nvmf_namespaces

    @nvmf_namespaces.setter
    def nvmf_namespaces(self, nvmf_namespaces):
        """Sets the nvmf_namespaces of this TableReporterParamsFilter.


        :param nvmf_namespaces: The nvmf_namespaces of this TableReporterParamsFilter.  # noqa: E501
        :type nvmf_namespaces: GetNvmfNamespacesRequestBody
        """

        self._nvmf_namespaces = nvmf_namespaces

    @property
    def namespace_groups(self):
        """Gets the namespace_groups of this TableReporterParamsFilter.  # noqa: E501


        :return: The namespace_groups of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetNamespaceGroupsRequestBody
        """
        return self._namespace_groups

    @namespace_groups.setter
    def namespace_groups(self, namespace_groups):
        """Sets the namespace_groups of this TableReporterParamsFilter.


        :param namespace_groups: The namespace_groups of this TableReporterParamsFilter.  # noqa: E501
        :type namespace_groups: GetNamespaceGroupsRequestBody
        """

        self._namespace_groups = namespace_groups

    @property
    def iscsi_luns(self):
        """Gets the iscsi_luns of this TableReporterParamsFilter.  # noqa: E501


        :return: The iscsi_luns of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetIscsiLunsRequestBody
        """
        return self._iscsi_luns

    @iscsi_luns.setter
    def iscsi_luns(self, iscsi_luns):
        """Sets the iscsi_luns of this TableReporterParamsFilter.


        :param iscsi_luns: The iscsi_luns of this TableReporterParamsFilter.  # noqa: E501
        :type iscsi_luns: GetIscsiLunsRequestBody
        """

        self._iscsi_luns = iscsi_luns

    @property
    def tasks(self):
        """Gets the tasks of this TableReporterParamsFilter.  # noqa: E501


        :return: The tasks of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetTasksRequestBody
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this TableReporterParamsFilter.


        :param tasks: The tasks of this TableReporterParamsFilter.  # noqa: E501
        :type tasks: GetTasksRequestBody
        """

        self._tasks = tasks

    @property
    def user_audit_logs(self):
        """Gets the user_audit_logs of this TableReporterParamsFilter.  # noqa: E501


        :return: The user_audit_logs of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetUserAuditLogsRequestBody
        """
        return self._user_audit_logs

    @user_audit_logs.setter
    def user_audit_logs(self, user_audit_logs):
        """Sets the user_audit_logs of this TableReporterParamsFilter.


        :param user_audit_logs: The user_audit_logs of this TableReporterParamsFilter.  # noqa: E501
        :type user_audit_logs: GetUserAuditLogsRequestBody
        """

        self._user_audit_logs = user_audit_logs

    @property
    def system_audit_logs(self):
        """Gets the system_audit_logs of this TableReporterParamsFilter.  # noqa: E501


        :return: The system_audit_logs of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetSystemAuditLogsRequestBody
        """
        return self._system_audit_logs

    @system_audit_logs.setter
    def system_audit_logs(self, system_audit_logs):
        """Sets the system_audit_logs of this TableReporterParamsFilter.


        :param system_audit_logs: The system_audit_logs of this TableReporterParamsFilter.  # noqa: E501
        :type system_audit_logs: GetSystemAuditLogsRequestBody
        """

        self._system_audit_logs = system_audit_logs

    @property
    def iscsi_lun_snapshots(self):
        """Gets the iscsi_lun_snapshots of this TableReporterParamsFilter.  # noqa: E501


        :return: The iscsi_lun_snapshots of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetIscsiLunSnapshotsRequestBody
        """
        return self._iscsi_lun_snapshots

    @iscsi_lun_snapshots.setter
    def iscsi_lun_snapshots(self, iscsi_lun_snapshots):
        """Sets the iscsi_lun_snapshots of this TableReporterParamsFilter.


        :param iscsi_lun_snapshots: The iscsi_lun_snapshots of this TableReporterParamsFilter.  # noqa: E501
        :type iscsi_lun_snapshots: GetIscsiLunSnapshotsRequestBody
        """

        self._iscsi_lun_snapshots = iscsi_lun_snapshots

    @property
    def iscsi_connections(self):
        """Gets the iscsi_connections of this TableReporterParamsFilter.  # noqa: E501


        :return: The iscsi_connections of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetIscsiConnectionsRequestBody
        """
        return self._iscsi_connections

    @iscsi_connections.setter
    def iscsi_connections(self, iscsi_connections):
        """Sets the iscsi_connections of this TableReporterParamsFilter.


        :param iscsi_connections: The iscsi_connections of this TableReporterParamsFilter.  # noqa: E501
        :type iscsi_connections: GetIscsiConnectionsRequestBody
        """

        self._iscsi_connections = iscsi_connections

    @property
    def consistency_groups(self):
        """Gets the consistency_groups of this TableReporterParamsFilter.  # noqa: E501


        :return: The consistency_groups of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetConsistencyGroupsRequestBody
        """
        return self._consistency_groups

    @consistency_groups.setter
    def consistency_groups(self, consistency_groups):
        """Sets the consistency_groups of this TableReporterParamsFilter.


        :param consistency_groups: The consistency_groups of this TableReporterParamsFilter.  # noqa: E501
        :type consistency_groups: GetConsistencyGroupsRequestBody
        """

        self._consistency_groups = consistency_groups

    @property
    def users(self):
        """Gets the users of this TableReporterParamsFilter.  # noqa: E501


        :return: The users of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetUsersRequestBody
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this TableReporterParamsFilter.


        :param users: The users of this TableReporterParamsFilter.  # noqa: E501
        :type users: GetUsersRequestBody
        """

        self._users = users

    @property
    def vm_entity_filters(self):
        """Gets the vm_entity_filters of this TableReporterParamsFilter.  # noqa: E501


        :return: The vm_entity_filters of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetEntityFiltersRequestBody
        """
        return self._vm_entity_filters

    @vm_entity_filters.setter
    def vm_entity_filters(self, vm_entity_filters):
        """Sets the vm_entity_filters of this TableReporterParamsFilter.


        :param vm_entity_filters: The vm_entity_filters of this TableReporterParamsFilter.  # noqa: E501
        :type vm_entity_filters: GetEntityFiltersRequestBody
        """

        self._vm_entity_filters = vm_entity_filters

    @property
    def snapshot_plans(self):
        """Gets the snapshot_plans of this TableReporterParamsFilter.  # noqa: E501


        :return: The snapshot_plans of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetSnapshotPlansRequestBody
        """
        return self._snapshot_plans

    @snapshot_plans.setter
    def snapshot_plans(self, snapshot_plans):
        """Sets the snapshot_plans of this TableReporterParamsFilter.


        :param snapshot_plans: The snapshot_plans of this TableReporterParamsFilter.  # noqa: E501
        :type snapshot_plans: GetSnapshotPlansRequestBody
        """

        self._snapshot_plans = snapshot_plans

    @property
    def global_alert_rules(self):
        """Gets the global_alert_rules of this TableReporterParamsFilter.  # noqa: E501


        :return: The global_alert_rules of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetGlobalAlertRulesRequestBody
        """
        return self._global_alert_rules

    @global_alert_rules.setter
    def global_alert_rules(self, global_alert_rules):
        """Sets the global_alert_rules of this TableReporterParamsFilter.


        :param global_alert_rules: The global_alert_rules of this TableReporterParamsFilter.  # noqa: E501
        :type global_alert_rules: GetGlobalAlertRulesRequestBody
        """

        self._global_alert_rules = global_alert_rules

    @property
    def alerts(self):
        """Gets the alerts of this TableReporterParamsFilter.  # noqa: E501


        :return: The alerts of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetAlertsRequestBody
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this TableReporterParamsFilter.


        :param alerts: The alerts of this TableReporterParamsFilter.  # noqa: E501
        :type alerts: GetAlertsRequestBody
        """

        self._alerts = alerts

    @property
    def vm_placement_groups(self):
        """Gets the vm_placement_groups of this TableReporterParamsFilter.  # noqa: E501


        :return: The vm_placement_groups of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetVmPlacementGroupsRequestBody
        """
        return self._vm_placement_groups

    @vm_placement_groups.setter
    def vm_placement_groups(self, vm_placement_groups):
        """Sets the vm_placement_groups of this TableReporterParamsFilter.


        :param vm_placement_groups: The vm_placement_groups of this TableReporterParamsFilter.  # noqa: E501
        :type vm_placement_groups: GetVmPlacementGroupsRequestBody
        """

        self._vm_placement_groups = vm_placement_groups

    @property
    def vm_templates(self):
        """Gets the vm_templates of this TableReporterParamsFilter.  # noqa: E501


        :return: The vm_templates of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetVmTemplatesRequestBody
        """
        return self._vm_templates

    @vm_templates.setter
    def vm_templates(self, vm_templates):
        """Sets the vm_templates of this TableReporterParamsFilter.


        :param vm_templates: The vm_templates of this TableReporterParamsFilter.  # noqa: E501
        :type vm_templates: GetVmTemplatesRequestBody
        """

        self._vm_templates = vm_templates

    @property
    def elf_images(self):
        """Gets the elf_images of this TableReporterParamsFilter.  # noqa: E501


        :return: The elf_images of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetElfImagesRequestBody
        """
        return self._elf_images

    @elf_images.setter
    def elf_images(self, elf_images):
        """Sets the elf_images of this TableReporterParamsFilter.


        :param elf_images: The elf_images of this TableReporterParamsFilter.  # noqa: E501
        :type elf_images: GetElfImagesRequestBody
        """

        self._elf_images = elf_images

    @property
    def vm_volumes(self):
        """Gets the vm_volumes of this TableReporterParamsFilter.  # noqa: E501


        :return: The vm_volumes of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetVmVolumesRequestBody
        """
        return self._vm_volumes

    @vm_volumes.setter
    def vm_volumes(self, vm_volumes):
        """Sets the vm_volumes of this TableReporterParamsFilter.


        :param vm_volumes: The vm_volumes of this TableReporterParamsFilter.  # noqa: E501
        :type vm_volumes: GetVmVolumesRequestBody
        """

        self._vm_volumes = vm_volumes

    @property
    def vlans(self):
        """Gets the vlans of this TableReporterParamsFilter.  # noqa: E501


        :return: The vlans of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetVlansRequestBody
        """
        return self._vlans

    @vlans.setter
    def vlans(self, vlans):
        """Sets the vlans of this TableReporterParamsFilter.


        :param vlans: The vlans of this TableReporterParamsFilter.  # noqa: E501
        :type vlans: GetVlansRequestBody
        """

        self._vlans = vlans

    @property
    def disks(self):
        """Gets the disks of this TableReporterParamsFilter.  # noqa: E501


        :return: The disks of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetDisksRequestBody
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this TableReporterParamsFilter.


        :param disks: The disks of this TableReporterParamsFilter.  # noqa: E501
        :type disks: GetDisksRequestBody
        """

        self._disks = disks

    @property
    def vdses(self):
        """Gets the vdses of this TableReporterParamsFilter.  # noqa: E501


        :return: The vdses of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetVdsesRequestBody
        """
        return self._vdses

    @vdses.setter
    def vdses(self, vdses):
        """Sets the vdses of this TableReporterParamsFilter.


        :param vdses: The vdses of this TableReporterParamsFilter.  # noqa: E501
        :type vdses: GetVdsesRequestBody
        """

        self._vdses = vdses

    @property
    def elf_data_stores(self):
        """Gets the elf_data_stores of this TableReporterParamsFilter.  # noqa: E501


        :return: The elf_data_stores of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetElfDataStoresRequestBody
        """
        return self._elf_data_stores

    @elf_data_stores.setter
    def elf_data_stores(self, elf_data_stores):
        """Sets the elf_data_stores of this TableReporterParamsFilter.


        :param elf_data_stores: The elf_data_stores of this TableReporterParamsFilter.  # noqa: E501
        :type elf_data_stores: GetElfDataStoresRequestBody
        """

        self._elf_data_stores = elf_data_stores

    @property
    def vms(self):
        """Gets the vms of this TableReporterParamsFilter.  # noqa: E501


        :return: The vms of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetVmsRequestBody
        """
        return self._vms

    @vms.setter
    def vms(self, vms):
        """Sets the vms of this TableReporterParamsFilter.


        :param vms: The vms of this TableReporterParamsFilter.  # noqa: E501
        :type vms: GetVmsRequestBody
        """

        self._vms = vms

    @property
    def nfs_exports(self):
        """Gets the nfs_exports of this TableReporterParamsFilter.  # noqa: E501


        :return: The nfs_exports of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetNfsExportsRequestBody
        """
        return self._nfs_exports

    @nfs_exports.setter
    def nfs_exports(self, nfs_exports):
        """Sets the nfs_exports of this TableReporterParamsFilter.


        :param nfs_exports: The nfs_exports of this TableReporterParamsFilter.  # noqa: E501
        :type nfs_exports: GetNfsExportsRequestBody
        """

        self._nfs_exports = nfs_exports

    @property
    def iscsi_targets(self):
        """Gets the iscsi_targets of this TableReporterParamsFilter.  # noqa: E501


        :return: The iscsi_targets of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetIscsiTargetsRequestBody
        """
        return self._iscsi_targets

    @iscsi_targets.setter
    def iscsi_targets(self, iscsi_targets):
        """Sets the iscsi_targets of this TableReporterParamsFilter.


        :param iscsi_targets: The iscsi_targets of this TableReporterParamsFilter.  # noqa: E501
        :type iscsi_targets: GetIscsiTargetsRequestBody
        """

        self._iscsi_targets = iscsi_targets

    @property
    def usb_devices(self):
        """Gets the usb_devices of this TableReporterParamsFilter.  # noqa: E501


        :return: The usb_devices of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetUsbDevicesRequestBody
        """
        return self._usb_devices

    @usb_devices.setter
    def usb_devices(self, usb_devices):
        """Sets the usb_devices of this TableReporterParamsFilter.


        :param usb_devices: The usb_devices of this TableReporterParamsFilter.  # noqa: E501
        :type usb_devices: GetUsbDevicesRequestBody
        """

        self._usb_devices = usb_devices

    @property
    def nics(self):
        """Gets the nics of this TableReporterParamsFilter.  # noqa: E501


        :return: The nics of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetNicsRequestBody
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this TableReporterParamsFilter.


        :param nics: The nics of this TableReporterParamsFilter.  # noqa: E501
        :type nics: GetNicsRequestBody
        """

        self._nics = nics

    @property
    def clusters(self):
        """Gets the clusters of this TableReporterParamsFilter.  # noqa: E501


        :return: The clusters of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetClustersRequestBody
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this TableReporterParamsFilter.


        :param clusters: The clusters of this TableReporterParamsFilter.  # noqa: E501
        :type clusters: GetClustersRequestBody
        """

        self._clusters = clusters

    @property
    def datacenters(self):
        """Gets the datacenters of this TableReporterParamsFilter.  # noqa: E501


        :return: The datacenters of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetDatacentersRequestBody
        """
        return self._datacenters

    @datacenters.setter
    def datacenters(self, datacenters):
        """Sets the datacenters of this TableReporterParamsFilter.


        :param datacenters: The datacenters of this TableReporterParamsFilter.  # noqa: E501
        :type datacenters: GetDatacentersRequestBody
        """

        self._datacenters = datacenters

    @property
    def hosts(self):
        """Gets the hosts of this TableReporterParamsFilter.  # noqa: E501


        :return: The hosts of this TableReporterParamsFilter.  # noqa: E501
        :rtype: GetHostsRequestBody
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this TableReporterParamsFilter.


        :param hosts: The hosts of this TableReporterParamsFilter.  # noqa: E501
        :type hosts: GetHostsRequestBody
        """

        self._hosts = hosts

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
        if not isinstance(other, TableReporterParamsFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TableReporterParamsFilter):
            return True

        return self.to_dict() != other.to_dict()
