from drinks_api_client import *
import boto3
s3 = boto3.client('s3')

def read_and_upload(file_name, bucket_name, destination_file):
    # first arg is to read from ......... then write to
    s3.upload_file(file_name, bucket_name, destination_file)

def read_data_from(bucket, object):
    obj = s3.get_object(Bucket=bucket, Key=object)
    text = obj['Body'].read()
    data = json.loads(text)
    return data

def store_restaurant_data(restaurants, bucket):
    for restaurant in restaurants:
        data = find_receipts(restaurant)
        file_name = cleaned_name(restaurant)
        s3.put_object(Body=json.dumps(data),
        Bucket=bucket,
        Key=f'{file_name}.json')


