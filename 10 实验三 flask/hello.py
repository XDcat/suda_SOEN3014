import json
import sqlite3
import time

from flask import Flask
from flask import request
import logging

"""
返回格式规约
    res = {
        "state": 1,  # 状态码。1 为正常请求; 0为正常请求，其余错误信息，具体方法指定。
        "error": None,  # 错误信息
        "client": {
            "method": request.method,  # 请求方法
            "ip": request.remote_addr,  # 客户端ip地址
            "user": request.remote_user,  # 客户端用户名字
        },  # 客户端信息
        "time": {
            "request_time": time.time(),  # 请求时间
            "return_time": None  # 返回时间
        },
        "data": None  # 具体数据
    }
"""
# 日志格式
logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')
app = Flask(__name__)


def select_all():
    """从数据库中，找到学生的数据"""
    try:
        # 查询数据并返回
        conn = sqlite3.connect('data.db3')
        c = conn.cursor()
        cols_name = c.execute("pragma table_info(test);").fetchall()  # 获取表的信息
        cols_name = [i[1] for i in cols_name]  # 取出列名
        select_all = c.execute("select * from test").fetchall()
    except Exception as e:
        logging.info(e)
        return None
    finally:
        conn.close()

    # 组合列名和信息
    res = []
    for select_one in select_all:
        tmp = {}
        for i, d in enumerate(select_one):
            tmp[cols_name[i]] = d
        res.append(tmp)
    return res


def all_similar():
    """计算全班所有最相似的人"""
    # 获取所有信息
    data = select_all()

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
                  pow(float(data[i]['SG']) - float(data[j]['SG']), 2) + \
                  pow(float(data[i]['TZ']) - float(data[j]['TZ']), 2) + \
                  pow(float(data[i]['XC']) - float(data[j]['XC']), 2) + \
                  pow(float(data[i]['XM']) - float(data[j]['XM']), 2) + \
                  pow(float(data[i]['XW']) - float(data[j]['XW']), 2) + \
                  pow(float(data[i]['YW']) - float(data[j]['YW']), 2)
            distance.append(
                [
                    data[i]['ID'], data[i]['NAME'], data[j]['ID'], data[j]['NAME'], dis
                ]
            )
    return sorted(distance, key=lambda x: x[4])


def find_similar(num):
    """计算全班所有最相似的人"""
    # 获取所有信息
    data = select_all()

    num = str(num)
    j = None
    for i in data:
        if i["ID"] == num:
            j = i
            data.remove(i)
            break

    # 判断是否存在
    if j is None:
        return None

    # 计算距离
    distance = []
    for i in range(len(data)):
        try:
            float(data[i]['JK'])
            float(j['JK'])
            float(data[i]['SG'])
            float(j['SG'])
            float(data[i]['TZ'])
            float(j['TZ'])
            float(data[i]['XC'])
            float(j['XC'])
            float(data[i]['XM'])
            float(j['XM'])
            float(data[i]['XW'])
            float(j['XW'])
            float(data[i]['YW'])
            float(j['YW'])
        except:
            continue

        dis = pow(float(data[i]['JK']) - float(j['JK']), 2) + \
              pow(float(data[i]['SG']) - float(j['SG']), 2) + \
              pow(float(data[i]['TZ']) - float(j['TZ']), 2) + \
              pow(float(data[i]['XC']) - float(j['XC']), 2) + \
              pow(float(data[i]['XM']) - float(j['XM']), 2) + \
              pow(float(data[i]['XW']) - float(j['XW']), 2) + \
              pow(float(data[i]['YW']) - float(j['YW']), 2)

        distance.append(
            [
                data[i]['ID'], data[i]['NAME'], j['ID'], j['NAME'], dis
            ]
        )
    return sorted(distance, key=lambda x: x[4])


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "HELLO"


@app.route('/similar', methods=['GET', 'POST'])
def similar_most():
    """找出全班体型最接近的两位同学；"""
    # 0. 返回信息的结构
    res = {
        "state": 1,  # 状态码
        "client": {
            "method": request.method,  # 请求方法
            "ip": request.remote_addr,  # 客户端ip地址
            "user": request.remote_user,  # 客户端用户名字
        },  # 客户端信息
        "time": {
            "request_time": time.time(),  # 请求时间
            "return_time": None  # 返回时间
        },
    }
    # 1. 获取全班同学信息
    data = all_similar()
    if data is None:
        res["state"] = 0
        res["error"] = "查询数据库出错"
    else:
        res["data"] = {"most_similar": data[0][: -1]}

    res["time"]["return_time"] = time.time()  # 返回时间
    return json.dumps(res, ensure_ascii=False)


@app.route('/similar/find', methods=['GET', 'POST'])
def similar_find():
    """找出体型与传入学号最接近的两位同学；"""
    # 0. 返回信息的结构
    res = {
        "state": 1,  # 状态码
        "client": {
            "method": request.method,  # 请求方法
            "ip": request.remote_addr,  # 客户端ip地址
            "user": request.remote_user,  # 客户端用户名字
        },  # 客户端信息
        "time": {
            "request_time": time.time(),  # 请求时间
            "return_time": None  # 返回时间
        },
    }
    # 1. Get 方法
    # 1.1 判断是否有输入
    if request.method == "GET":
        args = request.args

    # 2. Post 方法
    elif request.method == "POST":
        if request.get_json():
            args = json.loads(request.get_json())
        else:
            args = None



    logging.debug("传入的args: {}".format(args))
    if args is None:
        res["state"] = 0
        res["error"] = "并未使用json传入数据"
    else:
        if "num" in args.keys():
            # 进行查询
            data = find_similar(args["num"])
            if data is None:
                res["state"] = 0
                res["error"] = "此学生并不再数据库中"
            else:
                res["data"] = {"most_similar": data[0][: -1]}

        else:
            res["state"] = 0
            res["error"] = "未输入num参数，用于查询"


    res["time"]["return_time"] = time.time()  # 返回时间
    return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
