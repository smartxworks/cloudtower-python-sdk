# RELEASE NOTE

## release 日期 2022-07-08

v2.1.0 release

- feature:ClusterApi: [update_cluster_network_setting] 新增更新集群网络配置 api
- feature:ClusterApi: [update_cluster_virtualization_setting] 新增更新集群虚拟化设置 api
- feature:ClusterApi: [update_cluster_ha_setting] 新增更新集群高可用设置 api
- feature:ClusterApi: [update_cluster_enable_iscsi_setting] 新增更新集群块功能启用设置 api
- feature:VmApi: [migratevm_across_cluster] 新增跨集群迁移虚拟机 api
- feature:VmApi: [abort_migrate_vm_across_cluster] 新增取消跨集群迁移 api
- feature:VmApi: [stop_vm_in_cutover_migration] 新增关闭源虚拟机 api
- feature:VmApi: [update_vmHostOptions] 新增更新虚拟机 guest os 设置 api，更新 dns, hostname 与 ntp server，需要虚拟机工具的支持。
- feature:VmApi: [reset_vmG_guest_ss_password] 新增更新虚拟机 guest os 用户密码 api，需要虚拟机工具的支持。
- feature:VmApi: [update_vm_owner] 新增更新虚拟机拥有者 api
- feature:SecurityApi: [update_password_security] 新增更新密码安全设置 api
- feature:SecurityApi: [update_access_restriction] 新增更新访问限制 api
- feature:SecurityApi: [update_session_timeout] 新增更新会话超时 api
- feature:VcenterAccountApi: [update_vcenter_account] 新增更新 vcenter 账号 api
- feature:VcenterAccountApi: [create_vcenter_account] 新增添加 vcenter 账号 api
- feature:VsphereEsxiAccountApi: [update_vsphere_esxi_account] 新增更新 vsphere esxi 账号 api
- feature:SvtImageApi: [upload_svt_image] 新增上传虚拟机镜像 api 工具
- feature:TableReporterApi: [export_csv] 新增导出 CSV 报表 api
- feature:UploadTaskApi: [cancel_upload_task] 新增取消上传 api
- feature:LabelApi: [add_labels_to_resources],[remove_labels_from_resources] 新增想内容库模板，内容库镜像，隔离策略，安全策略添加，删除标签

- bugfix:ContentLibraryImageApi,ElfImageApi: 修复了上传类 Api 无法正确执行的问题，并优化了上传类 Api 的执行逻辑，第一次上传时会上传第一个分片而非只是创建一个上传任务，详见[示例](/examples/upload/readme.md)

- optimize:VmTemplateApi: 优化了模板创建时根据传入的 cpu 参数和模板参数计算缺省值的逻辑
- optimize:ContentLibraryImageApi: 优化了分发的逻辑，不再同时上传一个镜像至多个集群，等待上传置单个集群后再分发。
- optimize: 添加了 `util.login` 方法来维护登录逻辑，不再需要手动赋值 token。
- optimize: 添加了 `util.get_svt_image_version` 方法来获取一个虚拟机工具镜像的版本号
- optimize: 优化了对文件参数的处理，现在可以传递一个 `bytes` 来作为文件类的参数，而非只能使用文件路径

## release 日期：2022-06-13

v2.0.0.post1 release

- bugfix: [Cluster],[ClusterWhereInput]: 修复 `usedMemoryBytes`, `usedCpuUsage` 的数据类型 Long -> Double
- bugfix: [Host],[HostWhereInput]: 修复 `usedMemoryBytes`, `usedCpuUsage`的数据类型 Long -> Double
- bugfix: [Datacenter],[DatacenterWhereInput]: 修复 `usedMemoryBytes`, `usedCpuUsage` 的数据类型 Long -> Double

## release 日期：2022-05-20

v2.0.0 release

- feature: 开放内容库相关 Api [ContentLibraryImage], [ContentLibraryVMTemplate]
- feature: 新增 [Metric] 功能，用于查询资源性能指标

## release 日期：2022-05-20

v1.10.0.post1 release

- bugfix: [Witness] 从 `Witness` 中移除了 `management_ip`

## release 日期：2022-05-17

v1.10.0 release

- **breaking change**: 直接使用 `**kwargs` 来构造参数，避免部分构造函数的参数数量超过 255 导致的 3.7- 及以下版本的 Python3 无法使用 sdk 的问题, 如果使用 `param = Param(args1,args2,args3)` 形式构建参数，需要替换为 `param = Param(args1=args1,args2=args2,args3=args3)` 或者 `param = Param(**{'args1':args1,'args2':args2,'args3':args3})`
- feature: UserApi: [createRootUser]: 创建初始 root 用户，创建用户需要传递 role id，而获取 role id 需要鉴权，提供一个接口在没有账号被建立的情况下创建一个默认的 root 用户，不需要鉴权;
- feature: VmApi: [expand_vm_disk]: 提供扩容指定虚拟盘的能力;
- feature: VmApi: [eject_iso_from_vm_cd_rom]: 将 iso 从 vm cdrom 中卸载;
- feature: VmApi: [toggle_vm_cd_rom_disable]: 禁用、启用 vm cdrom;
- feature: VmApi: [update_vm_nic_basic_info]: 更新一个虚拟机网卡的常用信息，包括 IP 地址，网关地址，子网掩码，需要虚拟机工具的支持;
- feature: VmApi: [update_vm_nic_advance_info]: 更新一个虚拟机网卡的非常用信息，包括接入的虚拟网络，sriov 网卡的直连网卡，mac 地址，是否启用，以及是否开启镜像模式;
- feature: VmApi: [update_vm_advanced_options]: 更新虚拟机的高级信息，包括 CPU 兼容性，虚拟机时钟(UTC、LocalTime)，是否开启为 windows 优化，以及虚拟机显卡型号;
- optimize: 提供了更加完整的错误返回信息，包含了错误发生的位置，graphql operationName，并透传 tower server 状态码。
- optimize: 缩短了部分变量类型名称。
- bugfix: VmApi: [create_vm_from_template], []: 修复了无法在使用模板创建虚拟机时挂载已存在的虚拟机和 cd-rom 的问题，修正 MountDiskParams 中的 index 为可选项。
- bugfix: 使用了更加准确的数字类型，将以 Byte，HZ 为单位的数字类型从 Double 转为了 Long;
- bugfix: 修复 `waitTask` 在 task 出错时会轮询直到超时;
- bugfix: 将分类错误的 endpoint 移至正确的 api 下:
  - [get_iscsi_connections]: IscsiApi -> IscsiConnectionApi
  - [create_nvmf_subsystem]: DefaultApi -> NvmfSubsystemApi
  - [delete_nvmf_subsystem]: DefaultApi -> NvmfSubsystemApi
  - [update_nvmf_subsystem]: DefaultApi -> NvmfSubsystemApi
