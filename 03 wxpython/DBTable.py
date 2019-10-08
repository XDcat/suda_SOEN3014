# # -*- coding:utf-8 -*-
# '''
# __author__ = 'XD'
# __mtime__ = 2019/10/8
# __project__ = 工业实践课程
# Fix the Problem, Not the Blame.
# '''
# import sqlite3
#
# import wx.grid
#
#
# class DBTable(wx.grid.GridTableBase):
#     def __init__(self, path, table):
#         # 创建游标对象
#         connect = sqlite3.connect(path)
#         c = connect.cursor()
#
#         # 查询字段名称
#         cols = c.execute("pragma table_info(%s);" % table).fetchall()
#         cols = [col[1] for col in cols]
#         # 查询数据
#         self.data = c.execute("select * from %s" % table).fetchall()
#
#     def GetNumberRows(self):
#         return len(self.data)
#
#     def GetNumberCols(self):
#         return len(self.data[0]) if self.data else 0
#
#     def IsEmptyCell(self, row, col):
#         return self.data[row][col]
#
#     def GetValue(self, row, col):
#         return self.data[row][col]
#
#     def SetValue(self, row, col, value):
#         self.data[row][col] = value
