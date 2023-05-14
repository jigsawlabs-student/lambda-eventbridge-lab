import json
import boto3
import requests
s3 = boto3.client('s3')

bucket = s3.create_bucket(Bucket = 'jigsaw-sample-json')

url = "https://data.texas.gov/resource/naix-2893.json?taxpayer_name=HONDURAS MAYA CAFE %26 BAR LLC"
response = requests.get(url)
json_obj = response.json()

s3.put_object(
     Body=json.dumps(json_obj),
     Bucket='jigsaw-sample-json',
     Key='drink_receipts.json'
)

# s3 = boto3.client('s3')
# sample = s3.get_object(Bucket='jigsaw-sample-json', Key='drink_receipts.json')
# sample['Body'].read()

# https://levelup.gitconnected.com/loading-data-from-s3-to-aws-athena-7c56c63efccc
# https://adamtheautomator.com/aws-athena/
# https://www.youtube.com/watch?v=M5ptG0YaqAs&ab_channel=BeABetterDev

# https://aws-dojo.com/excercises/excercise33/ - storing data in temp path