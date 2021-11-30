#-*- conding:utf-8 -*-
#@File      :all.py
#@Time      : 18:44
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import json
import os
import requests
from configs.conf import *
from configs.path import test_xlsx
from tools.update_data import update_data
import datetime
from tools.allureUitl import alluer_new
from tools.md5Uitl import get_md5
from configs.path import *
import time
import win32gui
import allure
import win32con
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tools.ExcelData import ExcelData

from tools.Base import *
class all:

    """
    所有模块
    """
    def __init__(self,token,inData,conftest=True):
        self.header = {"Cookie":"{0}".format(token)}
        self.proxies = {"https":"http://127.0.0.1:8888"}
        self.inData = inData
        self.new_url= url+inData["url"]
        self.data = json.loads(inData["params"])
        self.conftest=conftest

    def ParameterlessAdjustment(self):
        """所有测试用例集合"""
        body = requests.post(url=self.new_url,headers=self.header,json=self.data)
        print("\n\n"+self.inData["case_id"]+"-"+self.inData["case_name"])
        print(self.inData)
        print(self.data)
        print(self.new_url)
        print(self.header)
        print(body.json())
        print(self.inData)
        print(json.loads(self.inData["response_expect_result"]))
        print(self.conftest)
        inData = update_data(self.inData,self.data,self.new_url,self.header,body.json(),json.loads(self.inData["response_expect_result"]),self.conftest)
        return inData,body