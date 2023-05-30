import json
import boto3
import requests
from datetime import datetime
from pathlib import Path

def build_directory(dir_path):
    Path(dir_path).mkdir(parents=True, exist_ok=True)

def build_files_dir_names(rest_name, dir_prefix = '/tmp'):
    dir_name = cleaned_name(rest_name)
    full_dir_path = f'{dir_prefix}/{dir_name}'
    file_name = build_datetime_name()
    path_prefix_file_name = f'{full_dir_path}/{file_name}'
    return {'dir_name': dir_name, 
            'full_dir_path': full_dir_path, 
            'file_name': file_name, 
            'path_prefix_file_name': path_prefix_file_name
            }

def build_datetime_name():
    now = datetime.now()
    txt_datetime = now.strftime("%m-%d-%Y-%H:%M:%S")
    object_name = f'{txt_datetime}.json'
    return object_name

def cleaned_name(rest_name):
    cleaned_name = rest_name.lower().replace(' ', '_')
    return cleaned_name

def write_to_json(data, file_name):
    with open(file_name, 'w') as f:
        f.write(json.dumps(data))

def find_receipts(name):
    url = "https://data.texas.gov/resource/naix-2893.json"
    response = requests.get(url, params = {'taxpayer_name': name})
    return response.json()

