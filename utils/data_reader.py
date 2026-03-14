import json

def get_test_data():

    with open("testdata/testdata.json") as f:
        data = json.load(f)

    return data