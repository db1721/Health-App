from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
import boto3
import botocore
from botocore.exceptions import ClientError
import logging
import json
import random
import decimal
import os
os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = 'AKIAIOSFODNN7EXAMPLE'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'


#****************************************
#S3 methods
#****************************************
def getS3object(object_name):
    """
    Download a file form selected bucket
    
    """
    PORT_S3=9444
    def connect():
        return boto3.client("s3", endpoint_url="http://localhost:%s" % PORT_S3)
    s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
    )
    bucket_name = "exercises"

    try:
        connect()
        s3.Bucket(bucket_name).download_file(Filename='standing_bicep_curls.jpeg')
        # s3.Bucket(bucket_name).download_file(object_name, "{0}".format(object_name))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
