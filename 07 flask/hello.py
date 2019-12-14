# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/11/6
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import json

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/class")
def get_class():
    return "卓越工程师班"


@app.route("/do_request", methods=["GET", "POST"])
def do_request():
    print("this is /do_request")
    if request.method == "POST":
        data = request.get_data()
        print(data)
        print(json.loads(data.decode("utf-8")))
    return "你好呀"


@app.route("/do_request_json", methods=["GET", "POST"])
def do_request_json():
    print("this is /do_request_json")
    if request.method == "POST":
        print(request.get_json())
        if request.is_json:
            print("收到的数据为 Json")
            data = request.get_json()
            print(data)
        else:
            print("收到的数据不是 json")
    return "你好呀"
