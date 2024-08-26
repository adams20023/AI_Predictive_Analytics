# src/s3_storage.py
import boto3
import os

def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_name)
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def download_from_s3(bucket, object_name, file_name):
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket, object_name, file_name)

