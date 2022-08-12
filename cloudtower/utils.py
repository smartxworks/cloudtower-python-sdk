import time
from cloudtower.api_client import ApiClient
from cloudtower.models import GetTasksRequestBody, TaskWhereInput, TaskStatus, UserSource
from cloudtower.exceptions import ApiException
from cloudtower.api.task_api import TaskApi
from cloudtower.api.user_api import UserApi


def wait_tasks(ids, api_client, interval=5, timeout=300, exit_on_error=False):
    """wait_tasks  # noqa: E501

      This method will poll tasks status until they are complete or timeout,
      will raise an exception when timeout or some tasks failed.
      >>> thread = wait_tasks(ids, api_client)
      >>> result = thread.get()
      :param ids: (required) the list of task ids need to poll
      :type ids: list[str]
      :param api_client: (required) the api client to construct TaskApi
      :type api_client: ApiClient
      :param interval: The interval of polling. Default is 5.
      :type interval: int, optional
      :param timeout: The threshold to raise timeout exception. Default is 300.
      :type timeout: int, optional
      :param exit_on_error: Whether to exit on error immediately,
                            or wait all tasks are done.
                            Default is False.
      :type exit_on_error: bool, optional
    """
    task_api = TaskApi(api_client)
    start = time.time()
    error_ids = []
    while len(ids):
        now = time.time()
        if (now-start) > timeout:
            raise ApiException(
                408, "Timeout while waiting for task finished")
        time.sleep(interval)
        tasks = task_api.get_tasks(get_tasks_request_body=GetTasksRequestBody(
            where=TaskWhereInput(
                id_in=ids
            )
        ))
        for task in tasks:
            if task.status == TaskStatus.FAILED:
                if exit_on_error:
                    raise ApiException(500, "Task %s failed" % task.id)
                else:
                    ids.remove(task.id)
                    error_ids.append(task.id)
            elif task.status == TaskStatus.SUCCESSED:
                ids.remove(task.id)
    if len(error_ids):
        raise ApiException(500, "All Tasks failed" if len(
            error_ids) else "Tasks %s failed" % error_ids)
    return


def login(api_client: ApiClient, username, password, source=UserSource.LOCAL):
    """login # noqa: E501
    the method will try to login with provided username and password
    :params api_client: (required) api client to set up login status
    :type api_client: ApiClient
    :param username: (required) username to login
    :type username: str    
    :param password: (required) password to login
    :type password: str
    :param source: login user's source, default is local
    :type password: UserSource
    """
    user_api = UserApi(api_client)
    login_res = user_api.login({
        "username": username,
        "password": password,
        "source": source
    })
    api_client.configuration.api_key["Authorization"] = login_res.data.token
    return
