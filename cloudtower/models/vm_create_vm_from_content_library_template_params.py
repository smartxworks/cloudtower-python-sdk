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


class VmCreateVmFromContentLibraryTemplateParams(object):
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
        'cloud_init': 'TemplateCloudInit',
        'is_full_copy': 'bool',
        'template_id': 'str',
        'max_bandwidth_policy': 'VmDiskIoRestrictType',
        'max_bandwidth': 'int',
        'max_iops_policy': 'VmDiskIoRestrictType',
        'max_iops': 'int',
        'io_policy': 'VmDiskIoPolicy',
        'vcpu': 'int',
        'status': 'VmStatus',
        'firmware': 'VmFirmware',
        'ha': 'bool',
        'vm_nics': 'list[VmNicParams]',
        'disk_operate': 'VmDiskOperate',
        'memory': 'int',
        'cpu_cores': 'int',
        'cpu_sockets': 'int',
        'guest_os_type': 'VmGuestsOperationSystem',
        'folder_id': 'str',
        'description': 'str',
        'name': 'str',
        'host_id': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'cloud_init': 'cloud_init',
        'is_full_copy': 'is_full_copy',
        'template_id': 'template_id',
        'max_bandwidth_policy': 'max_bandwidth_policy',
        'max_bandwidth': 'max_bandwidth',
        'max_iops_policy': 'max_iops_policy',
        'max_iops': 'max_iops',
        'io_policy': 'io_policy',
        'vcpu': 'vcpu',
        'status': 'status',
        'firmware': 'firmware',
        'ha': 'ha',
        'vm_nics': 'vm_nics',
        'disk_operate': 'disk_operate',
        'memory': 'memory',
        'cpu_cores': 'cpu_cores',
        'cpu_sockets': 'cpu_sockets',
        'guest_os_type': 'guest_os_type',
        'folder_id': 'folder_id',
        'description': 'description',
        'name': 'name',
        'host_id': 'host_id',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """VmCreateVmFromContentLibraryTemplateParams - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cloud_init = None
        self._is_full_copy = None
        self._template_id = None
        self._max_bandwidth_policy = None
        self._max_bandwidth = None
        self._max_iops_policy = None
        self._max_iops = None
        self._io_policy = None
        self._vcpu = None
        self._status = None
        self._firmware = None
        self._ha = None
        self._vm_nics = None
        self._disk_operate = None
        self._memory = None
        self._cpu_cores = None
        self._cpu_sockets = None
        self._guest_os_type = None
        self._folder_id = None
        self._description = None
        self._name = None
        self._host_id = None
        self._cluster_id = None
        self.discriminator = None

        if "cloud_init" in kwargs:
            self.cloud_init = kwargs["cloud_init"]
        if "is_full_copy" in kwargs:
            self.is_full_copy = kwargs["is_full_copy"]
        if "template_id" in kwargs:
            self.template_id = kwargs["template_id"]
        if "max_bandwidth_policy" in kwargs:
            self.max_bandwidth_policy = kwargs["max_bandwidth_policy"]
        if "max_bandwidth" in kwargs:
            self.max_bandwidth = kwargs["max_bandwidth"]
        if "max_iops_policy" in kwargs:
            self.max_iops_policy = kwargs["max_iops_policy"]
        if "max_iops" in kwargs:
            self.max_iops = kwargs["max_iops"]
        if "io_policy" in kwargs:
            self.io_policy = kwargs["io_policy"]
        if "vcpu" in kwargs:
            self.vcpu = kwargs["vcpu"]
        if "status" in kwargs:
            self.status = kwargs["status"]
        if "firmware" in kwargs:
            self.firmware = kwargs["firmware"]
        if "ha" in kwargs:
            self.ha = kwargs["ha"]
        if "vm_nics" in kwargs:
            self.vm_nics = kwargs["vm_nics"]
        if "disk_operate" in kwargs:
            self.disk_operate = kwargs["disk_operate"]
        if "memory" in kwargs:
            self.memory = kwargs["memory"]
        if "cpu_cores" in kwargs:
            self.cpu_cores = kwargs["cpu_cores"]
        if "cpu_sockets" in kwargs:
            self.cpu_sockets = kwargs["cpu_sockets"]
        if "guest_os_type" in kwargs:
            self.guest_os_type = kwargs["guest_os_type"]
        if "folder_id" in kwargs:
            self.folder_id = kwargs["folder_id"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        if "host_id" in kwargs:
            self.host_id = kwargs["host_id"]
        if "cluster_id" in kwargs:
            self.cluster_id = kwargs["cluster_id"]

    @property
    def cloud_init(self):
        """Gets the cloud_init of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The cloud_init of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: TemplateCloudInit
        """
        return self._cloud_init

    @cloud_init.setter
    def cloud_init(self, cloud_init):
        """Sets the cloud_init of this VmCreateVmFromContentLibraryTemplateParams.


        :param cloud_init: The cloud_init of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type cloud_init: TemplateCloudInit
        """

        self._cloud_init = cloud_init

    @property
    def is_full_copy(self):
        """Gets the is_full_copy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The is_full_copy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_full_copy

    @is_full_copy.setter
    def is_full_copy(self, is_full_copy):
        """Sets the is_full_copy of this VmCreateVmFromContentLibraryTemplateParams.


        :param is_full_copy: The is_full_copy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type is_full_copy: bool
        """
        if self.local_vars_configuration.client_side_validation and is_full_copy is None:  # noqa: E501
            raise ValueError("Invalid value for `is_full_copy`, must not be `None`")  # noqa: E501

        self._is_full_copy = is_full_copy

    @property
    def template_id(self):
        """Gets the template_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The template_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this VmCreateVmFromContentLibraryTemplateParams.


        :param template_id: The template_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type template_id: str
        """
        if self.local_vars_configuration.client_side_validation and template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `template_id`, must not be `None`")  # noqa: E501

        self._template_id = template_id

    @property
    def max_bandwidth_policy(self):
        """Gets the max_bandwidth_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The max_bandwidth_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_bandwidth_policy

    @max_bandwidth_policy.setter
    def max_bandwidth_policy(self, max_bandwidth_policy):
        """Sets the max_bandwidth_policy of this VmCreateVmFromContentLibraryTemplateParams.


        :param max_bandwidth_policy: The max_bandwidth_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type max_bandwidth_policy: VmDiskIoRestrictType
        """

        self._max_bandwidth_policy = max_bandwidth_policy

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The max_bandwidth of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this VmCreateVmFromContentLibraryTemplateParams.


        :param max_bandwidth: The max_bandwidth of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type max_bandwidth: int
        """

        self._max_bandwidth = max_bandwidth

    @property
    def max_iops_policy(self):
        """Gets the max_iops_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The max_iops_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: VmDiskIoRestrictType
        """
        return self._max_iops_policy

    @max_iops_policy.setter
    def max_iops_policy(self, max_iops_policy):
        """Sets the max_iops_policy of this VmCreateVmFromContentLibraryTemplateParams.


        :param max_iops_policy: The max_iops_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type max_iops_policy: VmDiskIoRestrictType
        """

        self._max_iops_policy = max_iops_policy

    @property
    def max_iops(self):
        """Gets the max_iops of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The max_iops of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: int
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this VmCreateVmFromContentLibraryTemplateParams.


        :param max_iops: The max_iops of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type max_iops: int
        """

        self._max_iops = max_iops

    @property
    def io_policy(self):
        """Gets the io_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The io_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: VmDiskIoPolicy
        """
        return self._io_policy

    @io_policy.setter
    def io_policy(self, io_policy):
        """Sets the io_policy of this VmCreateVmFromContentLibraryTemplateParams.


        :param io_policy: The io_policy of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type io_policy: VmDiskIoPolicy
        """

        self._io_policy = io_policy

    @property
    def vcpu(self):
        """Gets the vcpu of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The vcpu of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: int
        """
        return self._vcpu

    @vcpu.setter
    def vcpu(self, vcpu):
        """Sets the vcpu of this VmCreateVmFromContentLibraryTemplateParams.


        :param vcpu: The vcpu of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type vcpu: int
        """

        self._vcpu = vcpu

    @property
    def status(self):
        """Gets the status of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The status of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: VmStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VmCreateVmFromContentLibraryTemplateParams.


        :param status: The status of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type status: VmStatus
        """

        self._status = status

    @property
    def firmware(self):
        """Gets the firmware of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The firmware of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: VmFirmware
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this VmCreateVmFromContentLibraryTemplateParams.


        :param firmware: The firmware of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type firmware: VmFirmware
        """

        self._firmware = firmware

    @property
    def ha(self):
        """Gets the ha of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The ha of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: bool
        """
        return self._ha

    @ha.setter
    def ha(self, ha):
        """Sets the ha of this VmCreateVmFromContentLibraryTemplateParams.


        :param ha: The ha of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type ha: bool
        """

        self._ha = ha

    @property
    def vm_nics(self):
        """Gets the vm_nics of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The vm_nics of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: list[VmNicParams]
        """
        return self._vm_nics

    @vm_nics.setter
    def vm_nics(self, vm_nics):
        """Sets the vm_nics of this VmCreateVmFromContentLibraryTemplateParams.


        :param vm_nics: The vm_nics of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type vm_nics: list[VmNicParams]
        """

        self._vm_nics = vm_nics

    @property
    def disk_operate(self):
        """Gets the disk_operate of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The disk_operate of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: VmDiskOperate
        """
        return self._disk_operate

    @disk_operate.setter
    def disk_operate(self, disk_operate):
        """Sets the disk_operate of this VmCreateVmFromContentLibraryTemplateParams.


        :param disk_operate: The disk_operate of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type disk_operate: VmDiskOperate
        """

        self._disk_operate = disk_operate

    @property
    def memory(self):
        """Gets the memory of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The memory of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VmCreateVmFromContentLibraryTemplateParams.


        :param memory: The memory of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type memory: int
        """

        self._memory = memory

    @property
    def cpu_cores(self):
        """Gets the cpu_cores of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The cpu_cores of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """Sets the cpu_cores of this VmCreateVmFromContentLibraryTemplateParams.


        :param cpu_cores: The cpu_cores of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type cpu_cores: int
        """

        self._cpu_cores = cpu_cores

    @property
    def cpu_sockets(self):
        """Gets the cpu_sockets of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The cpu_sockets of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: int
        """
        return self._cpu_sockets

    @cpu_sockets.setter
    def cpu_sockets(self, cpu_sockets):
        """Sets the cpu_sockets of this VmCreateVmFromContentLibraryTemplateParams.


        :param cpu_sockets: The cpu_sockets of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type cpu_sockets: int
        """

        self._cpu_sockets = cpu_sockets

    @property
    def guest_os_type(self):
        """Gets the guest_os_type of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The guest_os_type of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: VmGuestsOperationSystem
        """
        return self._guest_os_type

    @guest_os_type.setter
    def guest_os_type(self, guest_os_type):
        """Sets the guest_os_type of this VmCreateVmFromContentLibraryTemplateParams.


        :param guest_os_type: The guest_os_type of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type guest_os_type: VmGuestsOperationSystem
        """

        self._guest_os_type = guest_os_type

    @property
    def folder_id(self):
        """Gets the folder_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The folder_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this VmCreateVmFromContentLibraryTemplateParams.


        :param folder_id: The folder_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type folder_id: str
        """

        self._folder_id = folder_id

    @property
    def description(self):
        """Gets the description of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The description of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VmCreateVmFromContentLibraryTemplateParams.


        :param description: The description of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The name of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmCreateVmFromContentLibraryTemplateParams.


        :param name: The name of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def host_id(self):
        """Gets the host_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The host_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this VmCreateVmFromContentLibraryTemplateParams.


        :param host_id: The host_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type host_id: str
        """

        self._host_id = host_id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501


        :return: The cluster_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this VmCreateVmFromContentLibraryTemplateParams.


        :param cluster_id: The cluster_id of this VmCreateVmFromContentLibraryTemplateParams.  # noqa: E501
        :type cluster_id: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

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
        if not isinstance(other, VmCreateVmFromContentLibraryTemplateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VmCreateVmFromContentLibraryTemplateParams):
            return True

        return self.to_dict() != other.to_dict()
