import logging
from multiprocessing.pool import ThreadPool

from cloudtower.models import UploadResourceType, UploadTaskStatus
from cloudtower.api import UploadTaskApi, ContentLibraryImageApi, ElfImageApi

logger = logging.getLogger(__name__)


def get_svt_image_version(path):
    p = ""
    with open(path, "rb") as file:
        file.seek(32*1024+190)
        p = file.read(128).decode("utf-8").strip()
    return p


def get_content_library_image_by_upload_task(api_client, get_upload_tasks_request_body):
    pool = ThreadPool(10)
    try:
        upload_task_api = UploadTaskApi(api_client)
        image_api = ContentLibraryImageApi(api_client)
        tasks = upload_task_api.get_upload_tasks(get_upload_tasks_request_body)
        results = dict()
        for task in tasks:
            if task.resource_type == UploadResourceType.CONTENT_LIBRARY_IMAGE:
                if task.status == UploadTaskStatus.SUCCESSED:
                    elf_image_local_ids = task.args.get(
                        "uploadElfImageLocalIds", None)
                    zbs_volume_ids = task.args.get(
                        "uploadIscsiLunZbsVolumeIds", None)
                    if elf_image_local_ids is not None and len(elf_image_local_ids) > 0:
                        args = {
                            "where": {
                                "elf_images_some": {
                                    "local_id": elf_image_local_ids[0]
                                }
                            }
                        }
                        results[task.id] = pool.apply_async(
                            func=image_api.get_content_library_images, kwds={
                                "get_content_library_images_request_body": args
                            })
                    elif zbs_volume_ids is not None and len(zbs_volume_ids) > 0:
                        args = {
                            "where": {
                                "iscsi_luns_some": {
                                    "zbs_volume_id": zbs_volume_ids[0]
                                }
                            }
                        }
                        results[task.id] = pool.apply_async(
                            func=image_api.get_content_library_images, kwds={
                                "get_content_library_images_request_body": args
                            })
                else:
                    logger.warning("upload task %s's status is %s but not success",
                                   task.id, task.status)
            else:
                logger.warning("upload task %s's type is %s but not CONTENT_LIBRARY_IMAGE",
                               task.id, task.resource_type)
        pool.close()
        pool.join()
        for task_id in results.keys():
            images = results[task_id].get()
            if len(images) > 0:
                results[task_id] = images[0]
            else:
                results[task_id] = None
        return results
    finally:
        pool.terminate()


def get_elf_image_by_upload_task(api_client, get_upload_tasks_request_body):
    pool = ThreadPool(10)
    try:
        upload_task_api = UploadTaskApi(api_client)
        image_api = ElfImageApi(api_client)
        tasks = upload_task_api.get_upload_tasks(get_upload_tasks_request_body)
        results = dict()
        for task in tasks:
            if task.resource_type == UploadResourceType.ELF_IMAGE:
                if task.status == UploadTaskStatus.SUCCESSED:
                    attributes = task.args.get("attributes", None)
                    local_id = attributes.get("uuid", None)
                    if local_id is not None:
                        args = {
                            "where": {
                                "local_id": local_id
                            }
                        }
                        results[task.id] = pool.apply_async(
                            func=image_api.get_elf_images, kwds={
                                "get_elf_images_request_body": args
                            })
                else:
                    logger.warning("upload task %s's status is %s but not success",
                                   task.id, task.status)
            else:
                logger.warning("upload task %s's type is %s but not ELF_IMAGE",
                               task.id, task.resource_type)
        pool.close()
        pool.join()
        for task_id in results.keys():
            images = results[task_id].get()
            if len(images) > 0:
                results[task_id] = images[0]
            else:
                results[task_id] = None
        return results
    finally:
        pool.terminate()
