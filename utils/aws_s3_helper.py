import boto3
import os

def upload_file_to_s3(file_path, bucket, key):
    if not os.path.exists(file_path):
        return

    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket, key)
