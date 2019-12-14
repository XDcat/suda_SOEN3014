# -*- coding: utf-8 -*-
import requests
import json
from pprint import pprint

def do_request(data):
    print(data)
    ip = [
        # 'http://10.40.34.87:5000/body',
        # "http://127.0.0.1:5000/body",
        "http://127.0.0.1:5000/all"
    ]
    return requests.post("http://127.0.0.1:5000/all", json=json.dumps(data))

def connect():
    data = {
        "ID": 1709404010,
        "NAME": "曾连杰",
        "GENDER": "M",
        "AGE": 19,
        "JK": 60,
        "XW": 60,
        "YW": 60,
        "XC": 60,
        "XM": 41,
        "SG": 171,
        "TZ": 60,
    }




    response = do_request(data)
    pprint(response.content)
    pprint(json.loads(response.content))

if __name__ == '__main__':
    connect()