# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/11/20
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import json
import logging

import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')
url = "http://127.0.0.1:5000"
def test_service():
        _url = url
        _url += "/trans"
        logging.debug(_url)
        response = requests.post(_url, json={"text": "hello"})
        logging.debug(response)
        logging.debug(response.text)
if __name__ == '__main__':
    test_service()

