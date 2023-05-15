from s3_client import *
def test_read_and_upload():
    file_name = './test_data/sample.json'
    # fill in bucket name here
    bucket_name = ''
    read_and_upload(file_name, bucket_name)
    obj = s3.get_object(Bucket=bucket_name, Key=object)
    text = obj['Body'].read()
    data = json.loads(text)
    assert data == [{'hello': 'world'}, {'hola': 'mundo'}]

def test_store_restaurant_data():
    restaurants = ['']
    bucket_name = '' # fill in bucket name here
    store_restaurant_data(restaurants, bucket_name)
    assert s3.list_objects(Bucket=bucket_name) == ['']