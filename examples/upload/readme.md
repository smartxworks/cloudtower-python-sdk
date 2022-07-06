## 文件上传

CloudTower 的文件上传需要首先创建一个上传任务，然后使用 Api 分片上传文件，分片大小为 8MB，SDK 简化了上传步骤，将上传类资源的分片上传和创建上传任务封装为同一个 api，这里以上传虚拟机工具镜像为例。

```python
from cloudtower import (
    ApiClient,
    Configuration,
)
from cloudtower.utils import login, get_svt_image_version
from cloudtower.api import SvtImageApi
import os

def upload_svt_image(api_client: ApiClient, path: str):
    svt_api = SvtImageApi(api_client)
    version = get_svt_image_version(path)
    with open(path, 'rb') as iso:
        chunk = iso.read(8*1024*1024)
        resp = svt_api.upload_svt_image(file=chunk, version=version, size=str(
            os.path.getsize(path)), cluster_id="cl3kursoo2pxm0858veopm4qs", name="test-from-python-sdk")
        upload_task_id = resp[0].id
        chunk = iso.read(8*1024*1024)
        while len(chunk) > 0:
            resp = svt_api.upload_svt_image(file=chunk, version=version, size=str(
                os.path.getsize(path)), cluster_id="cl3kursoo2pxm0858veopm4qs", name="test-from-python-sdk", upload_task_id=upload_task_id)
            chunk = iso.read(8*1024*1024)

conf = Configuration(host="http://api-test.dev-cloudtower.smartx.com/v2/api")
api_client = ApiClient(conf)
login(api_client, "root", "HC!r0cks")
upload_svt_image(api_client, 'D:\\SMTX_VMTOOLS_2_12_1_20210521153518.iso')
```
