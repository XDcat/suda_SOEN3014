# -*- coding: utf-8 -*-
import requests
import json
from pprint import pprint

url1 = "http://127.0.0.1:5000/similar"
url2 = "http://127.0.0.1:5000/similar/find"


def connect():
    data = {
        "num": "17274060"
    }
    data = None

    response = requests.post("http://127.0.0.1:5000/similar/find", json=json.dumps(data))
    pprint(response.content)
    pprint(json.loads(response.content))


if __name__ == '__main__':
    print("1. 测试查找所有学生中最相似的同学")
    print("1.1 使用get方法")
    print(json.loads(requests.get(url1).content))
    print("1.2 使用post方法")
    print(json.loads(requests.post(url1).content))
    print("2. 找出体型与传入学号最接近的两位同学")
    print("2.1 成功 使用get方法")
    print(json.loads(requests.get(url2 + "?num=1727406005").content))
    print("2.2 成功 使用post方法")
    print(json.loads(requests.post(url2, json=json.dumps({"num": "1727406005"})).content))
    print("2.3 失败 使用get方法，没有参数")
    print(json.loads(requests.get(url2 + "").content))
    print("2.4 失败 使用get方法，没有相应参数")
    print(json.loads(requests.get(url2 + "?num1=1727406005").content))
    print("2.5 失败 使用get方法，传入不存在的学号")
    print(json.loads(requests.get(url2 + "?num=00000000").content))
    print("2.6 失败 使用post方法，没有数据")
    print(json.loads(requests.post(url2).content))
    print("2.7 失败 使用post方法，没有相应数据")
    print(json.loads(requests.post(url2, json=json.dumps({"num1": "1727406005"})).content))
    print("2.8 失败 使用post方法，传入不存在的学号")
    print(json.loads(requests.post(url2, json=json.dumps({"num1": "0000000"})).content))
