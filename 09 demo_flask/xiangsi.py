# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/12/4
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import sqlite3
import math
from pprint import pprint

def similarity():
    try:
        # conn = sqlite3.connect('data.db3')  # 我把这个db3文件就放在当前目录，所以可以这样写
        # c = conn.cursor()
        # select_all = c.execute("select * from test").fetchall()
        # 查询数据并返回
        conn = sqlite3.connect('data.db3')  # 我把这个db3文件就放在当前目录，所以可以这样写
        c = conn.cursor()
        cols_name = c.execute("pragma table_info(test);").fetchall()
        cols_name = [i[1] for i in cols_name]  # 取出列名
        select_all = c.execute("select * from test").fetchall()
    except Exception as e:
        print(e)
        return e
    finally:
        conn.close()
    data = []
    for select_one in select_all:
        tmp = {}
        for i, d in enumerate(select_one):
            tmp[cols_name[i]] = d
        data.append(tmp)

    # 计算距离
    distance = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            try:
                float(data[j]['JK'])
                float(data[j]['JK'])
                float(data[i]['SG'])
                float(data[j]['SG'])
                float(data[i]['TZ'])
                float(data[j]['TZ'])
                float(data[i]['XC'])
                float(data[j]['XC'])
                float(data[i]['XM'])
                float(data[j]['XM'])
                float(data[i]['XW'])
                float(data[j]['XW'])
                float(data[i]['YW'])
                float(data[j]['YW'])
            except:
                continue

            dis = pow(float(data[i]['JK']) - float(data[j]['JK']), 2) + \
                  pow(float(data[i]['SG']) - float(data[j]['SG']), 2)+ \
                  pow(float(data[i]['TZ']) - float(data[j]['TZ']), 2)+ \
                  pow(float(data[i]['XC']) - float(data[j]['XC']), 2)+ \
                  pow(float(data[i]['XM']) - float(data[j]['XM']), 2)+ \
                  pow(float(data[i]['XW']) - float(data[j]['XW']), 2)+ \
                  pow(float(data[i]['YW']) - float(data[j]['YW']), 2)
            distance.append(
                [
                    data[i]['ID'], data[i]['NAME'], data[j]['ID'], data[j]['NAME'], math.sqrt(dis)
                ]
            )
    # pprint(distance)
    pprint(sorted(distance, key=lambda x: x[4]))
if __name__ == '__main__':
    similarity()