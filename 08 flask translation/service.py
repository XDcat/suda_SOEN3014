# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/11/20
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import hashlib
import json
import logging
import random
import sqlite3
import time
import urllib

import requests
from flask import Flask, request

logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')

sql_path = r"D:\Box\Pycharm_Project\工业实践课程\07 flask\uni_industry_practice.db"
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World"


@app.route("/trans", methods=["GET", "POST"])
def do_trans():
    if request.method == "POST":
        data = json.loads(request.get_json())
        logging.debug("收到的数据为：%s" % data)
        # 将查询的数据加入到数据库中
        conn = sqlite3.connect(sql_path)
        c = conn.cursor()
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        c.execute("insert into request(create_time, content) VALUES (?, ?)", (create_time, data["text"]))
        conn.commit()
        conn.close()
        # 翻译文字
        tran_data = translate(data["text"], fromLang=data["from"], toLang=data["to"], flag=True)
        logging.debug("翻译文字: \n %s" % tran_data)
        # Todo: 保存到数据库中
        response_json =  {
            "tran_before": data["text"],
            "tran_after": tran_data,
        }
        return json.dumps(response_json)
    if request.method == "GET":
        return "Hello, I'm trans"
    return "{\"error\": 0}"


def translate(text, fromLang="auto", toLang="zh", flag=False):
    """
    翻译 text 为英文
    :param text: 需要翻译的文本
    :param flag: True 只返回文本；False 返回原始 json
    :return:
    """
    logging.debug("需要翻译的文字：%s" % text)
    # 将 id 和 密匙 使用配置文件
    appid = '20191016000342020'  # 填写你的appid
    secretKey = 'FERT7SoJhp0WagCy2Gz3'  # 填写你的密钥

    myurl = 'https://api.fanyi.baidu.com/api/trans/vip/translate'  # 部分网址
    salt = random.randint(32768, 65536)
    q = text
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    # 请求
    try:
        reponse = requests.get(myurl)  # 构建 get 请求
        logging.debug(reponse)
        logging.debug(reponse.text)
        result = json.loads(reponse.text)
        logging.debug(result)
    except Exception as e:
        logging.warning(e)

    if not flag:
        return result
    else:
        return "\n".join([i["dst"] for i in result["trans_result"]])
