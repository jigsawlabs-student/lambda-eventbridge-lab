from src.drinks_api_client import *

def test_find_receipts():
    receipts = find_receipts()
    assert type(receipts) == list
    assert type(receipts[0]) == dict

def test_cleaned_name():
    rest_name = 'HONDURAS MAYA CAFE & BAR LLC'
    assert cleaned_name(rest_name) == 'honduras_maya_cafe_&_bar_llc.json'

def test_write_to_json():
    data = [{'hello': 'world'}]
    rest_name = 'HONDURAS MAYA CAFE & BAR LLC'
    
    write_to_json(data, rest_name)
    file_name = './data/honduras_maya_cafe_&_bar_llc.json'
    f = open(file_name, "r")
    text = f.read()
    read_text = json.loads(text)
    assert read_text == data

def test_read_from_file():
    data = [{'hello': 'world'}]
    file_name = 'honduras_maya'
    with open(f'./data/{rest_name}.json', 'w') as f:
        f.write(json.dumps(data))
    rest_name = 'HONDURAS MAYA'
    assert read_from_file(rest_name) == data
    
    