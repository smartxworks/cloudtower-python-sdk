# Cloudtower Python SDK

Python 环境下的 Cloudtower SDK，适用于 2.7 和 3.4 及以上版本

- [源码地址](https://github.com/Sczlog/cloudtower-python-sdk)
- [下载地址](https://github.com/Sczlog/cloudtower-python-sdk/releases)

## 安装

- ### whl

  ```shell
  pip install cloudtower_python_sdk-$VERSION-py2.py3-none-any.whl
  ```

- ### tar.gz

  ```shell
  tar xvzf python-sdk-$VERSION.tar.gz
  cd python-sdk-$VERSION
  python setup.py install
  ```

- ### git 源码安装

  ```
  git clone https://github.com/Sczlog/cloudtower-python-sdk.git
  cd clodtower-python-sdk
  python setup.py install
  ```

- ### git pip 安装

  ```shell
  pip install git+https://github.com/Sczlog/cloudtower-python-sdk.git
  ```

- ### pypi 安装
  ```shell
  pip install cloudtower-python-sdk
  ```

## 使用

### 创建实例：

#### 创建 `ApiClient` 实例

```py
 from cloudtower_python_sdk.configuration import Configuration
 from cloudtower_python_sdk import ApiClient

 # 配置 operation-api endpoint
 configuration = Configuration(host="http://your.tower.com/v2/api")

 client = ApiClient(configuration)
```

#### 创建对应的 API 实例：

```py
 from cloudtower_python_sdk.api.vm_api import VmApi
 vm_api = VmApi(client)
```

### 鉴权：

```py
 from cloudtower_python_sdk.api.user_api import UserApi
 from cloudtower_python_sdk.models import UserSource
 # 通过 UserApi 中的 login 方法来获得 token。
 user_api = UserApi(client)
 login_res = user_api.login({
     "username": "your_username",
     "password": "your_password",
     "source": UserSource.LOCAL
 })
 # 将 token 配置在 configuration.api_key["Authorization"] 中，
 # 这样所有使用当前 client 的 api 都会获得鉴权的 token 信息。
 configuration.api_key["Authorization"] = login_res.data.token
```

### 获取资源

```py
# 从 models package 中获取参数定义
from cloudtower_python_sdk.models import GetVmsRequestBody,VmWhereInput
vms = vm_api.get_vms({
  "where": {
    "id": "vm_id"
  },
  "first":1,
})
```

### 更新资源

> 资源更新会产生相关的异步任务，若需要对该资源进行后续的操作或读取该资源字段，请在异步任务结束后再获取相关的资源字段。详见`通用指南`。

```py
from cloudtower_python_sdk.models import VmStartParams

start_res = vm_api.start_vm({
  "where": {
    "id": "stopped_vm_id"
  },
})
```

### 自定义 header

> 请求支持设置返回语言的设置，可以增加 `content-language` 参数来设置返回的语言。 可选值 `en-US`, `zh-CN`。默认为 `en-US`。

```py
    vms = vm_api.get_vms(
      {
        "where": {
          "id": "vm_id"
        }
      },
      content_language="zh-CN"
    )
```

### 等待异步任务结束

#### 参数说明

| 参数名        | 类型      | 是否必须 | 说明                                                                                 |
| ------------- | --------- | -------- | ------------------------------------------------------------------------------------ |
| ids           | list[str] | 是       | 需查询的 task 的 id 列表                                                             |
| api_client    | ApiClient | 是       | 查询所使用的 ApiClient 实例                                                          |
| interval      | int       | 否       | 轮询的间隔时间，默认为 5s                                                            |
| timeout       | int       | 否       | 超时时间，默认为 300s                                                                |
| exit_on_error | bool      | 否       | 是否在单个 Task 出错时立即退出，否则则会等待全部 Task 都完成后再退出，默认为 False。 |

#### 错误说明

| 错误码 | 说明             |
| ------ | ---------------- |
| 408    | 超时             |
| 500    | 异步任务内部错误 |

```py
    from cloudtower_python_sdk.utils import wait_tasks
    try:
     wait_tasks([res.task_id for res in start_res], api_client)
    except ApiException as e:
     # 处理错误
    else:
     # task完成后的回调
```

#### 其他

> 上述请求的发送都是同步的请求，会堵塞当前进程。如果需要使用异步请求，请在对应请求参数中加上 `async_req=True`。
> 通过返回结果 `ApplyResult.get()` 来获取对应的结果。

```py
    vms = vm_api.get_vms(
      {
        "where": {
          "id": "vm_id"
        }
      },
      async_req=True
    )
    print(vms.get()[0].name)
```

### 使用完成后销毁 ApiClient 实例：

```py
client.close()
```

## 操作示例

### 获取虚拟机

#### 获取所有虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api.vm_api import VmApi

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
vms = vm_api.get_vms({})
```

#### 分页获取虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api.vm_api import VmApi

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
vms_from_51_to_100 = vm_api.get_vms({
  "first": 50,
  "skip": 50,
})
```

#### 获取所有已开机虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api.vm_api import VmApi
from cloudtower_python_sdk.models import VmStatus

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
running_vms = vm_api.get_vms(
    {
        "where": {
            "status": VmStatus.RUNNING
        }
    },
)
```

#### 获取名称或描述中包含特定字符串的虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api.vm_api import VmApi

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
vms_name_contains = vm_api.get_vms(
    {
        "where": {
            "name_contains": "string"
        }
    },
)
```

#### 获取所有 vcpu > n 的虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api.vm_api import VmApi

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
vms_has_4_more_vcpu = vm_api.get_vms(
    {
        "where": {
            "vcpu_gt": 4
        }
    },
)
```

### 从模版创建虚拟机

#### 仅指定 id

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vms = vm_api.create_vm_from_template([
    {
        "template_id": "template_id",
        "name": "vm_name",
        "is_full_copy": False
    }
])
tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]
vm_ids = [
    with_task_vm.data.id for with_task_vm in with_task_vms]
wait_tasks(tasks, api_client)
created_vms = vm_api.get_vms({
    "where": {
        "id_in": vm_ids
    }
})
```

#### 配置与模板不同的虚拟盘参数

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.models import (
    VmCreateVmFromTemplateParamsDiskOperateModifyDisks,
    VmDiskParams,
    Bus,
    VmVolumeElfStoragePolicyType
)
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vms = vm_api.create_vm_from_template([
    {
        "template_id": "template_id",
        "name": "vm_name",
        "is_full_copy": False,
        "disk_operate": {
            "remove_disks": {
                "disk_index": [0, 1]
            },
            "modify_disks":   [
                {
                    "disk_index": 2,
                    "vm_volume_id": "new_volume_id"
                }
            ],
            "new_disks":   {
                "mount_cd_roms": [
                    {
                        "index": 0,
                        "boot": 0,
                        "elf_image_id": "elf_image_id"
                    }
                ],
                "mout_disks": [
                    {
                        "index": 1,
                        "bus": Bus.VIRTIO,
                        "boot": 1,
                        "vm_volume_id": "vm_volume_id"
                    }
                ],
                "mount_new_create_disks": [
                    {
                        "vm_volume": {
                            "elf_storage_policy": VmVolumeElfStoragePolicyType._2_THIN_PROVISION,
                            "size": 4*1024*1024*1024,
                            "name": "disk_name",
                        },
                        "bus": Bus.IDE,
                        "boot": 3,
                        "index": 3
                    }
                ]
            }
        }
    }
])

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]
vm_ids = [
    with_task_vm.data.id for with_task_vm in with_task_vms]
wait_tasks(tasks, api_client)
created_vms = vm_api.get_vms({
    "where": {
        "id_in": vm_ids
    }
})
```

#### 配置与模版不同的网卡参数

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.models import (
    VmNicParams,
    VmNicModel
)
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vms = vm_api.create_vm_from_template([
    {
        "template_id": "template_id",
        "name": "vm_name",
        "is_full_copy": False,
        "vm_nics": [
            {
                "connect_vlan_id": "alternative_vlan_id",
                "enabled": True,
                "model": VmNicModel.SRIOV
            }
        ]
    }
])
tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]
vm_ids = [
    with_task_vm.data.id for with_task_vm in with_task_vms]
wait_tasks(tasks, api_client)
created_vms = vm_api.get_vms({
    "where": {
        "id_in": vm_ids
    }
})
```

### 创建空白虚拟机

#### 简单创建

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.models import (
    VmStatus,
    VmFirmware,
    Bus
)
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vm = vm_api.create_vm([
    {
        "cluster_id": "cluster_id",
        "name": "vm_name",
        "ha": True,
        "cpu_cores": 4,
        "cpu_sockets": 4,
        "memory": 4*1024*1024*1024,
        "vcpu": 16,
        "status": VmStatus.STOPPED,
        "firmware": VmFirmware.BIOS,
        "vm_nics": [
            {
                "connect_vlan_id": "vlan_id",
            }
        ],
        "vm_disks": {
            "mount_disks": [{
                "index": 0,
                "boot": 0,
                "bus": Bus.VIRTIO,
                "vm_volume_id": "vm_volume_id"
            }],
            "mount_cd_roms": [{
                "index": 1,
                "boot": 1,
            }],
        }
    }
])[0]

wait_tasks([with_task_vm.task_id], api_client)
created_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

#### 创建时配置虚拟盘

##### CD-ROM 加载 ISO

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.models import (
    VmStatus,
    VmFirmware,
    Bus
)
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vm = vm_api.create_vm([
    {
        "cluster_id": "cluster_id",
        "name": "vm_name",
        "ha": True,
        "cpu_cores": 4,
        "cpu_sockets": 4,
        "memory": 4*1024*1024*1024,
        "vcpu": 16,
        "status": VmStatus.STOPPED,
        "firmware": VmFirmware.BIOS,
        "vm_nics": [
            {
                "connect_vlan_id": "vlan_id",
            }
        ],
        "vm_disks": {
            "mount_cd_roms": [{
                "index": 0,
                "boot": 0,
                "elf_image_id": "elf_image_id"
            }],
        }
    }
])[0]

wait_tasks([with_task_vm.task_id], api_client)
created_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

##### 挂载虚拟卷为虚拟盘

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.models import (
    VmStatus,
    VmFirmware,
    Bus
)
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vm = vm_api.create_vm([
    {
        "cluster_id": "cluster_id",
        "name": "vm_name",
        "ha": True,
        "cpu_cores": 4,
        "cpu_sockets": 4,
        "memory": 4*1024*1024*1024,
        "vcpu": 16,
        "status": VmStatus.STOPPED,
        "firmware": VmFirmware.BIOS,
        "vm_nics": [
            {
                "connect_vlan_id": "vlan_id",
            }
        ],
        "vm_disks": {
            "mount_disks": [{
                "index": 0,
                "boot": 0,
                "bus": Bus.VIRTIO,
                "vm_volume_id": "vm_volume_id"
            }],
        }
    }
])[0]

wait_tasks([with_task_vm.task_id], api_client)
created_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

##### 新增虚拟盘

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.models import (
    VmStatus,
    VmFirmware,
    Bus,
    VmVolumeElfStoragePolicyType
)
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vm = vm_api.create_vm([
    {
        "cluster_id": "cluster_id",
        "name": "vm_name",
        "ha": True,
        "cpu_cores": 4,
        "cpu_sockets": 4,
        "memory": 4 * 1024*1024*1024,
        "vcpu": 16,
        "status": VmStatus.STOPPED,
        "firmware": VmFirmware.BIOS,
        "vm_nics": [
            {
                "connect_vlan_id": "vlan_id",
            }
        ],
        "vm_disks": {
            "mount_new_create_disks": [{
                "index": 0,
                "boot": 0,
                "bus": Bus.VIRTIO,
                "vm_volume": {
                    "elf_storage_policy": VmVolumeElfStoragePolicyTyp_2_THIN_PROVISION,
                    "size": 10 * 1024 * 1024 * 1024,
                    "name": "new_volume_name"
                }
            }],
        }
    }
])[0]

wait_tasks([with_task_vm.task_id], api_client)
created_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

#### 创建时配置虚拟网卡

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.models import (
    VmStatus,
    VmFirmware,
    Bus,
    VmNicModel,
    VmVolumeElfStoragePolicyType
)
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)
with_task_vm = vm_api.create_vm([
    {
        "cluster_id": "cluster_id",
        "name": "vm_name",
        "ha": True,
        "cpu_cores": 4,
        "cpu_sockets": 4,
        "memory": 4 * 1024*1024*1024,
        "vcpu": 16,
        "status": VmStatus.STOPPED,
        "firmware": VmFirmware.BIOS,
        "vm_nics": [
            {
                "connect_vlan_id": "vlan_id",
                "mirror": True,
                "model":	VmNicModel.VIRTIO
            }
        ],
        "vm_disks": {
            "mount_disks": [{
                "index": 0,
                "boot": 0,
                "bus": Bus.VIRTIO,
                "vm_volume_id": "vm_volume_id"
            }],
            "mount_cd_roms": [{
                "index": 1,
                "boot": 1,
            }],
        }
    }
])[0]

