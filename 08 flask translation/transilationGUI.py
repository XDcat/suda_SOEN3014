# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/16
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import json
import logging
import socket

# 设置 logging 格式
# logging.basicConfig(level=logging.DEBUG)
import requests
import wx

logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')


def translate(text, fromLang="auto", toLang="zh", flag=False, addr="localhost"):
    # 使用 socket 翻译
    _url = "http://127.0.0.1:5000/trans"
    data = {
        "text": text,
        "from": fromLang,
        "to": toLang,
    }
    logging.debug(_url)
    response = requests.post(_url, json=json.dumps(data))
    logging.debug("返回的response: %s" % response)
    logging.debug("返回的内容：%s" % response.text)
    return json.loads(response.text)["tran_after"]

class TranslationFrame(wx.Frame):
    def __init__(self, parent, title="翻译"):
        super(TranslationFrame, self).__init__(parent, title=title, size=(500, 300))
        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):
        self.panel = wx.Panel(self, -1)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        # from
        self.from_text = wx.TextCtrl(self.panel, -1, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        self.from_text.SetInsertionPoint(0)

        # 翻译按钮
        self.translate_button = wx.Button(self.panel, -1, "翻译")
        self.Bind(wx.EVT_BUTTON, self.evt_translate, self.translate_button)

        # to
        self.to_text = wx.TextCtrl(self.panel, -1, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        self.to_text.SetInsertionPoint(0)

        # 布局
        self.vbox.Add(self.from_text, -1, flag=wx.EXPAND)
        self.vbox.Add(self.translate_button, 0, flag=wx.ALIGN_CENTER)
        self.vbox.Add(self.to_text, -1, flag=wx.EXPAND)

        self.panel.SetSizer(self.vbox)

    def evt_translate(self, evt):
        # 点击翻译按键
        fr_text = self.from_text.GetValue()
        to_text = translate(fr_text, toLang='en', flag=True)

        logging.debug(to_text)
        if not fr_text:
            # 如果是空字符，跳出
            return
        self.to_text.SetValue(to_text)


if __name__ == '__main__':
    app = wx.App()
    TranslationFrame(None)
    app.MainLoop()
