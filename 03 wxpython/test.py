# coding=utf-8

import wx
import wx.gizmos as gizmos

cityNames = {
    "Beijing": u"北京",
    "Wuhan": u"武汉",
    "Shanghai": u"上海",
}


def GetCityChinexeName(id):
    return cityNames.get(id, '')


class CollegeTreeListCtrl(wx.gizmos.TreeListCtrl):
    def __init__(self, parent=None, id=-1, pos=(0, 0), size=wx.DefaultSize,
                 style=wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT):
        wx.gizmos.TreeListCtrl.__init__(self, parent, id, pos, size, style)

        self.root = None
        self.InitUI()
        pass

    def InitUI(self):
        self.il = wx.ImageList(16, 16, True)

        self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
        self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_FILE_OPEN, wx.ART_OTHER, (16, 16)))
        self.il.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
        self.SetImageList(self.il)

        self.AddColumn(u'学校名称')
        self.AddColumn(u'是否985')
        self.AddColumn(u'学校类型')

        pass

    def ShowItems(self, datas):
        self.SetColumnWidth(0, 150)
        self.SetColumnWidth(1, 40)
        self.SetColumnWidth(2, 47)

        self.root = self.AddRoot(u'中国大学')
        self.SetItemText(self.root, "", 1)
        self.SetItemText(self.root, "", 2)

        # 填充整个树
        cityIDs = datas.keys()
        for cityID in cityIDs:
            child = self.AppendItem(self.root, cityID)
            lastList = datas.get(cityID, [])
            childTitle = GetCityChinexeName(cityID) + u" (共" + str(len(lastList)) + u"所大学)"
            self.SetItemText(child, childTitle, 0)
            self.SetItemText(child, "", 1)
            self.SetItemText(child, "", 2)
            self.SetItemImage(child, 0, which=wx.TreeItemIcon_Normal)
            self.SetItemImage(child, 1, which=wx.TreeItemIcon_Expanded)
            for index in range(len(lastList)):
                college = lastList[index]
                # TreeItemData是每一个ChildItem的唯一标示
                # 以便在点击事件中获得点击项的位置信息
                data = wx.TreeItemData(cityID + "|" + str(index))
                last = self.AppendItem(child, str(index), data=data)
                self.SetItemText(last, college.get('collegeName', ''), 0)
                self.SetItemText(last, college.get('if_985_type', ''), 1)
                self.SetItemText(last, college.get('collegeType', ''), 2)
                self.SetItemImage(last, 0, which=wx.TreeItemIcon_Normal)
                self.SetItemImage(last, 1, which=wx.TreeItemIcon_Expanded)
        self.Expand(self.root)
        pass

    def refreshDataShow(self, newDatas):
        if self.root != None:
            self.DeleteAllItems()

        if newDatas != None:
            self.ShowItems(newDatas)

    def DeleteSubjectItem(self, treeItemId):
        self.Delete(treeItemId)
        self.Refresh()
        pass

self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnTreeListCtrlClickFunc, self.treeListCtrl)

self.colleges = {
    u'Beijing': [
        {'collegeName': u'北京大学', 'if_985_type': u'是', 'collegeType': u'综合类'},
        {'collegeName': u'清华大学', 'if_985_type': u'是', 'collegeType': u'理工类'},
        {'collegeName': u'北京邮电大学', 'if_985_type': u'否', 'collegeType': u'理工类'}],
    u'Wuhan': [
        {'collegeName': u'武汉大学', 'if_985_type': u'是', 'collegeType': u'综合类'},
        {'collegeName': u'华中科技大学', 'if_985_type': u'是', 'collegeType': u'理工类'}
    ],
    u'Shanghai': [
        {'collegeName': u'上海交通大学', 'if_985_type': u'是', 'collegeType': u'理工类'},
        {'collegeName': u'复旦大学', 'if_985_type': u'是', 'collegeType': u'综合类'},
        {'collegeName': u'同济大学', 'if_985_type': u'是', 'collegeType': u'综合类'}
    ]
}

# TreeCtrl显示数据接口
self.treeListCtrl.refreshDataShow(self.colleges)
