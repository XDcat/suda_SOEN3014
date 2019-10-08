# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/6
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import os
import sqlite3

import wx
import wx.grid


class DBTable(wx.grid.GridTableBase):
    """ 在展示表格时,会重新绘制表格,需要自己继承 GridTableBase"""
    def __init__(self, path, table):
        super(DBTable, self).__init__()
        # 创建游标对象
        connect = sqlite3.connect(path)
        c = connect.cursor()

        # 查询字段名称
        cols = c.execute("pragma table_info(%s);" % table).fetchall()
        self.cols = [col[1] for col in cols]
        # 查询数据
        self.data = c.execute("select * from %s" % table).fetchall()

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0]) if self.data else 0

    def IsEmptyCell(self, row, col):
        return bool(self.data[row][col])

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        self.data[row][col] = value

    def GetColLabelValue(self, col):
        return self.cols[col]

    def SetColLabelValue(self, col, label):
        self.cols[col] = label


class ShowGridPanel(wx.Panel):
    """
    展示表格
    """

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.grid = wx.grid.Grid(self, -1)

        # 添加布局方式
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.grid, -1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def draw_table(self, path, table):
        """在表格中绘制数据表"""
        try:
            # 创建游标对象
            connect = sqlite3.connect(path)
            c = connect.cursor()

            # 查询字段名称
            cols = c.execute("pragma table_info(%s);" % table).fetchall()
            cols = [col[1] for col in cols]
            # 查询数据
            tuples = c.execute("select * from %s limit 100" % table).fetchall()

            print(len(tuples), len(cols))
            # 绘制图表
            self.grid.ForceRefresh()
            grid_table = DBTable(path, table)
            self.grid.SetTable(grid_table, True)
            # 绘制列名
            for index, col in enumerate(cols):
                self.grid.SetColLabelValue(index, col)

        finally:
            pass


class DatabaseTreePanel(wx.Panel):
    """
    树形表
    """

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        """
        文档树
        1. root 我的连接 只用于表述
        2. 数据库文件
        3. 数据库
        4. 表
        5. 字段
        """
        self.tree = wx.TreeCtrl(self,
                                style=wx.TR_NO_LINES | wx.TR_HAS_BUTTONS | wx.TR_TWIST_BUTTONS
                                # style 没有线条 | 有按钮 | 按钮为箭头
                                )

        # 设置图标
        isz = (16, 16)  # 图标大小
        icons = wx.ImageList(*isz)  # 使用 ImageList 存储图标
        # icon_common = icons.Add(wx.ArtProvider.GetBitmap(wx.ART_ADD_BOOKMARK, wx.ART_OTHER, isz))  # 通用的图标（暂时）
        icons.Add(wx.Image(r"./resource/icon/link.png", wx.BITMAP_TYPE_PNG).Scale(*isz).ConvertToBitmap())
        icons.Add(wx.Image(r"./resource/icon/sqlite3.png", wx.BITMAP_TYPE_PNG).Scale(*isz).ConvertToBitmap())
        icons.Add(wx.Image(r"./resource/icon/db.png", wx.BITMAP_TYPE_PNG).Scale(*isz).ConvertToBitmap())
        icons.Add(wx.Image(r"./resource/icon/table.png", wx.BITMAP_TYPE_PNG).Scale(*isz).ConvertToBitmap())
        icons.Add(wx.Image(r"./resource/icon/col.png", wx.BITMAP_TYPE_PNG).Scale(*isz).ConvertToBitmap())

        self.tree.SetImageList(icons)
        self.icons = icons

        # 添加根节点
        self.root = self.tree.AddRoot("我的连接")
        self.tree.SetItemImage(self.root, 0)

        # 添加布局方式
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.tree, 1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def add_database(self, path, fn_click_table=None):
        """在 tree 中添加数据库数据"""
        db_file_name = os.path.split(path)[-1][:-3]
        # 添加 tree: 数据库文件
        db_file_item = self.tree.AppendItem(self.root, db_file_name)
        self.tree.SetItemImage(db_file_item, 1)

        # 连接数据库
        try:
            conn = sqlite3.connect(path)
            c = conn.cursor()  # 创建游标对象
            # 数据表
            dbs = c.execute("select name from sqlite_master where type='table';").fetchall()
            for db in dbs:
                # 每一个数据表
                table_name = db[0]
                cols = c.execute("pragma table_info(%s);" % table_name).fetchall()

                # 添加 tree: 数据库
                table_item = self.tree.AppendItem(db_file_item, table_name, data={"path": path, "name": table_name})
                self.tree.SetItemImage(table_item, 3)

                for col in cols:
                    # 具体字段
                    col_name = col[1]

                    # 添加 tree: 字段
                    col_item = self.tree.AppendItem(table_item, col_name)
                    self.tree.SetItemImage(col_item, 4)

        except Exception as e:
            print(e)

    def get_db_path_by_name(self, db_name):
        return self.db_dict[db_name]


