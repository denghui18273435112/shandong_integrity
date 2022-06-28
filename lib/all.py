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
from tools.commonly_method import *
import traceback
from tools.Base import *

#分页所需
pageNum= 1
pageSize= 5
count=0
class all:
    def __init__(self):
        pass
    def case_ALL(self,all_token, inData,data_storage=None,conftest=True):
        self.token_XH = all_token["integrity_association_token"]
        self.token_SGS = all_token["integrity_province_token"]
        self.token_DSGS = all_token["integrity_prefectureLevel_token"]
        self.conftest =conftest
        self.data = json.loads(inData["params"])
        self.inData = inData
        self.new_url= url+inData["url"]
        case_id = self.inData["case_id"]
        try:
        ##############################根据接口不同选择不同的token##############
            if "PD_01" in inData["case_id"]:
                self.header = {"Cookie":"{0}".format(self.token_DSGS)}
            elif "PD_02" in inData["case_id"]:
                self.header = {"cookie":"{0}".format(self.token_SGS)}
            elif "case0C_03" in case_id:
                self.header = {"Cookie":"{0}".format(self.token_DSGS)}
            elif "case0C_05" in case_id:
                self.header = {"Cookie":"{0}".format(self.token_SGS)}
            elif "case0C_06" in case_id:
                self.header = {"Cookie":"{0}".format(self.token_XH)}
            else:
                self.header = {"Cookie":"{0}".format(self.token_XH)}
        ##############################重新调整接口参数##############################
            if "case005" in case_id:
                self.data["id"] = data_storage["case001"]["data"]["list"][0]["member_id"]
            elif "case010" in case_id:
                self.data["id"] = data_storage["case001"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["case001"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["case009"]["data"]["url"]
            elif "case011" in case_id:
                self.data["id"] = data_storage["case001"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["case001"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["case009"]["data"]["url"]
            elif "case012" in case_id:
                self.data["id"] = data_storage["case002_1"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["case002_1"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["case009"]["data"]["url"]
            elif "case013" in case_id:
                self.data["id"] = data_storage["case002_2"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["case002_2"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["case009"]["data"]["url"]
            elif "case014" in case_id or "case015" in case_id:
                self.data["date_end"] = date_YmdHMS(4)
                self.data["company_id"] = data_storage["ED_02"]["data"][0]["id"]
                self.data["company"][0] = data_storage["ED_02"]["data"][0]["id"]
            elif "case016" in case_id or "case017" in case_id:
                self.data["date_begin"] = "{}-01-01".format(date_YmdHMS(5))
                self.data["date_end"] = date_YmdHMS(4)
                self.data["dateRange"][0] = "{}-01-01".format(date_YmdHMS(5))
                self.data["dateRange"][1] = date_YmdHMS(4)
                self.data["company_id"] = data_storage["ED_02"]["data"][0]["id"]
                self.data["company"][0] = data_storage["ED_02"]["data"][0]["id"]
            elif "case018" in case_id or "case019" in case_id:
                self.data["bdate"] = "{}-01-01".format(date_YmdHMS(5))
                self.data["edate"] = date_YmdHMS(4)
            elif "case020" in case_id:
                self.data["company_id"] = data_storage["ED_02"]["data"][0]["id"]
                self.data["company"][0] = data_storage["ED_02"]["data"][0]["id"]
            elif "case021" in case_id:
                self.data["date_begin"] = "{}-01-01".format(date_YmdHMS(5))
                self.data["date_end"] = date_YmdHMS(4)
            elif "caseA_03" in case_id or "caseA_04" in case_id:
                self.data["member_ids"][0] = data_storage["case001"]["data"]["list"][0]["member_id"]
            elif "caseA_05" in case_id:
                self.data["idNumbers"][0] = data_storage["case001"]["data"]["list"][0]["id_number"]
            elif "caseA_07" in case_id:
                self.data["photo_array"][0]["photo"] = data_storage["caseA_06"]["data"]["url"]
            elif "caseA_08" in case_id:
                self.data["id"] = data_storage["case001"]["data"]["list"][0]["member_id"]
            elif "caseA_09" in case_id:
                self.data["id"] = data_storage["case001"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["case001"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["case009"]["data"]["url"]
            elif "caseA_10" in case_id:
                self.data["id"] = data_storage["case002_1"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["case002_1"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["case009"]["data"]["url"]
            elif "caseB_01" in case_id:
                self.data["id"] = data_storage["case002"]["data"]["list"][0]["id"]
            elif "case0C_05" in case_id or "case0C_06" in case_id:
                self.data["ids"][0] = data_storage["case0C_04"]["data"]["list"][0]["id"]
            elif "case0C_03" in case_id:
                self.data["reward_company"] = "测试数据01-{}".format(date_YmdHMS(2))
                self.data["file_code_name"] = "测试数据01-{}".format(date_YmdHMS(2))
            elif "caseD_03" in case_id:
                self.data["ids"][0] = data_storage["caseD_02"]["data"]["list"][0]["id"]
                self.data["honorDate"] = "{}".format(date_YmdHMS(7))
            elif "caseD_04" in case_id:
                self.data["id"] = data_storage["caseD_02"]["data"]["list"][0]["id"]
            elif "caseD_05" in case_id:
                self.data[0] = data_storage["caseD_02"]["data"]["list"][0]["id"]
            elif "caseD_06" in case_id:
                self.data["id"] = data_storage["caseD_02"]["data"]["list"][0]["id"]
            elif "caseZ_006" in case_id or "caseZ_007" in case_id:
                self.data["id"] = data_storage["caseZ_003"]["data"]["list"][0]["id"]
            elif "caseZ_008" in case_id or "caseZ_009" in case_id or "caseZ_011" in case_id:
                self.data["ids"][0] = data_storage["caseZ_003"]["data"]["list"][0]["id"]
            elif "caseZ_010" in case_id:
                self.data["ids"][0] = data_storage["caseZ_003"]["data"]["list"][0]["id"]
                self.data["BTime"] = "{}-01-01 01:01:01".format(int(date_YmdHMS(5))-2)
                self.data["ETime"] = "{}-01-01 01:01:01".format(int(date_YmdHMS(5))+2)
            elif "caseZ_012" in case_id:
                self.data["ids"][0] = data_storage["caseZ_004"]["data"]["list"][0]["id"]
        ##################################需要传入表格用来##############################
            if "PD_01" in case_id:
                self.request_file = {'file':('01-山东在职人员导入模板.xlsx',open(file_path_02,"rb"),file_type)}
            elif "PD_02" in case_id:
                self.request_file = {'file':('02-山东离职人员导入模板.xlsx',open(file_path_03,"rb"),file_type)}
            elif "case004" in case_id:
                self.request_file = {'file':('03-入职前诚信级别批量查询模板.xlsx',open(file_path_04,"rb"),file_type)}
            elif "case009" in case_id:
                self.request_file = {'file':('99-图片.jpg',open(file_path_05,"rb"),file_type)}
            elif "caseA_06" in case_id:
                self.request_file = {'file':('111_431226199407030014.jpg',open(file_path_06,"rb"),file_type)}
            elif "caseA_11" in case_id:
                self.request_file = {'file':('04-山东在职人员业务指标导入模板.xlsx',open(file_path_07,"rb"),file_type)}
            elif "caseD_01" in case_id:
                self.request_file = {'file':('05-山东讲师资质导入模板.xlsx',open(file_path_08,"rb"),file_type)}
            else:
                self.request_file = {}
            body = requests.post(url=self.new_url,headers=self.header,json=self.data,files=self.request_file)
        except BaseException:
            traceback.print_exc()
            self.data["actual_result"] = traceback.format_exc()
        finally:
            print(self.inData["case_id"])
            data_storage[case_id] = body.json()
            inData = update_data(self.inData,self.data,self.new_url,self.header,body.json(),json.loads(self.inData["response_expect_result"]),self.conftest)
            return inData,body