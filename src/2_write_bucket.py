import json
import boto3

s3 = boto3.client('s3')
# response = s3.create_bucket(Bucket = 'jigsaw-sample-json')

# json_object = {'hello': 'world'}

# s3.upload_file('./yelp-lunch-nyc.csv', 'jigsaw-sample-json', 'lunch.csv')

# obj = s3.get_object(Bucket='jigsaw-sample-json', Key='lunch.csv')

# obj['Key'].read()