class Sqlite3GUI(wx.Frame):
    def __init__(self, parent, title="Sqlite3 GUI"):
        super(Sqlite3GUI, self).__init__(parent, title=title, size=(500, 300))  # 调用父类构造方法
        self.InitUI()  # 添加布局内容
        self.Center()  # 居中
        self.Show()  # 可见

    def InitUI(self):
        # 将界面划分成两块
        self.splitter = wx.SplitterWindow(self, -1)

        # 添加菜单
        self.menubar = wx.MenuBar()
        self.SetMenuBar(self.menubar)
        # File 菜单项
        file_menu = wx.Menu()
        open_item = wx.MenuItem(file_menu, -1, text="open", kind=wx.ITEM_NORMAL)  # 打开文件
        self.Bind(wx.EVT_MENU, self.open_file, open_item)
        file_menu.Append(open_item)
        self.menubar.Append(file_menu, "File")
        # 测试按钮
        test_item = wx.MenuItem(file_menu, -1, text="test", kind=wx.ITEM_NORMAL)
        file_menu.Append(test_item)
        self.Bind(wx.EVT_MENU, self.test_open, test_item)


        # 添加 tree
        self.db_panel = DatabaseTreePanel(self.splitter)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.sel_table, self.db_panel.tree)
        # 添加展示界面
        self.show_panel = ShowGridPanel(self.splitter)

        # # 两个部分的交互
        # # 1. 点击表名展示表的数据
        # self.Bind()

        # Frame 布局
        self.splitter.SplitVertically(self.db_panel, self.show_panel)

    def sel_table(self, evt):
        """ 选择表后,展示数据"""
        # 表
        data = self.db_panel.tree.GetItemData(evt.GetItem())
        if data:
            path = data.get("path", None)
            table = data.get("name", None)
            if path and table:
                self.show_panel.draw_table(path, table)

    def open_file(self, evt):
        """ 打开 sqlite 文件 """
        # 文件窗口对象
        dlg = wx.FileDialog(
            self,
            message="选择 sqlite 文件",  # 标题
            defaultDir=os.getcwd(),  # 默认路径
            defaultFile="",  # 默认选中文件
            wildcard="*.db",  # 文件通配符
            style=wx.FD_OPEN | wx.FD_MULTIPLE |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
        )

        # 打开文件窗口
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()  # 选中的文件的路径
            for path in paths:
                # 添加文件到 tree
                self.db_panel.add_database(path, fn_click_table=self.sel_table)
        self.db_panel.tree.Expand(self.db_panel.root)

        dlg.Destroy()  # 回收资源
    def test_open(self, evt):
        """ 打开一个测试文件 """
        path = r"D:\Box\Pycharm_Project\工业实践课程\03 wxpython\resource\test\sudaStu.db"
        self.db_panel.add_database(path, fn_click_table=self.sel_table)

if __name__ == '__main__':
    app = wx.App()
    Sqlite3GUI(None)
    app.MainLoop()
