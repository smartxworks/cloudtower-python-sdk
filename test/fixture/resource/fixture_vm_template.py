import pytest
import time

from cloudtower.models import (
    GetVmTemplatesRequestBody,
    VmTemplateCreationParams,
    VmTemplateDeletionParams,
    VmTemplateWhereInput
)


@pytest.fixture(scope="function")
def vm_template(vm_template_api, stopped_vm, default_cluster, wait_task):
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
    wait_task(clone_result[0].task_id)
    yield clone_result[0].data
    templates = vm_template_api.get_vm_templates(get_vm_templates_request_body=GetVmTemplatesRequestBody(
        where=VmTemplateWhereInput(
            id=clone_result[0].data.id
        )
    ))
    if len(templates) == 0:
        return
    delete_param = VmTemplateDeletionParams(
        where=VmTemplateWhereInput(
            id=clone_result[0].data.id
        )
    )
    delete_result = vm_template_api.delete_vm_template(
        vm_template_deletion_params=delete_param
    )
    wait_task(delete_result[0].task_id)