wait_tasks([with_task_vm.task_id], api_client)
created_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

### 编辑虚拟机

#### 编辑基本信息

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)

with_task_vm = vm_api.update_vm({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "name": "new_name",
        "description": "new_description",
        "ha": False,
        "vcpu": 2 * 8,
        "cpu_cores": 2,
        "cpu_sockets": 8,
        "memory": 8*1024*1024*1024,
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)

updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

#### CD-ROM 编辑

##### 添加 CD-ROM

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)

with_task_vm = vm_api.add_vm_cd_rom({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "vm_cd_roms": [
            {
                "elf_image_id": "elf_image_id",
                "index": 0,
                "boot": 0
            }
        ]
    }
})[0]
wait_tasks([with_task_vm.task_id], api_client)

updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

##### 删除 CD-ROM

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)

with_task_vms = vm_api.remove_vm_cd_rom({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "cd_rom_ids": ["cd_rom_to_remove_id_1", "cd_rom_to_remove_id_2"]
    }
})

wait_tasks([with_task_vm.task_id], api_client)

updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

#### 虚拟卷操作

##### 添加新虚拟卷

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.models import Bus, VmVolumeElfStoragePolicyType
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)

with_task_vm = vm_api.add_vm_disk({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "vm_disks": {
            "mount_new_create_disks": [
                {
                    "vm_volume": {
                        "elf_storage_policy": VmVolumeElfStoragePolicyType._2_THIN_PROVISION,
                        "size": 40*1024*1024*1024,
                        "name": "new_volume_name"
                    },
                    "index": 1,
                    "boot": 1,
                    "bus": Bus.VIRTIO,
                }
            ]
        }
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)

updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

##### 挂载已存在虚拟卷为虚拟盘

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.models import Bus
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)

