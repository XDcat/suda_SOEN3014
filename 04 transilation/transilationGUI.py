# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/10/16
__project__ = 工业实践课程
Fix the Problem, Not the Blame.
'''
import hashlib
import json
import logging
import random
import urllib

import requests
# 设置 logging 格式
# logging.basicConfig(level=logging.DEBUG)
import wx

logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')


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
