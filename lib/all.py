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
        self.token_SXH = all_token["token-001"]
        self.token_SX_XH = all_token["token-002"]
        self.token_SX_SGS = all_token["token-003"]
        self.token_SX_DSGS = all_token["token-004"]
        self.token_ZJ_XH = all_token["token-005"]
        self.token_ZJ_SGS = all_token["token-006"]
        self.token_ZJ_DSGS = all_token["token-007"]
        self.conftest =conftest
        self.data = json.loads(inData["params"])
        self.inData = inData
        self.new_url= url+inData["url"]
        case_id = self.inData["case_id"]
        try:
        ##############################根据接口不同选择不同的token;
        #token-001:省协会；token-002：寿险协会；token-003寿险公司；token-004寿险地市token-005：中介协会；token-006中介公司；token-007中介地市##############################
            if inData["token"] =="token-004":
                self.header = {"Cookie":"{0}".format(self.token_SX_DSGS)}
            elif inData["token"] =="token-003":
                self.header = {"Cookie":"{0}".format(self.token_SX_SGS)}
            elif inData["token"] =="token-002":
                self.header = {"Cookie":"{0}".format(self.token_SX_XH)}
            elif inData["token"] =="token-005":
                self.header = {"Cookie":"{0}".format(self.token_ZJ_XH)}
            elif inData["token"] =="token-006":
                self.header = {"Cookie":"{0}".format(self.token_ZJ_SGS)}
            elif inData["token"] =="token-007":
                self.header = {"Cookie":"{0}".format(self.token_ZJ_DSGS)}
            else:
                self.header = {"Cookie":"{0}".format(self.token_SXH)}
        ##############################重新调整接口参数##############################
            if "caseA003" in case_id:
                self.data["id"] = data_storage["AA01"]["data"]["list"][0]["member_id"]
            elif "caseA008" in case_id:
                self.data["id"] = data_storage["AA01"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["AA01"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["caseA007"]["data"]["url"]
            elif "caseA009" in case_id:
                self.data["id"] = data_storage["AA02"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["AA02"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["caseA007"]["data"]["url"]
            elif "case010" in case_id:
                self.data["id"] = data_storage["AA03"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["AA03"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["caseA007"]["data"]["url"]
            elif "caseA011" in case_id:
                self.data["id"] = data_storage["AA04"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["AA04"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["caseA007"]["data"]["url"]
            elif "caseB001" in case_id or "caseB002" in case_id:
                self.data["date_end"] = date_YmdHMS(4)
                self.data["company_id"] = data_storage["ED_02"]["data"][0]["id"]
                self.data["company"][0] = data_storage["ED_02"]["data"][0]["id"]
            elif "caseC001" in case_id or "caseC002" in case_id:
                self.data["date_begin"] = "{}-01-01".format(date_YmdHMS(5))
                self.data["date_end"] = date_YmdHMS(4)
                self.data["dateRange"][0] = "{}-01-01".format(date_YmdHMS(5))
                self.data["dateRange"][1] = date_YmdHMS(4)
                self.data["company_id"] = data_storage["ED_02"]["data"][0]["id"]
                self.data["company"][0] = data_storage["ED_02"]["data"][0]["id"]
            elif "caseD001" in case_id or "case019" in case_id:
                self.data["bdate"] = "{}-01-01".format(date_YmdHMS(5))
                self.data["edate"] = date_YmdHMS(4)
            elif "caseE001" in case_id:
                self.data["company_id"] = data_storage["ED_02"]["data"][0]["id"]
                self.data["company"][0] = data_storage["ED_02"]["data"][0]["id"]
            elif "caseE004" in case_id:
                self.data["date_begin"] = "{}-01-01".format(date_YmdHMS(5))
                self.data["date_end"] = date_YmdHMS(4)
            elif "caseB005" in case_id or "caseB006" in case_id:
                self.data["member_ids"][0] = data_storage["AA01"]["data"]["list"][0]["member_id"]
            elif "caseB007" in case_id:
                self.data["idNumbers"][0] = data_storage["AA01"]["data"]["list"][0]["id_number"]
            elif "caseB009" in case_id:
                self.data["photo_array"][0]["photo"] = data_storage["caseB008"]["data"]["url"]
            elif "caseB010" in case_id:
                self.data["id"] = data_storage["AA01"]["data"]["list"][0]["member_id"]
            elif "caseB011" in case_id:
                self.data["id"] = data_storage["AA01"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["AA01"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["caseA007"]["data"]["url"]
            elif "caseB012" in case_id:
                self.data["id"] = data_storage["AA03"]["data"]["list"][0]["id"]
                self.data["member_id"] = data_storage["AA03"]["data"]["list"][0]["member_id"]
                self.data["photo"] = data_storage["caseA007"]["data"]["url"]
            elif "caseC003" in case_id:
                self.data["id"] = data_storage["AA02"]["data"]["list"][0]["id"]
            elif "caseE005" in case_id or "caseE006" in case_id:
                self.data["ids"][0] = data_storage["caseE003"]["data"]["list"][0]["id"]
            elif "caseE002" in case_id:
                self.data["reward_company"] = "测试数据01-{}".format(date_YmdHMS(2))
                self.data["file_code_name"] = "测试数据01-{}".format(date_YmdHMS(2))
            elif "caseH04" in case_id:
                self.data["ids"][0] = data_storage["caseH03"]["data"]["list"][0]["id"]
                self.data["honorDate"] = "{}".format(date_YmdHMS(7))
            elif "caseH05" in case_id:
                self.data["id"] = data_storage["caseH03"]["data"]["list"][0]["id"]
            elif "caseH06" in case_id:
                self.data[0] = data_storage["caseH03"]["data"]["list"][0]["id"]
            elif "caseH07" in case_id:
                self.data["id"] = data_storage["caseH03"]["data"]["list"][0]["id"]
            elif "caseZ08" in case_id or "caseZ09" in case_id or "caseZ11" in case_id:
                self.data["ids"][0] = data_storage["caseZ03"]["data"]["list"][0]["id"]
            elif "caseZ10" in case_id:
                self.data["ids"][0] = data_storage["caseZ03"]["data"]["list"][0]["id"]
                self.data["BTime"] = "{}-01-01 01:01:01".format(int(date_YmdHMS(5))-2)
                self.data["ETime"] = "{}-01-01 01:01:01".format(int(date_YmdHMS(5))+2)
            elif "caseZ12" in case_id:
                self.data["ids"][0] = data_storage["caseZ04"]["data"]["list"][0]["id"]
            elif "caseQ01" in case_id or "caseQ05" in case_id or "caseQ06" in case_id or "caseQ07" in case_id:
                self.data["dateBegin"]= date_YmdHMS(4)
                self.data["dateEnd"]= date_YmdHMS(4)
            elif "caseQ03" in case_id or "caseQ04" in case_id:
                self.data["dateBegin"]= "{}-01-01".format(date_YmdHMS(5))
                self.data["dateEnd"]= date_YmdHMS(4)
            elif "caseQ08" in case_id:
                self.data["dateBegin"]= "{0}-{1}".format(str(date_YmdHMS(6)),str(date_YmdHMS(8)))
                self.data["dateEnd"]= "{0}-{1}".format(str(date_YmdHMS(6)),str(date_YmdHMS(8)))
            elif "caseG07" in case_id:
                self.data["Date"][0]= "{}-01-01".format(date_YmdHMS(5))
                self.data["Date"][1]= "{}".format(date_YmdHMS(4))
            elif "caseQ02" in case_id:
                self.data["dateBegin"]= "{0}".format(str(date_YmdHMS(6)))
                self.data["dateEnd"]= "{0}".format(str(date_YmdHMS(6)))
        ##################################需要传入表格用来##############################
            if "PD_01" in case_id:
                self.request_file = {'file':('01-山东在职人员导入模板.xlsx',open(file_path_02,"rb"),file_type)}
            elif "PD_02" in case_id:
                self.request_file = {'file':('02-山东离职人员导入模板.xlsx',open(file_path_03,"rb"),file_type)}
            elif "caseA002" in case_id:
                self.request_file = {'file':('03-入职前诚信级别批量查询模板.xlsx',open(file_path_04,"rb"),file_type)}
            elif "caseA007" in case_id:
                self.request_file = {'file':('99-图片.jpg',open(file_path_05,"rb"),file_type)}
            elif "caseB008" in case_id:
                self.request_file = {'file':('111_431226199407030014.jpg',open(file_path_06,"rb"),file_type)}
            elif "caseB013" in case_id:
                self.request_file = {'file':('04-山东在职人员业务指标导入模板.xlsx',open(file_path_07,"rb"),file_type)}
            elif "caseH02" in case_id:
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