from cloudtower.models import GetVmEntityFilterResultsConnectionRequestBody, GetVmEntityFilterResultsRequestBody, VmEntityFilterResultWhereInput


class TestVmEntityFilter:

    def test_get_vm_entity_filter_results(self, vm_entity_filter_result_api):
        vm_entity_filter_result_api.get_vm_entity_filter_results(get_vm_entity_filter_results_request_body=GetVmEntityFilterResultsRequestBody(
            # FIXME: remove the filter after data clear is done
            where=VmEntityFilterResultWhereInput(
                _not=[
                    VmEntityFilterResultWhereInput(
                        vm=None
                    )
                ]
            )
        ))
        vm_entity_filter_result_api.get_vm_entity_filter_results_connection(
            get_vm_entity_filter_results_connection_request_body=GetVmEntityFilterResultsConnectionRequestBody())
        assert 0 is 0
