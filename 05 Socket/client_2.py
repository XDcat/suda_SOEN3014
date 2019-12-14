# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/23
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import logging
import socket

logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')


if __name__ == '__main__':
    addr = "localhost"
    # addr = "10.40.32.93"
    logging.debug("addr %s" % addr)
    client= socket.socket()
    client.connect((addr, 6080))
    client.send("你好呀".encode("utf8"))
    logging.debug(client.recv(1024).decode("utf-8"))
    client.close()