with_task_vm = vm_api.add_vm_disk({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "vm_disks": {
            "mount_disks": [
                {
                    "vm_volume_id": "vm_volume_id",
                    "index": 1,
                    "boot": 1,
                    "bus": Bus.VIRTIO,
                }
            ]
        }
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)

updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

##### 卸载虚拟盘

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.models import Bus, VmVolumeElfStoragePolicyType
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))
vm_api = VmApi(api_client)

with_task_vm = vm_api.remove_vm_disk({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "disk_ids": ["disk_to_remove_id_1", "disk_to_remove_id_2"]
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)

updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

#### 网卡操作

##### 添加网卡

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.models import VmNicModel
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)

with_task_vm = vm_api.add_vm_nic({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "vm_nics": [
            {
                "connect_vlan_id": "target_vlan_id",
                "enabled": True,
                "model": VmNicModel.VIRTIO,
                "ip_address": "ip_address",
                "gateway": "gateway",
                "subnet_mask": "subnet_mask"
            },
            {
                "connect_vlan_id": "target_vlan_id2",
                "enabled": True,
                "mirror": True,
                "model": VmNicModel.VIRTIO,
                "ip_address": "ip_address2",
                "gateway": "gateway2",
                "subnet_mask": "subnet_mask2"
            }
        ]
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)
updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

##### 编辑网卡

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)

