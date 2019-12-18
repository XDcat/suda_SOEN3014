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
import os
import random
import time
import urllib

import pygame
from playsound import playsound

import requests
# 设置 logging 格式
# logging.basicConfig(level=logging.DEBUG)
import wx

logging.basicConfig(level=logging.DEBUG,
                    format='%(module)s - fnc: %(funcName)s() - line: %(lineno)d - %(levelname)s - %(message)s')

LANG = {'自动检测': 'auto', '中文': 'zh', '英语': 'en', '粤语': 'yue', '文言文': 'wyw', '曰语': 'jp', '韩语': 'kor', '法语': 'fra',
        '西班牙语': 'spa', '泰语': 'th', '阿拉伯语': 'ara', '俄语': 'ru', '葡萄牙语': 'pt', '德语': 'de', '意大利语': 'it', '希腊语': 'el',
        '荷兰语': 'nl', '波兰语': 'pl', '保加利亚语': 'bul', '爱沙尼亚语': 'est', '丹麦语': 'dan', '芬兰语': 'fin', '捷克语': 'cs',
        '罗马尼亚语': 'rom', '斯洛文尼亚语': 'slo', '瑞典语': 'swe', '匈牙利语': 'hu', '繁体中文': 'cht', '越南语': 'vie'}


def translate(text, fromLang="auto", toLang="zh", flag=False):
    """
    翻译 text 为英文
    :param text: 需要翻译的文本
    :param flag: True 只返回文本；False 返回原始 json
    :return:
    """
    logging.debug("from: {}, to: {}, text: {}".format(fromLang, toLang, text))
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
        reponse = requests.get(myurl, timeout=3)  # 构建 get 请求
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


def get_baidu_voice(text):
    API_KEY = 'rk8AIyoPXv2XH0ONtCBhdRT6'
    SECRET_KEY = 'RGGV61KeA5zgum5b1YDt9YjGVF5SfCkX'
    TTS_URL = 'http://tsn.baidu.com/text2audio'
    token = "24.4bd396d2dc462615fbc34c8fba456dac.2592000.1579249257.282335-18055848"
    data = {
        "tex": text,  # 要进行语音合成的内容
        "tok": token,  # 个人的鉴权认证Acess Token
        "cuid": "DC-85-DE-F9-08-59",  # 随便一个值就好了，官网推荐是个人电脑的MAC地址
        "ctp": 1,  # 客户端类型，web端固定值1
        "lan": "zh",  # 中文语言
        "spd": 5,  # 语速
        "pit": 5,  # 语调
        "vol": 5,  # 音量
        "per": 4,  # 男女声，4是度丫丫
        "aue": 3,  # 音频格式，3是mp3
    }
    try:
        r = requests.post(TTS_URL, data=data, timeout=3)
        mp3 = r.content  # mp3二进制数据
        # 将mp3的二进制数据保存到本地的mp3
        pth = "./{}.mp3".format(hashlib.md5(text.encode()).hexdigest())
        logging.debug(pth)
        with open(pth, "wb") as f:
            f.write(mp3)
        return pth

    except Exception as e:
        print(e)


class TranslationFrame(wx.Frame):
    def __init__(self, parent, title="翻译"):
        super(TranslationFrame, self).__init__(parent, title=title, size=(300, 500))
        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):
        # 设置图标
        self.icon = wx.Icon('./icon.png')
        self.SetIcon(self.icon)

        self.panel = wx.Panel(self, -1)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        # from
        self.from_ch = wx.Choice(self.panel, -1, choices=["自动检测", "中文", "英语", "日语"])
        self.from_ch.SetSelection(0)
        self.from_voice = wx.Button(self.panel, -1, "发声")
        self.Bind(wx.EVT_BUTTON, self.evt_voice, self.from_voice)
        self.from_text = wx.TextCtrl(self.panel, -1, "你好呀！", style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        self.from_text.SetInsertionPoint(0)

        # 翻译按钮
        self.translate_button = wx.Button(self.panel, -1, "翻译")
        self.Bind(wx.EVT_BUTTON, self.evt_translate, self.translate_button)

        # to
        self.to_ch = wx.Choice(self.panel, -1, choices=list(LANG.keys())[1:])
        self.to_ch.SetSelection(1)
        self.to_voice = wx.Button(self.panel, -1, "发声")
        self.Bind(wx.EVT_BUTTON, self.evt_to_voice, self.to_voice)
        self.to_text = wx.TextCtrl(self.panel, -1, "", style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        self.to_text.SetInsertionPoint(0)

        # 布局
        # 1. from的布局
        self.hbox_from = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox_from.Add(wx.StaticText(self.panel, -1, "原文字"), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT,
                           border=5)
        self.hbox_from.Add(self.from_ch, 0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        self.hbox_from.Add(self.from_voice, 0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)

        # 2. to的布局
        self.hbox_to = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox_to.Add(wx.StaticText(self.panel, -1, "翻译后"), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT,
                         border=5)
        self.hbox_to.Add(self.to_ch, 0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        self.hbox_to.Add(self.to_voice, 0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)

        self.vbox.Add(self.hbox_from, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        self.vbox.Add(self.from_text, -1, flag=wx.EXPAND | wx.ALL, border=5)
        self.vbox.Add(self.hbox_to, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        self.vbox.Add(self.to_text, -1, flag=wx.EXPAND | wx.ALL, border=5)
        self.vbox.Add(self.translate_button, 0, flag=wx.ALL, border=5)

        self.panel.SetSizer(self.vbox)

    def evt_translate(self, evt):
        # 点击翻译按键
        fr_text = self.from_text.GetValue()
        to_text = translate(fr_text, fromLang=LANG[self.from_ch.GetStringSelection()],
                            toLang=LANG[self.to_ch.GetStringSelection()], flag=True)

        logging.debug(to_text)
        if not fr_text:
            # 如果是空字符，跳出
            return

        self.to_text.SetValue(to_text)

    def evt_voice(self, evt):
        pygame.mixer.init()
        voice = get_baidu_voice(self.from_text.GetValue())
        logging.debug("播放 {}".format(voice))
        try:

            playsound(voice)
        finally:
            os.remove(voice)

    def evt_to_voice(self, evt):
        pygame.mixer.init()
        voice = get_baidu_voice(self.to_text.GetValue())
        logging.debug("播放 {}".format(voice))
        try:

            playsound(voice)
        finally:
            os.remove(voice)


if __name__ == '__main__':
    app = wx.App()
    TranslationFrame(None)
    app.MainLoop()
