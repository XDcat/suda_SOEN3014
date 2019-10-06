# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/6
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import wx
from wx import gizmos


class TreePanel(wx.Panel):
    """
    树形表
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)


        self.tree = gizmos.TreeListCtrl
class Sqlite3GUI(wx.Frame):
    def __init__(self, parent, title="Sqlite3 GUI"):
        super(Sqlite3GUI, self).__init__(parent, title=title, size=(500, 300))  # 调用父类构造方法
        self.InitUI()  # 添加布局内容
        self.Center()  # 居中
        self.Show()  # 可见
    def InitUI(self):
        # 设置布局方式
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)
        # 树形数据
        treePanel = TreePanel(self)
        vbox.Add(treePanel, 1, wx.ALL |wx.EXPAND, 1)


if __name__ == '__main__':
    app = wx.App()
    Sqlite3GUI(None)
    app.MainLoop()
