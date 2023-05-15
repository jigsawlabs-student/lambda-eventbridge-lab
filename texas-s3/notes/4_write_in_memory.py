import json
import boto3
import requests
import io

s3 = boto3.client('s3')

url = "https://data.texas.gov/resource/naix-2893.json?taxpayer_name=HONDURAS MAYA CAFE %26 BAR LLC"
response = requests.get(url)
receipts = response.json()

file = io.StringIO("")
for receipt in receipts:
    file.write(json.dumps(receipt))
    file.write('\n')


text = file.getvalue()
s3.put_object(
     Body=text,
     Bucket='jigsaw-sample-json',
     Key='drinks.json'
)
