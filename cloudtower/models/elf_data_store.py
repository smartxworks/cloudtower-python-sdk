# coding: utf-8
try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cloudtower.configuration import Configuration


class ElfDataStore(object):
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
        'cluster': 'NestedCluster',
        'description': 'str',
        'external_use': 'bool',
        'id': 'str',
        'internal': 'bool',
        'ip_whitelist': 'str',
        'iscsi_target': 'NestedIscsiTarget',
        'local_id': 'str',
        'name': 'str',
        'nfs_export': 'NestedNfsExport',
        'nvmf_subsystem': 'NestedNvmfSubsystem',
        'replica_num': 'int',
        'thin_provision': 'bool',
        'type': 'ElfDataStoreType'
    }

    attribute_map = {
        'cluster': 'cluster',
        'description': 'description',
        'external_use': 'external_use',
        'id': 'id',
        'internal': 'internal',
        'ip_whitelist': 'ip_whitelist',
        'iscsi_target': 'iscsi_target',
        'local_id': 'local_id',
        'name': 'name',
        'nfs_export': 'nfs_export',
        'nvmf_subsystem': 'nvmf_subsystem',
        'replica_num': 'replica_num',
        'thin_provision': 'thin_provision',
        'type': 'type'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ElfDataStore - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())

        self._cluster = None
        self._description = None
        self._external_use = None
        self._id = None
        self._internal = None
        self._ip_whitelist = None
        self._iscsi_target = None
        self._local_id = None
        self._name = None
        self._nfs_export = None
        self._nvmf_subsystem = None
        self._replica_num = None
        self._thin_provision = None
        self._type = None
        self.discriminator = None

        if "cluster" in kwargs:
            self.cluster = kwargs["cluster"]
        if "description" in kwargs:
            self.description = kwargs["description"]
        if "external_use" in kwargs:
            self.external_use = kwargs["external_use"]
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "internal" in kwargs:
            self.internal = kwargs["internal"]
        if "ip_whitelist" in kwargs:
            self.ip_whitelist = kwargs["ip_whitelist"]
        self.iscsi_target = kwargs.get("iscsi_target", None)
        if "local_id" in kwargs:
            self.local_id = kwargs["local_id"]
        if "name" in kwargs:
            self.name = kwargs["name"]
        self.nfs_export = kwargs.get("nfs_export", None)
        self.nvmf_subsystem = kwargs.get("nvmf_subsystem", None)
        if "replica_num" in kwargs:
            self.replica_num = kwargs["replica_num"]
        if "thin_provision" in kwargs:
            self.thin_provision = kwargs["thin_provision"]
        if "type" in kwargs:
            self.type = kwargs["type"]

    @property
    def cluster(self):
        """Gets the cluster of this ElfDataStore.  # noqa: E501


        :return: The cluster of this ElfDataStore.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ElfDataStore.


        :param cluster: The cluster of this ElfDataStore.  # noqa: E501
        :type cluster: NestedCluster
        """
        if self.local_vars_configuration.client_side_validation and cluster is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def description(self):
        """Gets the description of this ElfDataStore.  # noqa: E501


        :return: The description of this ElfDataStore.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ElfDataStore.


        :param description: The description of this ElfDataStore.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def external_use(self):
        """Gets the external_use of this ElfDataStore.  # noqa: E501


        :return: The external_use of this ElfDataStore.  # noqa: E501
        :rtype: bool
        """
        return self._external_use

    @external_use.setter
    def external_use(self, external_use):
        """Sets the external_use of this ElfDataStore.


        :param external_use: The external_use of this ElfDataStore.  # noqa: E501
        :type external_use: bool
        """
        if self.local_vars_configuration.client_side_validation and external_use is None:  # noqa: E501
            raise ValueError("Invalid value for `external_use`, must not be `None`")  # noqa: E501

        self._external_use = external_use

    @property
    def id(self):
        """Gets the id of this ElfDataStore.  # noqa: E501


        :return: The id of this ElfDataStore.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ElfDataStore.


        :param id: The id of this ElfDataStore.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def internal(self):
        """Gets the internal of this ElfDataStore.  # noqa: E501


        :return: The internal of this ElfDataStore.  # noqa: E501
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this ElfDataStore.


        :param internal: The internal of this ElfDataStore.  # noqa: E501
        :type internal: bool
        """
        if self.local_vars_configuration.client_side_validation and internal is None:  # noqa: E501
            raise ValueError("Invalid value for `internal`, must not be `None`")  # noqa: E501

        self._internal = internal

    @property
    def ip_whitelist(self):
        """Gets the ip_whitelist of this ElfDataStore.  # noqa: E501


        :return: The ip_whitelist of this ElfDataStore.  # noqa: E501
        :rtype: str
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        """Sets the ip_whitelist of this ElfDataStore.


        :param ip_whitelist: The ip_whitelist of this ElfDataStore.  # noqa: E501
        :type ip_whitelist: str
        """
        if self.local_vars_configuration.client_side_validation and ip_whitelist is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_whitelist`, must not be `None`")  # noqa: E501

        self._ip_whitelist = ip_whitelist

    @property
    def iscsi_target(self):
        """Gets the iscsi_target of this ElfDataStore.  # noqa: E501


        :return: The iscsi_target of this ElfDataStore.  # noqa: E501
        :rtype: NestedIscsiTarget
        """
        return self._iscsi_target

    @iscsi_target.setter
    def iscsi_target(self, iscsi_target):
        """Sets the iscsi_target of this ElfDataStore.


        :param iscsi_target: The iscsi_target of this ElfDataStore.  # noqa: E501
        :type iscsi_target: NestedIscsiTarget
        """

        self._iscsi_target = iscsi_target

    @property
    def local_id(self):
        """Gets the local_id of this ElfDataStore.  # noqa: E501


        :return: The local_id of this ElfDataStore.  # noqa: E501
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this ElfDataStore.


        :param local_id: The local_id of this ElfDataStore.  # noqa: E501
        :type local_id: str
        """
        if self.local_vars_configuration.client_side_validation and local_id is None:  # noqa: E501
            raise ValueError("Invalid value for `local_id`, must not be `None`")  # noqa: E501

        self._local_id = local_id

    @property
    def name(self):
        """Gets the name of this ElfDataStore.  # noqa: E501


        :return: The name of this ElfDataStore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElfDataStore.


        :param name: The name of this ElfDataStore.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nfs_export(self):
        """Gets the nfs_export of this ElfDataStore.  # noqa: E501


        :return: The nfs_export of this ElfDataStore.  # noqa: E501
        :rtype: NestedNfsExport
        """
        return self._nfs_export

    @nfs_export.setter
    def nfs_export(self, nfs_export):
        """Sets the nfs_export of this ElfDataStore.


        :param nfs_export: The nfs_export of this ElfDataStore.  # noqa: E501
        :type nfs_export: NestedNfsExport
        """

        self._nfs_export = nfs_export

    @property
    def nvmf_subsystem(self):
        """Gets the nvmf_subsystem of this ElfDataStore.  # noqa: E501


        :return: The nvmf_subsystem of this ElfDataStore.  # noqa: E501
        :rtype: NestedNvmfSubsystem
        """
        return self._nvmf_subsystem

    @nvmf_subsystem.setter
    def nvmf_subsystem(self, nvmf_subsystem):
        """Sets the nvmf_subsystem of this ElfDataStore.


        :param nvmf_subsystem: The nvmf_subsystem of this ElfDataStore.  # noqa: E501
        :type nvmf_subsystem: NestedNvmfSubsystem
        """

        self._nvmf_subsystem = nvmf_subsystem

    @property
    def replica_num(self):
        """Gets the replica_num of this ElfDataStore.  # noqa: E501


        :return: The replica_num of this ElfDataStore.  # noqa: E501
        :rtype: int
        """
        return self._replica_num

    @replica_num.setter
    def replica_num(self, replica_num):
        """Sets the replica_num of this ElfDataStore.


        :param replica_num: The replica_num of this ElfDataStore.  # noqa: E501
        :type replica_num: int
        """
        if self.local_vars_configuration.client_side_validation and replica_num is None:  # noqa: E501
            raise ValueError("Invalid value for `replica_num`, must not be `None`")  # noqa: E501

        self._replica_num = replica_num

    @property
    def thin_provision(self):
        """Gets the thin_provision of this ElfDataStore.  # noqa: E501


        :return: The thin_provision of this ElfDataStore.  # noqa: E501
        :rtype: bool
        """
        return self._thin_provision

    @thin_provision.setter
    def thin_provision(self, thin_provision):
        """Sets the thin_provision of this ElfDataStore.


        :param thin_provision: The thin_provision of this ElfDataStore.  # noqa: E501
        :type thin_provision: bool
        """
        if self.local_vars_configuration.client_side_validation and thin_provision is None:  # noqa: E501
            raise ValueError("Invalid value for `thin_provision`, must not be `None`")  # noqa: E501

        self._thin_provision = thin_provision

    @property
    def type(self):
        """Gets the type of this ElfDataStore.  # noqa: E501


        :return: The type of this ElfDataStore.  # noqa: E501
        :rtype: ElfDataStoreType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElfDataStore.


        :param type: The type of this ElfDataStore.  # noqa: E501
        :type type: ElfDataStoreType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, ElfDataStore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElfDataStore):
            return True

        return self.to_dict() != other.to_dict()
