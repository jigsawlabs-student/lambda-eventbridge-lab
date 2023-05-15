import json
import boto3
import requests

def find_receipts(name):
    url = "https://data.texas.gov/resource/naix-2893.json"
    response = requests.get(url, params = {'taxpayer_name': name})
    return response.json()

def cleaned_name(rest_name):
    cleaned_name = rest_name.lower().replace(' ', '_')
    return cleaned_name

def write_to_json(data, rest_name):
    clean_name = cleaned_name(rest_name)
    with open(f'./data/{clean_name}.json', 'w') as f:
        f.write(json.dumps(data))

def read_from_file(rest_name):
    cleaned_name = rest_name.lower().replace(' ', '_')
    f = open(f'./data/{cleaned_name}.json', "r")
    text = f.read()
    return json.loads(text)

name = 'HONDURAS MAYA CAFE & BAR LLC'
receipts = find_receipts(name)

