# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/23
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/23
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import hashlib
import json
import logging
import random
import socket
import urllib

import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')


HOST = "localhost"
PORT = 6080
BUF_SIZE = 1024
ADDR = (HOST, PORT)

def translate(text, fromLang="auto", toLang="zh", flag=False):
    """
    翻译 text 为英文
    :param text: 需要翻译的文本
    :param flag: True 只返回文本；False 返回原始 json
    :return:
    """
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


if __name__ ==  '__main__':
    logging.debug("开启服务")
    server = socket.socket()  # 获取对象
    server.bind(ADDR)  # 绑定地址
    server.listen(5)  # 连接数目

    while True:
        client, addr = server.accept()  # 建立连接 （client 对象， 地址）
        # logging.debug("连接：%s" % addr)
        logging.debug("连接：{}".format(addr))
        while True:
            data = client.recv(1024).decode()
            if data:
                logging.debug("接收数据：{}".format(data))
                tran_data = translate(data, toLang="en", flag=True)
                client.send(tran_data.encode("utf8"))
                break

    # WHO ARE YOU