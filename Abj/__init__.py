from decouple import AutoConfig
import requests
import os 
from minio import Minio

dir_path = os.path.abspath(os.curdir)
config = AutoConfig(search_path=dir_path)


# Bucket Connections.
client = Minio(
    config('BUCKET_API'),
    access_key=config('BUCKET_ACCESS_KEY'),
    secret_key=config('BUCKET_SECRET_KEY'),
    secure=False
)

# Request Plan
# Update Job Status.
def update_status(job_id, status, status_msg=None, data=None):
        pload = {'job_id': job_id, 'data': data, 'status': status, 'status_msg': status_msg}
        headers = {}
        r =requests.post(config('PLATFORM_API') + 'api/job', data = pload, headers = headers)
        print(r)
        return None







def putInBucket(path, filename, file):
    print('Start Moving To: ' + config('BUCKET_NAME'))
    # Move File To The File.
    # Upload data.
    result = client.fput_object(
        config('BUCKET_NAME'),  path + '/' + filename, file,
    )
    print(
        "created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,
        ),
    )
    if not result:
        print('Error')
        return False
    else:
        return True

def getFromBucket(path):
    print('Get File From: ' + config('BUCKET_NAME'))
    # Move File To The File.
    # Upload data.

    # Get data of an object.
    try:
        response = client.get_object(
            config('BUCKET_NAME'), path
        )
        # Read data from response.
    finally:
        response.release_conn()

    if not response:
        print('Error')
        return False
    else:
        return response.data


# putInBucket('/model/test/id','result.json', '/Users/ahd/Desktop/abj_python3/Abj/test.json')
# getFromBucket('/model/test/id/result.json');