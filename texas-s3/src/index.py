import json

from s3_client import *
from drinks_api_client import *

def lambda_handler(event, context):
    rest_name = 'HONDURAS MAYA CAFE & BAR LLC'
    
    receipts = find_receipts(rest_name)
    files_and_names = build_files_dir_names(rest_name, dir_prefix = '/tmp')
    (dir_name, full_dir_path, file_name, path_prefix_file_name) = files_and_names.values()
    build_directory(full_dir_path)
    write_to_json(receipts, path_prefix_file_name)
    
    bucket_name = 'jigsawtxdrinks'
    
    read_and_upload(path_prefix_file_name, bucket_name, destination_file=f'{dir_name}/{file_name}')
    
    return {'file_name': file_name}

print(lambda_handler({}, {}))