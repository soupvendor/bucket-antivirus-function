# -*- coding: utf-8 -*-
import boto3
import botocore.exceptions
import os

clamav_ver = os.getenv("CLAMAV_LATEST", default=None)
s3_bucket = os.getenv("S3_BUCKET", default=None)

client = boto3.client("s3")
s3 = boto3.resoruce("s3")

zip = f"lambda-{clamav_ver}.zip"

try:
    response = client.head_object(Bucket=s3_bucket, Key=zip)
    if response:
        print(f"{zip} exists, skipping.")
    else:
        s3.Object(s3_bucket, zip).upload_file("../build/lambda.zip")
        print(f"Successfully uploaded {zip}")

except botocore.exceptions.ClientError as err:
    print(err)
