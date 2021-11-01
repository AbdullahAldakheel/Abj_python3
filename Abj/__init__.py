import logging
from datetime import datetime
import json
from decouple import AutoConfig
import requests
import os 
import time
from minio import Minio
from minio.error import S3Error





	
dir_path = os.path.abspath(os.curdir)
extra_tags={}
config = AutoConfig(search_path=dir_path)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Request Plan
# Update Job Status.
def update_status(job_id, status, status_msg=None, data=None):
        pload = {'job_id': job_id, 'data': data, 'status': status, 'status_msg': status_msg}
        headers = {}
        r =requests.post(config('PLATFORM_API') + 'api/job', data = pload, headers = headers)
        print(r)
        return None







def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        config('BUCKET_API'),
        access_key=config('BUCKET_ACCESS_KEY'),
        secret_key=config('BUCKET_SECRET_KEY'),
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("abj")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "asiatrip", "asiaphotos-2015.zip", "/home/user/Photos/asiaphotos.zip",
    )
    print(
        "'/home/user/Photos/asiaphotos.zip' is successfully uploaded as "
        "object 'asiaphotos-2015.zip' to bucket 'asiatrip'."
    )