with_task_vm = vm_api.update_vm_nic({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "nic_index": 0,
        "enable": False,
        "mirror": False,
        "mac_address": "mac_address",
        "ip_address": "ip_address",
        "gateway": "gateway",
        "subnet_mask": "subnet_mask"
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)
updated_vm = vm_api.get_vms({
    "where": {
        "id": "vm_id"
    }
})
```

##### 移除网卡

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)

with_task_vm = vm_api.remove_vm_nic({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "nic_index": [0, 1]
    }
})

wait_tasks([with_task_vm.task_id], api_client)
updated_vm = vm_api.get_vms({
    "where": {
        "id": with_task_vm.data.id
    }
})
```

#### 虚拟机迁移

##### 迁移至指定主机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)

with_task_vm = vm_api.mig_rate_vm({
    "where": {
        "id": "vm-id"
    },
    "data": {
        "host_id": "target_host_id"
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)
```

##### 自动调度到合适的主机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)

with_task_vm = vm_api.mig_rate_vm({
    "where": {
        "id": "vm-id"
    }
})[0]

wait_tasks([with_task_vm.task_id], api_client)
```

### 虚拟机电源操作

#### 虚拟机开机:

##### 指定虚拟机开机，自动调度到合适的虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.start_vm({
    "where": {
        "id": "vm_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

opened_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

##### 批量虚拟机开机，自动调度到合适的虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vms = vm_api.start_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]

wait_tasks(tasks, api_client)

opened_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

##### 开机至指定主机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.start_vm({
    "where": {
        "id": "vm_id"
    },
    "data": {
        "host_id": "host_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

opened_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

#### 虚拟机关机

##### 指定虚拟机关机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.shut_down_vm({
    "where": {
        "id": "vm_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

closed_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

##### 批量虚拟机关机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vms = vm_api.shut_down_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]
vm_ids = [with_task_vm.data.id for with_task_vm in with_task_vms]

wait_tasks(tasks, api_client)

closed_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

##### 强制关机指定虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.force_shut_down_vm({
    "where": {
        "id": "vm_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

closed_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

##### 强制关机批量虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vms = vm_api.force_shut_down_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]

wait_tasks(tasks, api_client)

closed_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

#### 虚拟机重启

##### 重启指定虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.restart_vm({
    "where": {
        "id": "vm_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

restarted_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

##### 重启批量虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vms = vm_api.restart_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]

wait_tasks(tasks, api_client)

restarted_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

##### 重启指定虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.force_restart_vm({
    "where": {
        "id": "vm_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

restarted_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

##### 强制重启批量虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vms = vm_api.force_restart_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]

wait_tasks(tasks, api_client)

restarted_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

#### 虚拟机暂停

##### 暂停指定虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.suspend_vm({
    "where": {
        "id": "vm_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

suspended_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

##### 暂停批量虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vms = vm_api.suspend_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]

wait_tasks(tasks, api_client)

suspended_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

#### 虚拟机恢复

##### 恢复指定虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vm = vm_api.resume_vm({
    "where": {
        "id": "vm_id"
    }
})[0]

wait_tasks(with_task_vm.task_id, api_client)

resumed_vm = vm_api.get_vms({"where": {"id": "vm_id"}})[0]
```

##### 恢复批量虚拟机

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_vms = vm_api.resume_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_vm.task_id for with_task_vm in with_task_vms]

wait_tasks(tasks, api_client)

resumed_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

### 删除虚拟机

#### 回收站

##### 移入回收站

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_delete_vms = vm_api.move_vm_to_recycle_bin({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_delete_vm.task_id for with_task_delete_vm in with_task_delete_vms]

wait_tasks(tasks, api_client)

vm_moved_to_recycle_bin = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

##### 从回收站恢复

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_delete_vms = vm_api.recover_vm_from_recycle_bin({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_delete_vm.task_id for with_task_delete_vm in with_task_delete_vms]

wait_tasks(tasks, api_client)

recovered_vms = vm_api.get_vms({"where": {"id_in": ["vm_id_1", "vm_id_2"]}})
```

#### 永久删除

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import VmApi
from cloudtower_python_sdk.utils import wait_tasks

api_client = ApiClient(Configuration(host="http://your.tower.com/v2/api"))

vm_api = VmApi(api_client)
with_task_delete_vms = vm_api.delete_vm({
    "where": {
        "id_in": ["vm_id_1", "vm_id_2"]
    }
})

tasks = [with_task_delete_vm.task_id for with_task_delete_vm in with_task_delete_vms]

wait_tasks(tasks, api_client)
```

## 场景示例

### 虚拟机备份

```py
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.api.vm_api import VmApi
from cloudtower_python_sdk.api.vm_snapshot_api import VmSnapshotApi
from cloudtower_python_sdk.api.iscsi_lun_snapshot_api import IscsiLunSnapshotApi
from cloudtower_python_sdk.models import (
    ConsistentType,
    VmToolsStatus
)
from cloudtower_python_sdk.utils import wait_tasks


def create_vm_snapshot(
    api_client: ApiClient,
    target_vm_name: str,
    target_snapshot_name: str,
    consistent_type: ConsistentType
):
    vm_api = VmApi(api_client)
    vm_snapshot_api = VmSnapshotApi(api_client)
    iscsi_lun_snapshot_api = IscsiLunSnapshotApi(api_client)
    # 1. 获取所需备份的虚拟机的信息，这里我们需要vm的id来构建创建snapshot的参数
    vm = vm_api.get_vms({
        "where": {
            "name": target_vm_name
        },
        "first": 1
    })
    # vm 已安装并启动 VMTools 时，consistent_type 可以使用 FILE_SYSTEM_CONSISTENT 代表文件系统一致性快照
    if vm.vm_tools_status != VmToolsStatus.RUNNING and consistent_type == ConsistentType.FILE_SYSTEM_CONSISTENT:
        consistent_type = ConsistentType.CRASH_CONSISTENT

    # 2. 创建虚拟机快照
    snapshots_with_task = vm_snapshot_api.create_vm_snapshot({
        "data": [
            {
                "vm_id": vm.id,
                "name": target_snapshot_name,
                "consistent_type": consistent_type
            }
        ]
    })

    # 3. 等待Task完成
    wait_tasks([snapshots_with_task[0].task_id], api_client)

    # 4. 根据返回的id查询生成的虚拟机快照
    snapshot = vm_snapshot_api.get_vm_snapshots({
        "where": {
            "id": snapshots_with_task.data.id
        }
    })[0]
    # 5. 根据返回的snapshot中的vm_disks包含了快照的虚拟盘信息
    # type 为 DISK 表示对应一个卷，其中会包含一个 snapshot_local_id 则表示该虚拟卷对应的lun快照的 local_id
    # type 为 CD-ROM则代表为被挂载的CD-ROM，不会产生lun快照
    lun_snapshot_ids = []
    for disk in snapshot.vm_disks:
        if disk.type == "DISK":
            lun_snapshot_ids.append(disk.snapshot_local_id)

    lun_snapshots = iscsi_lun_snapshot_api.get_iscsi_lun_snapshots({
        "where": {
            "local_id_in": lun_snapshot_ids
        }
    })

    return {
        "vm_snapshot": snapshot,
        "lun_snapshots": lun_snapshots
    }

```

### Dashboard 构建

```py
from functools import reduce
from datetime import datetime, timedelta
from cloudtower_python_sdk import ApiClient
from cloudtower_python_sdk.configuration import Configuration
from cloudtower_python_sdk.api import (
    VmApi,
    ClusterApi,
    AlertApi,
    HostApi,
    DiskApi,
    ClusterSettingsApi,
    GlobalSettingsApi
)
from cloudtower_python_sdk.models import (
    SeverityEnum,
    ClusterType,
    ClusterWhereInput,
    DatacenterWhereInput,
    Hypervisor,
    ConnectState,
    HostState,
    HostStatus,
    DiskType,
    DiskUsageStatus,
    DiskHealthStatus
)

api_client = ApiClient(Configuration(host="http://tower.smartx.com/v2/api"))

byte_units = ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]

hz_units = ["Hz", "KHz", "MHz", "GHz", "THz"]


def convert_iso_date(date: str):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")


def format_unit(base: int, units, step=1024):
    if not len(units):
        raise Exception("no unit provided")
    if base <= 0:
        return "0" + units[0]
    for unit in units:
        if base < step:
            return "{:.2f}{}".format(base, unit)
        base /= step
    return "{:.2f}{}".format(base, units[-1])


def build_dashboard(api_client: ApiClient, datacenter_id: str = None, cluster_id: str = None):
    result = {}
    cluster_api = ClusterApi(api_client)
    clusters = cluster_api.get_clusters({
        "where": {"id": cluster_id} if cluster_id is not None else {"datacenters_some": {"id": datacenter_id}} if datacenter_id is not None else None
    })

    cluster_ids = [cluster.id for cluster in clusters]

    if cluster_id is not None:
        result["cluster_info"] = build_cluster_info(api_client, cluster_id)

    result["alerts"] = build_alerts(api_client, cluster_ids)
    result["disks"] = build_disks(api_client, cluster_ids)
    result["recycle_bin_info"] = build_recycle_bin(api_client, cluster_ids)

    metric = build_metrics(api_client, clusters, cluster_ids)

    if "cpu" in metric:
        result["cpu"] = metric["cpu"]
    if "memory" in metric:
        result["memory"] = metric["memory"]
    if "storage" in metric:
        result["storage"] = metric["storage"]
    if "clusters" in metric:
        result["clusters"] = metric["clusters"]
    if "hosts" in metric:
        result["hosts"] = metric["hosts"]
    if "data_recovery" in metric:
        result["data_recovery"] = metric["data_recovery"]
    return result


def build_alerts(api_client: ApiClient, cluster_ids):
    alert_api = AlertApi(api_client)
    alerts = alert_api.get_alerts({
        "where": {
            "ended": False,
            "cluster": {
                "id_in": cluster_ids
            },
        }
    })
    critial_alerts = [
        alert for alert in alerts if alert.severity == SeverityEnum.CRITICAL]
    notice_alerts = [
        alert for alert in alerts if alert.severity == SeverityEnum.NOTICE]
    info_alerts = [
        alert for alert in alerts if alert.severity == SeverityEnum.INFO]
    return {
        "critical": critial_alerts,
        "notice": notice_alerts,
        "info": info_alerts
    },


def build_cluster_info(api_client: ApiClient, cluster_id: str):
    cluster_api = ClusterApi(api_client)
    cluster: Cluster = cluster_api.get_clusters({
        "where": {
            "id": cluster_id
        },
        "first": 1
    })[0]
    mode = []
    if cluster.version[0] >= 5:
        if cluster.hypervisor == Hypervisor.ELF:
            mode.append("Boost")
        if cluster.rdma_enabled:
            mode.append('RDMA')
        if cluster.pmem_enabled:
            mode.append('PEEM')
    return {
        "version": cluster.version,
        "uuid": cluster.id,
        "license_type": cluster.license_type,
        "license_expire_date": cluster.license_expire_date if cluster.license_expire_date is not None else "Perpetual",
        "software": cluster.software_edition,
        "cpu_architecture": cluster.architecture,
        "mode": mode
    }


def build_disks(api_client: ApiClient, cluster_ids):
    disk_api = DiskApi(api_client)
    disks = disk_api.get_disks({
        "where": {
            "host": {
                "cluster": {
                    "id_in": cluster_ids
                }
            }
        }
    })
    ssd = {
        "healthy": 0,
        "warning": 0,
        "error": 0,
        "total": 0
    }
    hdd = {
        "healthy": 0,
        "warning": 0,
        "error": 0,
        "total": 0,
    }
    pmem = {
        "healthy": 0,
        "warning": 0,
        "error": 0,
        "total": 0
    }

    for disk in disks:
        if disk.type == DiskType.SSD:
            target = ssd
        elif disk.type == DiskType.HDD:
            target = hdd
        elif disk.type == DiskType.PMEM:
            target = pmem
        if disk.health_status in [DiskHealthStatus.UNHEALTHY, DiskHealthStatus.SUBHEALTHY, DiskHealthStatus.SMART_FAILED]:
            target['error'] += 1
        elif disk.usage_status in [DiskUsageStatus.UNMOUNTED, DiskUsageStatus.PARTIAL_MOUNTED]:
            target['warning'] += 1
        else:
            target['healthy'] += 1
        target['total'] += 1
    return {
        "ssd": ssd,
        "hdd": hdd,
        "pmem": pmem
    }


def build_metrics(api_client: ApiClient, clusters, cluster_ids):
    result = {}
    host_api = HostApi(api_client)

    hosts = host_api.get_hosts({
        "where": {
            "cluster": {
                "id_in": cluster_ids
            }
        }
    })

    cpu = {
        "total_cpu_cores": 0,
        "total_cpu_hz": 0,
        "used_cpu_hz": 0,
    }
    hosts_info = {
        "healthy": 0,
        "error": 0,
        "idle": 0,
        "unhealthy": 0,
        "removing": 0,
        "unknown": 0
    }
    memory = {
        "total_memory": 0,
        "used_memory": 0,
    }
    storage = {
        "total": 0,
        "used": 0,
        "invalid": 0,
        "available": 0
    }
    clusters_info = {
        "HCI_cluster": {
            "SMTX_VM_service": {
                "count": 0,
                "abnormal": 0
            },
            "SMTX_HCI_for_vSphere": {
                "count": 0,
                "abnormal": 0
            }
        },
        "distributed_storage_cluster": {
            "SMTX_ZBS": {
                "count": 0,
                "abnormal": 0
            }
        }
    }
    data_recovery = [
    ]

    for host in hosts:
        cluster = next(
            cluster for cluster in clusters if cluster.id == host.cluster.id)
        if cluster.hypervisor == Hypervisor.ELF:
            memory['total_memory'] += 0 if host.total_memory_bytes is None else host.total_memory_bytes
            memory['used_memory'] += (0 if host.running_pause_vm_memory_bytes is None else host.running_pause_vm_memory_bytes) + \
                (0 if host.os_memory_bytes is None else host.os_memory_bytes)
        if host.state == HostState.IDLE:
            hosts_info["idle"] += 1
        elif host.state == HostState.REMOVING:
            hosts_info["removing"] += 1
        elif host.status == HostStatus.CONNECTED_HEALTHY:
            hosts_info["healthy"] += 1
        elif host.status == HostStatus.CONNECTED_WARNING:
            hosts_info["unhealthy"] += 1
        elif host.status == HostStatus.SESSION_EXPIRED or host.status == HostStatus.CONNECTED_ERROR:
            hosts_info["error"] += 1
        else:
            hosts_info["unknown"] += 1

    for cluster in clusters:
        if cluster.type == ClusterType.SMTX_ZBS:
            clusters_info["distributed_storage_cluster"]["SMTX_ZBS"]["count"] += 1
            if cluster.connect_state == ConnectState.DISCONNECTED or cluster.connect_state == ConnectState.REMOVING:
                clusters_info["distributed_storage_cluster"]["SMTX_ZBS"]["abnormal"] += 1
        elif cluster.type == ClusterType.SMTX_OS:
            cpu["total_cpu_cores"] += 0 if cluster.total_cpu_cores is None else cluster.total_cpu_cores
            cpu["total_cpu_hz"] += 0 if cluster.total_cpu_hz is None else cluster.total_cpu_hz
            cpu["used_cpu_hz"] += 0 if cluster.used_cpu_hz is None else cluster.used_cpu_hz
            if cluster.hypervisor == Hypervisor.VMWARE:
                clusters_info["HCI_cluster"]["SMTX_HCI_for_vSphere"]["count"] += 1
                memory["total_memory"] += 0 if cluster.total_memory_bytes is None else cluster.total_memory_bytes
                memory["used_memory"] += 0 if cluster.used_memory_bytes is None else cluster.used_memory_bytes
                if cluster.connect_state == ConnectState.DISCONNECTED or cluster.connect_state == ConnectState.REMOVING:
                    clusters_info["HCI_cluster"]["SMTX_HCI_for_vSphere"]["abnormal"] += 1
            elif cluster.hypervisor == Hypervisor.ELF:
                clusters_info["HCI_cluster"]["SMTX_VM_service"]["count"] += 1
                if cluster.connect_state == ConnectState.DISCONNECTED or cluster.connect_state == ConnectState.REMOVING:
                    clusters_info["HCI_cluster"]["SMTX_VM_service"]["abnormal"] += 1
        if cluster.recover_data_size > 0:
            data_recovery.append({
                "cluster": cluster.name,
                "recover_data_size": format_unit(cluster.recover_data_size, byte_units),
                "speed": "{}/s".format(format_unit(cluster.recover_speed, byte_units))
            })
        storage["total"] += 0 if cluster.total_data_capacity is None else cluster.total_data_capacity
        storage["used"] += 0 if cluster.used_data_space is None else cluster.used_data_space
        storage["invalid"] += 0 if cluster.failure_data_space is None else cluster.failure_data_space
    if len(clusters) > 1 or clusters[0].type != ClusterType.SMTX_ZBS:
        cpu["cpu_usage"] = "{:.2f}%".format(
            cpu["used_cpu_hz"] / cpu["total_cpu_hz"])
        cpu["total_cpu_hz"] = format_unit(cpu["total_cpu_hz"], hz_units, 1000)
        cpu["used_cpu_hz"] = format_unit(cpu["used_cpu_hz"], hz_units, 1000)
        result['cpu'] = cpu
        memory["memory_usage"] = "{:.2f}%".format(
            memory["used_memory"] / memory["total_memory"])
        memory["total_memory"] = format_unit(
            memory["total_memory"], byte_units)
        memory["used_memory"] = format_unit(
            memory["used_memory"], byte_units)
        result["memory"] = memory
    storage["available"] = format_unit(
        storage["total"] - storage["used"] - storage["invalid"], byte_units)
    storage["total"] = format_unit(storage["total"], byte_units)
    storage["used"] = format_unit(storage["used"], byte_units)
    storage["invalid"] = format_unit(storage["invalid"], byte_units)
    result["storage"] = storage
    result["hosts"] = storage
    result["clusters"] = clusters_info
    result["data_recovery"] = data_recovery
    return result


def build_recycle_bin(api_client: ApiClient, cluster_ids):
    vm_api = VmApi(api_client)
    cluster_settings_api = ClusterSettingsApi(api_client)
    global_settings_api = GlobalSettingsApi(api_client)

    global_setting = global_settings_api.get_global_settingses({
        "first": 1
    })[0]

    cluster_settings = cluster_settings_api.get_cluster_settingses({
        "where": {
            "cluster": {
                "id_in": cluster_ids
            }
        }
    })
    vms = vm_api.get_vms({
        "where": {
            "cluster": {
                "id_in": cluster_ids
            },
            "in_recycle_bin": True
        }
    })

    recycle_bin_info = {
        "count": len(vms),
        "size": 0,
        "size_release_today": 0,
        "size_release_in_7_days": 0
    }

    for vm in vms:
        cluster_setting = next(
            (setting for setting in cluster_settings if setting.cluster.id == vm.cluster.id), None)
        setting = global_setting if cluster_setting is None else cluster_setting
        retain_duration = setting.vm_recycle_bin.retain
        deleted_time = convert_iso_date(vm.deleted_at)
        diff = retain_duration - (datetime.now() - deleted_time).days
        if diff <= 1:
            recycle_bin_info["size_release_today"] += vm.size
        elif diff <= 7:
            recycle_bin_info["size_release_in_7_days"] += vm.size
        recycle_bin_info["size"] += vm.size
    recycle_bin_info["size"] = format_unit(
        recycle_bin_info["size"], byte_units)
    recycle_bin_info["size_release_today"] = format_unit(
        recycle_bin_info["size_release_today"], byte_units)
    recycle_bin_info["size_release_in_7_days"] = format_unit(
        recycle_bin_info["size_release_in_7_days"], byte_units)
    return recycle_bin_info
```
