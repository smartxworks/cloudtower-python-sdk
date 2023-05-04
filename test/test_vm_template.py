import time

from cloudtower.models import (
    GetVmTemplatesRequestBody,
    GetVmTemplatesConnectionRequestBody,
    VmTemplateCreationParams,
    VmTemplateUpdationParams,
    VmTemplateUpdationParamsData,
    VmTemplateDeletionParams,
    VmTemplateWhereInput,
    ConvertVmTemplateToVmParams,
    VmCreateVmFromTemplateParams,
    VmOperateParams,
    VmDeleteParams,
    VmWhereInput,
)


class TestVmTemplate:

    def test_get_vm_templates(self, vm_template_api):
        vm_template_api.get_vm_templates(get_vm_templates_request_body=GetVmTemplatesRequestBody())
        vm_template_api.get_vm_templates_connection(
            get_vm_templates_connection_request_body=GetVmTemplatesConnectionRequestBody())
        assert 0 is 0

    def test_clone_vm_template_and_update_and_delete(self, vm_template_api, stopped_vm, default_cluster, wait_task):
        clone_param = [
            VmTemplateCreationParams(
                name="tower-python-sdk-test-vm-template-clone"+str(int(time.time())),
                vm_id=stopped_vm.id,
                cluster_id=default_cluster.id,
                cloud_init_supported=False
            )
        ]
        clone_result = vm_template_api.clone_vm_template_from_vm(
            vm_template_creation_params=clone_param
        )
        assert clone_result is not None
        wait_task(clone_result[0].task_id)

        update_param = VmTemplateUpdationParams(
            data=VmTemplateUpdationParamsData(
                name="tower-python-sdk-test-vm-template-updated"+str(int(time.time()))
            ),
            where=VmTemplateWhereInput(
                id=clone_result[0].data.id
            )
        )
        update_result = vm_template_api.update_vm_template(
            vm_template_updation_params=update_param
        )
        assert update_result is not None
        wait_task(update_result[0].task_id)

        delete_param = VmTemplateDeletionParams(
            where=VmTemplateWhereInput(
                id=clone_result[0].data.id
            )
        )
        delete_result = vm_template_api.delete_vm_template(
            vm_template_deletion_params=delete_param
        )
        assert delete_result is not None
        wait_task(delete_result[0].task_id)

    def test_convert_vm_template_and_delete(self, vm_template_api, stopped_vm, default_cluster, wait_task):
        convert_param = [
            VmTemplateCreationParams(
                name="tower-python-sdk-test-vm-template-convert"+str(int(time.time())),
                cluster_id=default_cluster.id,
                vm_id=stopped_vm.id,
                cloud_init_supported=False
            )
        ]
        convert_result = vm_template_api.convert_vm_template_from_vm(
            vm_template_creation_params=convert_param
        )
        assert convert_result is not None
        wait_task(convert_result[0].task_id)
        update_param = VmTemplateUpdationParams(
            data=VmTemplateUpdationParamsData(
                name="tower-python-sdk-test-vm-template-updated"+str(int(time.time()))
            ),
            where=VmTemplateWhereInput(
                id=convert_result[0].data.id
            )
        )
        update_result = vm_template_api.update_vm_template(
            vm_template_updation_params=update_param
        )
        assert update_result is not None
        wait_task(update_result[0].task_id)

        delete_param = VmTemplateDeletionParams(
            where=VmTemplateWhereInput(
                id=convert_result[0].data.id
            )
        )
        delete_result = vm_template_api.delete_vm_template(
            vm_template_deletion_params=delete_param
        )
        assert delete_result is not None
        wait_task(delete_result[0].task_id)

    def test_convert_vm_template_to_vm(self, vm_api, vm_template_api, vm_template, wait_task):
        convert_param = [
            ConvertVmTemplateToVmParams(
                converted_from_template_id=vm_template.id,
                name="tower-python-sdk-test-vm-template-convert-to-vm"+str(int(time.time())),
            )
        ]
        convert_result = vm_api.convert_vm_template_to_vm(
            convert_vm_template_to_vm_params=convert_param
        )
        assert convert_result is not None
        wait_task(convert_result[0].task_id)

        delete_param = VmDeleteParams(
            where=VmWhereInput(
                id=convert_result[0].data.id
            )
        )
        delete_result = vm_api.delete_vm(
            vm_delete_params=delete_param
        )
        wait_task(delete_result[0].task_id)

    def test_create_vm_from_template(self, vm_api, vm_template_api, vm_template, wait_task):
        create_param = [
            VmCreateVmFromTemplateParams(
                template_id=vm_template.id,
                name="tower-python-sdk-test-vm-from-template"+str(int(time.time())),
                cluster_id=vm_template.cluster.id,
                is_full_copy=False
            )
        ]
        create_result = vm_api.create_vm_from_template(
            vm_create_vm_from_template_params=create_param
        )
        assert create_result is not None
        wait_task(create_result[0].task_id)

        delete_param = VmDeleteParams(
            where=VmWhereInput(
                id=create_result[0].data.id
            )
        )
        delete_result = vm_api.delete_vm(
            vm_delete_params=delete_param
        )
        wait_task(delete_result[0].task_id)
