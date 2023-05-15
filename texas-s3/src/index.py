from s3_client import *
from drinks_api_client import *
import boto3
import os

s3 = boto3.client('s3')

rest_name = 'HONDURAS MAYA CAFE & BAR LLC'

# receipts = find_receipts(rest_name)

# write_to_json(data, rest_name)

# bucket_name = 'jigsawtxdrinks'
# bucket = s3.create_bucket(Bucket = bucket_name)

# file_name = cleaned_name(rest_name)
# object_name = f'./data/{file_name}'
# read_and_upload(object_name, bucket_name)
# read_data_from(bucket_name, object_name)




