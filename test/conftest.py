import pytest
import json
import os
import time
import glob

from cloudtower_python_sdk.models import GetTasksRequestBody, TaskWhereInput, TaskStatus, GetGlobalSettingsesRequestBody, GlobalRecycleBinUpdationParams
from cloudtower_python_sdk.exceptions import ApiException

TIMEOUT = 5 * 60

# dynamic load fixture from fixture folder
pytest_plugins = [
    fixture_file.replace("/", ".").replace(".py", "")
    for fixture_file in glob.glob(
        "test/fixture/**/[!__]*.py",
        recursive=True
    )
]


@pytest.fixture(scope="session")
def wait_task(task_api):
    def wait(id):
        start = time.time()
        query_task = task_api.get_tasks(get_tasks_request_body=GetTasksRequestBody(
            where=TaskWhereInput(
                id=id
            )
        ))[0]

        while query_task.status == TaskStatus.EXECUTING or query_task.status == TaskStatus.PENDING:
            now = time.time()
            if (now-start) > TIMEOUT:
                raise ApiException(408, "Timeout while waiting for task finished")
            time.sleep(3)
            query_task = task_api.get_tasks(get_tasks_request_body=GetTasksRequestBody(
                where=TaskWhereInput(
                    id=id
                )
            ))[0]
        if query_task.status != TaskStatus.SUCCESSED:
            raise ApiException(500, "Task failed")
        return
    return wait


@pytest.fixture(scope="session")
def wait_entity_async_status():
    def wait(api, func, args, parse=lambda val: getattr(val, '_entity_async_status') if hasattr(val, '_entity_async_status') else None):
        try:
            func = getattr(api, func)
        except AttributeError as e:
            raise ApiException(400, "incorrect function")
        start = time.time()
        val = func(args)
        val = val if not isinstance(val, list) else (val[0] if len(val) != 0 else None)
        if val is None:
            # return is resource is removed
            return
        while bool(parse(val)):
            # if entity async status is not null, meaning resource is updating
            now = time.time()
            if (now-start) > TIMEOUT:
                raise ApiException(408, "Timeout while waiting for task finished")
            time.sleep(3)
            val = func(args)
            val = val[0] if isinstance(val, list) else val
        return
    return wait


@pytest.fixture(scope="function")
def open_recycle_bin_if_close(global_settings_api, wait_task):
    origin = None

    def open_recycle_bin():
        setting = global_settings_api.get_global_settingses(
            get_global_settingses_request_body=GetGlobalSettingsesRequestBody())[0]
        if not setting.vm_recycle_bin.enabled:
           # if global setting is not enabled, open it
            origin = {
                "enabled": False,
                "retain": setting.vm_recycle_bin.retain,
            }
            open_recycle_bin_result = global_settings_api.update_global_recycle_bin_setting(global_recycle_bin_updation_params=GlobalRecycleBinUpdationParams(
                enabled=True,
                retain=30
            ))
            wait_task(open_recycle_bin_result.task_id)
        return
    yield open_recycle_bin
    if origin is not None:
        # return global setting to its original state
        close_recycle_bin_result = global_settings_api.update_global_recycle_bin_setting(
            global_recycle_bin_updation_params=GlobalRecycleBinUpdationParams(
                enabled=origin["enabled"],
                retain=origin["retain"]
            )
        )
        wait_task(close_recycle_bin_result.task_id)


@pytest.fixture(scope="function")
def close_recycle_bin_if_open(global_settings_api, wait_task):
    origin = None

    def close_recycle_bin():
        setting = global_settings_api.get_global_settingses(
            get_global_settingses_request_body=GetGlobalSettingsesRequestBody())[0]
        if setting.vm_recycle_bin.enabled:
           # if global setting is not enabled, open it
            origin = {
                "enabled": True,
                "retain": setting.vm_recycle_bin.retain,
            }
            close_recycle_bin_result = global_settings_api.update_global_recycle_bin_setting(global_recycle_bin_updation_params=GlobalRecycleBinUpdationParams(
                enabled=False,
                retain=30
            ))
            wait_task(close_recycle_bin_result.task_id)
        return
    yield open_recycle_bin
    if origin is not None:
        # return global setting to its original state
        open_recycle_bin_result = global_settings_api.update_global_recycle_bin_setting(
            global_recycle_bin_updation_params=GlobalRecycleBinUpdationParams(
                enabled=origin["enabled"],
                retain=origin["retain"]
            )
        )
        wait_task(open_recycle_bin_result.task_id)
