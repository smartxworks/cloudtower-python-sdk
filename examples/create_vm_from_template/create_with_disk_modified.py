from cloudtower.api import VmApi, ContentLibraryVmTemplateApi, ClusterApi
from cloudtower.utils import login, wait_tasks
from cloudtower.configuration import Configuration
from cloudtower.models import Bus, VmVolumeElfStoragePolicyType
from cloudtower import ApiClient
import os


configuration = Configuration(host=os.getenv("CLOUDTOWER_ENDPOINT"))
client = ApiClient(configuration)

login(client, os.getenv("CLOUDTOWER_USERNAME"), os.getenv("CLOUDTOWER_PASSWORD"))


def create_vm_from_template_modify_disk(template_name, cluster_name, vm_name, disk_operate):
    """
    通过内容库模板创建一台虚拟机，配置虚拟机的磁盘
    :param template_name: 模板名称
    :param cluster_name: 集群名称
    :param vm_name: 虚拟机名称
    :param disk_operate: 磁盘操作，使用详见 create_vm_from_template_modify_disk_example 方法
    :return: 被创建的虚拟机
    """
    vm_api = VmApi(client)
    cluster_api = ClusterApi(client)
    template_api = ContentLibraryVmTemplateApi(client)

    cluster = cluster_api.get_clusters({
        "where": {
            "name": cluster_name
        }
    })
    if len(cluster) == 0:
        raise Exception("cluster not found")

    template = template_api.get_content_library_vm_templates({
        "where": {
            "name": template_name
        }
    })
    if len(template) == 0:
        raise Exception("template not found")

    with_task_vms = vm_api.create_vm_from_content_library_template([
        {
            "template_id": template[0].id,
            "cluster_id": cluster[0].id,
            "name": vm_name,
            "is_full_copy": False,
            "disk_operate": disk_operate
        }
    ])
    tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]
    vm_ids = [
        with_task_vm.data.id for with_task_vm in with_task_vms]
    wait_tasks(tasks, client)
    return vm_api.get_vms({
        "where": {
            "id_in": vm_ids
        }
    })[0]


def create_vm_from_template_modify_disk_example():
    """
    通过模板创建虚拟机时，如果希望对原有的磁盘进行任何修改，可以通过 disk_operate 参数进行配置
    disk_operate 参数的类型是 VmDiskOperate，它是一个字典，包含以下字段：
    - remove_disks 由于删除指定index的磁盘
    - modify_disks 修改现有磁盘的配置，目前仅支持修改总线，如果有其他修改可以通过，删除原有盘
    - new_disks 新增磁盘，类型是 VmDiskParams，它是一个字典，包含以下字段：
        - mount_cd_roms 挂载 cd-rom
        - mount_disks 挂载已有磁盘
        - mount_new_create_disks 挂载新磁盘
    """
    disk_operate = {
        "remove_disks": {
            "disk_index": [0]  # 用于删除指定 index 的磁盘，index 从 0 开始计算，这里既是删除第一块磁盘
        },
        "new_disks": {
            "mount_cd_roms": [
                {
                    "boot": 2,  # 启动顺序
                    "content_library_image_id": ""  # 指定挂载内容库镜像的 id
                }
            ],
            "mount_disks": [
                {
                    "boot": 3,  # 启动顺序
                    "bus": Bus.VIRTIO,  # 总线类型
                    "vm_volume_id": "cljm6x2g1405g0958tp3zkhvh"  # 被挂载虚拟卷的 id
                }
            ],
            "mount_new_create_disks": [
                {
                    "boot": 4,
                    "bus": Bus.VIRTIO,
                    "vm_volume": {
                        "name": "test",  # 新建虚拟卷的名称
                        "size": 10 * 1024 * 1024 * 1024,  # 新建虚拟卷的大小，单位是字节
                        "elf_storage_policy": VmVolumeElfStoragePolicyType._2_THIN_PROVISION  # 存储策略
                    }
                }
            ]
        }
    }
    create_vm_from_template_modify_disk("template-name", "cluster-name", "vm-name", disk_operate)
