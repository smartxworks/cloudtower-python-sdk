from cloudtower.api import VmApi, ContentLibraryVmTemplateApi, ClusterApi
from cloudtower.utils import login, wait_tasks
from cloudtower.configuration import Configuration
from cloudtower import ApiClient
import os


configuration = Configuration(host=os.getenv("CLOUDTOWER_ENDPOINT"))
client = ApiClient(configuration)

login(client, os.getenv("CLOUDTOWER_USERNAME"), os.getenv("CLOUDTOWER_PASSWORD"))


def create_vm_from_template_with_cloudinit(template_name, cluster_name, vm_name, cloud_init):
    """
    通过内容库模板创建一台虚拟机，配置虚拟机的 cloud-init，需要模板启用
    :param template_name: 模板名称
    :param cluster_name: 集群名称
    :param vm_name: 虚拟机名称
    :param cloud_init: cloud-init 配置，使用详见 create_vm_from_template_with_cloudinit_example 方法
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
            "cloud_init": cloud_init
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


def create_vm_from_template_with_cloudinit_example():
    """
    cloudinit 可以用于配置虚拟机的初始化，例如配置网络、配置默认账户密码等，需要模板创建时已经安装 cloud-init 或者 cloudbase-init 服务才能正常工作
    cloud_init 配置项是 TemplateCloudInit 类型，是一个字典，包含以下字段
    - default_user_password: 配置默认用户密码
    - nameservers: dns 服务地址，是一个字符串列表，最多支持配置3个
    - networks: 网络配置，一个字典列表
        - ip_address: ip 地址，配置静态地址后必填
        - net_mask: 子网，配置静态地址后必填
        - nic_index: 配置网卡的顺序，以 0 为起始
        - routes: 静态路由配置，一个字典列表
            - gateway: 网关地址
            - network: 目标网络
            - netmask: 目标子网
    - hostname: 主机名
    - public_keys: 登陆用的公钥
    - user_data: 用户数据配置
    """
    cloud_init = {
        "default_user_password": "password",
        "nameservers": [
            "114.114.114.114"
        ],
        "networks": [
            {
                "ip_address": "192.168.20.1",
                "net_mask": "255.255.240.0",
                "nic_index": 0,
                "routes": [
                    {
                        "gateway": "192.168.16.1", # 默认网关配置
                        "network": "0.0.0.0",
                        "netmask": "0.0.0.0",
                    },
                ]
            }
        ],
        "hostname": "test",
        "public_keys": [
            "key_content"
        ],
        "user_data": "user_data"
    }
    create_vm_from_template_with_cloudinit("template_name", "cluster_name", "vm_name", cloud_init)
