import json
import sqlite3

from flask import Flask
from flask import request

app = Flask(__name__)

'''
sqlite3 建表语句，只有一个字段，ID

create table student(
ID TEXT NOT NULL
)
'''

@app.route('/all', methods=['GET', 'POST'])
def all():
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

    response_json = {}
    response_json["data"] = []
    for select_one in select_all:
        tmp = {}
        for i, d in enumerate(select_one):
            tmp[cols_name[i]] = d
        response_json["data"].append(tmp)
    return json.dumps(response_json, ensure_ascii=False)





#
# @app.route('/all', methods=['GET', 'POST'])
# def all():
#     try:
#         conn = sqlite3.connect('data.db3')  # 我把这个db3文件就放在当前目录，所以可以这样写
#         c = conn.cursor()
#         select_all = c.execute("select * from test").fetchall()
#     except Exception as e:
#         print(e)
#         return e
#     finally:
#         conn.close()
#     res = {}
#     res["stu"] = []
#     return "HELLO"




@app.route('/', methods=['GET', 'POST'])
def hello():
    return "HELLO"


@app.route('/body', methods=['GET', 'POST'])
def hello_world():
    # print(request.headers)  # Content - Type: application / json

    # 获取客户端传过来的json数据
    jsondata = request.get_json()
    # 把json数据转为python的字典
    pydict = json.loads(jsondata)
    # 然后就能这样访问某个key对应的值啦
    # print(pydict['from'])

    # 请求里的数据拿到了，那就连接数据库操作吧
    try:
        conn = sqlite3.connect("clothes.db")  # 我把这个db3文件就放在当前目录，所以可以这样写
        c = conn.cursor()
#         # 我们更常用的场景应该是从客户端发来的json中解析出数据，然后存入数据，因此这里把sql语句的值改成客户端传来的值
        c.execute(
            'insert into stu(ID, NAME, GENDER, AGE, JK, XW, YW, XC, XM, SG, TZ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?)', (
                pydict["ID"], pydict["NAME"], pydict["GENDER"], pydict["AGE"], pydict["JK"], pydict["XW"], pydict["YW"],
                pydict["XC"], pydict["XM"], pydict["SG"], pydict["TZ"]))
        conn.commit()  # 这个要加，否则数据库里会没有效果
        #
        #         # # 查询数据并返回
        #         # conn = sqlite3.connect('class4suda.db3')  # 我把这个db3文件就放在当前目录，所以可以这样写
        #         # c = conn.cursor()
        #         # cols_name = c.execute("pragma table_info(student);").fetchall()
        #         # cols_name = [i[1] for i in cols_name]  # 取出列名
        #         # select_all = c.execute("select * from student").fetchall()
    except Exception as e:
        print(e)
        return str(e)
    finally:
        conn.close()  # 一定养成关闭连接的好习惯
    # print(select_all)  # [('123456789',), ('123456789',), ('源语言',), ('源语言',), ('源语言',)]
    # print(cols_name)  # [(0, 'ID', 'TEXT', 1, None, 0)]
    # response_json = {}
    # response_json["response_json"] = jsondata
    # response_json["data"] = []
    # for select_one in select_all:
    #     tmp = {}
    #     for i, d in enumerate(select_one):
    #         tmp[cols_name[i]] = d
    #     response_json["data"].append(tmp)
    return "HELLO"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)