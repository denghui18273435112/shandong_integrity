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
from tools.Base import time_YmdHMS
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
from tools.commonly_method import *
from tools.Base import *
class all:
    """
    所有模块
    """
    def __init__(self,inData,token=None,token_province=None,token_city=None,conftest=True):
        self.token = token
        self.token_province = token_province
        self.token_city = token_city
        if "case_3_SubmitImport_01" in inData["case_id"]\
                or "case_3_DepartureImport_01" in inData["case_id"] :
            self.header = {"Cookie":"{0}".format(token_city)}
            print("地市")
        elif "case_3_creditlogAudit_01" in inData["case_id"]\
                or "case_3_Finish_01" in inData["case_id"]:
            self.header = {"Cookie":"{0}".format(token_province)}
            print("省公司")
        else:
            self.header = {"Cookie":"{0}".format(token)}
            print("省协会")
        self.proxies = {"https":"http://127.0.0.1:8888"}
        self.inData = inData
        self.new_url= url+inData["url"]
        self.data = json.loads(inData["params"])
        self.conftest = conftest

    def ParameterlessAdjustment(self,company=None,company_province=None,company_city=None,rewards_id=None):
        """所有测试用例集合"""

        #替换字段值；如日期、年费、公司id
        if isinstance(self.data,list):
            pass
        else:
            for key in self.data.keys():
                if key == "pageNum":
                    self.data[key] = 1
                if key == "pageSize":
                    self.data[key] = 20
                if key == "bdate":
                    self.data[key] = "{}-01-01".format(date_YmdHMS(5))
                if key == "edate":
                    self.data[key] = "{}".format(date_YmdHMS(4))
                if key == "date_begin":
                    self.data[key] = "1900-01-01"
                if key == "date_end" or key == "honorDate":
                    self.data[key] = "{}".format(date_YmdHMS(4))
                if key == "dateRange":
                    self.data[key][0] = "{}-01-01".format(date_YmdHMS(5))
                    self.data[key][1] = "{}".format(date_YmdHMS(4))
                if key == "company_id":
                    if self.inData["case_id"] == "case_3_SubmitImport_01":
                        self.data[key] = "{}".format(company_city)
                    else:
                        self.data[key] = "{}".format(company)
                if key == "company":
                    if self.inData["case_id"] == "case_3_overtimecomplaintGetList_01"\
                            or self.inData["case_id"] == "case_1_IndicatorsSummary":
                        pass
                    else:
                        if self.inData["case_id"] != "case_IndicatorsSummary":
                            self.data[key][0] = company
                        if self.inData["case_id"] == "case_3_SubmitImport_01":
                            self.data[key][0] = company_city


        #接口操作具有依耐性
        if self.inData["case_id"] == "case_3_creditlogAudit_01" or  self.inData["case_id"] == "case_3_creditlogAudit_02":
            id = requests_zzl("case_3_creditlogGetAuditList_01",self.token)["data"]["list"][0]["id"]
            self.data["ids"].append(id)

        if self.inData["case_id"] == "case_3_overtimecomplaintAdd_01":
            body = requests_zzl("case_3_overtimecomplaintQuery_01",self.token)
            job_record_id = body["data"]["id"]
            complaint_company_id = body["data"]["company_id"]
            self.data["complaint_company_id"]=complaint_company_id
            self.data["job_record_id"]=job_record_id

        if self.inData["case_id"] == "case_3_Acceptance_01"\
            or self.inData["case_id"] == "case_3_Finish_01":
            id = requests_zzl("case_3_overtimecomplaintGetList_01",self.token)["data"]["list"][0]["id"]
            self.data["id"]=id

        if self.inData["case_id"] == "case_1_lecturermanageDelAwardInfo":
            id = requests_zzl("case_1_lecturermanageGetAwardInfo",self.token)["data"][0]["id"]
            self.data["id"]=id


        #需要导入表格的操作
        request_file = None
        if self.inData["case_id"] == "case_2_membercompanyEntryImport_01":
            request_file = {'file': (excel_1_name,open(excel_1,"rb"), file_application)}
        if self.inData["case_id"] == "case_2_membercompanyEntryImport_02":
            request_file = {'file': (excel_2_name,open(excel_2,"rb"), file_application)}
        if self.inData["case_id"] == "case_2_membercompanyEntryImport_03":
            request_file = {'file': (excel_3_name,open(excel_3,"rb"), file_application)}
        if self.inData["case_id"] == "case_2_membercompanyEntryImport_04":
            request_file = {'file': (excel_4_name,open(excel_4,"rb"), file_application)}
        if self.inData["case_id"] == "case_3_EntryImport_01":
            request_file = {'file': (excel_5_name,open(excel_5,"rb"), file_application)}
        if self.inData["case_id"] == "case_3_ImportWorkBusiness_01":
            request_file = {'file': (excel_6_name,open(excel_6,"rb"), file_application)}
        if self.inData["case_id"] == "case_2_DepartureImport_01":
            request_file = {'file': (excel_10_name,open(excel_10,"rb"), file_application)}
        if self.inData["case_id"] == "case_3_DepartureImport_01":
            request_file = {'file': (excel_21_name,open(excel_21,"rb"), file_application)}


        #区分是否上传文件；请求
        if "case_2" in self.inData["case_id"]\
           or "case_3_EntryImport_01" in self.inData["case_id"]\
           or "case_3_ImportWorkBusiness_01" in self.inData["case_id"]\
           or "case_3_DepartureImport_01" in self.inData["case_id"]:
                body = requests.post(url=self.new_url, headers=self.header, data=self.data, files=request_file,proxies=self.proxies)
        else:
            body = requests.post(url=self.new_url, headers=self.header, json=self.data,proxies=self.proxies)

        #打印,生成报告
        if self.conftest==True:
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