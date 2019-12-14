# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/11/13
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
from unittest import TestCase

import requests


class TestDo_request(TestCase):
    pass


if __name__ == '__main__':
    url = "http://127.0.0.1:5000/do_request"
    data = {
        "name": "zlj",
        "age": "19"
    }
    response = requests.post(url, data=data)

