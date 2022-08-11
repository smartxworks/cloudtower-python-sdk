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


class LabelOrderByInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    CLUSTER_NUM_ASC = "cluster_num_ASC"
    CLUSTER_NUM_DESC = "cluster_num_DESC"
    CONSISTENCY_GROUP_NUM_ASC = "consistency_group_num_ASC"
    CONSISTENCY_GROUP_NUM_DESC = "consistency_group_num_DESC"
    CONSISTENCY_GROUP_SNAPSHOT_NUM_ASC = "consistency_group_snapshot_num_ASC"
    CONSISTENCY_GROUP_SNAPSHOT_NUM_DESC = "consistency_group_snapshot_num_DESC"
    CONTENT_LIBRARY_IMAGE_NUM_ASC = "content_library_image_num_ASC"
    CONTENT_LIBRARY_IMAGE_NUM_DESC = "content_library_image_num_DESC"
    CONTENT_LIBRARY_VM_TEMPLATE_NUM_ASC = "content_library_vm_template_num_ASC"
    CONTENT_LIBRARY_VM_TEMPLATE_NUM_DESC = "content_library_vm_template_num_DESC"
    CREATEDAT_ASC = "createdAt_ASC"
    CREATEDAT_DESC = "createdAt_DESC"
    DATACENTER_NUM_ASC = "datacenter_num_ASC"
    DATACENTER_NUM_DESC = "datacenter_num_DESC"
    DISK_NUM_ASC = "disk_num_ASC"
    DISK_NUM_DESC = "disk_num_DESC"
    ELF_IMAGE_NUM_ASC = "elf_image_num_ASC"
    ELF_IMAGE_NUM_DESC = "elf_image_num_DESC"
    HOST_NUM_ASC = "host_num_ASC"
    HOST_NUM_DESC = "host_num_DESC"
    ID_ASC = "id_ASC"
    ID_DESC = "id_DESC"
    ISCSI_LUN_NUM_ASC = "iscsi_lun_num_ASC"
    ISCSI_LUN_NUM_DESC = "iscsi_lun_num_DESC"
    ISCSI_LUN_SNAPSHOT_NUM_ASC = "iscsi_lun_snapshot_num_ASC"
    ISCSI_LUN_SNAPSHOT_NUM_DESC = "iscsi_lun_snapshot_num_DESC"
    ISCSI_TARGET_NUM_ASC = "iscsi_target_num_ASC"
    ISCSI_TARGET_NUM_DESC = "iscsi_target_num_DESC"
    ISOLATION_POLICY_NUM_ASC = "isolation_policy_num_ASC"
    ISOLATION_POLICY_NUM_DESC = "isolation_policy_num_DESC"
    KEY_ASC = "key_ASC"
    KEY_DESC = "key_DESC"
    NAMESPACE_GROUP_NUM_ASC = "namespace_group_num_ASC"
    NAMESPACE_GROUP_NUM_DESC = "namespace_group_num_DESC"
    NFS_EXPORT_NUM_ASC = "nfs_export_num_ASC"
    NFS_EXPORT_NUM_DESC = "nfs_export_num_DESC"
    NFS_INODE_NUM_ASC = "nfs_inode_num_ASC"
    NFS_INODE_NUM_DESC = "nfs_inode_num_DESC"
    NIC_NUM_ASC = "nic_num_ASC"
    NIC_NUM_DESC = "nic_num_DESC"
    NVMF_NAMESPACE_NUM_ASC = "nvmf_namespace_num_ASC"
    NVMF_NAMESPACE_NUM_DESC = "nvmf_namespace_num_DESC"
    NVMF_NAMESPACE_SNAPSHOT_NUM_ASC = "nvmf_namespace_snapshot_num_ASC"
    NVMF_NAMESPACE_SNAPSHOT_NUM_DESC = "nvmf_namespace_snapshot_num_DESC"
    NVMF_SUBSYSTEM_NUM_ASC = "nvmf_subsystem_num_ASC"
    NVMF_SUBSYSTEM_NUM_DESC = "nvmf_subsystem_num_DESC"
    SECURITY_POLICY_NUM_ASC = "security_policy_num_ASC"
    SECURITY_POLICY_NUM_DESC = "security_policy_num_DESC"
    SYSTEM_VLAN_NUM_ASC = "system_vlan_num_ASC"
    SYSTEM_VLAN_NUM_DESC = "system_vlan_num_DESC"
    TOTAL_NUM_ASC = "total_num_ASC"
    TOTAL_NUM_DESC = "total_num_DESC"
    VALUE_ASC = "value_ASC"
    VALUE_DESC = "value_DESC"
    VDS_NUM_ASC = "vds_num_ASC"
    VDS_NUM_DESC = "vds_num_DESC"
    VM_NUM_ASC = "vm_num_ASC"
    VM_NUM_DESC = "vm_num_DESC"
    VM_SNAPSHOT_NUM_ASC = "vm_snapshot_num_ASC"
    VM_SNAPSHOT_NUM_DESC = "vm_snapshot_num_DESC"
    VM_TEMPLATE_NUM_ASC = "vm_template_num_ASC"
    VM_TEMPLATE_NUM_DESC = "vm_template_num_DESC"
    VM_VLAN_NUM_ASC = "vm_vlan_num_ASC"
    VM_VLAN_NUM_DESC = "vm_vlan_num_DESC"
    VM_VOLUME_NUM_ASC = "vm_volume_num_ASC"
    VM_VOLUME_NUM_DESC = "vm_volume_num_DESC"

    allowable_values = [CLUSTER_NUM_ASC, CLUSTER_NUM_DESC, CONSISTENCY_GROUP_NUM_ASC, CONSISTENCY_GROUP_NUM_DESC, CONSISTENCY_GROUP_SNAPSHOT_NUM_ASC, CONSISTENCY_GROUP_SNAPSHOT_NUM_DESC, CONTENT_LIBRARY_IMAGE_NUM_ASC, CONTENT_LIBRARY_IMAGE_NUM_DESC, CONTENT_LIBRARY_VM_TEMPLATE_NUM_ASC, CONTENT_LIBRARY_VM_TEMPLATE_NUM_DESC, CREATEDAT_ASC, CREATEDAT_DESC, DATACENTER_NUM_ASC, DATACENTER_NUM_DESC, DISK_NUM_ASC, DISK_NUM_DESC, ELF_IMAGE_NUM_ASC, ELF_IMAGE_NUM_DESC, HOST_NUM_ASC, HOST_NUM_DESC, ID_ASC, ID_DESC, ISCSI_LUN_NUM_ASC, ISCSI_LUN_NUM_DESC, ISCSI_LUN_SNAPSHOT_NUM_ASC, ISCSI_LUN_SNAPSHOT_NUM_DESC, ISCSI_TARGET_NUM_ASC, ISCSI_TARGET_NUM_DESC, ISOLATION_POLICY_NUM_ASC, ISOLATION_POLICY_NUM_DESC, KEY_ASC, KEY_DESC, NAMESPACE_GROUP_NUM_ASC, NAMESPACE_GROUP_NUM_DESC, NFS_EXPORT_NUM_ASC, NFS_EXPORT_NUM_DESC, NFS_INODE_NUM_ASC, NFS_INODE_NUM_DESC, NIC_NUM_ASC, NIC_NUM_DESC, NVMF_NAMESPACE_NUM_ASC, NVMF_NAMESPACE_NUM_DESC, NVMF_NAMESPACE_SNAPSHOT_NUM_ASC, NVMF_NAMESPACE_SNAPSHOT_NUM_DESC, NVMF_SUBSYSTEM_NUM_ASC, NVMF_SUBSYSTEM_NUM_DESC, SECURITY_POLICY_NUM_ASC, SECURITY_POLICY_NUM_DESC, SYSTEM_VLAN_NUM_ASC, SYSTEM_VLAN_NUM_DESC, TOTAL_NUM_ASC, TOTAL_NUM_DESC, VALUE_ASC, VALUE_DESC, VDS_NUM_ASC, VDS_NUM_DESC, VM_NUM_ASC, VM_NUM_DESC, VM_SNAPSHOT_NUM_ASC, VM_SNAPSHOT_NUM_DESC, VM_TEMPLATE_NUM_ASC, VM_TEMPLATE_NUM_DESC, VM_VLAN_NUM_ASC, VM_VLAN_NUM_DESC, VM_VOLUME_NUM_ASC, VM_VOLUME_NUM_DESC]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, **kwargs):  # noqa: E501
        """LabelOrderByInput - a model defined in OpenAPI"""  # noqa: E501
        self.local_vars_configuration = kwargs.get("local_vars_configuration", Configuration.get_default_copy())
        self.discriminator = None

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
        if not isinstance(other, LabelOrderByInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LabelOrderByInput):
            return True

        return self.to_dict() != other.to_dict()
